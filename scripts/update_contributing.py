#!/usr/bin/env python3
"""Insert canonical generated blocks into CONTRIBUTING.md."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "CONTRIBUTING.md"
BLOCKS_DIR = ROOT / "CONTRIBUTING.blocks"


@dataclass(frozen=True)
class BlockSpec:
    name: str
    filename: str
    insert_before: str
    legacy_heading: str | None = None

    @property
    def begin(self) -> str:
        return f"<!-- BEGIN GENERATED: {self.name} -->"

    @property
    def end(self) -> str:
        return f"<!-- END GENERATED: {self.name} -->"


BLOCKS = (
    BlockSpec(
        name="interactive-scope-selection",
        filename="35-interactive-scope-selection.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="foundation-sufficiency",
        filename="30-foundation-sufficiency.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="computational-ecosystem",
        filename="37-computational-ecosystem.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="ontological-coherence",
        filename="38-ontological-coherence.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="semantic-lock-in",
        filename="39-semantic-lock-in.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="cumulative-foundations",
        filename="39-cumulative-foundations.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="exploratory-research",
        filename="39-zz-exploratory-research.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="semantic-distance",
        filename="39-zzz-semantic-distance.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="mathematical-exposition",
        filename="39-zzzz-mathematical-exposition.md",
        insert_before="## Audit mathematical pivots under computational pressure",
    ),
    BlockSpec(
        name="publication-workflow",
        filename="40-publication.md",
        insert_before="## Generated style-guide workflow",
        legacy_heading="## Single-command publication workflow",
    ),
)


def block_bytes(spec: BlockSpec) -> bytes:
    path = BLOCKS_DIR / spec.filename
    data = path.read_bytes().rstrip(b"\n")
    if not data:
        raise SystemExit(f"empty contributor block: {path}")
    return (
        spec.begin.encode()
        + b"\n"
        + data
        + b"\n"
        + spec.end.encode()
        + b"\n\n"
    )


def replace_or_insert(current: bytes, spec: BlockSpec) -> bytes:
    block = block_bytes(spec)
    begin = spec.begin.encode()
    end = spec.end.encode()

    if begin in current:
        start = current.index(begin)
        finish = current.index(end, start) + len(end)
        while finish < len(current) and current[finish : finish + 1] == b"\n":
            finish += 1
        return current[:start] + block + current[finish:]

    if spec.legacy_heading is not None:
        legacy = spec.legacy_heading.encode()
        if legacy in current:
            start = current.index(legacy)
            next_heading = current.find(b"\n## ", start + len(legacy))
            if next_heading < 0:
                raise SystemExit(
                    f"unable to find heading after legacy section: {spec.legacy_heading}"
                )
            return current[:start] + block + current[next_heading + 1 :]

    marker = spec.insert_before.encode()
    if marker not in current:
        raise SystemExit(f"missing insertion heading: {spec.insert_before}")
    start = current.index(marker)
    return current[:start] + block + current[start:]


def rendered_bytes() -> bytes:
    current = OUTPUT.read_bytes()
    for spec in BLOCKS:
        current = replace_or_insert(current, spec)
    return current


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
