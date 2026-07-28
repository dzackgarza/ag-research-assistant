
## 44. Make mathematical development cumulative

Real research progress requires the framework to remember its mathematics in versioned, searchable form and to reuse it. A category, functor, universal construction, theorem, certificate, backend adapter, or convention established in one task must become a dependency of later tasks. If every new problem is solved from first principles in a fresh local vocabulary, the project does not accumulate a foundation and sustained research becomes impossible.

Treat failure to recover and reuse established mathematics as a correctness failure, not merely duplicated code. Reconstructing a weaker local theory can change the ambient category, equality convention, theorem strength, functoriality, and coherence of the work.

### 44.1 Recover the actual project foundation before beginning substantial work

At the start of a task, after a context reset, and when resuming an old notebook, search the version-controlled project rather than relying on conversational memory. Inspect relevant source files, symbol definitions, category declarations, prior decisions, analyses, tests, notebooks, and connected repositories.

Identify at least:

1. the ambient categories and truncation conventions already in force;
2. existing objects, morphisms, diagram categories, and universal constructions;
3. available predicates, axioms, certificates, and theorem-propagation rules;
4. established ownership and naming conventions;
5. current backend implementations, bridges, and explicit gates;
6. earlier examples and regressions that exercise the same mathematics;
7. unresolved limitations or planned extensions already recorded.

Before writing new public code, form a reuse map

\[
\text{current goal}
\longrightarrow
\text{existing foundational constructions}
\longrightarrow
\text{smallest genuinely missing extension}.
\]

Do not infer that a construction is absent because it is not present in the current chat context or immediately visible in one notebook.

### 44.2 Resurvey periodically during long work

A single survey at task start is insufficient. Reopen the project foundation whenever any of the following occurs:

- a new public noun, parent, category, or method is proposed;
- a second special-case helper begins to resemble an earlier one;
- an implementation starts reproducing products, pullbacks, localizations, quotients, factorization, equality, or comparison logic;
- a backend limitation tempts the work to change categorical level or representation;
- the task changes from a local computation to a family, gluing, descent, quotient, or moduli construction;
- a foundational primitive is extended during the session;
- a context window, kernel, process, or collaborator changes;
- a limitation, completion claim, or major architectural pivot is about to be reported;
- the user points out that an abstraction or operation was already implemented.

At each trigger, stop adding local patches until the current work has been reconciled with the versioned foundation.

### 44.3 Reuse by composition before reimplementation

Every new construction should state which existing categories, functors, arrows, limits, colimits, predicates, and backend routes it composes. Prefer derived syntax and composition over a parallel method family.

A duplicate implementation is justified only when there is a genuine mathematical or computational distinction, such as a different ambient category, hypotheses, backend representation, or algorithmic regime. In that case, provide the comparison map, equivalence, forgetful functor, or dispatch relation connecting it to the existing construction. Do not let two unrelated public interfaces silently claim to implement the same mathematics.

### 44.4 Extend the foundation at its natural owner

When an existing abstraction is nearly sufficient, extend it rather than routing around it in the current example. Add the missing datum or operation at the most general mathematically correct owner, preserve the established categorical level, and use assertion or capability gates for unsupported presentations.

A foundational extension should:

1. state the exact mathematical object or operation being added;
2. identify the existing construction it extends;
3. preserve or explicitly transform the project’s equality and coherence conventions;
4. supply the necessary comparison maps and universal witnesses;
5. route current special cases through the extended primitive;
6. retain earlier examples as regressions;
7. expose unsupported cases honestly rather than creating a second local theory.

Do not confuse reuse with freezing an inadequate foundation. Cumulative research sometimes requires repairing, strengthening, or replacing an earlier primitive; the requirement is that the improvement be assimilated into the shared foundation.

### 44.5 Propagate refinements through dependent work

A foundation is not improved merely because a new general class or method exists. Update downstream constructions to use it, remove obsolete parallel helpers, and re-establish every affected theorem, naturality square, and regression.

After a foundational change, audit:

- direct and indirect callers;
- convenience methods that should become derived syntax;
- duplicated local implementations;
- tests written at an older categorical level;
- documentation and notebook prose using superseded terminology;
- backend adapters whose contracts must now preserve additional structure;
- claims of completeness or correctness that depended on the old primitive.

A general abstraction left unused while the motivating notebook continues through its old private code is not cumulative progress.

### 44.6 Maintain a versioned foundation inventory

Keep a searchable record of the project’s reusable mathematics. This may be encoded in source documentation, a dependency graph, symbol indices, construction registries, or dedicated foundation notes; it need not become a separate bureaucracy. It must nevertheless let a later agent recover:

- the standard name and mathematical type of each construction;
- its ambient category and categorical level;
- its defining objects, morphisms, and universal property;
- the source location of its implementation;
- dependencies on earlier constructions;
- derived consumers and convenience interfaces;
- backend coverage and capability gates;
- theorem, certificate, and regression status;
- known limitations and intended extension points.

Update this inventory when a foundation is added, refined, replaced, or deprecated. Query it before declaring that an operation must be invented.

### 44.7 Treat context loss as a retrieval problem, not permission to restart

After a long interruption or context reset, do not reconstruct the theory from recollection and do not ask the user to restate settled foundations. Recover the state from the repository, local corpus, notebooks, decisions, and tests. If the persisted records are insufficient, identify that documentation gap and repair it before building a parallel foundation.

The project’s source of truth is the versioned artifact, not the current model context. Memory loss must trigger retrieval, not reinvention.

### 44.8 Define progress by compounding capability

At the end of substantial work, state internally and, when useful, visibly:

1. which prior foundations were reused;
2. which foundation was extended or corrected;
3. which new construction is now available to later work;
4. which earlier special cases were migrated to it;
5. which new regressions and comparison theorems protect the extension;
6. which limitations remain explicitly gated.

A one-off computation may answer a bounded research question, but it should not be described as framework progress unless its valid mathematics has been integrated into the reusable foundation. The cumulative loop is

\[
\text{survey}
\longrightarrow
\text{reuse}
\longrightarrow
\text{extend}
\longrightarrow
\text{propagate}
\longrightarrow
\text{record}
\longrightarrow
\text{reuse again}.
\]

### 44.9 Repair foundation amnesia from the earliest divergence

When later work has rebuilt mathematics already present in the project:

1. freeze the parallel implementation;
2. identify the last point where the established foundation was still being used;
3. map every local object, method, and theorem to the corresponding prior construction;
4. extend the prior construction only where a genuine gap remains;
5. migrate valid computations and tests into the shared layer;
6. remove or demote duplicate public interfaces;
7. re-audit downstream claims for changed hypotheses, equality, naturality, and coherence;
8. update the foundation inventory so the same failure cannot recur after another context reset.

Do not preserve a parallel foundation merely because time has been invested in it. Research work compounds only when improvements are consolidated into the common mathematical substrate.
