# Changelog

This document is for repository contributors and users tracking revisions. It is not part of the prompt consumed by the Algebraic Geometry Research Assistant.

## 0.4.0 — 2026-07-27

Performed a longitudinal analysis of the full Coble-notebook assistant transcript and converted the recurring correction patterns into assistant-facing and contributor-facing guidance.

- Added `ANALYSES/COBLE_NOTEBOOK_CHAT.md`, covering 85 user turns and 84 assistant turns.
- Identified premature abstraction closure, representation capture, epistemic substitution, nounification, functorial blindness, local-global collapse, false canonicity, predicate inflation, artifact detachment, reactive remediation, scope dysregulation, and expository displacement as root cognitive failures.
- Added an abstraction-completion test requiring the assistant to continue beyond the first reusable helper or object-oriented wrapper to the standard parent, functor, diagram, or universal construction.
- Added a precise assertion taxonomy separating precondition gates, capability gates, mathematical postconditions, theorem-backed regressions, representation checks, and prohibited oracle assertions.
- Added invariant-verification requirements for noncanonical orderings, bases, charts, trivializations, coordinate models, and equality-up-to-isomorphism or scalar.
- Added local-to-global, gluing, cocycle, descent, and parameter-space requirements for schemes, covers, quotients, and families.
- Added certificate requirements for partial classification predicates such as ADE, K3, Enriques, and del Pezzo recognizers.
- Added notebook narrative, clean-execution, persisted-state, and downstream dependency-audit requirements.
- Added contributor guidance for analyzing correction trajectories, separating symptoms from causes, retaining positive counterexamples, and testing rule strength against every recurrence.
- Added incidents P-0009 through P-0013 for answer-first computation, one-rung remediation, false canonicity, local-to-global collapse, and persisted-notebook drift.
- Added `ANALYSES/` to the README audience and file-routing map.

## 0.3.3 — 2026-07-27

Corrected the treatment of partial Sage backend coverage.

- Replaced blanket anti-assertion rules with a distinction among mathematical preconditions, implementation preconditions, and research-scope boundaries.
- Required mathematically general semantic interfaces even when executable coverage is limited to special Sage representations.
- Made case routing, assertion gates, and `NotImplementedError` valid mechanisms for honest partial backend coverage.
- Added an implementation escalation ladder: native Sage routing, composition of Sage primitives, established external-system bridges, general reference implementations, and literature algorithms or theorems.
- Required an explicit scope decision based on implementation complexity, integration risk, immediate necessity, and likely reuse.
- Required substantial deferred generalizations to become actionable backlog entries with a concrete route, while supported research computations continue.
- Required unsupported current inputs either to receive the minimum correct extension or to be reported as blocked.
- Corrected P-0002 and P-0007 and added editor/maintainer incident P-0008 for misclassifying assertion-gated coverage as semantic narrowing.

## 0.3.2 — 2026-07-27

Separated the assistant and editor failures exposed by the product-construction correction sequence.

- Expanded P-0002 to record the independent AG-assistant failures: presentation-first reasoning, unsupported Sage claims, incomplete fiber-product data, rhetorical abstraction, speculative backend dispatch, assertion-based scope narrowing, and unevidenced status claims.
- Added forward-facing remediation rules requiring re-analysis of the mathematics and Sage implementation before announcing a revised architecture.
- Made headings and task-status labels subject to the same evidence standard as prose progress claims.
- Added contributor guidance against oscillating between literal incident transcription and destructive one-slogan compression.
- Required multi-defect incident decomposition, role classification for concrete examples, and coverage maps from each source defect to a resulting rule or regression criterion.
- Added editor/maintainer incident P-0007 for overfitted patching followed by underfitted “smallest invariant principle” compression.

## 0.3.1 — 2026-07-27

Clarified audiences, contributor responsibilities, and failure classification.

- Added the standard `CONTRIBUTING.md` entry point for contributor and editor guidance.
- Distinguished instructions to repository editors from instructions intended for the deployed AG assistant.
- Added an explicit README audience map and file-routing table.
- Required every correction to be classified by target actor and failure class before editing.
- Separated AG-assistant incidents from editor/maintainer incidents in `INCIDENTS.md`.
- Added incident P-0006 for misrouting conversation-level editor instructions into the assistant prompt.
- Reduced `MAINTENANCE.md` to repository mechanics and delegated editorial judgment to `CONTRIBUTING.md`.
- Made explicit that only `STYLE_GUIDE.md` is intended for upload as operational custom-GPT guidance.

## 0.3.0 — 2026-07-27

Restructured the repository by audience.

- Replaced the self-referential assistant prompt with an assistant-facing algebraic-geometry and Sage behavioral guide.
- Moved storage, version-control, deployment, and update procedure to `MAINTENANCE.md`.
- Moved source failures, provenance, and regression criteria to `INCIDENTS.md`.
- Added explicit mathematical-thinking rules against engineering-first API design.
- Added Sage-specific guidance for ambient parent structures, divisor and Picard data, group actions and linearizations, morphisms and graph constructions, linear systems, local singularity theory, double covers, backend audits, partial operations, and evidence-sensitive reporting.
- Recorded incident P-0004 for the notebook-interface report and incident P-0005 for placing repository-maintenance prose in the assistant prompt.

## 0.2.1 — 2026-07-27

- Preferred direct commits to the default branch when authorized and sufficient.
- Prohibited unrequested branch and pull-request ceremony.
- Added criteria for workflows that genuinely require review or isolation.

## 0.2.0 — 2026-07-27

- Required complete diagrams and ambient categories for universal constructions.
- Prohibited treating a finite backend list as mathematical generality.
- Required remediation to eliminate the original structural defect.
- Prohibited assertion gates that exclude required functionality.

## 0.1.1 — 2026-07-27

- Established repository-backed canonical storage.
- Prohibited chat or model memory as canonical storage.
- Required committed updates before preservation claims.

## 0.1.0 — 2026-07-27

- Created the initial behavioral guide.
