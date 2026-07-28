
## 43. Derive universal constructions inside the established \(\infty\)-categorical foundation

When a project has already fixed an ambient categorical universe, that choice is operative mathematics, not background commentary. Later constructions must be assembled inside that universe from its existing diagram categories, slices, subcategories, universal objects, mapping objects, and comparison cells. Only afterward may a backend project to ordinary maps, sets, equations, matrices, or coordinates.

Do not restart from a bare Hom-set formula or invent an operation-specific helper when the project already contains the categorical construction from which that formula is derived. Conversely, do not invoke higher-categorical language decoratively: every categorical level, cell, truncation, and projection must determine actual mathematical data used by the implementation.

### 43.1 Use the general universal-object derivation schema

For a proposed construction, identify the following data explicitly.

1. **Ambient category.** Name the category or \(\infty\)-category \(\mathcal C\) and the project convention for its mapping objects and higher cells.
2. **Diagram category.** Choose the existing functor category \(\operatorname{Fun}(K,\mathcal C)\), arrow category, slice, coslice, comma category, or category of cones or cocones in which the relevant diagrams live.
3. **Admissible diagrams.** Express the hypotheses by a full or replete subcategory, an axiomatic refinement, a pullback of categories, or another standard classifier.
4. **Universal object.** Define the desired object as an initial object, final object, limit, colimit, adjoint image, reflective localization, or representer in that category.
5. **Comparison cells.** Obtain mediators, lifts, projections, units, counits, or other comparison maps as points of the appropriate mapping objects.
6. **Derived components.** Obtain ordinary maps, equations, matrices, or coordinate formulas by evaluation, truncation, or an explicit forgetful functor.
7. **Coherence.** Retain the contractibility, uniqueness, naturality, or higher coherence supplied by the universal construction.

A future reader should be able to reconstruct the complete derivation

\[
\text{existing diagram category}
\longrightarrow
\text{admissible subcategory}
\longrightarrow
\text{universal object}
\longrightarrow
\text{mapping object of comparison cells}
\longrightarrow
\text{explicit backend component}.
\]

The particular categories and arrows depend on the problem. Do not turn one regression example into the standing ontology for unrelated constructions.

### 43.2 Worked regression example: localization

The following localization derivation is a worked example grounding the general schema. It is not a requirement that every universal construction use these particular categories or symbols.

Let \(\mathcal C=\mathbf{CRing}\) at the categorical level already fixed by the project. Its arrow category is

\[
\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C),
\]

with evaluation functors

\[
\operatorname{ev}_0,\operatorname{ev}_1:
\operatorname{Ar}(\mathcal C)\longrightarrow\mathcal C.
\]

For \(R\in\mathcal C\), the coslice is the fiber

\[
\mathcal C_{R/}
\simeq
\{R\}\times_{\mathcal C,\operatorname{ev}_0}
\operatorname{Ar}(\mathcal C).
\]

Thus an object of \(\mathcal C_{R/}\) is an arrow \(R\to T\). A morphism in the coslice is already a comparison cell in \(\operatorname{Ar}(\mathcal C)\) whose source component is \(\operatorname{id}_R\). Under this project convention, no separate ambient \(2\)-category needs to be invented before one can speak about morphisms between arrows.

For a multiplicatively closed subset \(S\subseteq R\), let

\[
\operatorname{Inv}_S(R)\subseteq\mathcal C_{R/}
\]

be the replete full subcategory on arrows \(\phi:R\to T\) satisfying

\[
\phi(S)\subseteq T^\times.
\]

A localization is an initial object

\[
\ell:R\longrightarrow L
\]

of \(\operatorname{Inv}_S(R)\). The localized ring is recovered by evaluation:

\[
L=\operatorname{ev}_1(\ell)=\ell.\operatorname{codomain}.
\]

For every admissible \(\phi:R\to T\), initiality gives a contractible mapping object

\[
\operatorname{Map}_{\operatorname{Inv}_S(R)}(\ell,\phi).
\]

A point

\[
\alpha_\phi:\ell\longrightarrow\phi
\]

is the full universal comparison cell. In the ordinary truncated case it is the commutative square

\[
\begin{CD}
R @>{\operatorname{id}_R}>> R\\
@V{\ell}VV @VV{\phi}V\\
L @>{\widetilde\phi}>> T,
\end{CD}
\]

