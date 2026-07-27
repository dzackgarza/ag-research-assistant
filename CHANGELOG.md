# Changelog

This document is for repository contributors and users tracking revisions. It is not part of the prompt consumed by the Algebraic Geometry Research Assistant.

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
