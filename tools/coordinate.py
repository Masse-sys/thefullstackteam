"""Shared build reservations over ordinary fast-forward Git pushes. Python 3.12+."""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
import socket
import subprocess
import sys
import time
import uuid


class CoordinationError(Exception):
    pass


def git(*args, data=None, env=None, ok=True):
    try:
        result = subprocess.run(["git", *args], input=data, text=True,
                                encoding="utf-8", capture_output=True, env=env, timeout=60)
    except subprocess.TimeoutExpired:
        raise CoordinationError("Git timed out. Re-read status before retrying; do not write.") from None
    if ok and result.returncode:
        # Do not echo URLs, credential helpers or remote output to logs.
        raise CoordinationError("Git operation failed; check connectivity and access.")
    return result


def canonical(path):
    value = path.replace("\\", "/").strip("/")
    if path.startswith(("/", "\\")) or ":" in value:
        raise CoordinationError("Paths must be repository-relative.")
    if value == ".":
        return "."
    if not value or any(p in ("", ".", "..") for p in value.split("/")) or any(c in value for c in "*?[]\n\r"):
        raise CoordinationError("Use literal file/directory paths, without traversal or globs.")
    return value.casefold()


def overlaps(a, b):
    return a == "." or b == "." or a == b or a.startswith(b + "/") or b.startswith(a + "/")


def reject_alias(path):
    root = Path(git("rev-parse", "--show-toplevel").stdout.strip())
    current = root
    for part in path.replace("\\", "/").split("/"):
        current = current / part
        if current.is_symlink() or getattr(current, "is_junction", lambda: False)():
            raise CoordinationError("Symlink/junction scopes are not supported; use actual paths.")


def context():
    root = git("rev-parse", "--show-toplevel").stdout.strip()
    branch = git("symbolic-ref", "--quiet", "--short", "HEAD").stdout.strip()
    if branch in ("main", "master", "codex/coordination"):
        raise CoordinationError("Use a dedicated build branch and worktree.")
    workspace = hashlib.sha256((socket.gethostname() + "\0" + os.path.normcase(str(Path(root).resolve()))).encode()).hexdigest()
    return branch, workspace


def read_state(remote, ref):
    listing = git("ls-remote", "--refs", remote, ref).stdout.strip()
    if not listing:
        return None, {"version": 1, "claims": []}
    # A private temporary ref avoids shared FETCH_HEAD races between worktrees.
    local = "refs/codex-coordination/" + uuid.uuid4().hex
    try:
        git("fetch", "--quiet", "--no-write-fetch-head", remote, ref + ":" + local)
        revision = git("rev-parse", local).stdout.strip()
        state = json.loads(git("show", revision + ":state.json").stdout)
    finally:
        git("update-ref", "-d", local, ok=False)
    if state.get("version") != 1 or not isinstance(state.get("claims"), list):
        raise CoordinationError("Unknown coordination journal format; stop.")
    required = {"id", "session", "issue", "owner", "branch", "workspace", "paths", "resources", "base"}
    ids = set()
    for claim in state["claims"]:
        if not isinstance(claim, dict) or not required.issubset(claim):
            raise CoordinationError("Invalid coordination journal; stop.")
        if not isinstance(claim["paths"], list) or not claim["paths"] or not isinstance(claim["resources"], list):
            raise CoordinationError("Invalid scope in journal; stop.")
        if any(not isinstance(claim[k], str) or not claim[k] for k in required - {"issue", "paths", "resources"}):
            raise CoordinationError("Invalid identity in journal; stop.")
        if type(claim["issue"]) is not int or claim["issue"] <= 0 or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", claim["base"]):
            raise CoordinationError("Invalid issue/base in journal; stop.")
        if claim["id"] in ids or any(not isinstance(r, str) or not r.strip() for r in claim["resources"]):
            raise CoordinationError("Invalid resource or duplicate claim in journal; stop.")
        ids.add(claim["id"])
        claim["paths"] = [canonical(p) for p in claim["paths"]]
        claim["resources"] = [r.strip().casefold() for r in claim["resources"]]
    return revision, state


