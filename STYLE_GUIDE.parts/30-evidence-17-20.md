## 17. Computation, evidence, and verification

Distinguish clearly among:

- a mathematical construction that exists abstractly;
- a proposed Sage implementation;
- code that has been written;
- code that has executed;
- an output obtained from execution;
- a theorem-derived conclusion;
- an independently verified result.

Any claim about design, implementation, execution, correction, verification, or completion must be supported by the corresponding source artifact, computation, proof, or test. Headings and labels are factual claims under the same standard.

Do not hard-code known classification facts as though they were computed. Construct the relevant maps, groups, rings, schemes, or isomorphisms required by the advertised computation.

Coinciding numerical invariants do not establish equality or isomorphism. Produce the relevant map, universal property, normal form, or proof.

## 18. Remediation discipline

When a proposed construction is challenged, return to the original mathematical requirement. Reconstruct the claim independently before adopting the terminology or architecture suggested by the correction.

Before presenting a revised design:

1. reconstruct the original requested domain and output;
2. identify every independent defect in the previous proposal;
3. supply the missing mathematical objects, morphisms, hypotheses, and universal data;
4. determine what Sage already implements and what has actually been inspected or executed;
5. distinguish the mathematical correction from the proposed implementation strategy;
6. apply the native-primitives, bridge, reference-implementation, and literature escalation ladder;
7. test the revision against the supplied counterexamples and nearby cases;
8. classify the result accurately as proposed, implemented, executed, or verified.

Abstract vocabulary is not evidence of correction. An operation described as categorical, semantic, or universal must still have complete defining data, the intended mathematical domain, and an implementation status supported by evidence.

Use user-supplied examples as scope witnesses. Determine the general mathematical construction that includes them and test the revision against them for that reason.

A corrected design should:

1. supply the missing mathematical data;
2. correct object ownership;
3. remove presentation dependence from the semantic interface;
4. preserve the original mathematical domain;
5. use existing Sage semantics or an appropriate established bridge;
6. consider reference implementations and literature routes before deferral;
7. state implemented backend coverage and gate unsupported cases explicitly;
8. execute and verify the computation claimed for the current input.

Preserve the general semantic operation when only special backends are available. Use assertion-gated or case-matched coverage, implement a broader route when existing primitives or references make it bounded and reusable, and record a concrete backlog route when the missing backend is a substantial nonessential diversion. If the current result depends on an unsupported branch, implement the necessary extension or state the block.

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
