# Coble Notebook Transcript: Identity, Isomorphism, and Representation Discipline

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** `Coble-Notebook (3).md`, especially the correction sequences concerning points, affine covers, sections, Cox rings, graded algebras, relative spectra, singularity classification, and products.  
**Status:** contributor-facing analysis; not part of the prompt uploaded to the AG assistant.

## 1. Correction to the preceding analysis

The earlier longitudinal analysis correctly identified coordinate capture, premature abstraction closure, and the substitution of invariants for proofs. Its wording remained too imprecise. In particular, it described a polynomial ring as a “model” of the Cox ring and spoke broadly of coordinate “models.”

That language repeats the underlying failure. The relevant mathematics does not say merely that two objects are usable models of one phenomenon. It says that there are two distinct objects in a specified category and a named morphism between them. In the supported projective and toric cases, the morphism is a graded-algebra isomorphism.

The central failure is therefore sharper than representation capture:

> The assistant systematically collapses mathematical relations into informal identity.

It treats equality, isomorphism, equivalence, realization, presentation, coercion, and agreement of invariants as though all licensed the same replacement of one object by another.

This relation collapse is one of the clearest signs that the assistant is not reasoning at research-mathematics level. A careful mathematician asks what the objects are, where they live, what the comparison map is, what structure it preserves, and what has actually been proved. The assistant repeatedly skips that work because the objects are familiar or computationally interchangeable in the current example.

## 2. The exact relations that must be distinguished

The transcript requires an explicit hierarchy.

### 2.1 Definitional identity

Two expressions may denote literally the same stored object or reduce to the same definition. Only here is silent replacement generally harmless.

Even definitional identity is relative to the implementation. Mathematical prose should not claim definitional equality merely because Sage interns, caches, or coerces two objects to one parent.

### 2.2 Equality in a parent

For elements `a, b` of one parent `A`, the claim

\[
a=b\quad\text{in }A
\]

has a specific meaning supplied by `A`. It is not the same as two elements having equal coordinate lists in different parents.

Likewise, equality of morphisms is equality in a Hom-set. It requires common domain and codomain and is stronger than agreement on a sampled set of points.

### 2.3 Equality of subobjects in a fixed ambient object

Two ideals, subschemes, submodules, or loci can be compared only after their ambient object and conventions are fixed. Even then, several distinct statements occur:

- equal ideals;
- equal radicals;
- equal saturated ideals;
- equal closed subschemes;
- equal supports;
- equal rational-point sets.

The transcript repeatedly moved among these without naming the distinction.

### 2.4 Isomorphism in a category

An isomorphism is data:

\[
\Phi:A\xrightarrow{\sim}B
\]

in a named category. It includes a morphism, an inverse, and verification that the two composites are identities. The category matters. An isomorphism of underlying sets does not imply an isomorphism of groups; an isomorphism of ungraded rings does not imply an isomorphism of graded algebras; an isomorphism of abstract schemes does not automatically respect a base, polarization, action, marking, or embedding.

### 2.5 Canonical and natural isomorphism

Calling an isomorphism canonical adds a proof obligation. One must identify why it is independent of choices and how it behaves functorially. A family of objectwise isomorphisms is not a natural isomorphism without the naturality squares.

### 2.6 Chosen isomorphism

A basis, coordinate system, trivialization, marking, or embedding may determine an isomorphism. The resulting map is useful but not intrinsic. Its choice must remain visible because later constructions can depend on it.

### 2.7 Equivalence of categories

An equivalence is not equality of categories and not an objectwise isomorphism. It requires functors and natural isomorphisms, or fully faithfulness and essential surjectivity. The assistant’s general habit of “regarding” one category as another would be especially dangerous here.

### 2.8 Realization or presentation morphism

A coordinate realization may be a morphism that is not an isomorphism. An embedding, quotient map, localization, completion, affinization, normalization, or forgetful map cannot be treated as a mere change of notation.

### 2.9 Agreement after applying a functor

Two objects can have equal images after forgetting structure or applying an invariant. This proves only equality or isomorphism of the images, not of the original objects.

### 2.10 Numerical or invariant agreement

Equal dimensions, ranks, Hilbert series, Gram matrices, Hodge numbers, Milnor numbers, Tjurina numbers, and other invariants are usually necessary or suggestive conditions. Without a completeness theorem, they are not identifications.

