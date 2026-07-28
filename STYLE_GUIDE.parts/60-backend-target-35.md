## 35. Preserve the mathematical target under backend pressure

When a computation or Sage backend fails, preserve the mathematical problem before changing the computational route.

### 35.1 Record every restriction as a morphism and its logical effect

If a family is given by a morphism

\[
\pi:\mathcal X\to S,
\]

then passing to a pencil, a principal open, or a single fiber means base change along a named morphism

\[
T\to S.
\]

The resulting family \(\mathcal X_T\to T\) is not the original family over \(S\). A fiber over \(t\in T\) is another base change and is not a substitute for the relative construction over \(T\).

Before a pivot, state which of the following is true:

1. the new construction proves the original claim;
2. it proves a weaker lemma needed by the original claim;
3. it supplies a witness or regression example only;
4. it changes the research question and leaves the original task open.

Do not let execution convenience decide this logical relation.

A nonconstant coefficient vector or varying equation does not by itself prove that a family is non-isotrivial. Prove that the moduli map is nonconstant, that an isomorphism-invariant of the fibers varies, or that the family cannot become constant after the relevant base change and automorphism action.

### 35.2 Distinguish exact loci from certified subopens

A sufficient certificate for smoothness is not automatically the defining equation of the discriminant.

If a polynomial \(\Delta_{\mathrm{cert}}\) is obtained from resultants, Gröbner denominators, Jacobian minors, or another sufficient criterion, state precisely whether

\[
D(\Delta_{\mathrm{cert}})
\]

is:

- the exact smooth locus;
- a proved principal subopen of the smooth locus;
- a conservative subopen containing a chosen point;
- or only a heuristic candidate.

Extraneous factors, degree-drop factors, and saturation choices must remain visible. Do not call a conservative certificate “the discriminant” or claim that it records exactly all singular parameters without an elimination or theorem proving exactness.

### 35.3 Treat relative objects as objects of a slice category

A scheme over \(S\) is the structure morphism \(X\to S\), equivalently an object of \(\mathrm{Sch}/S\). The same absolute scheme may carry several different maps to \(S\).

Do not repair lost relative structure by attaching informal side metadata or by inventing an operation such as `X.as_scheme_over(f)` whose result merely impersonates a new scheme. Preserve the named morphism \(f:X\to S\), or construct an explicit slice object whose data are exactly \(X\) and \(f\).

Base change must consume the full cospan. If a backend ignores the supplied parameter morphism and falls back to canonical coefficient coercions, repair the base-change primitive or its finite-presentation backend. Do not compensate by repeatedly changing the source scheme, chart metadata, or downstream family objects.

### 35.4 Repair the earliest violated semantic invariant

When several downstream operations fail for the same reason, identify the first construction that lost the required mathematics.

Examples:

- if covered charts remember only their immediate chart base and forget the parameter base, repair the covered-scheme or chart constructor;
- if a covered morphism lacks overlap compatibility, repair the general covered-morphism representation;
- if base change ignores a noncanonical structure map, repair affine-algebra or scheme base change;
- if a quotient or lifted action fails after base change, first verify that the underlying morphism and action were represented functorially.

Do not successively add special methods to a lift, then an overlap, then a source scheme, then a product backend when all failures arise from one missing structure morphism or functorial constructor.

### 35.5 Derive overlap maps functorially

A global morphism of covered schemes consists of local morphisms together with compatibility on overlaps. The overlap maps are not optional conveniences added only when a quotient or base change needs them.

When a local chart morphism restricts to a localization or open subscheme, construct the induced overlap morphism through the localization or restriction universal property. Coordinate formulas may implement this map, but they must not replace the functorial derivation.

Do not install coordinate-specific overlap formulas on one named involution when the real missing primitive is restriction of covered morphisms to overlaps.

### 35.6 Do not avoid legitimate mathematical parents

The prohibition on bespoke wrappers does not mean that no new parent may be defined.

A linear subsystem

\[
V\hookrightarrow H^0(X,L)
\]

is a standard mathematical object with an ambient section space, an inclusion map, a basis, a base locus, and a projectivization. If Sage lacks a parent preserving those semantics, implement or repair that standard parent. Do not misuse the complete linear system, a representation-specific isotypic component, or a generic module subspace merely to avoid introducing a necessary mathematical object.

The test is not whether a class is new. The test is whether it represents a standard object with the correct maps and is reusable at its natural mathematical level.

### 35.7 Implement affine base change from the tensor-product universal property

For affine schemes

\[
\operatorname{Spec}R\to\operatorname{Spec}A
\leftarrow\operatorname{Spec}B,
\]

the governing algebra is

\[
R\otimes_A B.
\]

Once this has been identified, organize the backend around explicit \(A\)-algebra structure maps, finite presentations, and the universal maps into the tensor product.

For polynomial, quotient, and localization presentations:

- preserve the explicit coefficient morphism \(A\to B\);
- base-change generators and relations systematically;
- map inverted elements to units and verify the localization universal property;
- return the changed algebra together with the canonical morphisms;
- patch a defective Sage homomorphism or localization primitive when that is the actual obstruction.

Do not replace this construction by repeated experiments with `change_ring()`, `base_extend()`, parent identity, private attributes, or constructor argument permutations after the universal algebra is already known.

### 35.8 Match method and category scope to actual support

Do not install `base_change()` on a generic affine-scheme class merely because it works for polynomial rings, selected localizations, or finite presentations. Put the method on the smallest Sage category whose objects uniformly carry the required data and algorithm, or gate the supported presentation explicitly.

Likewise, category refinement must not be used to claim that every object in a broad category supports a backend that has only been implemented for a narrow ring tower.

### 35.9 Preserve blocked work in the final report

When the original relative construction remains blocked, state that explicitly even if a useful pencil, principal subopen, or rational fiber has been constructed.

A verified fiber may prove nonemptiness or provide a regression case. It does not prove that:

- the family was base-changed;
- the quotient family exists over the new base;
- the smooth locus was computed exactly;
- the moduli map is nonconstant;
- or the missing Sage primitive was repaired.

Record the exact root blocker and the mathematically correct implementation route. Do not let a successful specialization erase an unresolved family-level obligation.

