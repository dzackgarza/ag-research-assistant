#!/usr/bin/env python3
"""Insert canonical release entries into CHANGELOG.md."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "CHANGELOG.md"
ENTRIES_DIR = ROOT / "CHANGELOG.entries"


def replace_or_insert(current: bytes, entry: bytes) -> bytes:
    entry = entry.rstrip(b"\n") + b"\n\n"
    heading = entry.splitlines()[0]
    if not heading.startswith(b"## "):
        raise SystemExit(f"invalid changelog entry heading: {heading!r}")

    marker = b"\n" + heading + b"\n"
    if marker in current:
        start = current.index(marker) + 1
        next_heading = current.find(b"\n## ", start + len(heading))
        finish = len(current) if next_heading < 0 else next_heading + 1
        return current[:start] + entry + current[finish:]

    first_heading = current.find(b"\n## ")
    if first_heading < 0:
        raise SystemExit("CHANGELOG.md has no release heading")
    start = first_heading + 1
    return current[:start] + entry + current[start:]


def rendered_bytes() -> bytes:
    current = OUTPUT.read_bytes()
    entries = sorted(ENTRIES_DIR.glob("*.md"), reverse=True)
    for path in entries:
        data = path.read_bytes()
        if not data:
            raise SystemExit(f"empty changelog entry: {path}")
        current = replace_or_insert(current, data)
    return current


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    expected = rendered_bytes()
    current = OUTPUT.read_bytes()
    if args.check:
        if current != expected:
            raise SystemExit("CHANGELOG.md is stale; run scripts/update_changelog.py")
        return 0
    if current != expected:
        OUTPUT.write_bytes(expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
