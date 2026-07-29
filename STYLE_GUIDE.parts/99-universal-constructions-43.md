
## 43. Derive universal constructions inside the established categorical foundation

When a project has fixed an ambient categorical or \(\infty\)-categorical universe, later constructions must be assembled from its existing diagram categories, slices, subcategories, universal objects, mapping objects, and comparison cells. Ordinary maps, sets, equations, matrices, and coordinates are obtained afterward by explicit evaluation, truncation, or forgetful functors.

### 43.1 Use the universal-object derivation pattern

For each construction, identify:

1. **Ambient category.** The category or \(\infty\)-category \(\mathcal C\), its mapping objects, and its cell conventions.
2. **Diagram category.** The functor, arrow, slice, coslice, comma, cone, or cocone category in which the relevant diagrams live.
3. **Admissible diagrams.** The full or replete subcategory, axiomatic refinement, pullback, or classifier expressing the hypotheses.
4. **Universal object.** The initial object, final object, limit, colimit, adjoint image, reflective localization, or representer that defines the construction.
5. **Comparison cells.** The points of the relevant mapping objects giving mediators, lifts, projections, units, counits, or other universal maps.
6. **Derived components.** The evaluations, truncations, or forgetful images used by computational backends.
7. **Coherence.** The contractibility, uniqueness, naturality, or higher coherence retained by the full construction.

The mathematical derivation has the form

\[
\text{diagram category}
\longrightarrow
\text{admissible subcategory}
\longrightarrow
\text{universal object}
\longrightarrow
\text{mapping object of comparison cells}
\longrightarrow
\text{computational component}.
\]

Reuse the project's existing constructors at each stage. A new public abstraction is justified only by the genuinely new admissibility data or universal construction.

### 43.2 Localization as an example

Let \(\mathcal C=\mathbf{CRing}\) at the categorical level fixed by the project. The arrow category is

\[
\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C),
\]

and the coslice at \(R\) is the fiber

\[
\mathcal C_{R/}
\simeq
\{R\}\times_{\mathcal C,\operatorname{ev}_0}
\operatorname{Ar}(\mathcal C).
\]

For a multiplicatively closed subset \(S\subseteq R\), let

\[
\operatorname{Inv}_S(R)\subseteq\mathcal C_{R/}
\]

be the replete full subcategory of arrows \(\phi:R\to T\) satisfying \(\phi(S)\subseteq T^\times\). A localization is an initial object

\[
\ell:R\longrightarrow L
\]

of \(\operatorname{Inv}_S(R)\). For every admissible \(\phi\), the mapping object

\[
\operatorname{Map}_{\operatorname{Inv}_S(R)}(\ell,\phi)
\]

is contractible. A point \(\alpha_\phi:\ell\to\phi\) is the universal comparison cell. In the ordinary truncated case it is the commutative square

\[
\begin{CD}
R @>{\operatorname{id}_R}>> R\\
@V{\ell}VV @VV{\phi}V\\
L @>{\widetilde\phi}>> T,
\end{CD}
\]

and the familiar factor map \(\widetilde\phi:L\to T\) is its target component. The classical Hom-set bijection is the set-level truncation of this mapping-object formulation.

The same mode of thought applies, with problem-specific diagram categories and admissibility conditions, to quotients, free objects, products, pullbacks, coproducts, pushouts, sheafification, and representability problems.

### 43.3 Preserve the full comparison datum

When the mathematical result is a morphism in an arrow category, a commutative square, a natural transformation, a homotopy, or another cell, retain that object. A concrete map or coordinate formula may be exposed as a component, but it must remain connected to the full diagram from which it is derived.

Make every loss of categorical information explicit: name the evaluation, component projection, truncation, forgetful functor, or strictification theorem being applied, and state what information is discarded. The backend's representational limitations do not determine the mathematical level of the public interface.
