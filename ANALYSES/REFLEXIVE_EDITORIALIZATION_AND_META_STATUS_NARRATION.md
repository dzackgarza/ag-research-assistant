# Reflexive Editorialization and Meta-Status Narration

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** notebook excerpt on invariant \((4,4)\)-curves, double covers, lifts, and quotients, together with the user's correction that conversational scope clarifications had been inserted into the notebook as self-describing prose.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The notebook does not merely contain too much prose. It has allowed the history of the assistant-user interaction to become part of the mathematical artifact.

The opening says that the notebook “records a sequence of connected investigations,” explains that “there is no single immutable question,” enumerates six stages in the order the work developed, and adds a global warning that pencils or fibers do not replace universal questions. These sentences are intelligible as responses to earlier corrections. They are not the natural exposition of the mathematics.

The failure is

\[
\text{user correction}
\longrightarrow
\text{agent self-explanation}
\longrightarrow
\text{permanent notebook prose}.
\]

A correct edit should instead be

\[
\text{user correction}
\longrightarrow
\text{corrected claim or organization}
\longrightarrow
\text{ordinary mathematical exposition}.
\]

The notebook should preserve the result of the correction, not the conversational path by which the correction was obtained.

## 2. The artifact has become its own subject

Standard mathematical prose ordinarily makes objects and claims the grammatical subjects:

- the involution acts;
- the invariant subsystem has a given dimension;
- a divisor avoids the fixed locus;
- a cover admits two lifts;
- a quotient has specified singularities;
- a reflexive algebra reconstructs a cover.

Meta-status prose instead makes the artifact or workflow the subject:

- this notebook records;
- this section establishes;
- the investigation proceeds through stages;
- the next question changes;
- the notebook returns to the universal family;
- throughout, a pencil is only a witness.

The second mode is not more rigorous. It inserts a commentary layer between the reader and the mathematics. The reader must determine which sentences state mathematics and which sentences report the agent's current understanding of its own work.

## 3. Corrections were memorialized instead of assimilated

Several sentences in the excerpt can be read as fossils of previous corrections.

### No single central question

If the user corrects the assumption that one immutable question governs the notebook, the proper response is to remove a false thesis and organize the sections by their mathematical subjects. Writing

> There is no single immutable question governing every section.

does not improve the mathematics. It memorializes the correction.

### Pencil versus universal family

If a pencil was incorrectly allowed to stand for a universal parameter-space construction, every overstated claim must be repaired. At the first use of the pencil, a local sentence may state that it witnesses nonemptiness or supplies a regression example. A global warning in the introduction is unnecessary unless the distinction is genuinely central to understanding all later sections.

### Changing stages of work

The numbered list follows the chronology of the investigation: first invariant curves, then boundary phenomena, then one example, then a universal family, then a quotient, then a descended cover. Some of those dependencies may be mathematically natural, but the prose emphasizes how the work evolved. The notebook should instead use ordinary section headings and transitions determined by the mathematical dependency graph.

## 4. Epistemic precision does not require status narration

The project correctly requires distinctions among computed results, theorem-derived results, proposed work, and unsupported claims. The agent has interpreted this as a requirement to announce epistemic status in prose throughout the artifact.

The distinction can usually be made by ordinary mathematical form:

- code plus output or an assertion visibly records a computation;
- “By Proposition 2.7” visibly records a deduction;
- an `Assumption`, `Remark`, or hypothesis states a condition;
- “The construction over the full parameter space remains open” states one genuine limitation;
- an explicit question states a research direction.

A heading such as “What this notebook has established” adds no mathematical evidence. If a synthesis is useful, state a proposition or theorem collecting the conclusions, with precise hypotheses. If no synthesis is mathematically needed, omit it.

## 5. A better opening

The quoted opening can be reduced to a mathematical orientation such as:

