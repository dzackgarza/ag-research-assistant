
## 38. Stop when the required mathematical foundation is not yet coherent

Do not continue building higher-level geometry merely because each immediate special case can be patched. Before beginning descent, gluing, moduli, quotient, or other derived constructions, verify that the mathematical layer they depend on exists coherently enough to state and prove the next operation.

A collection of working examples is not a foundation. Passing regressions for selected rings, charts, covers, or morphisms does not show that the ambient categories, morphisms, universal constructions, and comparison principles required by the global theory are present.

### 38.1 Run a foundation-sufficiency audit

When downstream code starts acquiring generic-looking helpers, audit whether they belong to a missing foundational layer. Identify at least:

1. the ambient categories and their objects;
2. the actual morphisms, Hom-sets, identities, composition, and relation used to compare composites;
3. the relevant arrow, slice, coslice, diagram, or structured-object constructions;
4. the limits, colimits, quotients, localizations, tensor products, base changes, or other universal operations required;
5. the certificates or universal properties that verify those constructions;
6. the axioms and theorem-propagation rules needed by later dispatch;
7. the supported computational presentations and the gates for unsupported ones.

If these items are being implemented piecemeal inside a Čech complex, a cyclic-cover class, a quotient family, or another downstream object, the ownership boundary is wrong. Move the general mathematics to the foundational layer before adding more global structure.

### 38.2 Recognize foundation debt before it becomes patch accretion

Treat the following as evidence that the current task is resting on an incoherent substrate:

- several unrelated downstream constructions need new versions of the same arrow, localization, quotient, product, pullback, or equality machinery;
- canonical maps exist only as coercions, callables, or side metadata rather than morphisms in the advertised category;
- universal properties are replaced by presentation-specific formulas or path-normalization rules;
- each new parent implementation requires a different compatibility patch;
- higher-level proofs rely on operations whose mathematical contract is not represented;
- the next layer presupposes descent, gluing, functoriality, or theorem propagation that has not been defined;
- the code can certify selected examples but cannot state the general construction they are examples of.

Do not describe such work as “almost complete” because the current research example executes. Record the examples as regression tests for the eventual foundation.

### 38.3 Choose explicitly among continuation, foundational detour, and a hard gate

After the audit, classify the situation:

1. **The foundation is sufficient.** The remaining defect is a bounded backend implementation. Repair, shadow, bridge, or gate that backend and continue.
2. **A bounded foundational detour is required.** The missing layer is standard, well scoped, and directly unlocks the current work. Implement it first, move generic patches into it, and resume from the resulting abstractions.
3. **A substantial foundational detour is required.** Correct continuation would materially enlarge the project. Pause before doing more downstream work and present the user with:
   - the current valid mathematical and computational results;
   - the exact foundational gap;
   - the dependency chain showing why the requested next step requires it;
   - the minimal coherent foundation needed;
   - which existing patches become backends or regressions;
   - the alternative of preserving the present scope with an explicit unsupported gate.
4. **No correct route is presently known.** State the block and the research needed to resolve it. Do not continue with ill-defined approximations.

When the foundational detour materially changes scope, ask the user whether to take it. Give a mathematical recommendation and concrete alternatives; do not ask a vague process question. If the missing foundation is logically necessary for correctness, say so explicitly rather than presenting continued downstream patching as an equivalent option.

### 38.4 Build the minimal coherent foundation, not an imagined total library

Stopping for foundations does not require implementing all of mathematics. Determine the smallest coherent subtheory that supports the active theorem and nearby constructions. It must nevertheless have standard objects and morphisms, compositional ownership, universal constructions with their witnesses, and honest backend coverage.

Preserve successful specialized work by relocating it:

- coordinate formulas become backends for general constructions;
- special equality checks become certificates in the relevant Hom-set or diagram category;
- chart computations become regressions for affine and descent layers;
- family examples become downstream integration tests.

Do not discard correct computations, but do not let them define the foundation retroactively.
