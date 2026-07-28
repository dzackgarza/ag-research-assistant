# Backend Pressure and Mathematical Target Drift

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** recent Coble-family Sage work trace supplied by the user.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Overall assessment

The trace contains substantial good work. The assistant distinguishes backend failure from geometry, abandons a probabilistic Giac elimination result when exact certification is needed, derives parameter coordinates by exact linear algebra rather than hard-coded positions, verifies overlap squares and involutivity, and eventually states two precise backend blockers.

The principal defect is subtler: under computational pressure, the assistant repeatedly changes the mathematical object or theorem until it reaches something the current backend can execute.

The trajectory is:

\[
\text{smooth subopen of a 13-parameter family}
\rightsquigarrow
\text{one-dimensional pencil}
\rightsquigarrow
\text{principal subopen of that pencil}
\rightsquigarrow
\text{one rational fiber}.
\]

Each restricted construction can be mathematically valuable. The failure is allowing the later object to inherit the rhetoric of the earlier task without a precise implication.

## 2. Full discriminant problem replaced by a pencil

The initial goal is a certified smooth principal subopen in the full parameter base and base change of the K3 and Enriques families. Generic function-field Gröbner computations time out, after which the assistant says it is “replacing” the computation by a non-isotrivial pencil.

A pencil is a morphism

\[
\iota:\mathbf A^1\longrightarrow \mathbf A(V_+).
\]

The family on the pencil is the pullback of the universal family along \(\iota\). It is not a construction of a smooth open in the full 13-dimensional base.

A correct pivot report should say:

- the full discriminant or smooth subopen remains uncomputed;
- the pencil gives a one-dimensional test family;
- the resultant certificate constructs a principal subopen of that pencil;
- this may prove nonemptiness or provide a reusable witness;
- it does not solve the original full-base problem unless an additional argument lifts the result.

## 3. Nonconstant is not non-isotrivial

The trace calls the pencil “genuinely varying” because a second monomial is added with parameter \(t\), and calls the resulting family non-isotrivial.

This does not follow. Different equations or sections can define isomorphic fibers after scalar multiplication or automorphisms of the ambient variety. Non-isotriviality requires a nonconstant map to the relevant moduli space or stack, or a fiber invariant that genuinely varies and is complete enough to obstruct isomorphism.

The assistant must distinguish:

- a nonconstant map into a section space;
- a nonconstant map into a linear system;
- a nonconstant orbit in the quotient by ambient automorphisms;
- a nonconstant moduli map;
- a non-isotrivial family.

## 4. Certified subopen is not the discriminant complement

The iterated-resultant construction is a valid sufficient smoothness certificate: any chart singularity forces the resultant to vanish. The assistant correctly notes extraneous degree-drop factors and that the certificate excludes \(t=0\).

That means \(D(\Delta_{\mathrm{cert}})\) is a conservative principal subopen contained in the smooth locus of the pencil. It is not necessarily the exact smooth locus, and \(\Delta_{\mathrm{cert}}\) is not necessarily the discriminant polynomial.

Earlier wording that an elimination ideal or resultant “records exactly” the singular parameters must be removed unless the required saturation, projective closure, and elimination theorem are actually established.

## 5. Scheme-over data collapsed into an object wrapper

When base change fails because the affine source retains only a map to \(\operatorname{Spec}\mathbf Q\), the assistant invents

```sage
U.as_scheme_over(f)
```

to return “the same affine spectrum equipped with that structure morphism.”

Mathematically, an \(S\)-scheme is the morphism \(f:U\to S\), an object of the slice category \(\mathrm{Sch}/S\). The absolute scheme \(U\) has not changed. If Sage needs a first-class relative object, the correct shadow is a slice object containing \(U\) and \(f\), or the base-change operation should accept the explicit cospan.

Attaching a structure map as mutable or side metadata recreates the same identity-versus-structure collapse seen elsewhere in the logs.

## 6. The first failure site was not the root failure

The assistant successively patches:

1. the Enriques lift;
2. overlap morphisms for the sign involution;
3. the source affine scheme;
4. point morphism extraction;
5. the covered-product base check;
6. the generic affine-scheme method family;
7. polynomial, localization, and quotient ring extension.

