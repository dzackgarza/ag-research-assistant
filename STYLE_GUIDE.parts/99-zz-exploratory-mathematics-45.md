
## 45. Preserve exploratory mathematics before operationalizing it

A paper, book, database, lecture, or research conversation is not initially a task list. When extracting material from a source, first preserve the mathematics as mathematics: the objects, maps, equations, hypotheses, constructions, examples, conclusions, and relations among them. Do not immediately convert the source into a verification matrix, dependency ledger, checklist, ticket hierarchy, bounded agenda, or machine-checkable plan.

Research sources have more uses than supplying expected outputs. They can guide implementation, furnish examples and counterexamples, reveal algorithms, expose missing foundations, suggest generalizations, identify invariants, motivate experiments, connect separate constructions, and launch new questions. A rigid operational schema chosen too early can suppress precisely these uses.

### 45.1 Distinguish mathematical artifacts from operational artifacts

Keep the following artifact types conceptually separate.

1. **Source-derived mathematical exposition.** A faithful account of what the source defines, constructs, proves, computes, assumes, or observes.
2. **Computational commentary.** An explanation of which statements admit direct computation, theorem-mediated deduction, symbolic reproduction, numerical experiment, database comparison, or independent certification.
3. **Exploratory research notes.** Questions, variants, possible generalizations, parameter changes, conjectures, related examples, boundary cases, and connections suggested by the source.
4. **Verification and regression material.** Concrete examples or families whose expected behavior can check an implementation.
5. **Operational work tracking.** Assignments, statuses, prerequisites, destination files, bounded milestones, CI obligations, or subagent coordination.

These artifacts may refer to one another, but none should impersonate another. In particular, do not replace the mathematical exposition by the operational tracker. A source claim remains worth recording even when it is not currently computable, has no assigned notebook, or does not reduce to a Boolean pass/fail condition.

A research notebook may be a mathematical ledger in the sense that its objects, maps, assumptions, computations, and deductions are traceable. That does not make it a project-management ledger. Preserve this distinction.

### 45.2 Let the mathematical structure determine the organization

Organize source notes by the mathematics: constructions, diagrams, objects, morphisms, strata, examples, theorems, invariants, or conceptual themes. Use ordinary mathematical prose, displayed equations, precise maps, and theorem-style units when appropriate.

For each cluster of claims:

- state the mathematical assertion directly;
- name the objects and maps that relate its parts;
- present the calculation, proof, or cited theorem at the point where it is used;
- mention a possible computational realization only when it clarifies the mathematics or suggests a genuine experiment;
- record nearby questions, variants, and consequences in their natural mathematical context.

Do not wrap these points in a repeated narration of what the notebook has established, what the current code knows, or what stage of the investigation has been reached. The computation, displayed result, proof, and citation should carry that information. Add an explicit qualification only where the reader could otherwise mistake the strength or scope of the claim.

Do not force every statement into identical fields such as `status`, `destination`, `prerequisite`, `expected output`, and `verification method` unless the user has asked for that operational artifact. The source's mathematical dependencies need not coincide with a software work breakdown.

Headings and thematic lists are not the problem. The failure occurs when workflow metadata or commentary about the artifact becomes the primary representation of the mathematics and prematurely decides what is relevant, complete, computable, or worth retaining.

### 45.3 Keep source-derived notes generative and open-ended

When reading published mathematics for computational work, consider several uses simultaneously:

- reproduce a stated equation, degree, invariant, or diagram;
- independently check a theorem's hypotheses in explicit examples;
- compare two constructions or coordinate realizations;
- vary parameters, bases, singularity types, group actions, or divisor classes;
- search for boundary cases, failures, or counterexamples;
- generate families of examples and data;
- identify algorithms implicit in proofs;
- infer which general primitives the software lacks;
- formulate nearby conjectures or classification questions;
- connect the source to other papers, databases, formal libraries, or computational systems.

Do not close this space by declaring a finite list of source claims to be *the* verification agenda unless the user explicitly requests a bounded agenda. A paper-derived list should ordinarily be extensible: further reading and computation may add consequences, examples, or questions not visible during the first pass.