## 3. Cox rings and polynomial algebras

The strongest example occurs in the Cox-ring discussion.

The abstract Cox ring is a graded algebra of sections:

\[
\operatorname{Cox}(X)
=
\bigoplus_{[L]\in\operatorname{Pic}(X)}H^0(X,L),
\]

with whatever choices and hypotheses are required to define the multiplication globally.

For a supported product of projective spaces with chosen homogeneous coordinates, one separately has a graded polynomial algebra

\[
P=k[x_{i,j}].
\]

The correct statement is the existence of a chosen graded-algebra isomorphism

\[
\Phi_X:\operatorname{Cox}(X)\xrightarrow{\sim}P.
\]

The source and target are not equal. Their elements are not automatically the same objects. The isomorphism is part of the mathematical and computational data.

For a line bundle class `[L]`, the degree restriction is another named map:

\[
\Phi_{X,L}:
H^0(X,L)
\xrightarrow{\sim}
P_{[L]}.
\]

This restriction must be derived from a general morphism framework for graded algebras. It should not be reimplemented independently for each section space.

The transcript’s successive mistakes were:

1. treating sections as polynomials;
2. treating a section space as a polynomial subspace;
3. calling the polynomial ring the Cox ring;
4. introducing direct `polynomial()` methods that hid the comparison;
5. only later constructing a graded-algebra isomorphism and its degree restrictions.

The final architecture was closer to correct because it forced the distinction:

```sage
CoxX = X.cox_ring()
Phi = CoxX.polynomial_isomorphism()
Phi_L = Phi.restrict_degree(L)
F = Phi_L(s)
s = Phi_L.inverse()(F)
```

Sugar such as `s.to_polynomial()` is acceptable only if it literally delegates to `Phi_L`. The method should not create a second implicit coercion or let downstream code forget which realization was used.

## 4. Sections are not polynomials

An element

\[
s\in H^0(X,L)
\]

is a section of an invertible sheaf. Its parent is the section space. Its polynomial expression is an image under a chosen realization map.

This distinction matters operationally.

If the backend wants to differentiate or eliminate, the actual chain is:

\[
s
\xmapsto{\Phi_{X,L}}
F
\xmapsto{\text{coordinate algorithm}}
D(F).
\]

The assistant must then determine whether `D(F)`:

- is merely coordinate data;
- represents an intrinsic object;
- transforms naturally under a change of realization;
- must be transported back through another map;
- depends on a chart or trivialization.

Writing `F = s.polynomial()` and continuing as though `s` had become a polynomial erases the exact map on which the computation depends.

The same problem appears with monomial bases. A basis of `H^0(X,L)` may be indexed by monomials through `Phi_{X,L}`. The basis vectors remain sections. Their indices or polynomial images do not change their parent.

## 5. Points are not tuples

An `R`-valued point of a scheme `X` is a morphism

\[
p:\operatorname{Spec}R\to X.
\]

A tuple may be:

- input to a point constructor;
- homogeneous coordinates relative to a chosen projective presentation;
- affine coordinates of a lift to a chart;
- coordinates of component points under product projections.

These are related data, not the point itself.

For an affine chart

\[
j:U\hookrightarrow X,
\]

a coordinate tuple belongs to a point

\[
q:\operatorname{Spec}R\to U
\]

satisfying

\[
j\circ q=p.
\]

The transcript initially invented `affine_expression()` and patch-index helpers. The user correctly required actual affine schemes, open immersions, and point preimages. This was not an API-style preference. It restored the missing mathematical objects and maps.

Likewise, for a product `X = X_1 × X_2`, the component points are obtained by composing with projections. A `factor_coordinates()` method promotes an accidental coordinate decomposition to public semantics; the standard operation is composition with the product projections, followed by a chosen coordinate realization on each factor if needed.

## 6. Coordinate rings and schemes are contravariantly related

An affine scheme is not equal to its coordinate ring. The functor

\[
\operatorname{Spec}:\operatorname{CRing}^{op}\to\operatorname{AffSch}
\]

is contravariant. A ring homomorphism

\[
\varphi:A\to B
\]

induces a scheme morphism

