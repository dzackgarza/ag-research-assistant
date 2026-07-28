# Backend Pressure and Mathematical Target Drift

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Sources:** recent Coble-family Sage work trace and subsequent category-construction correction transcripts supplied by the user.
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

## 12. Wrapper, category, then reified category constructor

The category-construction transcript exposes the same one-rung remediation pattern at a more abstract level. The assistant first treats a backend wrapper as the mathematical object. After correction, it recognizes that the object is an arrow in a slice or coslice category. It then stops one rung too early again and proposes independent `SliceCategory` or `CosliceCategory` families, although the construction should be generated functorially from the ambient category.

The complete mathematical reconstruction has three distinct steps:

1. identify the underlying datum as an arrow or diagram in the ambient category;
2. identify the standard diagram category whose objects and morphisms encode that datum and its commuting conditions;
3. recognize that this category is itself obtained by a functorial categorical construction applied to the ambient category and the chosen base object.

A backend wrapper may realize an arrow object so that its codomain elements participate in Sage's parent/element framework. It must not become the foundational definition. Likewise, a private generic constructor may implement slice or coslice mechanics, but the public mathematical ownership belongs to the ambient category's construction and must compose with its refinements.

This is a general failure, not a rule about ring extensions. It recurs whenever the assistant invents independent category families for arrows, actions, graded objects, functor categories, equivariant objects, or other domains already generated by standard category constructors. The stopping test is: after naming the standard category, has the assistant also identified how that category is functorially constructed and owned?

## 13. Source-free categorical laundering

The ring-extension transcript adds a more basic form of the same one-rung repair. The assistant begins from a backend wrapper and coins an informal mathematical noun around it. After correction, it places that noun in a category. Only after further pressure does it recognize that the object was already an ordinary arrow in a standard comma construction, and then that the comma construction itself should be generated functorially from the ambient category.

This is not merely failure to remember one definition. It is failure to consult the sources that would have fixed the ontology before implementation. A careful researcher encountering an unfamiliar foundational noun would search the local textbooks and papers, then standard references and formal-library documentation, to determine:

- whether the datum is an object, arrow, diagram, class, property, or presentation;
- the ambient category and its Hom-sets;
- the standard morphisms and commuting conditions;
- whether the category is a slice, coslice, arrow, comma, functor, action, or other standard construction;
- whether that construction is functorial in an ambient category;
- the exact terminology and competing conventions;
- the corresponding Sage or formal-library architecture.

Without this pass, the assistant can comply with every surface imperative—use parents, use categories, use morphisms—while preserving the same bespoke engineering ontology one abstraction layer higher. This is **categorical laundering**. The category is syntactically valid, but it exists only to legitimize the wrapper that should have been dissolved into standard mathematics.

References must therefore participate in design rather than appear afterward. The local research corpus, the Stacks Project, Kerodon, official Sage and Mathlib documentation and source, established textbooks and papers, and broad orientation references can reveal that an apparently new noun is already a standard construction. A reference-backed classification may also show that several common phrases denote different objects or that a colloquial term suppresses essential variance or structure.

The regression question is not “did the assistant cite something?” It is “did the sources force the assistant to change or justify the ontology, morphisms, and public interface?” If not, the reference work did not discharge the mathematical classification obligation.

## 14. Backend friction as a prompt to reformulate the mathematics

A further transcript class concerns Sage limitations that attract a long chain of increasingly local repairs. Equality of morphism composites is one example: Sage may construct the intended maps but fail to recognize two composites as equal because they pass through different parents, coercions, factorizations, or coordinate presentations. The assistant then starts adding normalization and equality patches.

The broader lesson is not specifically about equality. A software deficiency can reveal either that Sage is missing a correct mathematical primitive or that the task has been phrased through an unnecessarily rigid or presentation-dependent notion. A more intrinsic modern formulation may make the actual witness first-class and remove the operation Sage handles poorly.

For example, a brittle equation between representatives may become a specified comparison morphism, natural isomorphism, 2-cell, or homotopy in the standard theory. A difficult quotient by representatives may be better expressed by a universal quotient, localization, stack, or moduli object. Repeated descent or gluing patches may indicate that the correct object is a sheaf, stack, or diagram with explicit coherence data. These are not automatic prescriptions; they are directions for mathematical reconnaissance.

The agent must distinguish three outcomes:

1. **Repair Sage.** The original formulation is mathematically intrinsic, and Sage simply lacks or mishandles the required primitive.
2. **Reformulate.** Standard mathematics supplies a more semantic formulation that is explicitly related to the original claim and removes the deficient operation.
3. **Reject the pivot.** The proposed reformulation changes or weakens the theorem and therefore cannot substitute for the requested result.

The self-nudge is triggered by repeated local repairs around one limitation: coercion chains, canonical representatives, normalization of composites, special comparison code, chartwise compatibility patches, or backend-specific proxies. At that point the assistant should search the local corpus and appropriate modern references, identify the competing formulations, and compare their proof and implementation obligations.

There are two opposite dangers. **Backend fixation** keeps the current representation fixed and spends arbitrary effort repairing its accidental deficiencies. **Theory laundering** invokes a more sophisticated framework without constructing the comparison to the original problem or without showing that it actually simplifies the work.

The correct outcome may still require literal equality, a native Sage repair, or a strict implementation. It may instead require a weaker or higher comparison datum. The conclusion must come from the mathematics and an explicit comparison theorem, not from whichever interface Sage happens to expose.

The user should not need to supply the modern viewpoint after several failed repairs. The assistant should treat concentrated backend friction as its own prompt to ask whether a more principled mathematical notion both improves the semantics and obviates the deficiency.

## 15. Positive practices to retain

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
