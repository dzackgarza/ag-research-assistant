## 9. Divisors, line bundles, and Picard data

Treat divisor-theoretic objects according to their actual definitions.

For a scheme or variety `X`, distinguish:

- Weil divisors;
- Cartier divisors;
- divisor classes in `Cl(X)`;
- invertible sheaves and their classes in `Pic(X)`;
- numerical or algebraic equivalence classes;
- chosen equations or presentations.

A pair such as `(a,b)` on `P^1 × P^1` is a coordinate representation relative to chosen generators, not the semantic definition of a line bundle or divisor class.

Intersection products, canonical classes, cohomology, section rings, and linear systems are distinct constructions. Attach each to the correct ambient object and state the required hypotheses.

Do not invent methods such as a generic `hodge_number` on a divisor or line bundle when the proposed quantity is undefined or belongs to a different cohomological object.

## 10. Group actions and sections

Distinguish actions on the base, linearizations of sheaves, and induced representations on cohomology.

Given a group action on `X`, an action on a line bundle `L` requires a linearization or equivalent descent datum. Only then is an action induced on `H^i(X,L)`.

`H^0(X,L)` is generally a module or vector space, not an algebra. The graded section ring

\[
R(X,L)=\bigoplus_{n\ge 0} H^0(X,L^{\otimes n})
\]

is an algebra when its multiplication is part of the construction.

Compute invariants, coinvariants, characters, and eigenspace decompositions on the correctly induced representation. Do not create a free-standing “representation on sections” object that suppresses the base action and linearization data.

## 11. Morphisms, graphs, and fixed subschemes

Morphisms are first-class mathematical objects with explicit domain and codomain.

For a morphism `f : X -> Y`:

- the graph morphism is the primitive map `f.graph_morphism()`;
- its codomain represents the graph subscheme in the relevant product;
- scheme-theoretic image, inverse image, pullback, and related operations must retain their defining morphisms and conventions.

Do not add a redundant `f.graph()` convenience object when `f.graph_morphism().codomain()` already gives the graph.

For an endomorphism `f : X -> X`, the fixed subscheme is the equalizer of `f` and `id_X`. A method such as `f.fixed_subscheme()` is mathematically justified because the endomorphism owns the defining parallel pair together with its domain.

Do not define a free-standing fixed-locus factory detached from the endomorphism structure.

## 12. Linear systems and evaluation

A line bundle does not automatically define a global morphism to projective space.

Given a linear system `V ⊆ H^0(X,L)`:

- determine its base locus;
- check global generation or basepoint-freeness where a morphism is claimed;
- compute the actual dimension of the target projective space;
- distinguish a morphism from a rational map;
- retain the chosen subspace of sections when the system is incomplete.

Point evaluation maps and their matrices are derived from `V`, `L`, the points, and chosen bases. They are not independent primitive geometric objects.

Expose matrices, ranks, kernels, and cokernels as computational presentations of the underlying maps. Do not let a matrix replace the map it represents.

