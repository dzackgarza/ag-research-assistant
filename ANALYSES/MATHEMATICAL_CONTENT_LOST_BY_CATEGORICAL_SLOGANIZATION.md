# Mathematical Content Lost by Categorical Sloganization

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** localization transcript and the subsequent criticism that the repository update replaced its mathematical content by vague advice.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The previous synthesis correctly noticed categorical-level regression and abstraction amnesia, but its main operational summary was too weak. Phrases such as “preserve the established categorical level,” “reuse prior abstractions,” and “retain the full witness” name desirable outcomes without teaching the assistant how to reconstruct the actual mathematics.

That compression loses the decisive insight of the transcript: the localization construction is obtained by a concrete sequence of standard category constructors, and every datum in the public API has a precise place in that sequence.

A future agent cannot recover that sequence from the slogan “preserve coherence.” It can technically comply while again building a bare map plus helper methods.

## 2. The actual derivation

Let \(\mathcal C\) be the project’s ambient \(\infty\)-category of commutative rings, with ordinary commutative rings embedded at the chosen truncation level. The arrow category is

\[
\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C).
\]

The source evaluation

\[
\operatorname{ev}_0:\operatorname{Ar}(\mathcal C)\to\mathcal C
\]

has fiber over \(R\) equal to the coslice

\[
\mathcal C_{R/}.
\]

Fix a multiplicative subset \(S\subseteq R\). Define the replete full subcategory

\[
\operatorname{Inv}_S(R)\subseteq\mathcal C_{R/}
\]

spanned by arrows \(\phi:R\to T\) satisfying \(\phi(S)\subseteq T^\times\).

A localization is an initial object

\[
\ell:R\to L
\]

of \(\operatorname{Inv}_S(R)\). Therefore, for every admissible \(\phi\),

\[
\operatorname{Map}_{\operatorname{Inv}_S(R)}(\ell,\phi)
\]

is contractible.

A point \(\alpha_\phi\) of this mapping object is a morphism in the arrow category. In the ordinary case it is the commutative square

\[
\begin{CD}
R @>{\operatorname{id}_R}>> R\\
@V{\ell}VV @VV{\phi}V\\
L @>{\widetilde\phi}>> T.
\end{CD}
\]

The usual factor map \(\widetilde\phi\) is only the target component of \(\alpha_\phi\). The localized ring is only the target \(L=\operatorname{ev}_1(\ell)\). The factorization equation is encoded by the square. Uniqueness and higher coherence are encoded by contractibility of the mapping object.

This is the exact content that the earlier synthesis should have preserved.

## 3. Why the Hom-set statement is insufficient as architecture

Precomposition with \(\ell\) gives the natural mapping-space equivalence

\[
\operatorname{Map}_{\mathcal C}(L,T)
\simeq
\operatorname{Map}_S(R,T),
\]

where the right-hand side is the full subspace of maps \(R\to T\) that invert \(S\). The classical bijection

\[
\operatorname{Hom}(L,T)
\cong
\{\phi:R\to T\mid \phi(S)\subseteq T^\times\}
\]

is its ordinary truncation. If that truncation is implemented as the primary semantic layer, it loses:

- the source component \(\operatorname{id}_R\);
- the fact that the lift is a morphism in \(\operatorname{Ar}(\mathcal C)\);
- composition of comparison cells;
- naturality in the target arrow;
- the project’s existing conventions for higher cells;
- the ability to reuse generic initial-object and slice machinery.

The formula for \(\widetilde\phi(r/s)\) is even further downstream: it is one backend computation of one component of one point in a contractible mapping object.

## 4. The general mathematical pattern

The localization example exemplifies a broad research habit:

1. identify the category of diagrams or structured arrows in which admissible candidates live;
2. impose the defining predicate by a full subcategory, pullback, or axiomatic refinement;
3. identify the construction as initial, final, a limit, a colimit, an adjoint image, or a reflective localization;
4. treat universal comparison maps as points of mapping objects;
5. extract equations or component maps by evaluation;
6. recover ordinary set-valued statements by explicit truncation.

This pattern gives:

- quotients as initial arrows killing specified relations;
- localizations as initial arrows inverting specified elements;
- free objects as initial objects in comma categories;
- products and pullbacks as final cones;
- coproducts and pushouts as initial cocones;
- units of reflective localizations as universal arrows into local objects.

A style guide that states only “reuse universal properties” does not transmit this method.

## 5. The iterative-reuse failure

The project already possessed:

\[
\operatorname{Ar}(\mathcal C),
\quad
\mathcal C_{R/},
\quad
\text{full subcategories},
\quad
\text{initial objects},
\quad
\text{mapping objects}.
\]

The localization construction should therefore have introduced only the new admissibility predicate “invert \(S\).” Everything else should have been inherited.

Instead, the assistant rebuilt:

- a new localization wrapper;
- a new factorization method;
- a new Hom-set theorem interface;
- a component-only return type;
- new equality and certification plumbing.

This is not ordinary code duplication. It means the project’s mathematics is not cumulative. Every local problem can forget the previously established ontology and restart at a weaker level.

## 6. Required editorial standard

When source material contains a concrete categorical derivation, the assistant-facing guide must preserve enough of it that the future agent can reconstruct:

- the ambient category;
- the diagram category;
- the relevant fiber, slice, or coslice;
- the admissible full subcategory;
- the universal object;
- the mapping object expressing its universal property;
- the comparison cell and all of its components;
- the explicit truncation producing the classical statement;
- the exact project abstractions reused.

A general phrase is acceptable only after this construction has been stated. It may summarize the mathematics; it may not replace it.

## 7. Reference points

The standard categorical facts can be checked in Kerodon:

- the arrow category is \(\operatorname{Fun}([1],\mathcal C)\);
- slices and coslices are fibers of the target and source evaluation functors;
- initial objects in an \(\infty\)-category have contractible mapping spaces to every object;
- for nerves of ordinary categories, commutative squares and unique strict mediators are recovered as truncated special cases.

The project-specific requirement is stronger than these general facts: once these constructions have been implemented, later work must literally derive new mathematics from them rather than merely mention them.