Eventually it discovers the root issue: covered affine charts have lost the composite structure map to the parameter scheme, and affine base change cannot form

\[
R_{\mathrm{chart}}\otimes_A B
\]

along a noncanonical map \(A\to B\).

A research-level debugging discipline should identify the earliest violated invariant before adding public methods. Here the earliest invariant is: every relative chart and covered morphism must retain its structure map to the family base, and base change must use that map.

## 7. Specialized overlap formulas substituted for covered-morphism semantics

The diagonal-sign involution has compatible local maps but no overlap maps. The assistant constructs an overlap involution by negating chosen localization generators, then installs `overlap_morphism()` and `base_change()` on that specialized class.

The mathematical missing object is a global morphism of covered schemes. Such a morphism must contain local maps and compatibility on overlaps. Its restriction to an overlap should be induced functorially by localization or open restriction.

Negating generators can be the coordinate implementation of the restricted involution. It should not be the public definition, and the method should not be special to one sign involution if every covered morphism needs the same restriction mechanism.

## 8. Avoiding wrappers becomes avoidance of standard objects

Later the assistant needs a rank-one section subspace. A generic module subspace does not preserve ambient section elements, while the available section-subspace parent is representation-specific. To “avoid inventing a new parent,” the assistant tries to use the complete linear system instead.

This is an overcorrection. The earlier criticism concerned invented software nouns with no mathematical semantics. A linear subsystem

\[
V\hookrightarrow H^0(X,L)
\]

is a standard mathematical object. It deserves a parent with an ambient inclusion if Sage lacks one. Reusing the complete linear system or an isotypic-component parent is less semantic, not more.

## 9. Universal algebra recognized but not used as the organizing primitive

The assistant eventually states the correct affine base-change algebra:

\[
\operatorname{Spec}(R\otimes_A B).
\]

After this recognition, it continues probing `change_ring`, `base_extend`, localization private attributes, parent identity, and constructor validation.

The correct backend design is to represent an affine \(A\)-algebra by its explicit structure map and a finite presentation, then construct the tensor product. Polynomial, quotient, and localization cases are presentation routes into the same universal object. If Sage's localization homomorphism cannot express a noncanonical coefficient map, that is a native primitive to repair or faithfully shadow.

The universal construction should organize the debugging; API trial-and-error should not determine the mathematics.

## 10. Method-family overreach

The trace considers extending the “native base-change family” to the generic `AffineScheme` class. But not every affine-scheme parent necessarily exposes a finite presentation or an implemented tensor-product route.

The method belongs on the smallest category of affine schemes or affine algebras for which the required structure map and algorithm are uniformly available. Otherwise the general method must dispatch and gate.

This is precisely where category refinement can help, but only if the refined category is mathematically true and the implementation contract is uniform.

## 11. A rational fiber does not complete the family

After the family-level construction remains blocked, the assistant selects \(t=1\), constructs a smooth free quotient fiber, and persists it.

This is good evidence:

- it proves the certified open is nonempty;
- it provides a new verified example;
- it can serve as a regression case.

It does not base-change the K3 or Enriques family to the principal open. It does not repair noncanonical affine base change. It does not construct the quotient family over the pencil.

The final report must preserve those obligations instead of allowing the successful fiber to become the apparent endpoint of the original task.

## 12. Positive practices to retain

The guidance should preserve the following strong behavior from the trace:

- distinguish a Sage backend exception from a mathematical nonexistence claim;
- reject probabilistic certification when exact proof is required;
- label conservative certificates and inspect extraneous factors;
- recover parameter coordinates through exact ambient linear algebra;
- use named parameter morphisms and verify pullback of the universal section;
- verify overlap squares, cocycles, involutivity, and quotient compatibility;
- inspect native Sage source and existing interfaces before writing replacements;
- state exact backend limitations when work is blocked.

The correction is not to make the assistant less persistent. It is to make persistence invariant under the mathematical goal: repair the correct primitive or record a logically explicit restriction, rather than repeatedly changing the object until execution succeeds.
