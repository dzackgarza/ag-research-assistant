# Categorical-Level Regression and Abstraction Amnesia

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** transcript concerning localization, arrow categories, universal lifting data, and a previously established higher-categorical foundation.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The transcript exposes two coupled failures.

First, the assistant regresses to a weaker categorical level. It initially describes localization through a set-valued Hom bijection and says that the user's 2-morphism language becomes valid only after separately specifying an ambient 2-category. This ignores the project's already established convention that ordinary categories are treated inside a truncated infinity-categorical universe and that morphisms between arrows are represented through the arrow category.

Second, the assistant forgets its own abstractions. The project had already implemented or adopted `Ar(C)`, slices or coslices, limits, and higher comparison data. Instead of deriving localization from those constructions, the assistant rebuilds a parallel local theory of bare ring maps, induced morphisms, and Hom-set equivalences.

The combined trajectory is:

\[
\text{established categorical foundation}
\longrightarrow
\text{local set-level reformulation}
\longrightarrow
\text{component-only API}
\longrightarrow
\text{user restores the forgotten foundation}.
\]

This is not merely an expository mistake. The weaker formulation changes what the implementation stores, what the tests can verify, and which coherence statements later work can express.

## 2. The project had already fixed the relevant level

For an infinity-category \(\mathcal C\), the arrow category is

\[
\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C).
\]

In the ordinary categorical case, its objects are arrows and its morphisms are commutative squares. Ordinary categories embed into the infinity-categorical setting through their nerves, and an initial object is characterized by contractible mapping spaces; in a discrete ordinary case this recovers a unique morphism. These are standard constructions, not special additions needed only for localization.

Kerodon records these points in its treatment of ordinary categories as infinity-categories, arrow categories, and initial objects. The project therefore did not need a second set-valued foundation in order to discuss the localization lift.

The relevant editorial principle is project-relative: once a project has declared its categorical universe and cell conventions, later work must use them. A local example does not reset the foundation.

## 3. Localization should have been derived from existing constructions

Fix an object \(R\in\mathcal C\) and a class of admissible arrows out of \(R\). These form a full subcategory of the coslice \(\mathcal C_{R/}\), itself obtained as the fiber of source evaluation on \(\operatorname{Ar}(\mathcal C)\).

For localization at a multiplicative subset \(S\), the admissible objects are arrows \(\phi:R\to T\) sending \(S\) to units. The localization arrow \(\ell:R\to S^{-1}R\) is initial in this subcategory. Hence for every admissible \(\phi\), the mapping object

\[
\operatorname{Map}(\ell,\phi)
\]

is contractible. A point is a morphism in the arrow category: a commutative square whose target component is the familiar factor map \(S^{-1}R\to T\).

The set-level bijection

\[
\operatorname{Hom}(S^{-1}R,T)
\cong
\{\phi:R\to T\mid \phi(S)\subseteq T^\times\}
\]

is a truncated presentation of the same universal construction. It may be a theorem, display, or backend realization. It should not be implemented as a parallel semantic foundation once the initial-object and arrow-category machinery exists.

## 4. Returning only the target component loses the categorical witness

The assistant first proposes returning only the factor map \(\widetilde\phi:S^{-1}R\to T\). That map is useful, but in the established framework it is a component of a morphism of arrows.

The full datum includes:

- the source component, typically \(\operatorname{id}_R\);
- the target component \(\widetilde\phi\);
- the source and target arrows \(\ell\) and \(\phi\);
- the commutative square \(\widetilde\phi\circ\ell=\phi\);
- the ambient arrow or coslice category;
- the uniqueness or contractibility statement.

Discarding the full cell prevents later composition, naturality, and coherence from being expressed through the project's existing machinery. Component accessors are appropriate sugar; component erasure is not.

## 5. The purge overcorrected in the opposite direction

The earlier invented universal-property wrapper was incoherent and needed to be removed. The assistant then overcorrected by declaring that the localization should simply be a bare ring homomorphism with a helper returning another ring homomorphism.

This is a recurring remediation defect:

\[
\text{bad structured wrapper}
\longrightarrow
\text{delete all structure}
\]

rather than

\[
\text{bad structured wrapper}
\longrightarrow
\text{recover the correct standard structured object}.
\]

The correct repair was to reuse the initial object in the admissible-arrow category and the morphisms in `Ar(C)`. Purging a false abstraction must not erase valid categorical structure that the false abstraction was unsuccessfully trying to approximate.

## 6. Categorical level must be conserved explicitly

A backend may store only strict maps or compare only Boolean equality. That does not determine the mathematical level of the public interface.

When a projection or truncation is necessary, the implementation must name it:

- pass from a mapping space to \(\pi_0\);
- extract the target component of a square;
- apply a forgetful functor;
- choose a strict representative using a strictification theorem;
- pass from equivalence or homotopy to a proposition asserting existence.

The result should state what information was forgotten. Silent truncation is especially dangerous because later code begins treating a backend limitation as the project's foundational mathematics.

The converse matters as well. Higher-categorical language should not be introduced merely to avoid proving a strict equality that the theorem genuinely requires. The rule is categorical conservation, not automatic escalation.

## 7. Abstraction amnesia prevents cumulative mathematics

The assistant's failure to reuse `Ar(C)`, slices, and initial objects means the project does not accumulate foundations. Each local task can trigger a fresh, weaker reconstruction. This creates:

- duplicate public interfaces for the same construction;
- inconsistent equality and coherence conventions;
- tests that operate at different categorical levels;
- repeated implementation of factorization and comparison logic;
- inability to use earlier universal constructions as dependencies;
- user effort spent reintroducing already settled theory.

A serious mathematical codebase needs an abstraction dependency ledger. Every foundational addition should state which existing constructions it composes from and what genuinely new datum remains.

## 8. Required prevention and remediation

Before implementing a new universal object or operation, the assistant should:

1. identify the project's ambient categorical universe;
2. search existing project abstractions and prior decisions;
3. express the construction through those categories, diagrams, and universal properties;
4. preserve full cells and mapping objects;
5. expose lower components only as derived accessors;
6. justify every truncation or strictification explicitly;
7. test composition and coherence in the existing framework.

When a parallel weaker layer has already accumulated:

1. freeze dependent work;
2. identify the earliest categorical divergence;
3. translate the local theory back into the established foundation;
4. remove duplicate interfaces;
5. preserve valid formulas as backends or component computations;
6. re-audit every downstream theorem for lost naturality or coherence.

The user should not need to remind the assistant that the framework already contains arrow categories, slices, limits, or higher-cell conventions. Forgetting those constructions is a correctness failure because it changes the mathematics being implemented.

## 9. Reference points

The categorical facts used in this analysis are standard and can be checked in Kerodon:

- Example 1.5.1.1: ordinary functors agree with functors between the nerves of ordinary categories;
- Warning 8.1.0.4: the arrow category is `Fun([1], C)`, and its morphisms are commutative squares in the ordinary case;
- Definition 4.7.3.1: an initial object of an infinity-category has contractible mapping spaces to every object.

These references support the general reconstruction. The specific requirement to reuse `Ar(C)`, slices, limits, and the project's chosen higher-cell conventions comes from the project's own established foundation and the supplied transcript.
