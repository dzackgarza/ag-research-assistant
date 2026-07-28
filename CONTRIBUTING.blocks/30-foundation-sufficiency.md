## Audit foundation sufficiency and detour decisions

When a transcript advances to descent, gluing, quotients, moduli, or another upper layer while generic infrastructure is still being invented inside the current example, audit whether the prerequisite mathematical foundation exists coherently.

Require the analysis to identify:

1. the upper-layer construction being attempted;
2. the categories, structured objects, arrows, and Hom-sets it presupposes;
3. the limits, colimits, localizations, quotients, tensor products, comparison cells, or other universal operations it requires;
4. which of those are genuinely present in Sage or the framework and which exist only as special formulas;
5. which current helper classes and certificates are foundational constructions in disguise;
6. whether successful examples prove only backend correctness or actual architectural completeness;
7. the minimal coherent foundation needed to state and verify the next layer;
8. whether that foundation is a bounded extension or a substantial scope-changing project;
9. which existing computations should be retained as backends, certificates, or regression tests;
10. whether the assistant surfaced the detour decision before continuing downstream work.

Flag **foundation evasion** when the assistant notices many missing primitives but continues higher-level implementation without deciding whether their common foundation must be built first. Flag **regression laundering** when successful special cases are presented as evidence that the general substrate is ready. Flag **downstream ownership inversion** when generic arrows, universal constructions, equality certificates, or theorem propagation are implemented inside a particular cover, family, or notebook layer.

Do not require an exhaustive foundational library. Require the smallest coherent subtheory needed by the current theorem and nearby constructions. It must include standard objects and morphisms, composition and comparison, universal constructions with their witnesses, theorem propagation where needed, and honest backend gates.

When the detour is bounded and clearly necessary, the assistant may take it directly. When it materially enlarges the project, the assistant should pause and present the user with the current valid results, exact foundational gap, dependency graph, minimal proposed foundation, expected reuse, and the alternative of preserving a narrower explicitly gated scope. The assistant should give a recommendation rather than ask an unstructured process question.

A valid assistant-facing rule should prevent the agent from rushing from partially patched local constructions into an ill-defined global layer merely because the next notebook cell can be written.
