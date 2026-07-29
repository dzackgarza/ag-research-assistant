
## 44. Make mathematical development cumulative

Research progress must compound. A category, functor, universal construction, theorem, certificate, backend adapter, or convention established in one task should become a dependency of later tasks. Reconstructing a fresh local theory for each new problem changes mathematical levels and conventions, duplicates work, and prevents the framework from becoming more capable.

### 44.1 Recover the project foundation before substantial work

At the start of a task, after a context reset, and when resuming an old notebook, search the version-controlled project and connected sources. Inspect the relevant definitions, category declarations, prior decisions, tests, notebooks, analyses, and related repositories.

Recover:

1. the ambient categories and truncation conventions;
2. existing objects, morphisms, diagram categories, and universal constructions;
3. predicates, axioms, certificates, and theorem-propagation rules;
4. ownership and naming conventions;
5. backend implementations, bridges, and capability gates;
6. examples and regressions exercising the same mathematics;
7. recorded limitations and intended extension points.

Relate the current goal to these foundations and identify the smallest genuinely missing extension. Absence from the current conversation or one notebook is not evidence that the construction is absent from the project.

### 44.2 Resurvey during long work

Repeat the survey when:

- a new public noun, parent, category, or method is proposed;
- a second special-case helper resembles an earlier one;
- product, pullback, localization, quotient, factorization, equality, or comparison logic begins to reappear;
- a backend limitation tempts a change of categorical level or representation;
- local work grows into a family, gluing, descent, quotient, or moduli construction;
- a foundational primitive changes;
- the context, kernel, process, or collaborator changes;
- a major architectural pivot is contemplated;
- the user points out that an abstraction or operation already exists.

Reconcile the new work with the persisted foundation before adding further local patches.

### 44.3 Reuse by composition and extend at the natural owner

State which existing categories, functors, arrows, limits, colimits, predicates, and backend routes supply the new construction. Prefer composition and derived syntax to a parallel public method family.

When a genuine gap remains, extend the shared construction at its most general mathematically correct owner. The extension should:

1. state the exact mathematical datum or operation added;
2. preserve or explicitly transform the project's equality and coherence conventions;
3. supply the necessary comparison maps and universal witnesses;
4. route the motivating special cases through the shared primitive;
5. retain earlier examples as regressions;
6. gate unsupported presentations explicitly.

A duplicate implementation is justified only by a genuine mathematical or computational distinction. Provide the comparison map, equivalence, forgetful functor, or dispatch relation connecting it to the existing construction.

### 44.4 Propagate foundational refinements

A foundational extension is incomplete until dependent work uses it. Audit direct and indirect callers, convenience methods, duplicate local implementations, tests, documentation, notebook prose, backend adapters, and mathematical claims affected by the change.

Migrate valid special-case computations into the shared layer, remove obsolete public interfaces, and re-establish the required naturality, functoriality, and coherence statements. A general abstraction left unused while the motivating notebook continues through private code does not improve the project foundation.

### 44.5 Make foundations discoverable at their owning source

Document reusable mathematics where it is defined. The owning source should make clear the standard name and mathematical type of the construction, its ambient category, defining objects and morphisms, universal property, stable dependencies, implementation location, and intended extension points.

Use source definitions, mathematical documentation, module and symbol structure, tests, capability gates, and generated indices as the searchable record. Before declaring that an operation must be invented, search those sources.

### 44.6 Treat context loss as a retrieval problem

After an interruption or context reset, recover settled mathematics from the repository, local corpus, notebooks, decisions, and tests. If those sources are insufficient, repair the documentation at the construction's natural owner before building a parallel foundation.

The source of truth is the versioned artifact, not the current model context.

### 44.7 Repair foundation amnesia from the earliest divergence

When later work has rebuilt mathematics already present in the project:

1. freeze the parallel implementation;
2. identify the last point where the established foundation was still used;
3. map every local object, method, and theorem to the corresponding prior construction;
4. extend the prior construction only where a genuine gap remains;
5. migrate valid computations and tests into the shared layer;
6. remove or demote duplicate public interfaces;
7. re-audit downstream hypotheses, equality, naturality, and coherence;
8. improve discoverability at the owning source where needed.

Research work compounds only when refinements are consolidated into the common mathematical substrate.
