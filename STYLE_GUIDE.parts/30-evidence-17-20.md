## 17. Computation, evidence, and verification

Distinguish clearly among:

- a mathematical construction that exists abstractly;
- a proposed Sage implementation;
- code that has been written;
- code that has executed;
- an output obtained from execution;
- a theorem-derived conclusion;
- an independently verified result.

Do not say “switching,” “constructing,” “implemented,” “fixed,” “verified,” or “decisive step” without evidence from the active notebook, source tree, or execution.

Headings, task labels, and status summaries are factual claims under the same standard. Do not write labels such as “Designed product structures” when only a possible direction has been formulated and no design artifact, implementation, or executed result exists.

Do not hard-code known classification facts as though they were computed. Construct the relevant maps, groups, rings, schemes, or isomorphisms required by the advertised computation.

Coinciding numerical invariants do not establish equality or isomorphism. Produce the relevant map, universal property, normal form, or proof.

## 18. Remediation discipline

When a proposed construction is challenged, return to the original mathematical requirement. Do not merely replace the vocabulary with more abstract terminology or add more cases.

Treat a user’s objection or counterexample as diagnostic evidence, not as a ready-made replacement architecture. Do not mirror the correction’s terminology and immediately announce that the system is “switching” to a categorical, semantic, universal, or backend-dispatched solution.

Before presenting a revised design:

1. reconstruct the original requested domain and output;
2. identify every independent defect in the previous proposal;
3. supply the missing mathematical objects, morphisms, hypotheses, and universal data;
4. determine what Sage already implements and what has actually been inspected or executed;
5. distinguish the mathematical correction from the proposed implementation strategy;
6. apply the native-primitives, bridge, reference-implementation, and literature escalation ladder;
7. test the revision against the supplied counterexamples and nearby cases;
8. report the result as proposed, implemented, executed, or verified according to evidence.

Abstract vocabulary is not evidence of correction. Calling an operation “categorical,” a layer “semantic,” or a construction “universal” does not establish that its defining data are complete, that it covers the intended domain, or that Sage implements it.

User-supplied examples may witness the intended scope. Do not turn them mechanically into a backend menu, but do not dismiss them as incidental until the revised construction has been shown to include them for the correct mathematical reason.

Check whether the remediation:

1. supplies the missing mathematical data;
2. corrects object ownership;
3. removes presentation dependence from the semantic interface;
4. preserves the original mathematical domain;
5. uses existing Sage semantics or an appropriate established bridge;
6. considers reference implementations and literature routes before deferral;
7. states implemented backend coverage and gates unsupported cases explicitly;
8. executes and verifies the computation claimed for the current input.

Do not narrow the semantic operation to the easiest supported presentation. Use assertion-gated or case-matched backend coverage when the general operation is mathematically correct but only special cases are computationally available. Implement a broader route when native primitives, a clean bridge, a reference implementation, or a citable algorithm makes it short and reusable. If the missing general backend is a substantial, nonessential diversion, record an actionable backlog strategy and continue the supported research computation. If the current result requires an unsupported branch, state the block or implement the necessary extension; do not claim completion. Do not treat the first counterexample named by the user as the complete specification.

## 19. Reporting style

Write in standard mathematical language. Prefer definitions, morphisms, diagrams, hypotheses, and precise return objects over software-design slogans.

Avoid invented engineering nouns when standard mathematical constructions exist. Do not describe a catalogue of classes and methods before explaining the mathematics they represent.

When reporting a missing Sage interface, organize the analysis in this order:

1. governing mathematical structure;
2. existing Sage representation and verified limitation;
3. mathematically correct ownership and primitive operation;
4. required hypotheses;
5. implementation strategy, including native, bridge, reference, or literature routes;
6. concrete notebook computations recovered from the interface;
7. executed verification.

The report must remain Sage-specific where Sage behavior matters, but its design must be controlled by algebraic geometry rather than by the accidental structure of one notebook.

## 20. Complete the abstraction chain

Do not stop mathematical reconstruction at the first implementation that is reusable, object-oriented, or more abstract than the preceding code.

Before accepting an interface, ask whether it is still merely:

- a coordinate helper for a standard geometric construction;
- a wrapper around a functorial map;
- a convenience object whose data are recovered by composition;
- a special case of a universal construction;
- an element-like object without its ambient parent;
- a presentation-specific realization of an intrinsic object.

Continue until the public interface is controlled by the standard mathematical construction, its parent or ambient category, its defining maps, and its hypotheses. Private backend helpers may remain presentation-specific.

A correction that moves from hard-coded coordinates to a helper, from a helper to a utility class, or from a utility class to a method has not necessarily reached the correct abstraction. Re-run the same completion test after every refactor.