\[
\operatorname{Spec}B\to\operatorname{Spec}A.
\]

The transcript often printed or manipulated a ring map as though it were the geometric map without keeping the variance visible. It also initially constructed relative spectra as absolute spectra plus side metadata, losing the structure morphism to the base.

A careful implementation must construct the base scheme and structure morphism as first-class data. Base change must be along a named base morphism, not a bare target ring accepted by coercion.

## 7. Local rings and equations

A germ or local ring is not equal to a chosen local equation.

A point of a general scheme may have:

- a local ring;
- a completed local ring;
- an ideal presentation in an affine chart;
- several generators;
- a hypersurface equation only under additional hypotheses.

The assistant repeatedly wanted methods such as `local_equation()` and `ADE_type()` on arbitrary points. The user forced the more mature order:

1. construct the point and ambient scheme;
2. construct the local ring or germ;
3. choose or compute a presentation;
4. establish hypersurface or complete-intersection hypotheses;
5. compute invariants or a normal form;
6. classify only with a complete theorem or explicit equivalence.

An equation is a presentation. A coordinate change producing a normal form is a morphism or automorphism of the appropriate local or completed ring. The classification result cannot skip those maps.

## 8. Matching invariants is not an isomorphism

The transcript repeatedly accepted weaker evidence as “good enough” for a harder claim.

Examples include:

- four expected points satisfying equations treated as the complete fixed locus;
- equal dimensions used to describe spaces as the same;
- Hessian rank and Tjurina number used as an ADE certificate;
- numerical K3 or Enriques invariants reported as direct computation of the surface type;
- degree and equations used to identify a quotient without fully displaying the quotient map and theorem;
- equality of coordinate expressions used in place of equality of semantic maps.

For an isomorphism claim, the assistant should seek:

- an explicit map and inverse;
- a universal property;
- a theorem with verified hypotheses;
- an equivalence certificate in the correct category.

Numerical invariants can be used to:

- reject impossible isomorphisms;
- select candidate classes;
- test regressions;
- supply hypotheses to a classification theorem.

They cannot silently replace the missing map or completeness argument.

This is a proof-burden failure. The assistant chooses the cheapest computable proxy and lets it stand for the intended mathematical conclusion.

## 9. Accidental isomorphisms are not definitions

Many examples in the notebook admit unusually concrete descriptions:

- `Pic(P^1 × P^1) ≅ Z^2` after choosing the two ruling classes;
- `H^0(P^n,O(d))` is isomorphic to a homogeneous polynomial space;
- the Cox ring of a product of projective spaces is isomorphic to a polynomial graded algebra after choosing coordinates;
- a finite-dimensional vector space is isomorphic to `k^n` after choosing a basis;
- the standard affine charts of projective space have coordinate rings that are polynomial rings.

The assistant repeatedly treats these special isomorphisms as definitions and designs the interface around them.

That causes immediate failure outside the special case:

- a general Picard group is not a tuple lattice with named coordinates;
- a section is not globally a polynomial in an arbitrary presentation;
- a Cox ring need not be polynomial;
- a scheme need not have one preferred affine cover;
- a point need not have one canonical coordinate tuple.

A research assistant must recognize an accidental simplification as a theorem or chosen identification valid in a special class, not as the ontology of the general object.

## 10. Backend-shaped nouns obscure standard mathematics

Names such as `ProductOfProjectiveSpaces`, `projective_product_equalizer`, `factor_blocks`, and `coordinate manager` arise from implementation structure. They are not generally the mathematical nouns a researcher needs.

A product of projective spaces is first a product in `Sch`. The specialized Sage class can be a private backend representation and a dispatch predicate. It should not determine the public construction.

The public operation should be a product or fiber product with projections and a universal property. One backend may recognize that all factors are projective spaces and use multihomogeneous coordinates.

This distinction is essential for research foresight. Blowups, K3 surfaces, Enriques surfaces, and closed subschemes may enter the same general scheme product even when they do not lie in the specialized backend class.

The assistant’s engineering instinct is to name the first supported data structure and build outward from it. The mathematical instinct should be to name the standard construction and route inward to the specialized data structure.

## 11. Code should be a ledger of mathematical transport

The notebook should make the following visible:

