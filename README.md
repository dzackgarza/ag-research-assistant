# Algebraic Geometry Research Assistant

This repository develops the operational guidance for a custom assistant that performs algebraic-geometry research and detailed Sage computations. It also contains the contributor-facing process needed to maintain that guidance without contaminating the assistant prompt with repository prose.

## Audiences

The repository has two distinct audiences.

### Algebraic Geometry Research Assistant

The deployed assistant consumes [`STYLE_GUIDE.md`](STYLE_GUIDE.md). That document is forward-facing operational guidance about mathematical reasoning, Sage computation, implementation, verification, and reporting.

Only `STYLE_GUIDE.md` is intended for upload to the custom GPT as behavioral guidance.

### Contributors and maintainers

Human and agent editors consume the remaining repository documentation:

- [`CONTRIBUTING.md`](CONTRIBUTING.md): how to classify corrections, extract rules, write assistant-facing guidance, preserve mathematical and Sage specificity, and review edits;
- [`MAINTENANCE.md`](MAINTENANCE.md): canonical storage, version-control operations, deployment, and mechanical update procedure;
- [`INCIDENTS.md`](INCIDENTS.md): classified source failures and regression evidence;
- [`ANALYSES/`](ANALYSES/): contributor-facing longitudinal analyses of substantial transcripts or recurring failure patterns;
- [`CHANGELOG.md`](CHANGELOG.md): concise revision history.

These files are not part of the AG assistant’s behavioral prompt.

## Failure classes

Corrections must distinguish two different actors.

### Failures of the AG assistant

These are defects in mathematical reasoning, Sage implementation, computation, or reporting. Examples include:

- failing to define ambient mathematical objects before manipulating elements;
- replacing intrinsic schemes or morphisms with coordinate-level artifacts;
- inventing unsupported Sage APIs before auditing existing semantics;
- treating derived matrices or equations as the primary mathematical object;
- claiming that an internal derivation was an executed computation;
- narrowing a general construction to a convenient special presentation.

Their forward-facing remedies belong in `STYLE_GUIDE.md`. Detailed source incidents belong in the AG-assistant section of `INCIDENTS.md`.

### Failures of contributors or maintainers

These are defects in producing and maintaining the guide. Examples include:

- confusing instructions to the current editor with instructions for the deployed AG assistant;
- writing vague slogans instead of operational rules;
- reflexively patching the guide around one incident;
- overfitting to named examples rather than identifying a recurring failure mode;
- abstracting away concrete algebraic geometry or Sage requirements;
- placing provenance, Git workflow, changelogs, or deployment procedure in the assistant prompt;
- silently deleting or weakening prior guidance during consolidation.

Their remedies belong in `CONTRIBUTING.md` or `MAINTENANCE.md`. Detailed source incidents belong in the editor/maintainer section of `INCIDENTS.md`.

A single conversation can reveal both failure classes. In that case, write separate rules for separate audiences; do not create one hybrid clause.

## File-routing rule

| File | Primary audience | Permitted content | Must not contain |
|---|---|---|---|
| `STYLE_GUIDE.md` | AG assistant | Forward-facing mathematical, Sage, computational, and reporting instructions | Repository process, provenance narratives, changelogs, editor guidance |
| `CONTRIBUTING.md` | Contributors/editors | Audience classification, rule extraction, writing standards, review criteria | Instructions that only the deployed assistant needs |
| `MAINTENANCE.md` | Maintainers | Storage, Git, update mechanics, deployment | Algebraic-geometry behavior that should reach the assistant |
| `INCIDENTS.md` | Contributors/reviewers | Classified failures, source evidence, regression criteria, rule mappings | Prompt prose intended to be uploaded verbatim |
| `ANALYSES/` | Contributors/reviewers | Deep transcript analysis, correction trajectories, causal taxonomies, coverage audits | Forward-facing prompt prose intended for direct upload |
| `CHANGELOG.md` | Contributors/users | Concise revision history | Normative behavioral guidance |
| `README.md` | All repository readers | Orientation and routing | Detailed prompt or maintenance specification |

## Current mathematical focus

The assistant-facing guide prioritizes mathematician-first reasoning over engineering-first API invention. It requires reconstruction of ambient structures, objects, morphisms, functorial dependencies, hypotheses, and universal properties before Sage classes or methods are proposed. Sage-specific ownership, source inspection, execution, backend behavior, and mathematical verification remain first-class requirements.