with

\[
\widetilde\phi\circ\ell=\phi.
\]

The familiar factor map \(\widetilde\phi:L\to T\) is only the target component of \(\alpha_\phi\). The source and target arrows, source component, commutative square, ambient coslice, and contractibility statement remain part of the semantic datum.

Equivalently, precomposition with \(\ell\) gives a natural equivalence of mapping spaces

\[
\operatorname{Map}_{\mathcal C}(L,T)
\simeq
\operatorname{Map}_S(R,T),
\]

where the right-hand side is the full subspace of maps that invert \(S\). The classical Hom-set bijection is the ordinary truncated shadow of this equivalence, not a second semantic foundation.

For a prime ideal \(\mathfrak p\subseteq R\), prime localization is this same construction with \(S=R\setminus\mathfrak p\). The locality of \(R_{\mathfrak p}\), its maximal ideal, and its residue morphism are properties and derived constructions of the codomain; they do not define another universal object.

### 43.3 Preserve the comparison cell and expose components as derived syntax

A schematic interface for the worked example may read

```sage
Inv = C.coslice(R).replete_full_subcategory(is_S_inverting)
ell = Inv.initial_object()
alpha = ell.lift(phi)
tilde_phi = alpha.target_component()
```

Here `alpha`, not `tilde_phi`, is the full universal comparison datum. The implementation should make the source and target arrows, both components, and the commutative square inspectable. A backend formula such as

\[
\widetilde\phi(r/s)=\phi(r)\phi(s)^{-1}
\]

computes one component of the cell; it does not replace the initial-object statement or the morphism in the arrow category.

If lifts are chosen coherently for all admissible targets, derive that choice from the initial-object structure through the project’s existing undercategory, section, or natural-transformation machinery. Do not create independent per-target helpers whose naturality must later be reconstructed by hand.

### 43.4 Reuse the same schema with problem-appropriate categories

The general pattern applies with different diagram categories and admissibility conditions. Examples include:

- a quotient \(R\to R/I\) as initial among arrows out of \(R\) that kill \(I\);
- a free object as an initial object in an appropriate comma category;
- products and pullbacks as final cones;
- coproducts and pushouts as initial cocones;
- sheafification as a reflective localization with its unit;
- universal families through the relevant representability or universal-arrow statement.

These examples illustrate one reusable mode of thought. They do not license operation-specific classes named after “the universal property.” The mathematical primitive is the universal object or diagram in its ambient category; the universal property characterizes it through mapping objects.

### 43.5 Record an explicit derivation ledger

For every foundational construction, record:

1. the prior category and diagram constructors used;
2. the admissibility predicate, subcategory, or classifier newly introduced;
3. the universal object or diagram obtained;
4. the mapping object containing comparison cells;
5. the full semantic output;
6. every evaluation, projection, truncation, or forgetful functor used to obtain backend data;
7. the composition, naturality, and coherence obligations inherited from the foundation;
8. the genuinely new datum that was not already available.

For the localization example, the derivation ledger is

\[
\operatorname{Ar}(\mathcal C)
\longrightarrow
\mathcal C_{R/}
\longrightarrow
\operatorname{Inv}_S(R)
\longrightarrow
\ell\in\operatorname{Init}(\operatorname{Inv}_S(R))
\longrightarrow
\operatorname{Map}(\ell,\phi)
\longrightarrow
\operatorname{ev}_1(\alpha_\phi)=\widetilde\phi.
\]

This displayed chain is a regression anchor showing the required precision. For another construction, write its own derivation rather than copying this one mechanically.

### 43.6 Make every loss of categorical information explicit

A weaker backend does not determine the mathematical level of the public interface. When computation requires forgetting structure, name the operation:

- apply \(\pi_0\) or another truncation to a mapping space;
- project a morphism in \(\operatorname{Ar}(\mathcal C)\) to one component;
- apply a forgetful functor from structured arrows to underlying arrows;
- choose a strict representative using a stated strictification theorem;
- pass from a coherent equivalence to a proposition only when the theorem requires no more.

State what information is lost and retain the full object whenever later composition or coherence may require it. Conversely, do not invoke \(\infty\)-categorical language merely to avoid a strict equation that the theorem genuinely requires.
