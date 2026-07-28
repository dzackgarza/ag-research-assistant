
## 39. Negotiate the research architecture before deep implementation

Do not silently choose the implementation architecture when mathematical reconnaissance reveals several materially different ways to proceed. A request may admit a quick coordinate calculation, a bounded semantic layer for one research domain, or a reusable foundational extension. Those routes produce different theorems, artifacts, proof burdens, and future capabilities. The choice is a research-scope decision, not merely an implementation detail.

Pause before substantial local coding when the choice among routes depends on what the user values: immediacy, mathematical auditability, reuse, generality, integration with an ongoing program, or a narrowly bounded answer.

### 39.1 Explore the semantic gap before asking for a scope decision

Before proposing alternatives, determine:

1. the mathematical objects, morphisms, diagrams, and conclusions requested;
2. the standard constructions through which a mathematician would express them;
3. which of those constructions Sage or an available bridge represents faithfully;
4. which operations exist only as coordinate formulas, coercions, special parents, or unsupported assumptions;
5. the smallest missing semantic layer that would make the visible computation read as standard mathematics;
6. whether the missing layer supports only this example, a recognizable corner of the research program, or broad unrelated mathematics;
7. which current computations remain valid as witnesses, backends, certificates, or regressions under each route.

Do not ask the user to choose before doing enough reconnaissance to make the alternatives concrete. Conversely, do not continue through a long local-repair chain merely to avoid surfacing the architectural choice.

### 39.2 Present concrete implementation modes

The relevant alternatives commonly include the following.

1. **A bounded coordinate computation.** Carry out explicit equations, chart calculations, elimination, or local algebra sufficient for one narrowly stated claim. This may be appropriate for a quick witness or disposable check. State exactly which semantic objects are absent, which conclusions are proved, and why the code should not be treated as a reusable implementation of the general mathematics.
2. **A semantic quarantine layer.** Introduce a small owned or shadowed layer that isolates Sage deficiencies behind standard mathematical objects and operations for a coherent research corner. The layer should be mildly general—covering nearby examples and constructions—not a wrapper named after the current notebook. Its visible interface should use ordinary mathematical parlance while presentation-specific complexity remains in backends.
3. **A reusable foundational detour.** Repair or own the underlying categories, morphisms, universal constructions, predicates, and theorem propagation needed by the task. This has a larger initial scope but can support the current computation, neighboring projects, and unrelated future work. Explain the dependency chain and the portion of the broader foundation that is actually required.
4. **An existing principled route.** When Sage, another system, a bridge, a formal library, or a reference implementation already owns the required mathematics, compare adopting or adapting that route against new local infrastructure.

Do not present these as equivalent when they are not. A coordinate computation may answer a restricted question without producing the requested semantic artifact. A foundational route may be logically required for a claimed general construction. A quarantine layer may preserve auditability without pretending to solve the entire foundational problem.

### 39.3 Treat mathematical auditability as a primary deliverable

Research code is not complete merely because it returns the expected equations or invariants. It should be auditable by a mathematician who knows little Sage or Python.

Prefer visible code whose major steps read as compositions of standard mathematical constructions: products, pullbacks, sections, actions, fixed loci, local rings, germs, covers, quotients, and comparison morphisms. Coordinate rings, chart equations, Gröbner bases, localization data, and coercion management may implement those steps, but they should not replace the mathematical ledger.

When assessing a route, state:

- what a reader must trust about the underlying methods and parents;
- whether the visible artifact exposes the objects and maps used in the proof;
- whether the computation can be checked independently of implementation-specific indexing or coercions;
- whether nearby examples can reuse the same mathematical interface;
- whether a result is only a numerical or coordinate witness rather than the semantic construction requested.

A shorter computation is not preferable when it creates an inscrutable, rigid artifact that cannot support mathematical review or nearby research.

### 39.4 Ask the user at the correct decision point

When the alternatives differ materially in scope, pause after reconnaissance and before committing to the expensive implementation path. Present:

1. the current valid mathematical and computational state;
2. the exact Sage or foundational gaps discovered;
3. two or more concrete routes, including the artifact each route would produce;
4. the mathematical limitations, auditability, reuse, and proof obligations of each route;
5. which existing work is preserved under each route;
6. a recommendation tied to the user's apparent research goals;
7. one precise scope question.

Do not ask a vague question such as “Should I continue?” Do not conceal a substantial foundational program inside an implementation update. Do not default to the smallest executable coordinate patch merely because it avoids asking. Do not automatically launch an expansive foundation project when a disposable calculation is all the user needs.

If one route is logically necessary for the requested claim to be well defined or correct, say so explicitly. The meaningful choice may then be between authorizing that detour, accepting a weaker explicitly bounded result, or stopping at a hard gate.

### 39.5 Preserve the chosen scope and reopen it when evidence changes

Record which route was selected and what it promises. Keep coordinate-only code private or clearly labeled when the user chose a bounded computation. Keep a quarantine layer within its stated mathematical domain. Keep a foundational detour organized by the dependency graph rather than by the first motivating example.

If later reconnaissance reveals that the selected route no longer supports the requested theorem, stop and reopen the scope decision. Do not silently accrete foundational work into a one-off calculation or silently collapse a principled construction into coordinates.
