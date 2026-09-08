"""Parse configuration and verify the repository's executable coordination contract."""
from pathlib import Path
import tomllib
import yaml


root = Path(__file__).resolve().parents[1]
for path in (root / ".codex").rglob("*.toml"):
    with path.open("rb") as stream:
        tomllib.load(stream)
for path in (root / ".github").rglob("*.yml"):
    # BaseLoader avoids YAML 1.1 interpreting GitHub's 'on' key as a boolean.
    with path.open(encoding="utf-8") as stream:
        document = yaml.load(stream, Loader=yaml.BaseLoader)
    assert isinstance(document, dict), f"Expected mapping: {path}"
workflow = yaml.load((root / ".github/workflows/team-guardrails.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
assert "pull_request" in workflow["on"]
assert workflow["jobs"]["structure"]["name"] == "Validate shared team configuration"
for filename in ("tools/coordinate.py", "tests/test_coordinate.py", "docs/operating-model/parallel-builds.md"):
    assert (root / filename).is_file(), filename
assert "parallel-builds.md" in (root / "AGENTS.md").read_text(encoding="utf-8")
print("Configuration parsed and coordination contract verified.")
