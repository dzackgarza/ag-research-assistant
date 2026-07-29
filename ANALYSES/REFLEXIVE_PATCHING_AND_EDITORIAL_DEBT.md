# Reflexive Patching and Editorial Debt

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** audit requested after repeated correction chains in which an editor misread an instruction, then added a permanent rule forbidding its own misreading.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The repository had begun to preserve some editing mistakes as assistant-facing behavior. The recurring sequence was

\[
X
\longrightarrow
X'
\longrightarrow
\text{“not }X'\text{”}
\longrightarrow
\text{“do }X\text{ and never }X'\text{.”}
\]

Here \(X\) is the user's intended principle, \(X'\) is the editor's mistaken interpretation, and the last clause is a reflexive patch. It would never have been written if the editor had understood \(X\) correctly on the first pass.

This produces several forms of debt:

- the deployed prompt records editor history rather than AG-assistant behavior;
- positive principles are surrounded by defensive exceptions;
- one correction creates a second section instead of revising the first;
- concrete examples become standing anti-examples;
- the guide grows without gaining mathematical coverage;
- later editors must reconcile rules whose conflict exists only because of an earlier misread.

The correct response to rejection of \(X'\) is ordinarily to remove \(X'\), recover \(X\), and rewrite the original clause. A counterrule belongs in the prompt only when source AG-assistant behavior independently demonstrates the opposite failure.

## 2. Counterfactual test

For each corrective clause, ask:

> Would this rule exist if the immediately preceding user instruction had been interpreted correctly?

If the answer is no, the clause is editorial residue. Delete it from the assistant prompt and preserve the history, if useful, in the changelog or contributor analysis.

A second test is source attribution:

> Which transcript shows the deployed AG assistant committing this failure?

An editor's one-turn mistake is not evidence about the deployed assistant.

## 3. Findings in the audited style guide

### 3.1 Transcript-specific evidence phrases

Section 17 still named the exact words and heading from the original toric-product exchange—“switching,” “decisive step,” and “Designed product structures.” Those phrases came from the first overfitted attempt to encode the incident. They were replaced by the durable rule that every claim of design, implementation, execution, correction, verification, or completion requires corresponding evidence.

Section 18 likewise repeated the editor's own imagined “switching to a categorical solution” response. It now requires independent reconstruction of the original mathematics before adopting terminology or architecture from a correction.

### 3.2 Paired converse clauses

Several sections used a pattern of asserting the desired principle and then appending “Conversely, do not...” to guard against an editor-created opposite:

- parameter schemes constructed by the same formalism;
- equality versus higher comparison cells;
- external CAS reuse versus native Sage implementation;
- timing of interactive architecture decisions.

These were rewritten as single positive decision rules. The exact mathematical relation, source of ownership, or research decision now determines the behavior directly.

### 3.3 Ledger language

The guide's “mathematical research ledger” and “derivation ledger” terminology risked reinforcing the same schema-first tendency criticized elsewhere. The intended content was auditability: visible objects, parents, maps, hypotheses, computations, and proof obligations. Section 32 now describes an auditable mathematical argument, and Section 43 asks for an explicit universal-object derivation rather than a ledger.

### 3.4 Ontological coherence and semantic lock-in

Sections 41 and 42 had grown additively after two corrections:

1. classify a coined abstraction mathematically;
2. recognize that hours of dependent work can become self-sealing.

The distinction is real, but the sections repeated decomposition, source search, remediation, and downstream audit. They are now separated by role:

- Section 41 types a proposed abstraction and distinguishes objects, statements, evidence, and algorithms;
- Section 42 governs longitudinal revalidation and the semantic stop-loss after dependence accumulates.

Progress-report wording and repeated remediation lists were removed.

### 3.5 Localization overfitting

The localization correction contained important mathematics, but the guide had reproduced a long operation-specific derivation and then appended warnings not to treat it as the universal template. This was the same overfit/counterrule pattern.

Section 43 now states the general derivation

\[
\text{diagram category}
\to
\text{admissible subcategory}
\to
\text{universal object}
\to
\text{mapping object}
\to
\text{computational component},
\]

and retains localization as one concise example. The full technical discussion remains in contributor analyses.

### 3.6 Foundation inventories and progress narration

Foundation-amnesia guidance had acquired clauses explaining that inventories should not become status prose and that cumulative progress should not be narrated. Those clauses existed because earlier editorial revisions had overextended the idea of a foundation inventory.

Section 44 now states the positive cumulative practice: retrieve, resurvey, compose, extend at the natural owner, propagate, and document at the owning source. Volatile state and progress-explanation topics were removed.

### 3.7 Transcription-typo rule

The semantic-pseudocode section contained a standing rule about charitably repairing isolated symbol typos. It was added only because the editor misread `pi` for the plainly intended `i_dP` and then generalized its own mistake. That paragraph was removed from the deployed guide. The correction remains historical contributor evidence, not AG-assistant behavior.

### 3.8 Category-refinement counterbalancing

The Sage category section ended with “category refinement is not universally preferable,” a defensive formulation created by balancing earlier category-refinement advice. It now states one ownership rule: use a category hierarchy for uniform structure, justified refinement for an existing parent already satisfying it, and targeted repairs or shadows for implementation-specific behavior.

## 4. Rules retained after the audit

The audit did not remove every two-sided distinction. Several are independently supported by the mathematics and source transcripts:

- semantic generality with partial assertion-gated backend coverage;
- interactive choice among a bounded calculation, a domain-specific semantic layer, an external implementation, and a foundational detour;
- distinction between a mathematically undefined operation and an unimplemented backend;
- distinction between the full categorical comparison datum and a computational component;
- preservation of exploratory mathematical prose alongside separate coordination artifacts.

These survive because both sides describe real research choices or failure modes, not because an editor once misstated the rule.

## 5. Editorial policy

Future corrections should modify the earliest incorrect canonical clause. Editors should not append a new exception, warning, or section until they have determined that the opposite behavior occurs independently in the AG-assistant source material.

The deployed prompt should contain durable forward-facing mathematical behavior. Editing history belongs in version control, changelogs, incident records, and analyses.
