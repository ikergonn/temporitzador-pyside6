from __future__ import annotations

from pathlib import Path
from uuid import uuid4


def make_test_repo_path() -> Path:
    base = Path(__file__).resolve().parent / "_tmp" / uuid4().hex
    base.mkdir(parents=True, exist_ok=False)
    return base / "incidents.json"


def cleanup_test_path(path: Path) -> None:
    base = path.parent
    for child in base.glob("*"):
        if child.is_file():
            child.unlink()
    base.rmdir()
    parent = base.parent
    if parent.exists() and not any(parent.iterdir()):
        parent.rmdir()

