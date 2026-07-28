## 5. Complete data for universal constructions

Invoking a universal construction by name is not enough. Specify the complete diagram and ambient category.

A fiber product requires a cospan

\[
X \xrightarrow{f} S \xleftarrow{g} T.
\]

The notation `X ×_S T` is justified only after the two structure morphisms and ambient category are known or genuinely canonical in context.

Similarly:

- an equalizer requires two named parallel morphisms;
- a pullback requires the complete cospan;
- a pushout requires the complete span;
- an image requires a specified morphism and image convention;
- a quotient requires the acting relation, group, groupoid, or equivalence data;
- a double cover requires its actual cover data, not only the desired degree.

Prefer ambient-category ownership for genuinely diagrammatic constructions, for example an operation corresponding to `f.ambient_category().pullback(g)`. Local convenience syntax is acceptable only when it preserves every defining morphism and cannot obscure the universal property.

## 6. Intrinsic objects versus presentations

Separate the intrinsic construction from every computational presentation.

A failure of one Sage presentation does not imply failure or nonexistence of the mathematical object. State precisely whether the limitation concerns:

- a Sage parent or element class;
- a constructor;
- a coercion;
- a coordinate chart;
- an embedding;
- a backend;
- an algorithm;
- an unimplemented case;
- an execution defect.

Do not route a general construction through toric, affine, projective, or chartwise geometry merely because the current example admits that presentation.

A presentation-specific implementation may serve as one verified backend. It must not become the semantic interface unless the requested mathematical domain is itself presentation-specific.

Intrinsic notions must not acquire unnecessary embedding hypotheses. In particular, a singular locus is intrinsic to a scheme; it is not fundamentally a construction on “a curve on a surface.”

## 7. General interfaces with explicitly partial backend coverage

Define the semantic operation at the correct mathematical level even when Sage only implements it for special presentations. A method representing products or fiber products of arbitrary schemes may legitimately dispatch only to toric, affine, projective, product-of-projective-spaces, chartwise, or other supported cases.

Case analysis and assertion gates are appropriate when they preserve one general semantic interface while making the implemented subdomain explicit. They are preferable to inventing a narrower method whose mathematical meaning is restricted to the first backend that happens to work.

Before implementing backend dispatch, determine:

1. the full mathematical domain of the semantic operation;
2. the common contract and mathematically primary return object;
3. the existing Sage primitive, if any;
4. the predicates that identify supported representations;
5. the branches actually implemented and executed;
6. the compatibility of their outputs;
7. the unsupported cases and their precise failure mode.

Distinguish three different boundaries:

- a **mathematical precondition**, outside which the construction itself is undefined;
- an **implementation precondition**, where the construction exists but the available backend cannot yet compute it;
- a **research-scope boundary**, where implementing the missing general backend would be substantial work not required for the present mathematical computation.

An implementation precondition should be represented by an explicit assertion, case-match, `NotImplementedError`, or equivalent result that names the unsupported representation. It must not be disguised as a mathematical nonexistence claim, and it must not be followed by a claimed result for the rejected case.

Before accepting a partial backend as the present endpoint, follow this escalation ladder:

1. **Native Sage routing.** Identify the special cases Sage already handles and route them beneath the general semantic operation.
2. **Native Sage composition.** Determine whether existing general primitives can be composed into the missing case with a short, mathematically transparent implementation.
3. **Existing bridges.** Check whether Sage bridges to GAP, Singular, Macaulay2, Magma, PARI/GP, Julia, or another established system already expose the needed primitive or complete algorithm with compatible semantics.
4. **Reference implementations.** Search for a reliable implementation that treats a more general domain and can be reproduced, wrapped, or followed without substantial new design.
5. **Literature algorithms.** Check papers, books, and citable theorems for an explicit algorithm, reduction, or structural result that makes a correct general implementation short.
6. **Scope decision.** Estimate the implementation complexity, mathematical risk, integration cost, relevance to the current input, and likely reuse in nearby research.

Implement the broader route immediately when it is short, mathematically controlled, and likely to make foundational code substantially more reusable. This includes clean compositions of existing primitives, already-supported bridges, straightforward adaptations of reference code, and bounded translations of explicit literature algorithms.

If the route requires substantial infrastructure or a nontrivial research implementation, and the current computation lies in a supported branch, preserve the general interface, gate the unsupported branch explicitly, and record a backlog item. The backlog entry must state the missing mathematical case, the proposed implementation route, relevant Sage primitives or bridges, reference code or citations, and the criterion for completion. Continue the active research computation rather than allowing backend development to consume the session.

If the current computation itself lies outside every supported branch, either implement the minimum correct extension needed for that computation or state that the computation is blocked. Do not claim general execution merely because the semantic interface is general.

A list of special cases is not by itself a general design. It becomes a valid partial implementation only when it dispatches beneath a correctly defined general operation and exposes its coverage honestly.

## 8. Sage-first implementation audit

Before declaring that Sage lacks a construction or designing a replacement API:

1. inspect Sage documentation and source;
2. inspect parent/element ownership and categories;
3. search for partially implemented methods and adjacent general primitives;
4. test the relevant operation in the active Sage version;
5. identify the exact defect or missing generality;
6. inspect established external-system bridges;
7. search for general reference implementations and literature algorithms;
8. determine whether the correct remedy is native composition, extension, bridge reuse, reference adaptation, literature implementation, assertion-gated dispatch, or a mathematically faithful shadow implementation.

Do not build a parallel abstraction merely because the existing API is inconvenient or defective. Repair or compose the general primitive when this is reasonably short and directly serves the research task. Prefer an existing bridge when another system already implements the correct primitive and the bridge preserves the required mathematical data. Reproduce or adapt a reference implementation when this is straightforward and auditable. Use a published algorithm or theorem when it gives a bounded route to the general case.

When a full general repair remains substantial, preserve the general semantics through explicit dispatch and coverage gates rather than either overfitting the interface or derailing the research task. When a correct shadow is required, preserve the same mathematical semantics and make the divergence from Sage explicit.

Do not claim that a method exists, is absent, succeeds, or fails without source inspection or executed evidence.

