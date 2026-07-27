# Algebraic Geometry Research Assistant

This repository develops and tracks the behavioral specification for a custom assistant that performs algebraic-geometry research and detailed Sage computations.

## Files

- [`STYLE_GUIDE.md`](STYLE_GUIDE.md) is the assistant-facing prompt. It contains only mathematical reasoning, Sage implementation, computation, and reporting behavior that the assistant itself should consume.
- [`MAINTENANCE.md`](MAINTENANCE.md) describes how corrections are extracted, reviewed, versioned, committed, and deployed.
- [`INCIDENTS.md`](INCIDENTS.md) preserves source failures and regression criteria.
- [`CHANGELOG.md`](CHANGELOG.md) records guide and repository revisions.

The separation is intentional. Repository process and historical provenance must not consume the assistant's behavioral prompt budget. Conversely, substantive mathematical and Sage constraints must appear in `STYLE_GUIDE.md`, not only in repository documentation.

## Current focus

The guide prioritizes mathematician-first reasoning over engineering-first API invention. In particular, the assistant must reconstruct ambient structures, objects, morphisms, functorial dependencies, hypotheses, and universal properties before proposing Sage classes or methods. Sage-specific ownership and implementation behavior remain first-class requirements.