Treat published assertions as external mathematical benchmarks, not as values to hard-code. The code may reproduce, verify, falsify, illustrate, or explore them. Agreement with an expected result is evidence only to the extent supplied by the actual computation and comparison theorem.

### 45.4 Do not reduce computation to certification

Computational research has several legitimate modes:

- construction;
- exact calculation;
- theorem-backed deduction;
- certification;
- falsification;
- comparison;
- experimentation;
- example generation;
- pattern detection;
- conjecture formation;
- exploration of nearby cases.

A verification-oriented schema tends to privilege only certification and regression. Preserve the other modes. Some source statements should become exact regressions; others are conceptual guidance, theorem-derived consequences, examples to generalize, or questions whose computational form is not yet known.

Express epistemic distinctions through ordinary mathematical writing rather than running status labels. A displayed computation followed by its result is visibly computational. A sentence beginning “By Proposition 3.4” is visibly theorem-mediated. A concise remark can say that a construction remains open or that a displayed family is only a witness. Do not repeatedly announce that a notebook “has established,” “has verified,” or “has not yet completed” material that the surrounding mathematics already makes clear.

Do not require every item to possess a complete executable specification before it can appear in the research notes.

### 45.5 Use operational schemas only for a real coordination need

A checklist, matrix, issue list, dependency graph, or machine-checkable plan can be appropriate when the user asks for one, when several agents must coordinate, when CI must enforce a bounded contract, or when a mature research program needs an explicit implementation schedule.

Even then:

1. derive the operational artifact from a separately preserved mathematical account;
2. state that it is a current projection of the research program, not the mathematics itself;
3. keep it extensible unless completeness has been proved or requested;
4. distinguish mathematical prerequisites from engineering sequencing choices;
5. avoid excluding claims merely because their computational route is unknown;
6. keep internal agent bookkeeping out of the visible research narrative unless it helps the user;
7. update the tracker when exploration changes the mathematical picture rather than forcing the research to conform to the initial schema.

The assistant may maintain private or contributor-facing ledgers for its own work. It must not allow those tools to dictate the form or scope of the mathematical artifact.

### 45.6 Write prose notebooks as sources for future research

A source-derived prose notebook should remain useful to a mathematician who is not presently executing the implementation. It should record enough mathematics to support later reconstruction and investigation:

- the source's actual claims and notation;
- the relevant equations, morphisms, and commutative diagrams;
- hypotheses and logical dependencies;
- examples and special cases;
- how the claims interact;
- possible computational realizations;
- open mathematical or implementation questions;
- mathematically motivated extensions and experiments.

Write these as ordinary mathematical sections and remarks. The primary grammatical subjects should be the schemes, maps, divisors, groups, families, loci, and theorems—not “this notebook,” “this section,” “the current stage,” or “what has been established.” A brief mathematical introduction may orient the reader; it should not narrate the document's editing history, evolving task definition, or internal status.

Keep detailed task tracking in a separate section or artifact when it is useful. Do not make readers decode project-management fields or self-description in order to recover the mathematics.

### 45.7 Detect premature administrative closure

Pause and return to the source mathematics when:

- the first response to “record the paper's computational facts” is to design a matrix, agenda, ledger, or schema;
- every mathematical statement is immediately assigned a status, prerequisite, destination, or owner;
- the assistant declares a bounded list before the source has been mined openly;
- claims are omitted because no current backend can verify them;
- source order and conceptual relations are replaced by implementation dependency order;
- exploratory questions are rewritten as obligations with fixed expected outputs;
- more effort is spent designing the tracking format than explaining the mathematics;
- the notebook becomes intelligible mainly to the agent managing the work rather than to a mathematician studying the source;
- corrections from the conversation reappear as warnings or disclaimers in the notebook instead of being assimilated into its mathematical organization.

The correction is not to discard all structure. Restore the ordinary mathematical exposition first, preserve the source as a generative research object, and add operational structure only where it has a demonstrated purpose.
