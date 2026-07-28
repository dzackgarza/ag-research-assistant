#!/usr/bin/env python3
"""Assemble the deployable STYLE_GUIDE.md from ordered source fragments."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "STYLE_GUIDE.parts"
OUTPUT = ROOT / "STYLE_GUIDE.md"


def assembled_bytes() -> bytes:
    parts = sorted(PARTS_DIR.glob("[0-9][0-9]-*.md"))
    if not parts:
        raise SystemExit(f"no style-guide fragments found in {PARTS_DIR}")

    data = bytearray()
    for part in parts:
        chunk = part.read_bytes()
        if not chunk:
            raise SystemExit(f"empty style-guide fragment: {part}")
        data.extend(chunk)

    if not data.endswith(b"\n"):
        data.extend(b"\n")
    return bytes(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if STYLE_GUIDE.md differs from the assembled fragments",
    )
    args = parser.parse_args()

    expected = assembled_bytes()
    current = OUTPUT.read_bytes() if OUTPUT.exists() else b""

    if args.check:
        if current != expected:
            raise SystemExit(
                "STYLE_GUIDE.md is stale; run scripts/build_style_guide.py"
            )
        return 0

    if current != expected:
        OUTPUT.write_bytes(expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