> Let
> \[
> Y=\mathbf P^1\times\mathbf P^1
> \]
> with involution
> \[
> \tau([x_0:x_1],[y_0:y_1])=([x_0:-x_1],[y_0:-y_1]).
> \]
> We study the \(\tau\)-invariant subsystem of \(|\mathcal O_Y(4,4)|\), the associated double covers, the lifts of \(\tau\), and their quotients.

The notebook can then begin immediately with the section space and its invariant subspace. Later sections may be titled by the mathematical constructions:

- The invariant linear system;
- The smooth fixed-point-avoiding locus;
- Singular strata at the fixed points;
- The double cover and its lifts;
- The Enriques quotient;
- The quotient \(Y/\langle\tau\rangle\);
- Reflexive cover algebras at the nodes.

This organization incorporates the corrected scope without discussing the correction.

## 6. Footnotes and remarks are the correct scale for most limitations

An incomplete universal-family construction may matter. Its place is ordinarily one concise remark at the point where the explicit pencil or fiber appears:

> **Remark.** This pencil proves that the smooth fixed-point-avoiding locus is nonempty; it does not compute the full discriminant in the invariant parameter space.

That is a mathematical qualification. Repeating the same point in the introduction, transition paragraphs, section conclusions, and final status summary becomes warning diffusion.

Likewise, a missing reflexive-algebra construction can be stated where the descended cover is introduced. Completed sections need not carry repeated reminders about that future extension.

## 7. Introductions and roadmaps are not prohibited

A mathematical paper may contain a substantial introduction, motivation, and section roadmap. The defect is not the existence of introductory prose. The defect is that the roadmap reports the agent's process rather than explaining the mathematics.

A legitimate roadmap:

- explains why several constructions are connected;
- states the principal mathematical results or questions;
- helps the reader navigate a long argument;
- uses the final logical organization of the material.

An illegitimate roadmap:

- preserves the chronological order in which the agent discovered problems;
- answers earlier user complaints in prose;
- repeats status and scope warnings;
- announces which sections are complete;
- describes how the notebook's governing question changed.

## 8. Conversation-to-artifact leakage

This incident is part of a general failure mode. Agents are trained to acknowledge corrections explicitly in conversation. When editing an artifact, they may reproduce that acknowledgment inside the document:

- “To avoid conflating the pencil with the universal family...”;
- “Because there is no single immutable question...”;
- “At this stage the notebook has established...”;
- “The remaining limitation is...”;
- “This section corrects the earlier approach...”

Such sentences may be appropriate in a response, changelog, or incident report. In a mathematical notebook, they often amount to conversation-to-artifact leakage.

The editor must decide separately:

1. what the assistant should say to the user about the correction;
2. what the corrected mathematical artifact should contain.

The two texts need not resemble one another.

## 9. Required prevention

The assistant should apply three tests before preserving explanatory prose in a mathematical notebook.

### Mathematical-subject test

What mathematical object, map, theorem, calculation, or question is the sentence about? If the answer is only “the notebook” or “the current work,” move or delete it.

### Assimilation test

Does the sentence encode a correction that should instead alter a definition, claim, proof, code cell, or section structure? If so, make the substantive edit and remove the explanation.

### Locality test

Does a scope condition or limitation matter everywhere, or only at one construction? Put it at the smallest mathematically adequate scope: equation, paragraph, footnote, remark, or section.

## 10. Editorial rule

Do not encode a phrase blacklist. The general defect is **reflexive editorial accretion**: conversational acknowledgments, status tracking, and warnings become permanent layers of prose around the mathematics.

A valid guide entry should require:

- mathematical subjects rather than artifact subjects;
- corrected mathematics rather than correction history;
- local qualifications rather than global warnings;
- theorem-style synthesis rather than status summaries;
- section order determined by mathematical structure rather than work chronology;
- separate operational artifacts for progress and outstanding-work tracking.

A future reader should be able to study the notebook without knowing that an agent was repeatedly corrected while writing it.