def publish(remote, ref, parent, state):
    payload = json.dumps(state, ensure_ascii=False, sort_keys=True) + "\n"
    blob = git("hash-object", "-w", "--stdin", data=payload).stdout.strip()
    tree = git("mktree", "-z", data="100644 blob " + blob + "\tstate.json\0").stdout.strip()
    args = ["commit-tree", tree]
    if parent:
        args += ["-p", parent]
    env = os.environ.copy()
    env.update(GIT_AUTHOR_NAME="Team coordination", GIT_AUTHOR_EMAIL="coordination@example.invalid",
               GIT_COMMITTER_NAME="Team coordination", GIT_COMMITTER_EMAIL="coordination@example.invalid")
    commit = git(*args, data="Update reservations " + uuid.uuid4().hex + "\n", env=env).stdout.strip()
    return git("push", "--porcelain", remote, commit + ":" + ref, ok=False).returncode == 0


def conflict(candidate, existing):
    if any(candidate[k] == existing[k] for k in ("issue", "branch", "workspace")):
        return True
    return (bool(set(candidate["resources"]) & set(existing["resources"])) or
            any(overlaps(a, b) for a in candidate["paths"] for b in existing["paths"]))


def run(args):
    ref = args.ref
    if not ref.startswith("refs/heads/codex/coordination") or git("check-ref-format", ref, ok=False).returncode:
        raise CoordinationError("Only codex/coordination journal branches are permitted.")
    if args.command == "status":
        return read_state(args.remote, ref)[1]
    branch, workspace = context()
    if args.command == "acquire":
        if args.issue <= 0 or not args.session.strip() or not args.owner.strip():
            raise CoordinationError("Issue, owner and session are required.")
        candidate = dict(id=uuid.uuid4().hex, session=args.session, issue=args.issue,
                         owner=args.owner, branch=branch, workspace=workspace,
                         paths=sorted(set(canonical(p) for p in args.paths)),
                         resources=sorted(set(r.strip().casefold() for r in args.resource)),
                         base=git("rev-parse", "HEAD").stdout.strip())
        if any(not r for r in candidate["resources"]):
            raise CoordinationError("Resource names cannot be empty.")
        for path in args.paths:
            reject_alias(path)
    for attempt in range(12):
        revision, state = read_state(args.remote, ref)
        if args.command == "acquire":
            if any(c["id"] == candidate["id"] for c in state["claims"]):
                return candidate  # Previous push succeeded but its response was lost.
            for existing in state["claims"]:
                if conflict(candidate, existing):
                    raise CoordinationError("Reserved by another claim: " + existing["id"])
            state["claims"].append(candidate)
        else:
            matches = [c for c in state["claims"] if c["id"] == args.claim]
            if not matches:
                if args.command == "release" and attempt:
                    return {"released": args.claim}
                raise CoordinationError("Reservation not found; do not write.")
            current = matches[0]
            if (current["session"], current["branch"], current["workspace"]) != (args.session, branch, workspace):
                raise CoordinationError("Reservation belongs to another session or worktree.")
            if args.command == "check":
                changed = git("diff", "--no-renames", "--name-only", "-z", current["base"], "--").stdout.split("\0")
                changed += git("ls-files", "--others", "--exclude-standard", "-z").stdout.split("\0")
                outside = [p for p in changed if p and not any(s == "." or canonical(p) == s or canonical(p).startswith(s + "/") for s in current["paths"])]
                if outside:
                    raise CoordinationError("Changes outside reserved scope: " + ", ".join(outside))
                for path in changed:
                    if path:
                        reject_alias(path)
                return {"valid": True, "claim": args.claim}
            state["claims"] = [c for c in state["claims"] if c["id"] != args.claim]
        if publish(args.remote, ref, revision, state):
            return candidate if args.command == "acquire" else {"released": args.claim}
        time.sleep(0.03 * (attempt + 1))
    raise CoordinationError("Journal update not confirmed. Inspect status before retrying; do not write.")


def main():
    if sys.version_info < (3, 12):
        raise SystemExit("STOP: Python 3.12+ is required for junction detection.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--ref", default="refs/heads/codex/coordination")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("status")
    acquire = commands.add_parser("acquire")
    acquire.add_argument("--issue", type=int, required=True)
    acquire.add_argument("--owner", required=True)
    acquire.add_argument("--session", required=True)
    acquire.add_argument("--paths", nargs="+", required=True)
    acquire.add_argument("--resource", action="append", default=[])
    for command in ("check", "release"):
        sub = commands.add_parser(command)
        sub.add_argument("--claim", required=True)
        sub.add_argument("--session", required=True)
    try:
        print(json.dumps(run(parser.parse_args()), ensure_ascii=False))
    except (CoordinationError, ValueError, KeyError, TypeError) as exc:
        parser.exit(2, "STOP: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
