"""Verify snapshot files; this is integrity evidence, not source/licence approval."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "release-manifest.json").read_text())
    expected = set()
    for item in manifest["files"]:
        relative = Path(item["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert item["path"] not in expected, "Duplicate manifest file"
        expected.add(item["path"])
        path = root / relative
        assert path.is_file() and not path.is_symlink(), f"Missing or unsafe: {relative}"
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"Changed: {relative}"
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()
              and not any(part in {".git", ".venv", "__pycache__"} for part in p.relative_to(root).parts)
              and p.suffix not in {".pyc", ".pyo"}}
    assert actual == expected | {"release-manifest.json"}, f"Unexpected/missing files: {actual ^ (expected | {'release-manifest.json'})}"
    print(f"Snapshot verified: {manifest['release_version']}, {len(expected)} exact allowlisted files. Public release status: {manifest['status']}.")


if __name__ == "__main__":
    main()
