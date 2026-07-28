#!/usr/bin/env python3
"""Insert canonical generated blocks into CONTRIBUTING.md."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "CONTRIBUTING.md"
BLOCKS_DIR = ROOT / "CONTRIBUTING.blocks"
BEGIN = "<!-- BEGIN GENERATED: publication-workflow -->"
END = "<!-- END GENERATED: publication-workflow -->"
INSERT_BEFORE = "## Generated style-guide workflow"
LEGACY_HEADING = "## Single-command publication workflow"


def block_bytes() -> bytes:
    path = BLOCKS_DIR / "40-publication.md"
    data = path.read_bytes().rstrip(b"\n")
    if not data:
        raise SystemExit(f"empty contributor block: {path}")
    return BEGIN.encode() + b"\n" + data + b"\n" + END.encode() + b"\n\n"


def rendered_bytes() -> bytes:
    current = OUTPUT.read_bytes()
    block = block_bytes()
    begin = BEGIN.encode()
    end = END.encode()

    if begin in current:
        start = current.index(begin)
        finish = current.index(end, start) + len(end)
        while finish < len(current) and current[finish : finish + 1] == b"\n":
            finish += 1
        return current[:start] + block + current[finish:]

    legacy = LEGACY_HEADING.encode()
    if legacy in current:
        start = current.index(legacy)
        next_heading = current.find(b"\n## ", start + len(legacy))
        if next_heading < 0:
            raise SystemExit("unable to find heading after legacy publication section")
        return current[:start] + block + current[next_heading + 1 :]

    marker = INSERT_BEFORE.encode()
    if marker not in current:
        raise SystemExit(f"missing insertion heading: {INSERT_BEFORE}")
    start = current.index(marker)
    return current[:start] + block + current[start:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    expected = rendered_bytes()
    current = OUTPUT.read_bytes()
    if args.check:
        if current != expected:
            raise SystemExit("CONTRIBUTING.md is stale; run scripts/update_contributing.py")
        return 0
    if current != expected:
        OUTPUT.write_bytes(expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
