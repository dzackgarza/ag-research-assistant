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

## Decompose incidents before generalizing

A single incident may expose several causally independent defects. Do not assume that every correction has one “smallest invariant principle,” or that the best edit is the shortest possible sentence. The goal is the smallest **sufficient** rule set: every material failure must be blocked without duplicating rules that truly have the same cause.

Analyze at least the following dimensions when they are present:

- the mathematical-semantic defect;
- the Sage representation, API, or source-audit defect;
- the implementation-coverage defect;
- the computation, evidence, or status-reporting defect;
- the defect in the assistant’s response to correction;
- the editor’s own extraction, drafting, or preservation defect.

Combine dimensions only when one operational rule genuinely prevents all of them. Do not erase a separate requirement merely because the failures occurred in the same paragraph.

Avoid oscillating between two invalid editing modes:

1. **incident transcription:** copying every named variety, backend, phrase, or counterexample into the standing guide;
2. **slogan compression:** reacting to that overfit by replacing all concrete requirements with one broad principle.

Concrete examples can have different roles:

- a **scope witness** showing that the intended domain is broader than the implementation;
- a **regression case** against which a rule must be tested;
- evidence that reveals an underlying cognitive defect;
- an incidental detail that need not appear in the assistant-facing guide.

Classify each example by its role. Do not automatically preserve every example as a rule, and do not automatically discard every example after stating an abstraction.

Before claiming that an incident has been incorporated, maintain a coverage map from each material source failure to at least one resulting clause or regression criterion. The edit underfits when any original defect could recur while all new wording is technically obeyed.

## Preserve semantic generality without forcing total implementation

Do not encode a blanket prohibition on assertion gates, case dispatch, `NotImplementedError`, or other explicit implementation boundaries. These mechanisms are often required to keep a mathematically general interface while Sage only computes special cases.

When an incident concerns limited computational coverage, require the assistant-facing rule to distinguish:

1. the most general mathematical object or construction to which the operation applies;
2. the special cases Sage already handles and can route directly;
3. whether existing Sage primitives compose into the general case with modest effort;
4. whether an established bridge to GAP, Singular, Macaulay2, Magma, Julia, PARI/GP, or another system already supplies the missing primitive or algorithm;
5. whether a general reference implementation can be followed or reproduced without substantial new design;
6. whether a paper, book, or citable theorem gives a direct algorithm or reduction;
7. whether implementing that route now is proportionate to the active research task and likely reuse.

The resulting guide should favor a principled escalation ladder:

- route verified native Sage cases first;
- compose existing Sage primitives when the generalization is short and reusable;
- use a clean existing bridge when it already owns the needed mathematics;
- adapt a reliable reference implementation when integration is straightforward;
- implement a literature algorithm when the translation is sufficiently bounded and valuable;
- otherwise preserve the general interface, gate unsupported backends explicitly, and record a backlog item with a concrete implementation strategy.

Do not label the last option as degradation or task narrowing. The semantic domain remains general; only current executable coverage is partial. Conversely, do not let a general method name conceal that the current input is unsupported.

Editors must preserve the research-scope judgment. A short, reusable foundational extension is often worth implementing immediately. A substantial backend project that is not needed for the present supported computation should not derail the research conversation; it should become an actionable backlog entry. If the current computation itself requires the unsupported branch, the assistant must either implement the minimum correct extension or report the block.

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
11. Every independent source defect maps to a resulting rule or regression criterion.
12. The edit avoids both incident transcription and slogan compression.
13. Any claim that the correction is complete follows a coverage audit rather than verbal agreement.
14. Semantic scope and implemented Sage coverage are distinguished explicitly.
15. Assertion gates preserve a general interface rather than masquerading as mathematical nonexistence.
16. The native-Sage, bridge, reference-implementation, and literature routes were considered before substantial new backend work was deferred.
17. A deferred generalization has an actionable strategy, not a vague TODO.

## Contributions and repository workflow

Follow `MAINTENANCE.md` for canonical storage, commits, branch policy, deployment, and preservation checks.

## Analyze correction trajectories

For long transcripts, do not treat each user correction as an independent incident. Build a correction trajectory.

For each recurring topic:

1. record the assistant's initial abstraction level;
2. record each user correction;
3. record the assistant's attempted remediation;
4. determine whether the remediation removed the root defect or merely moved it one layer;
5. identify the first point at which the standard mathematical construction was reached;
6. identify stale downstream code or prose left by earlier rungs.

A repeated sequence of coordinate code, helper function, utility namespace, object method, parent method, and ambient-category construction is evidence of **premature abstraction closure**. Contributor guidance should require the assistant to complete the abstraction chain, not merely move one rung upward after each objection.

Analyze the whole trajectory before drafting a rule. The final assistant response may be correct while concealing a long-lived failure mode that will recur elsewhere.

## Distinguish surface symptoms from causal failures

A source complaint can name a symptom without naming the cause.

Examples:

- “This looks hard-coded” may indicate answer-first computation, representation capture, or failure to use a universal construction.
- “This API is not semantic” may indicate missing parents, functoriality, variance, compositionality, or local-to-global data.
- “The notebook is hard to follow” may indicate theory left in chat, monolithic cells, missing intermediate objects, or tests mixed into narrative.
- “The assertion is overfit” may indicate false canonicity rather than a general objection to assertions.
- “Sage should know this” may require a source audit, a native patch, a correct shadow, or a bridge rather than a new wrapper.

For every proposed rule, state the causal failure it prevents. Reject rules that merely prohibit the vocabulary of the source complaint.

## Preserve positive and negative evidence

Incident analysis should record not only failures but also turns where the assistant correctly resisted or corrected the user.

Positive examples are especially valuable when they demonstrate:

- testing a user conjecture rather than agreeing;
- producing a counterexample;
- distinguishing a theorem deduction from a computation;
- identifying a descent or gluing obstruction;
- correcting variance or functoriality;
- refusing to claim a global object from local data.

Use positive examples as regression anchors for desired behavior. Do not write guidance that would punish the assistant for correctly challenging the user.

## Audit rule strength against recurrence

Before committing an assistant-facing rule, test it against every recurrence of the failure in the source transcript.

A rule is too weak when the assistant could obey it while still:

- hard-coding the expected answer;
- stopping at a reusable but nonstandard wrapper;
- promoting local data to a global object;
- asserting representation-sensitive equality;
- leaving theory outside the artifact;
- failing to propagate a corrected primitive downstream.

A rule is too broad when it prohibits valid capability gates, useful coordinate specializations, requested full output, or theorem-backed deductions.

Record the result of this strength audit in the analysis or incident record.

## Treat artifact-state failures as substantive incidents

Notebook corruption, stale cells, wrong kernels, duplicate imports, nonpersisted edits, and prose/code contradiction are not merely operational inconveniences. They invalidate mathematical and computational claims.

When a transcript contains an outage or state discontinuity, contributors must inspect whether the assistant:

- relied on live-kernel state;
- reopened the persisted artifact;
- verified the kernel and dependency graph;
- performed a clean execution;
- audited stale narrative and duplicate cells;
- rechecked downstream conclusions.

Add assistant-facing artifact-discipline rules and regression criteria when these obligations were missed.
