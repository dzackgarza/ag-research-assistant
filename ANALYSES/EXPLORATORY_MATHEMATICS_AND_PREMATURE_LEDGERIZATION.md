# Exploratory Mathematics and Premature Ledgerization

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** transcript concerning extraction of computationally meaningful assertions from a paper into a prose research notebook.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The assistant was asked to record mathematical facts from a paper that later notebooks should be able to reproduce, check, or investigate. Its first response was not to state the mathematics. It proposed a “computational verification agenda,” then a “verification matrix,” with fields for dependency, present status, foundational prerequisites, and destination notebook.

The failure is not merely an unattractive format. The assistant transformed an open research source into a bounded administrative object before understanding and preserving its mathematical uses.

The trajectory is:

\[
\text{published mathematics}
\longrightarrow
\text{finite list of verification targets}
\longrightarrow
\text{schema of statuses and dependencies}
\longrightarrow
\text{implementation contract}.
\]

This suppresses the source's role as exposition, example corpus, algorithmic guide, source of conjectures, and starting point for nearby investigations.

## 2. A research source is generative, not merely consumable

A paper can support many kinds of computational research:

- reproduce an equation, degree, divisor class, or singularity calculation;
- reconstruct a diagram of covers, quotients, actions, or lifts;
- independently test hypotheses or consequences in examples;
- extract an algorithm implicit in a proof;
- discover which semantic or algebraic foundations are absent from the current framework;
- vary parameters, bases, group actions, singularity types, or polarizations;
- search for boundary cases and counterexamples;
- produce families of examples and numerical data;
- compare with other papers, formal libraries, or databases;
- formulate generalizations and new questions.

A verification matrix ordinarily records only a narrow projection of this space: a claim, an expected result, prerequisites, and a completion state. That projection can be useful later, but it is not a faithful first representation of the research material.

## 3. Premature schemas make hidden mathematical decisions

A rigid schema does not merely organize neutral content. It implicitly decides:

- which claims matter;
- what counts as one item;
- which dependencies are mathematical rather than engineering choices;
- which notebook or workstream owns a statement;
- what form of evidence will count;
- whether the list is complete;
- whether a statement is worth recording before it is computable;
- whether the only legitimate computational use is verification.

Those decisions are often unknown during the first reading of a source. Fixing them early can prevent later recognition that one claim belongs to several constructions, that a proof yields a reusable algorithm, that an apparent regression suggests a family of experiments, or that the correct semantic foundation changes the computational decomposition.

## 4. Mathematical prose is not unstructured

The correction is not to replace every list by a shapeless narrative. Mathematical prose has its own rigorous structure:

- definitions and notation;
- named objects and morphisms;
- diagrams and equations;
- propositions and consequences;
- thematic sections;
- examples and special cases;
- logical and geometric dependencies;
- references to proofs and constructions.

For source-mining work, this structure should come first. The notebook can state what the paper claims, how the claims fit together, and what computations might reproduce or probe them. The mathematical organization remains legible even if no implementation status has been assigned.

## 5. Verification is only one computational mode

The assistant's phrase “verification targets” narrows computational mathematics to certification. In research, code may also:

- construct objects;
- falsify candidate statements;
- explore examples;
- generate data;
- compare models;
- detect patterns;
- test boundaries;
- suggest conjectures;
- reveal missing assumptions;
- discover a better formulation.

Some source claims should become exact regressions. Others are theorem-mediated deductions, guiding examples, prompts for generalization, or statements whose computational realization is itself an open problem. A prose note can preserve all of these roles without demanding a uniform executable contract.

## 6. Internal work tracking must remain subordinate

Agents and subagents may need ledgers, issue lists, dependency graphs, or machine-checkable plans. These are coordination devices. They should be separate from the mathematical research artifact unless the user explicitly asks for a combined document.

The distinction is especially important because “ledger” has two legitimate meanings in this project:

1. a **mathematical ledger**, where objects, maps, assumptions, computations, and deductions are traceable;
2. an **administrative ledger**, where tasks, statuses, owners, destinations, and prerequisites are tracked.

The first supports mathematical auditability. The second supports project management. Confusing them makes the visible notebook read like an agent control surface rather than research mathematics.

## 7. Correct source-mining workflow

A principled workflow is:

1. read and preserve the source-derived mathematics in its own terminology and conceptual organization;
2. state the relevant equations, maps, hypotheses, examples, and conclusions in ordinary mathematical prose;
3. annotate which parts current code computes, which follow by theorem, and which remain prospective;
4. record exploratory variants, questions, and connections suggested by the source;
5. extract concrete regression examples where appropriate;
6. only afterward, if coordination requires it, derive a separate implementation plan or verification matrix.

The operational artifact should be understood as a mutable projection of the research notes. New mathematical insight may change its items, dependencies, or scope.

## 8. Warning signs

The transcript exhibits several reusable warning signs:

- the assistant designs the schema before stating the claims;
- it says the “useful form” is a matrix rather than ordinary mathematical prose;
- it assigns destination notebooks before explaining the mathematical relations;
- it promises to make the source “operational” when the user asked to record and discuss it;
- it treats every statement as a future pass/fail obligation;
- it describes a closed agenda rather than a source for continuing investigation.

At any of these signs, the assistant should stop and ask what mathematical account a researcher would want to read independent of the implementation schedule.

## 9. General editorial rule

Editors should not encode a ban on the word “ledger,” on tables, or on structured planning. The general failure is **premature administrative closure**: allowing a coordination schema to determine the ontology, scope, and uses of research material before the mathematics has been preserved.

A good guide entry should therefore require:

- mathematical prose first;
- computational implications and exploratory directions second;
- operational tracking separately and only when useful;
- explicit openness to further facts and investigations;
- preservation of claims that are not yet computable;
- distinction between source assertions, actual computations, theorem deductions, and proposed experiments.

This prevents the assistant from converting exploratory research into a finite compliance exercise while retaining the legitimate uses of checklists and machine-readable plans in their proper domain.
