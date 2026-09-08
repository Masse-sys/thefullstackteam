"""Real Git integration tests: separate processes, clones and a bare remote."""
import concurrent.futures
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[1] / "tools" / "coordinate.py"

# Synchronize the first publish, guaranteeing both processes read the same state.
RACE_DRIVER = r'''
import pathlib, sys, time
sys.path.insert(0, sys.argv.pop(1))
import coordinate
barrier = pathlib.Path(sys.argv.pop(1))
participant = sys.argv.pop(1)
original = coordinate.publish
first = True
def publish(*args):
    global first
    if first:
        first = False
        (barrier / participant).touch()
        deadline = time.monotonic() + 20
        while len(list(barrier.iterdir())) < 2:
            if time.monotonic() > deadline:
                raise RuntimeError("Test barrier timeout")
            time.sleep(.01)
    return original(*args)
coordinate.publish = publish
coordinate.main()
'''


class CoordinationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.remote = self.root / "remote.git"
        self.git(self.root, "init", "--bare", str(self.remote))
        self.seed = self.root / "seed"
        self.git(self.root, "init", "-b", "main", str(self.seed))
        self.git(self.seed, "config", "user.name", "Test")
        self.git(self.seed, "config", "user.email", "test@example.invalid")
        (self.seed / "README.md").write_text("fixture\n")
        self.git(self.seed, "add", ".")
        self.git(self.seed, "commit", "-m", "fixture")
        self.git(self.seed, "remote", "add", "origin", str(self.remote))
        self.git(self.seed, "push", "origin", "main")
        self.git(self.remote, "symbolic-ref", "HEAD", "refs/heads/main")
        self.clones = []
        for name in ("a", "b"):
            clone = self.root / name
            self.git(self.root, "clone", str(self.remote), str(clone))
            self.git(clone, "checkout", "-b", "codex/build-" + name)
            self.clones.append(clone)

    def git(self, cwd, *args):
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                              text=True, encoding="utf-8", check=True).stdout.strip()

    def cli(self, clone, *args):
        return subprocess.run([sys.executable, str(TOOL), *args], cwd=clone,
                              capture_output=True, text=True, encoding="utf-8", timeout=45)

    def acquire(self, clone, issue="1", path="src", session="session-a", resource=None):
        args = ["acquire", "--issue", issue, "--owner", "fixture", "--session", session, "--paths", path]
        if resource:
            args += ["--resource", resource]
        return self.cli(clone, *args)

    def race(self, paths, issues, resources=None):
        barrier = self.root / "barrier"
        barrier.mkdir()
        def contender(i):
            args = [sys.executable, "-c", RACE_DRIVER, str(TOOL.parent), str(barrier), str(i),
                    "acquire", "--issue", str(issues[i]), "--owner", "fixture",
                    "--session", "session-" + str(i), "--paths", paths[i]]
            if resources:
                args += ["--resource", resources[i]]
            return subprocess.run(args, cwd=self.clones[i], capture_output=True,
                                  text=True, encoding="utf-8", timeout=45)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(contender, (0, 1)))
        for result in results:
            self.assertIn(result.returncode, (0, 2), result.stderr)
        return results

    def state(self):
        result = self.cli(self.clones[0], "status")
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)["claims"]

    def test_same_issue_concurrent_initialization(self):
        results = self.race(("src", "docs"), (1, 1))
        self.assertEqual(sorted(r.returncode for r in results), [0, 2])
        self.assertEqual(len(self.state()), 1)

    def test_overlapping_paths_concurrent(self):
        results = self.race(("SRC", "src/file.py"), (1, 2))
        self.assertEqual(sorted(r.returncode for r in results), [0, 2])

    def test_shared_resource_concurrent(self):
        results = self.race(("src", "docs"), (1, 2), ("staging-db", "STAGING-DB"))
        self.assertEqual(sorted(r.returncode for r in results), [0, 2])

    def test_disjoint_claims_survive_retry(self):
        results = self.race(("src", "src-other"), (1, 2))
        self.assertEqual([r.returncode for r in results], [0, 0], [r.stderr for r in results])
        self.assertEqual(len(self.state()), 2)

    def test_release_identity_and_old_release(self):
        a, b = self.clones
        first = json.loads(self.acquire(a).stdout)
        wrong = self.cli(a, "release", "--claim", first["id"], "--session", "wrong")
        self.assertEqual(wrong.returncode, 2)
        wrong_workspace = self.cli(b, "release", "--claim", first["id"], "--session", first["session"])
        self.assertEqual(wrong_workspace.returncode, 2)
        result = self.cli(a, "release", "--claim", first["id"], "--session", first["session"])
        self.assertEqual(result.returncode, 0, result.stderr)
        second = json.loads(self.acquire(a).stdout)
        old = self.cli(a, "release", "--claim", first["id"], "--session", first["session"])
        self.assertEqual(old.returncode, 2)
        self.assertEqual(self.state()[0]["id"], second["id"])

    def test_scope_check_rejects_untracked_and_committed_changes(self):
        a = self.clones[0]
        claim = json.loads(self.acquire(a).stdout)
        args = ("check", "--claim", claim["id"], "--session", claim["session"])
        self.assertEqual(self.cli(a, *args).returncode, 0)
        (a / "outside.txt").write_text("outside")
        self.assertEqual(self.cli(a, *args).returncode, 2)
        self.git(a, "add", "outside.txt")
        self.git(a, "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "outside scope")
        self.assertEqual(self.cli(a, *args).returncode, 2)

    def test_invalid_paths_and_main_are_rejected(self):
        for path in ("../secret", "/absolute", "C:/temp", "src/*"):
            self.assertEqual(self.acquire(self.clones[0], path=path).returncode, 2)
        self.assertEqual(self.acquire(self.seed).returncode, 2)

    def test_lost_push_response_recovers_own_claim(self):
        driver = '''
import sys
sys.path.insert(0, sys.argv.pop(1))
import coordinate
original = coordinate.publish
def publish(*args):
    original(*args)
    return False
coordinate.publish = publish
coordinate.main()
'''
        result = subprocess.run([sys.executable, "-c", driver, str(TOOL.parent), "acquire", "--issue", "1",
                                 "--owner", "fixture", "--session", "lost-response", "--paths", "src"],
                                cwd=self.clones[0], capture_output=True, text=True, timeout=45)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(self.state()), 1)
        self.assertEqual(self.state()[0]["id"], json.loads(result.stdout)["id"])

    def test_unknown_schema_fails_closed(self):
        a = self.clones[0]
        (a / "state.json").write_text('{"version": 999, "claims": []}')
        self.git(a, "add", "state.json")
        self.git(a, "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "unknown schema fixture")
        self.git(a, "push", "origin", "HEAD:refs/heads/codex/coordination")
        self.assertEqual(self.acquire(a).returncode, 2)

    def test_rename_from_outside_scope_is_rejected(self):
        a = self.clones[0]
        claim = json.loads(self.acquire(a).stdout)
        (a / "src").mkdir()
        self.git(a, "mv", "README.md", "src/README.md")
        result = self.cli(a, "check", "--claim", claim["id"], "--session", claim["session"])
        self.assertEqual(result.returncode, 2)

    def test_offline_and_corrupt_journal_fail_closed(self):
        a = self.clones[0]
        self.git(a, "remote", "set-url", "origin", str(self.root / "missing.git"))
        self.assertEqual(self.acquire(a).returncode, 2)
        self.git(a, "remote", "set-url", "origin", str(self.remote))
        (a / "state.json").write_text("{broken")
        self.git(a, "add", "state.json")
        self.git(a, "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "broken fixture")
        self.git(a, "push", "origin", "HEAD:refs/heads/codex/coordination")
        self.assertEqual(self.acquire(a).returncode, 2)

    def test_text_merge_can_pass_while_combined_behavior_fails(self):
        # Isolated fixture demonstrates why a reservation cannot replace tests.
        a, b = self.clones
        (a / "new-mode.txt").write_text("enabled")
        self.git(a, "add", ".")
        self.git(a, "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "new mode fixture")
        (b / "legacy-mode.txt").write_text("enabled")
        self.git(b, "add", ".")
        self.git(b, "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "legacy mode fixture")
        probe = "from pathlib import Path; assert not (Path('new-mode.txt').exists() and Path('legacy-mode.txt').exists())"
        for clone in (a, b):
            self.assertEqual(subprocess.run([sys.executable, "-c", probe], cwd=clone, capture_output=True).returncode, 0)
        self.git(a, "fetch", str(b), "codex/build-b")
        self.git(a, "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "merge", "--no-edit", "FETCH_HEAD")
        self.assertNotEqual(subprocess.run([sys.executable, "-c", probe], cwd=a, capture_output=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
