# State-Snapshot Prose and Synchronization Burden

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** user correction concerning self-announcing notebook prose, status tables, ledgers, phases, inventories, and other attempts to record the full state of a research artifact at one moment.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The failure is broader than verbosity or poor exposition. Coding agents frequently treat a human-facing research artifact as an external copy of their working memory.

They record:

- what the notebook currently contains;
- which cells or features are complete;
- which phase the work occupies;
- which claims have been verified;
- which methods exist;
- which limitations remain;
- how the investigation reached its current organization;
- a complete inventory of possible next steps.

This material appears useful to the agent at the instant it is written because it mirrors the agent's current internal state. It usually serves no durable reader. The user can inspect the notebook, and a later agent can recover the actual state from the versioned artifact, code, tests, outputs, and mathematical exposition.

The resulting pattern is

\[
\text{current artifact state}
\longrightarrow
\text{manual prose copy}
\longrightarrow
\text{artifact changes}
\longrightarrow
\text{stale prose and contradictions}.
\]

The problem is therefore a failure of audience modeling, temporal reasoning, and source-of-truth discipline.

## 2. A state snapshot is not mathematical documentation

Mathematical documentation explains objects and claims that remain meaningful when the implementation changes:

- what an object is;
- why it is being considered;
- where it lives;
- which maps relate it to other objects;
- which theorem or computation establishes a conclusion;
- which choice or convention is non-obvious;
- which references support the construction;
- which mathematical question remains open.

A state snapshot instead says that a particular collection of cells, methods, or subproblems is presently finished or unfinished. It has no independent mathematical content. Its truth depends on the exact physical state of the artifact at the moment of writing.

The notebook already contains that information more accurately. Repeating it in prose creates a second representation with no automatic synchronization.

## 3. Why the text becomes actively harmful

The cost is not merely that the prose is boring.

### 3.1 It creates synchronization obligations

Suppose a notebook records its state in an introduction, a roadmap, a phase table, section preambles, section conclusions, and a final status summary. A single new computation can require changes in all six places. Missing one update leaves the document inconsistent.

As the project grows, the assistant spends increasing effort searching for frozen descriptions of an older state rather than doing mathematics.

### 3.2 It obscures the authoritative source

When prose says that a construction is complete but the code no longer executes, or says that a limitation remains after the primitive has been implemented, the reader must decide whether to trust the prose, the cells, the tests, or the current source files.

The correct authority should be clear:

- mathematical claims belong to the proof, computation, or cited theorem;
- executable coverage belongs to the implementation and tests;
- historical state belongs to version control;
- unresolved mathematics belongs at the exact boundary where it arises.

### 3.3 It freezes an exploratory path

Phases, matrices, and exhaustive inventories make the current decomposition appear canonical. Research may later reveal that several listed tasks are one universal construction, that a purported dependency is merely an engineering choice, or that a paper suggests a different direction entirely.

A snapshot of today's plan can become an obstacle to tomorrow's mathematical reorganization.

### 3.4 It writes for no audience

The user usually knows what is being done. A mathematician reading the notebook needs the mathematics. A later agent can inspect the artifact. A collaborator needing project status should receive a deliberately scoped status report.

A paragraph whose only reader is the agent at the moment it externalizes its state has no place in the durable mathematical artifact.

## 4. Durable and transient information must be separated

A useful distinction is not “prose versus code” but **durable content versus transient state**.

### Durable content

Durable content includes:

- definitions, notation, maps, equations, and diagrams;
- mathematical motivation and the reason a cell or construction exists;
- non-obvious implementation choices that affect mathematical interpretation;
- theorem statements, proofs, citations, and comparison maps;
- hypotheses and scope conditions that change the claim;
- references to external mathematics;
- open mathematical questions and natural continuations.

### Transient state

Transient state includes:

- the current phase;
- lists of cells already written;
- declarations that the notebook “has established” what the preceding computation displays;
- manually maintained tables of implemented methods;
- completion percentages and status matrices;
- a full plan whose first steps are already underway;
- warnings preserving the history of earlier corrections;
- repeated descriptions of the present limitation in several sections.

Transient state may be useful privately or operationally, but it should not be copied into the durable mathematical narrative.

## 5. The useful forward-looking exception

One form of transient text is often genuinely useful: a concise pointer to the next mathematical step at the boundary where work stops.

For example:

> **Remark.** It remains to construct the quotient family over the full invariant parameter space.

This note preserves direction without pretending to describe the complete state of the project. It should be consumed. When the construction begins, the remark is replaced by the new mathematics or moved to the next unresolved boundary.

A forward pointer differs from a status snapshot:

- it records where the argument goes next, not everything currently present;
- it is local to the unfinished construction;
- it is deliberately temporary;
- its deletion is part of completing the work.

## 6. Version control, tests, and generated views have distinct roles

Historical snapshots belong in Git commits and diffs. Executable coverage belongs in tests and capability gates. Searchable architecture belongs in source definitions, module structure, symbol documentation, and generated indices.

When another audience genuinely needs a current status view, generate it from authoritative data where possible or maintain it as a separate artifact with an explicit owner. Do not make the research notebook carry a manually synchronized duplicate of the implementation state.

This also corrects an overreach in foundation-amnesia guidance. A reusable foundation must be discoverable, but discoverability does not require a prose inventory of every current consumer, backend, status, and limitation. Durable documentation should live with the construction; volatile coverage should be read from code and tests.

## 7. Relation to earlier failure modes

This failure unifies several observed tendencies:

- **self-announcement:** prose says that a cell or section exists instead of using its result;
- **premature ledgerization:** mathematics is converted into rows, statuses, and destinations;
- **reflexive editorial accretion:** corrections become permanent warnings;
- **foundation inventory growth:** reusable mathematics is duplicated into a manually maintained state description;
- **phase fixation:** session chronology becomes document structure;
- **completion narration:** the agent reports progress inside the artifact rather than simply making progress.

The shared cause is the belief that every momentary state must be explicitly represented in durable prose.

## 8. Editorial tests

For each status-like paragraph, determine:

1. What identifiable reader needs it?
2. What information does it add beyond the artifact itself?
3. Is it still useful after the next nearby edit?
4. Which source is authoritative if it disagrees with the code or tests?
5. How many places must be updated when the state changes?
6. Can it be generated, localized, shortened to a forward pointer, or deleted?

These questions are not a new notebook checklist. They are an editorial test for removing text before it becomes synchronization debt.

## 9. General correction

A mathematical research artifact should primarily preserve:

\[
\text{what the mathematics is}
\quad+
\text{why the construction matters}
\quad+
\text{how the claim follows}
\quad+
\text{where the mathematics naturally continues}.
\]

It should not attempt to preserve

\[
\text{a complete prose image of the artifact at time }t.
\]

The first form remains useful and supports cumulative research. The second becomes stale almost immediately, burdens every future edit, and eventually produces a chaotic document with no clear audience or source of truth.