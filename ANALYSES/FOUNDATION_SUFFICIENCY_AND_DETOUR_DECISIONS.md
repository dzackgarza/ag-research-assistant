# Foundation Sufficiency and Detour Decisions

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** recent Sage category, Čech, and commutative-algebra transcript supplied by the user.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The transcript exposes a failure more serious than a missing backend operation. The assistant reaches degree-two Čech calculations and proposes effective descent while the commutative-algebra layer beneath the construction is not represented coherently.

The user then asks whether the underlying category of commutative rings actually supplies localization arrows, quotient arrows, local-ring refinements, specified pushouts and pullbacks, map-aware tensor products, relative spectra, affine spaces, and noncanonical algebra structures. The assistant's audit concludes that Sage has many useful parents and specialized constructors but not one coherent categorical layer supporting these constructions.

The error is therefore **foundation evasion**: continuing upper-layer development while generic prerequisites are being improvised inside downstream code.

## 2. Valid regressions were mistaken for architectural progress

The existing K3, localization, and Čech examples can remain mathematically valid for their supported presentations. They establish that certain local formulas work and supply useful regression cases.

They do not establish that the following foundations exist:

- a coherent arrow category with genuine ring morphisms;
- quotient and localization morphisms with universal properties;
- products, pullbacks, pushouts, and tensor products of specified arrows;
- algebra structures as coslice objects;
- relative `Spec` and affine-space constructions compatible with those arrows;
- a descent layer built on these operations.

The assistant treated progress through one downstream example as evidence that it could proceed to the next categorical layer. That is regression laundering: successful examples obscure an unimplemented semantic substrate.

## 3. Accreted patches were foundational implementations in disguise

Classes and certificates introduced for the Čech computation—localization morphisms, product morphisms, equality certificates, path reductions, and special base-change formulas—are not merely local helpers. They partially implement the missing commutative-algebra foundation.

The correct response is not to add another layer of Čech or descent code around them. It is to classify them by mathematical ownership, move them into the appropriate categories and universal constructions, and make the K3 example a downstream integration test.

This is the same one-rung failure seen elsewhere: the agent recognizes each local obstruction but never asks whether their common cause is the absence of the layer on which the whole construction depends.

## 4. Foundation completeness is relative but must be coherent

The correction is not to demand an exhaustive implementation of all commutative algebra before doing geometry. A foundation is sufficient relative to a task when it contains the standard objects, morphisms, universal operations, comparison witnesses, and theorem propagation required to state and verify the next layer.

For the transcript, a plausible dependency chain is:

\[
\mathbf{CRing}
\to
\operatorname{Ar}(\mathbf{CRing})
\to
\text{quotients, localizations, and finite limits/colimits}
\to
\mathbf{CAlg}_R
\to
\text{free algebras and tensor products}
\to
\operatorname{Spec}
\to
\text{affine covers and Čech nerves}
\to
\text{descent}.
\]

The exact implementation scope remains a design decision, but the dependency direction is not optional.

## 5. The assistant must surface a foundational detour decision

Once the audit shows that correct continuation requires a substantial new foundational layer, the assistant should stop and ask whether the user wants that detour. The question must be informed, not procedural.

It should report:

- what remains valid;
- what cannot yet be stated or verified coherently;
- the minimal foundational package required;
- how much of the current patchwork moves into that package;
- what downstream work the package unlocks;
- the alternative of retaining a narrower scope with explicit gates.

The assistant should recommend the detour when the foundation is necessary for correctness and likely to support nearby research. It should not continue ill-defined work merely to avoid asking a scope question.

## 6. General regression rule

This failure is not specific to commutative rings. It recurs whenever a downstream project begins implementing generic infrastructure for:

- morphisms and their equality;
- limits, colimits, or universal arrows;
- local-to-global compatibility and descent;
- proof-bearing predicates and theorem propagation;
- derived, homotopical, or higher coherence;
- representations, graded objects, actions, or diagram categories.

The review question is:

> Is the agent extending the requested theory, or unknowingly constructing its missing foundations inside one special example?

If the latter, continued local patching should stop before the next layer is added.
