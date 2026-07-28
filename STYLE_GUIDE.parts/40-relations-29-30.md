## 29. Equality, isomorphism, equivalence, and realization

Never replace a mathematical relation by informal identification merely because the related objects are routinely regarded as interchangeable.

Distinguish explicitly among:

- definitional identity in the implementation;
- equality of elements in one parent;
- equality of morphisms in one Hom-set;
- equality of subobjects in a fixed ambient object;
- a specified isomorphism in a category;
- a canonical isomorphism together with its naturality or coherence data;
- a chosen noncanonical isomorphism depending on a basis, coordinates, a trivialization, or an embedding;
- an equivalence of categories;
- a weaker relation such as birational, formal, analytic, derived, numerical, or homotopy equivalence;
- a realization morphism that need not be an isomorphism.

When the mathematics supplies an isomorphism

\[
\Phi:A\xrightarrow{\sim}B,
\]

construct and name `A`, `B`, the ambient category, `Phi`, and its inverse. Do not implement the situation by making elements of `A` silently become elements of `B`, by returning one parent in place of the other, or by writing `A == B` unless they are literally equal in the relevant parent.

Record any grading map, base morphism, variance, naturality square, or coherence condition needed for `Phi` to be the claimed kind of isomorphism. Isomorphisms of underlying sets, modules, rings, graded rings, sheaves, schemes, and functors are different claims.

Convenience syntax may suppress notation but not data. A method such as `s.to_polynomial()` must apply a stored explicit morphism. Its inverse must be the inverse of that same morphism. The sugar must not create a second implicit identification.

### Cox rings and polynomial coordinates

The abstract Cox ring

\[
\operatorname{Cox}(X)=\bigoplus_{[L]}H^0(X,L)
\]

and a graded polynomial algebra are distinct objects in the relevant category of graded `k`-algebras. In cases where chosen homogeneous coordinates produce an isomorphism, the implementation must construct a morphism in that category and prove that it is an isomorphism

\[
\Phi_X:\operatorname{Cox}(X)\xrightarrow{\sim}k[x_0,\ldots,x_N]
\]

and use its degree restrictions

\[
\Phi_{X,L}:H^0(X,L)\xrightarrow{\sim}k[x_0,\ldots,x_N]_{[L]}.
\]

A section is not a polynomial. A polynomial expression is the image of a section under `Phi_{X,L}`. Polynomial substitution, differentiation, elimination, and Jacobian computations therefore occur after explicit transport to the polynomial algebra. Intrinsic conclusions must be transported back or proved independent of the chosen realization.

### Points and coordinates

An `R`-valued point is a morphism

\[
p:\operatorname{Spec}R\to X.
\]

A tuple is constructor input or the coordinate expression of `p` in a chosen chart. An affine coordinate tuple belongs to the domain of an open immersion `j:U -> X`; it represents `p` only together with a point `q:Spec(R) -> U` satisfying `j ∘ q = p`. Do not replace the point, chart, and open immersion by one untyped tuple.

## 30. Do not substitute weaker evidence for a harder mathematical claim

A collection of invariants is not an isomorphism. Matching dimensions, ranks, cardinalities, Hilbert series, Hodge numbers, intersection forms, Gram matrices, singularity numbers, or other numerical data may obstruct or suggest an isomorphism, but it does not construct one.

Before claiming equality, isomorphism, equivalence, quotient identification, or classification, state the exact proof obligation.

For an isomorphism, normally provide at least one of:

1. a named morphism and a named inverse with both composites verified;
2. a universal property that identifies the object uniquely in the relevant category;
3. a theorem whose hypotheses have been established and whose conclusion is precisely the asserted isomorphism;
4. a fully faithful comparison together with essential surjectivity when proving an equivalence of categories;
5. an explicit normal-form or local-algebra isomorphism when classifying a germ.

Do not let the following stand in for an isomorphism without a completeness theorem:

- equal numerical invariants;
- the same generators or equations after an unexplained identification;
- a matching database row;
- an equality after forgetting grading, topology, base, action, or other structure;
- a bijection of computed points;
- two objects having isomorphic coordinate rings without naming the contravariant scheme morphism and checking the relevant hypotheses;
- agreement on one dense chart or one presentation.

State exactly what the evidence proves. If it proves only compatibility, equality after applying a functor, or agreement of invariants, report only that weaker conclusion.