- the object and its parent;
- the ambient category;
- the named morphism being applied;
- the direction of functoriality;
- any chosen realization or isomorphism;
- the basis, chart, or trivialization on which coordinates depend;
- the computation in the target presentation;
- the map or theorem returning the conclusion to the semantic level;
- the exact claim established.

For example, the mathematically legible Cox computation is not:

```sage
F = s.polynomial()
```

but conceptually:

```sage
CoxX = X.cox_ring()
P = X.homogeneous_coordinate_algebra()
Phi = X.cox_coordinate_isomorphism()   # CoxX -> P
Phi_L = Phi.restrict_degree(L)
F = Phi_L(s)
```

The added names are not conventional software boilerplate. They are the mathematical proof data.

Likewise, a base change should display the base morphism; a pullback should display the cospan; a local coordinate expression should display the open immersion; a matrix should display the linear map and bases it represents.

## 12. Lack of research foresight

The transcript repeatedly constructs a public wrapper for the current notebook’s one special case:

- equalizers only for products of projective spaces;
- coordinate blocks only for the current product;
- a representation helper only for the current involution;
- polynomial conversion only for one degree;
- local singularity methods only for current plane germs;
- double-cover code only for one branch equation.

The user repeatedly pushes the assistant toward the natural mathematical generalization:

- categorical pullbacks;
- graded-algebra morphisms with degree restrictions;
- functorial pullback on Picard groups and cohomology;
- relative spectra;
- cyclic covers;
- local rings and germ presentations;
- general products with gated backends.

Research foresight does not mean implementing unlimited generality immediately. It means identifying the natural general construction before writing public code. Then either:

1. implement it because the extension is short and reusable;
2. expose the general interface with explicit special-case dispatch;
3. keep the one-off computation private and refuse to coin a public mathematical noun for it.

The assistant repeatedly chose a fourth, invalid outcome: publish a one-case wrapper and call it semantic.

## 13. Research-maturity diagnosis

The transcript resembles undergraduate computational practice in several ways:

- treating familiar isomorphic objects as literally equal;
- omitting maps because “everyone knows” the identification;
- replacing proof of isomorphism by matching invariants;
- reasoning from coordinates before determining the object;
- using special examples as definitions;
- regarding successful numerical output as sufficient evidence;
- accepting plausible terminology without checking a standard reference.

A research-level assistant must instead behave as though every identification will later be composed with another construction. That forces source, target, category, variance, choices, and coherence to remain explicit.

The standard should not be pedantic verbosity for its own sake. The standard is compositional correctness. Once an unnamed identification is used, later pullbacks, actions, gradings, base changes, and descent arguments no longer have a reliable type.

## 14. Required remediation tests

A future assistant response passes this failure class only if it can answer all of the following.

1. What are the two objects being compared?
2. In which categories do they live?
3. Are they equal, isomorphic, equivalent, or only related by a realization?
4. What is the named comparison morphism?
5. What is its inverse or the theorem proving it is an isomorphism?
6. What structures does it preserve: grading, base, action, topology, filtration, polarization, or marking?
7. Is the map canonical, natural, or choice-dependent?
8. What choices determine it?
9. Does all convenience syntax route through that exact map?
10. Are coordinate calculations transported through the map explicitly?
11. Are invariant coincidences reported only as invariant coincidences unless a completeness theorem is supplied?
12. Is a backend-specific class being mistaken for the public mathematical object?
13. Is the implementation general at the natural mathematical level, explicitly gated, or deliberately private?
14. Does the code read as a ledger of the mathematical argument and its transports?

## 15. Editorial correction

Contributor guidance should avoid the same imprecision. Words such as “model,” “identify,” “corresponds,” “regard as,” and “represented by” are not automatically wrong, but they must not replace the actual relation.

When editing the assistant guide, contributors should prefer formulations such as:

- “the chosen basis determines an isomorphism”;
- “the open immersion identifies this chart domain with this open subscheme”;
- “the graded-algebra isomorphism restricts in degree `[L]` to”;
- “the forgetful functor sends this object to”;
- “these invariants agree, but no isomorphism has been constructed”;
- “the backend realizes the abstract operation on this supported presentation.”

The goal is not to ban ordinary mathematical shorthand. It is to ensure that the implementation and proof have already constructed the relation that the shorthand suppresses.
