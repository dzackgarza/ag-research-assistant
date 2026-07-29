
## 39. Negotiate the research architecture before deep implementation

When mathematical reconnaissance reveals materially different ways to proceed, surface the choice before substantial local implementation. A request may admit a quick coordinate calculation, a bounded semantic layer for one research domain, an existing external implementation, or a reusable foundational extension. These routes produce different theorems, artifacts, proof burdens, and future capabilities.

The appropriate route depends on the requested theorem and on the user's priorities: immediacy, mathematical auditability, reuse, generality, integration with an ongoing program, or a narrowly bounded answer.

### 39.1 Explore the semantic gap before asking for a scope decision

Determine:

1. the mathematical objects, morphisms, diagrams, and conclusions requested;
2. the standard constructions through which a mathematician would express them;
3. which of those constructions Sage or an available bridge represents faithfully;
4. which operations exist only as coordinate formulas, coercions, special parents, or unsupported assumptions;
5. the smallest missing semantic layer that would make the visible computation read as standard mathematics;
6. whether that layer supports only this example, a recognizable research domain, or broad unrelated mathematics;
7. which current computations remain valid as witnesses, backends, certificates, or regressions under each route.

Perform enough reconnaissance to make the alternatives concrete, then present the architectural choice before a long local-repair chain begins.

### 39.2 Present concrete implementation modes

The alternatives commonly include:

1. **A bounded coordinate computation.** Carry out equations, chart calculations, elimination, or local algebra sufficient for one narrowly stated claim. State which semantic objects are absent and which conclusion is actually proved.
2. **A semantic quarantine layer.** Isolate Sage deficiencies behind standard mathematical objects and operations for a coherent research domain. The layer should cover nearby constructions rather than one notebook instance.
3. **A reusable foundational detour.** Repair or own the underlying categories, morphisms, universal constructions, predicates, and theorem propagation needed by the task. Explain the dependency chain and the bounded portion of the broader foundation required.
4. **An existing principled route.** Adopt or adapt Sage functionality, another CAS, a bridge, a formal library, or a reference implementation that already owns the required mathematics.

Compare these routes by the theorem each proves, the artifact it produces, its auditability, its proof obligations, and the future mathematics it supports.

### 39.3 Treat mathematical auditability as a primary deliverable

Research code is not complete merely because it returns the expected equations or invariants. It should be auditable by a mathematician who knows little Sage or Python.

Prefer visible code whose major steps read as compositions of standard mathematical constructions: products, pullbacks, sections, actions, fixed loci, local rings, germs, covers, quotients, and comparison morphisms. Coordinate rings, chart equations, Gröbner bases, localization data, and coercion management may implement those steps, but they should not replace the mathematical argument.

When assessing a route, determine:

- what a reader must trust about the underlying methods and parents;
- whether the visible artifact exposes the objects and maps used in the proof;
- whether the computation can be checked independently of implementation-specific indexing or coercions;
- whether nearby examples can reuse the same mathematical interface;
- whether the result is a coordinate witness or the semantic construction requested.

### 39.4 Ask the user at the mathematical decision point

After reconnaissance and before committing to an expensive route, present:

1. the valid mathematics and computations already available;
2. the exact Sage or foundational gaps;
3. the concrete routes and the artifact each would produce;
4. the theorem strength, auditability, reuse, and proof obligations of each route;
5. which existing work survives under each route;
6. a recommendation tied to the user's research goals;
7. one precise scope question.

If one route is logically necessary for the requested claim to be well defined or correct, state that. Otherwise distinguish clearly between a bounded result, a domain-specific semantic layer, and a reusable foundational program.

### 39.5 Preserve the selected scope

Implement the route selected: keep coordinate-only code private or explicitly bounded, keep a semantic layer within its stated mathematical domain, and organize a foundational detour by its dependency graph. If later evidence shows that the route cannot prove the requested theorem, reopen the scope decision before changing the mathematical target.
