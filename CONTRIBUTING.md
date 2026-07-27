# Contributing

This document is for human and agent contributors who edit this repository. It is not part of the prompt uploaded to the Algebraic Geometry Research Assistant.

## Repository audiences

The repository serves two primary audiences:

1. **The Algebraic Geometry Research Assistant.** It consumes `STYLE_GUIDE.md` as forward-facing operational guidance for mathematical reasoning, Sage computation, implementation, and reporting.
2. **Repository contributors and maintainers.** They consume `CONTRIBUTING.md`, `MAINTENANCE.md`, `INCIDENTS.md`, `CHANGELOG.md`, and `README.md` to decide how to extract, write, review, preserve, and deploy guidance.

Do not mix these audiences. Instructions about editing, version control, prompt maintenance, provenance, changelogs, or repository workflow belong in contributor-facing documentation, not in `STYLE_GUIDE.md`.

## Classify the input before editing

Every proposed correction must first be classified by both **target audience** and **failure class**.

### Target audience

Ask which actor the instruction governs:

- **AG-assistant instruction:** changes how the deployed assistant should reason, compute, implement, verify, or report.
- **Contributor instruction:** changes how editors should analyze incidents, formulate rules, maintain files, review diffs, or manage the repository.
- **Both:** requires separate wording in separate files. Do not write one hybrid clause.

The fact that an instruction was addressed to the current editing agent does not make it an AG-assistant instruction. Conversation-level directions such as “commit directly to main,” “do not store this in memory,” or “generalize beyond the literal incident” govern contributors unless they independently imply a forward-facing behavior for the deployed AG assistant.

### Failure class

Distinguish at least:

- **AG-assistant failures:** mathematical or computational defects in the deployed assistant, such as failing to define ambient objects, replacing intrinsic constructions with coordinates, inventing unsupported Sage APIs, reporting mental derivations as executed computations, or narrowing a general task to an easy presentation.
- **Editor/maintainer failures:** defects in producing or maintaining the guide, such as vague rules, reactive incident patching, destructive consolidation, audience confusion, overfitting to one example, loss of concrete algebraic geometry or Sage content, or placing repository process in the assistant prompt.

Record these classes explicitly in incident documentation. Do not infer that a maintainer failure should be copied into the assistant prompt.

## File routing

Use the following routing rules:

- `STYLE_GUIDE.md`: only instructions that the AG assistant should directly follow while doing algebraic geometry or Sage work.
- `CONTRIBUTING.md`: editorial principles, audience classification, rule extraction, writing standards, and review criteria for contributors.
- `MAINTENANCE.md`: mechanical repository operations, version control, deployment, and canonical-storage procedure.
- `INCIDENTS.md`: source failures, classified by actor, with regression evidence and mappings to resulting rules.
- `CHANGELOG.md`: concise revision history.
- `README.md`: repository orientation, audience map, and file map.

Only `STYLE_GUIDE.md` should be uploaded as operational guidance to the custom GPT unless deployment documentation explicitly states otherwise.

## Writing assistant-facing rules

Assistant-facing rules must be:

- forward-facing and imperative;
- mathematically substantive;
- usable without knowing the originating conversation;
- specific enough to alter future behavior;
- general enough to cover nearby algebraic-geometric and Sage cases;
- grounded by examples only when the examples sharpen the rule.

Do not include:

- incident chronology;
- admissions, apologies, or explanations of previous mistakes;
- repository-management instructions;
- changelog language;
- claims about canonical files or prompt deployment;
- editor-facing advice about how to formulate rules.

Examples in `STYLE_GUIDE.md` are regression anchors, not provenance narratives. State what the assistant must do, not how the rule was discovered.

## Extracting rules from incidents

Do not reflexively append a literal prohibition for every noun or phrase appearing in an incident.

For each incident:

1. reconstruct the intended mathematical or operational task;
2. identify the actor that failed;
3. identify the underlying cognitive or process defect;
4. determine the likely neighboring tasks in which the same defect would recur;
5. formulate the smallest set of rules that blocks that failure class without erasing important concrete constraints;
6. retain Sage-specific or algebraic-geometric examples when they materially improve future behavior;
7. store detailed chronology and regression criteria in `INCIDENTS.md`, not in the assistant prompt.

Avoid both extremes:

- **incident overfitting:** encoding a catalogue of named examples instead of the governing failure mode;
- **destructive abstraction:** replacing operational mathematical constraints with slogans such as “be rigorous” or “think mathematically.”

A valid generalization must still prevent the source incident and nearby variants.

## Preserve mathematics and Sage specificity

This repository is not a generic software-engineering style guide. Contributor edits must preserve the fact that the assistant performs algebraic geometry research and detailed Sage computations.

When editing rules:

- prefer standard mathematical objects, morphisms, functors, diagrams, hypotheses, and universal properties;
- retain Sage parent/element ownership, existing API behavior, source inspection, execution, and backend constraints where operationally important;
- do not replace concrete algebraic-geometric guidance with generic object-oriented design language;
- do not invent terminology when standard mathematical language exists;
- verify nontrivial mathematical corrections before encoding them as standing guidance.

## Review checklist

Before committing a change, verify:

1. The intended audience of every changed paragraph is explicit.
2. No contributor instruction was placed in `STYLE_GUIDE.md`.
3. No substantive AG-assistant behavior exists only in contributor documentation.
4. The resulting assistant rule is forward-facing and independent of incident chronology.
5. The rule addresses the underlying failure class, not only the literal example.
6. Concrete mathematical and Sage constraints were not abstracted away.
7. Existing valid guidance was not weakened, contradicted, or silently removed.
8. Examples clarify behavior rather than dominate the rule.
9. Incident records identify whether the failure belongs to the AG assistant or to editors/maintainers.
10. Only files appropriate to the correction were changed.

## Contributions and repository workflow

Follow `MAINTENANCE.md` for canonical storage, commits, branch policy, deployment, and preservation checks.
