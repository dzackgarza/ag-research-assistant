## 36. Build global constructions from general local primitives

Do not begin a difficult global construction at the most specialized family, cover, quotient, or moduli object and then chase backend failures downward through its charts. Reconstruct the mathematical dependency order first and implement from the general local primitive upward.

### 36.1 Draw the construction dependency graph before coding

Before extending a global Sage object, identify:

1. the global construction requested;
2. its affine-local construction;
3. the underlying algebraic universal operation;
4. the theorem or descent mechanism that globalizes it;
5. the existing Sage objects that should inherit the result compositionally;
6. the earliest missing primitive;
7. the competing implementation routes and their estimated complexity.

Do not optimize the next executable line before this dependency graph is understood. A short local patch can enter an expensive implementation basin whose later layers all depend on a more general missing primitive.

### 36.2 Construct pushouts of rings and algebras first

For explicit morphisms of commutative rings or algebras

\[
A\longrightarrow R,
\qquad
A\longrightarrow B,
\]

the local base-change primitive is the pushout

\[
R\otimes_A B.
\]

Construct the tensor product together with the canonical maps

\[
R\longrightarrow R\otimes_A B,
\qquad
B\longrightarrow R\otimes_A B,
\]

and verify its universal property in the relevant category of commutative rings or \(A\)-algebras. Do not begin by adding `base_change()` to a cyclic-cover family or another specialized global object when this algebraic pushout is not yet represented correctly.

Audit Sage's existing tensor-product, pushout, quotient, localization, and algebra-homomorphism implementations before writing a replacement. Test noncanonical coefficient morphisms, not only coercion-induced maps.

### 36.3 Obtain affine pullbacks by contravariant `Spec`

The affine-scheme pullback

\[
\operatorname{Spec}R
\times_{\operatorname{Spec}A}
\operatorname{Spec}B
\]

must be constructed as

\[
\operatorname{Spec}(R\otimes_A B).
\]

Return the pullback diagram: the apex, both projections, the original cospan, commutativity, and the universal morphism. Verify that `Spec` reverses the algebraic pushout maps into the correct scheme morphisms.

A family-specific affine base-change method is secondary sugar. It must delegate to this general affine pullback rather than own a parallel implementation.

### 36.4 Make standard affine presentations stable under the primitive

Verify the standard compatibilities

\[
(R/I)\otimes_A B
\cong
(R\otimes_A B)/I(R\otimes_A B)
\]

and

\[
R_f\otimes_A B
\cong
(R\otimes_A B)_{f\otimes 1}
\]

with explicit comparison morphisms and hypotheses. Polynomial extensions, quotient rings, localizations, Laurent presentations, and principal-open presentations are backend realizations of one tensor-product construction, not independent notions of base change.

If Sage cannot express a noncanonical coefficient map through a localization or quotient parent, repair that primitive or provide a faithful finite-presentation shadow. Do not successively replace nested localizations by quotient presentations, then Laurent rings, then specialized transition formulas without deciding which general algebraic interface is missing.

### 36.5 Globalize by covers, descent, or relative `Proj`

After affine pullbacks work:

1. base-change every affine chart;
2. base-change every overlap;
3. transport restriction morphisms;
4. verify pairwise compatibility and cocycle identities;
5. glue the changed charts;
6. glue the local projection morphisms;
7. verify the global universal property.

For projective or relatively projective schemes, inspect relative `Proj` and its base-change theorem before reconstructing the object chartwise. Use affine-cover gluing when that is the appropriate available route.

Cyclic covers, quotient families, actions, lifted involutions, and moduli families should inherit base change from the general scheme and morphism operations. Do not implement the dependency in the reverse direction.

### 36.6 Choose the broadest high-leverage primitive that is proportionate

When a specialized global computation exposes a missing primitive, compare:

- the cost of a general foundational repair;
- the accumulated cost of the current special case and likely neighboring cases;
- the mathematical and software reuse obtained;
- the risk of maintaining several inconsistent local implementations.

Implement the general primitive when its cost is reasonable and it removes a whole dependency class. Gate or backlog it when it is genuinely substantial, with a concrete implementation route that preserves the general mathematical interface.

### 36.7 Survey the mathematical and software landscape before descent into details

Before designing a new general primitive:

1. search Sage documentation, source, categories, tickets, and adjacent methods;
2. check whether categorical pullbacks, tensor products, relative `Spec`, relative `Proj`, affine covers, or descent infrastructure already exist partially;
3. inspect bridges to Singular, Macaulay2, GAP, Magma, PARI/GP, Julia, Oscar, or other relevant systems;
4. search for reference implementations in established computer-algebra systems or research code;
5. consult standard mathematical references and explicit algorithms;
6. compare the available semantics, supported domains, and integration cost.

Use web and literature research proactively when it can reveal a broad existing solution. Do not spend a long research session reinventing a tower of special cases without checking whether another system or reference implementation already provides the general operation.

### 36.8 Avoid greedy implementation paths and local minima

A sequence of individually reasonable local fixes can have poor global cost. Before committing to a route, compare at least two plausible paths and estimate:

- how many new parents, morphisms, and compatibility proofs each requires;
- whether each path preserves the standard mathematical abstraction;
- which downstream constructions become automatic;
- which Sage defects remain;
- whether the work is reusable beyond the current notebook.

Reassess after each new backend failure. Repeated need for special chart, overlap, point, localization, or family patches is evidence that the dependency direction is wrong. Stop and move to the governing local primitive rather than continuing greedily.
