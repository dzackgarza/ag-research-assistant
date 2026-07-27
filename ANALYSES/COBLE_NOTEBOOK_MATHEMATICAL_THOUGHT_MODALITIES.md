# Coble Notebook Logs: Mathematical Thought Modalities

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.
**Sources:** `Coble-Notebook.md`, `Coble-Notebook (1)(1).md`, and `Coble-Notebook (2).md`. These are cumulative snapshots of one correction trajectory, with minor exporter-tail differences; the longest snapshot contains the earlier material and the later framework, family, and backend phases.
**Status:** contributor-facing analysis; not part of the prompt uploaded to the AG assistant.

## 1. Correction to the failure-catalogue approach

The transcript should not primarily be read as a catalogue of forbidden method names, bad wrappers, missing assertions, or notebook formatting defects. Those are observable symptoms. The user generally found the defects without maintaining such a catalogue. The user applied ordinary research-mathematical reflexes:

- ask what the object actually is;
- ask in which category it lives;
- ask which morphism relates two nonidentical objects;
- ask whether the construction is standard and functorial;
- ask whether the local or coordinate computation descends to the global object claimed;
- ask what theorem converts the computed data into the stated conclusion;
- ask whether the public abstraction has reached the natural mathematical domain;
- ask whether the notebook reads as the mathematical argument.

The deepest problem is therefore not that the assistant failed to memorize enough prohibitions. It is that the assistant repeatedly approached the work as software synthesis decorated with mathematical language, whereas the user approached it as mathematics whose constructions happen to require Sage realizations.

A useful guide must teach the latter mode of thought. Incident-specific prohibitions remain useful as regression checks, but they should be consequences of a smaller collection of positive mathematical disciplines.

## 2. Governing contrast

The assistant's recurrent order of operations was approximately:

1. inspect the visible coordinate code;
2. invent a helper, wrapper, class, or method that reproduces it;
3. give the helper a mathematical-sounding name;
4. verify the motivating example;
5. treat reuse on one or two neighboring examples as evidence of semantic generality;
6. wait for the user to name the missing parent, map, functor, universal construction, descent datum, or theorem.

A research mathematician's order is different:

1. identify the standard mathematical objects;
2. type every datum by its parent, category, and base;
3. identify the relevant morphisms and variance;
4. recognize the standard construction or universal property;
5. state the hypotheses and exact proof obligation;
6. choose a computational presentation and construct the comparison maps;
7. compute in that presentation;
8. transport the result back to the intrinsic object;
9. expose only the mathematically natural operation, with presentation-specific code behind it.

The corrections in the transcript are best understood as repeated attempts to force the assistant from the first order of operations into the second.

## 3. Modality I: ontological typing

### 3.1 Ask what the thing is before manipulating it

Every object must be typed mathematically before code is designed around it. The relevant questions are:

- Is this an object, an element, a subobject, a morphism, a class of objects, or a presentation?
- What is its parent?
- What is the base scheme or base ring?
- What additional structure is part of the object: grading, action, polarization, marking, embedding, linearization, or descent datum?
- Is the current datum the object itself, an isomorphism class, or a chosen representative?

This single discipline explains many corrections that otherwise look unrelated.

### 3.2 Classes are not representatives

An element of `Pic(X)` is an isomorphism class of invertible sheaves. It is not automatically a particular invertible sheaf with restriction maps, stalks, local trivializations, a total space, or a chosen multiplication isomorphism. Some operations descend canonically to isomorphism classes; others require an actual representative or additional choices.

The transcript repeatedly let a Picard-class proxy impersonate a line bundle. A careful implementation must distinguish the Picard group `Pic(X)`, a class `[\mathcal L]` in it, and an actual invertible sheaf `\mathcal L` representing that class, and must retain the passage from the representative to its isomorphism class. If a method on a class constructs sections, stalks, total spaces, linearizations, or cyclic covers, it must either recover a canonical representative in the supported setting or make the chosen representative explicit.

The same issue occurs for:

- a Weil divisor versus its class in `Cl(X)`;
- a Cartier divisor versus the associated invertible sheaf;
- an embedded hyperplane-class subgroup versus the full Picard group;
- an equation versus the closed subscheme it defines;
- a normal form versus the germ it presents.

### 3.3 Elements retain their parents

A point is not a tuple. It is a morphism

\[
p:\operatorname{Spec}R\to X.
\]

A tuple may be input to a constructor or coordinates of a lift to an affine chart. A section is not a polynomial. A polynomial may be its image under a chosen graded-algebra isomorphism. A matrix is not a linear map. It is the matrix of a map after choosing bases.

The user repeatedly detected errors by noticing that the code had discarded the parent and retained only coordinates. That is a standard mathematical warning sign: operations on untyped tuples, lists, or polynomials are no longer visibly operations on the geometric objects under study.

### 3.4 Partial objects must not impersonate full objects

A Sage `Parent` is not mathematically justified merely because it satisfies a software interface. Its name must match the object it actually represents.

Examples from the trajectory include:

- a recognized subset of linear automorphisms must not be called the full `Aut(X)`;
- the image of `Pic(P^n) -> Pic(W)` must not be called `Pic(W)` when the full group is unknown;
- a classifier for a restricted class of plane-curve germs must not appear as a total `ADE_type()` operation;
- a collection of affine charts must not be called a global scheme before gluing data are supplied;
- cyclic-cover input data must not be presented as an actual global cover morphism before relative `Spec` or a correct global realization is constructed.

The mathematical question is not “does this class pass its tests?” It is “does this parent have the defining semantics of the object named?”

## 4. Modality II: relational and morphism-first thought

### 4.1 Mathematics does not permit silent replacement

When two objects are not literally equal, the relation between them is data. A careful mathematician asks:

- What is the map?
- What are its source and target?
- In which category is it a morphism?
- Is it an isomorphism, embedding, quotient, localization, completion, base change, or forgetful map?
- Is it canonical or chosen?
- What structure does it preserve?
- What inverse, naturality, or coherence data are available?

The transcript's Cox-ring corrections are the clearest example. The abstract graded algebra of sections and a polynomial graded algebra are distinct objects. In supported cases there is a chosen graded-algebra isomorphism

\[
\Phi_X:\operatorname{Cox}(X)\xrightarrow{\sim}k[x_0,\dots,x_N],
\]

and fixed-degree maps are restrictions of `Phi_X`. Calling a section a polynomial or implementing `H.polynomial(s)` without the stored comparison map erases the mathematical relation that justifies the computation.

### 4.2 Base change is along a morphism

`X.base_extend(S)` was criticized because a ring or field was supplied where the geometry requires a named base morphism. Base change is a pullback. Given

\[
X\to S\leftarrow T,
\]

one forms `X_T = X ×_S T`. The morphism `T -> S` is not optional metadata. It determines the construction.

This is the same discipline as refusing to write `X ×_S T` before naming the cospan. “Natural map” and implicit coercion are not substitutes for the actual morphism when several maps can exist or when functoriality matters.

### 4.3 Sugar must route through stored maps

Convenience syntax is appropriate only when it applies a named mathematical morphism already stored by the objects. For example:

- `s.to_polynomial()` applies the degree restriction of `Phi_X`;
- `H.from_polynomial(f)` applies its inverse;
- an element-level section pullback applies the parent-level linear map induced by `f^*`;
- a coordinate expression of a point is obtained by pulling it back through an open immersion.

A convenience method that recomputes an identification independently creates a second, untracked relation and breaks coherence.

## 5. Modality III: functorial thought

### 5.1 Ask for the parent-level map first

The assistant repeatedly invented methods on individual elements where the standard mathematics supplies a functor or natural transformation on parents.

For a morphism `f:X -> Y`, the fundamental data include

\[
f^*:\operatorname{Pic}(Y)\to\operatorname{Pic}(X)
\]

and, for an invertible sheaf `L` on `Y`,

\[
f^*:H^0(Y,L)\to H^0(X,f^*L).
\]

An operation such as `f.pullback_section(s)` is secondary syntax. It should be obtained by applying the induced map on section spaces. This parent-level formulation makes variance, codomain, functoriality, and hypotheses visible.

The same pattern governs:

- restriction to a subscheme;
- pushforward and pullback of sheaves;
- induced maps on cohomology;
- actions on sections;
- base change;
- evaluation.

### 5.2 Derived representation theory starts from an action and a linearization

Filtering monomials by signs is a coordinate realization of a representation-theoretic construction. The mathematical chain is:

1. a group action on `X`;
2. a linearization of `L` compatible with that action;
3. the induced representation on `H^i(X,L)`;
4. its isotypic decomposition;
5. invariants, sign spaces, characters, and matrices as derived data.

The assistant initially promoted the current `+/-` filtering procedure to an API. The user recognized it as the two-character case of the standard isotypic decomposition. The correction was not merely to rename the function. It was to reconstruct the functorial dependency chain.

### 5.3 Adjunctions and counits should be recognized

The coefficient expression `sum c_i s_i` led to several invented notions—“universal element,” “generic section,” and “affine section space”—before the standard construction was recognized. For the structure morphism `p:X -> Spec(k)`, the key map is the evaluation counit

\[
p^*p_*\mathcal L\to\mathcal L.
\]

After applying the relative-spectrum construction, this produces the evaluation morphism connecting the parameter scheme of sections to the total space of `L`. Choosing a basis merely writes the canonical map in coordinates.

A research-level reflex is to ask whether an apparently new map is a unit, counit, component of a natural transformation, or application of a familiar functor before inventing a new object around it.

## 6. Modality IV: recognition by universal property

### 6.1 Standard constructions should be recognized before equations are written

The user repeatedly moved the assistant from equations to universal constructions:

- fixed subscheme: equalizer of `f` and `id_X`;
- equalizer: pullback of the diagonal along `(id_X,f)`;
- graph: the morphism determined by a product universal property;
- base change: a fiber product;
- affine space or vector bundle: relative `Spec Sym`;
- complete linear system: projectivization of the section space together with its tautological map;
- cyclic cover: relative `Spec` of a graded algebra determined by root data;
- quotient: invariant-ring or categorical quotient with an actual quotient morphism.

The determinant equations for fixed points were not wrong. The error was treating them as the construction rather than as the coordinate equations obtained after constructing or recognizing the diagonal.

### 6.2 Universal properties control interfaces

A mathematically faithful pullback object should expose the apex, two projections, original cospan, commutativity, and universal morphism. A product helper that returns only equations has discarded the defining property.

Likewise, a “graph” method returning a subscheme can be redundant when the primitive graph morphism already has that subscheme as its codomain. The universal-property perspective identifies which data are primitive and which are recovered compositionally.

### 6.3 Abstract vocabulary is not universal-property reasoning

The assistant sometimes responded to criticism by announcing a “categorical product” or “semantic interface.” That is not the mathematical modality described here. Universal-property reasoning requires the actual diagram and the factorization property. The words `categorical`, `semantic`, and `universal` are empty unless the defining data are present.

## 7. Modality V: level discipline

Research mathematics constantly separates levels that software-oriented reasoning tends to flatten.

### 7.1 Intrinsic and presented

An intrinsic object may be calculated using a presentation, but the presentation is not the public ontology. The notebook should construct the intrinsic object first and then display its coordinate realization.

Examples:

- fixed subscheme before determinant equations;
- restriction map before its matrix;
- section before its polynomial image;
- local germ or local ring before a chosen equation;
- quotient before a specific invariant-ring presentation;
- line bundle before bidegree coordinates.

### 7.2 Local and global

Local equations do not constitute a global scheme, morphism, cover, quotient, or family. A global object requires overlaps, transition maps, cocycle conditions, and compatibility of local morphisms.

This failure recurred when:

- affine double-cover equations were reported as a global cover;
- chart dictionaries were presented as a family;
- local invariant-ring charts were presented as an Enriques quotient;
- local singularity checks were used without a global exclusion of further singular points.

A research mathematician naturally asks how the local data glue and whether the required descent datum exists.

### 7.3 Absolute and relative

`Spec(k[x])` may carry an absolute structure over `Spec(Z)`, but affine-line and family constructions require its specified structure over `Spec(k)`. Relative objects must retain their base and structure morphism.

Confusing absolute and relative schemes corrupts later fiber products, base change, and family morphisms. This is not a naming papercut; it changes the mathematical object.

### 7.4 Affine parameter spaces and projective linear systems

The affine space of sections and the projective linear system solve different moduli problems:

- the affine scheme retains zero and scalar multiples;
- the projective space parametrizes nonzero sections up to scalar, hence divisors;
- universal cover data may descend over one and not the other.

The transcript eventually found the `O(1)` obstruction to a canonical universal double cover over the projective linear system. This is exactly the kind of issue that disappears when parameter spaces are treated as interchangeable coefficient containers.

### 7.5 Families and fibers

A construction that exists on every fiber does not automatically form a family. One must check relative line bundles, base twists, flatness when relevant, and descent of all defining data. The universal K3-cover correction is a primary regression case.

### 7.6 Direct computation and indirect deduction

Computing a full-dimensional smooth open sublocus and using ambient upper and lower bounds can establish the dimension of a larger ADE locus. It does not compute the ADE locus itself. The assistant must preserve the distinction between:

- the object or locus directly constructed;
- the theorem-derived conclusion;
- the still-missing equations or stratification.

## 8. Modality VI: theorem-mediated proof

### 8.1 State the claim at its exact strength

A careful researcher identifies the precise conclusion before choosing evidence:

- equality;
- isomorphism;
- equivalence;
- normality;
- quotient identification;
- singularity classification;
- smoothness;
- dimension;
- ampleness;
- K3, Enriques, or del Pezzo classification.

Each has a different proof burden.

### 8.2 Invariants are inputs, not automatic certificates

Matching dimension, Hessian rank, Milnor number, Tjurina number, Hilbert series, or intersection form does not by itself prove an isomorphism or classification. A completeness theorem may convert a finite certificate into the conclusion, but then the theorem and its hypotheses are part of the proof.

The quotient-surface computation illustrates the correct architecture. Equations, dimension, degree, singular points, and local invariants were not enough by themselves to justify every stated conclusion. The notebook needed the finite quotient factorization, normality argument, local invariant-ring theorem, adjunction, Gorenstein property, and ampleness.

### 8.3 Predicates must not erase proofs

Methods such as `is_del_Pezzo()`, `is_K3()`, `is_Enriques()`, and `ADE_type()` are acceptable only as theorem applications with inspectable certificates. They should expose or retain:

- the definition or characterization used;
- the hypotheses checked;
- the intermediate objects and invariants;
- the theorem that makes the certificate complete;
- the scope in which the predicate is implemented.

A Boolean is not a substitute for the mathematical argument. In a research notebook, it is usually a summary of a proof object or certificate that should remain inspectable.

### 8.4 Counterexamples are a normal part of reasoning

The assistant did best when it tested the user's proposed equivalence and produced an `A_3` counterexample. That is standard research behavior. Agreement is not the objective; determining the correct theorem is.

The desired reflex is:

1. separate implications;
2. test the converse;
3. search for boundary examples;
4. identify missing hypotheses;
5. state the corrected theorem.

## 9. Modality VII: generalize along mathematics

### 9.1 The natural domain is determined by the construction

The public abstraction should usually be the standard mathematical construction, not the first family of Sage objects on which an algorithm works.

Examples:

- products of schemes, not `ProductOfProjectiveSpaces` as the public ontology;
- equalizers of morphisms, not a projective-minor equalizer helper;
- cyclic covers from root data, not a double-cover factory for one equation;
- affine covers by open immersions, not point-specific affine-expression helpers;
- isotypic decomposition, not `+/-` monomial filters;
- relative `Spec`, not an independent “generic section” object.

### 9.2 Method placement is not semantic completion

The transcript shows an important intermediate failure. The assistant removed a freestanding utility class and installed methods on Sage objects, then treated that as a Sage-native semantic design. The resulting surface still exposed:

- `factor_dimensions()`;
- `factor_blocks()`;
- `scheme_theoretic_image()` beside `image()`;
- `inverse_morphism()` beside categorical `inverse()`;
- `pullback_subscheme(Z)` without the second named morphism.

The user immediately recognized these as backend bookkeeping, redundant terminology, or incomplete diagram data. The general lesson is:

> A method becomes semantic because it is the standard mathematical operation owned by that object or diagram, not because it is syntactically attached to a Sage class.

### 9.3 Generality is not a regression suite

Passing tests on `(P^1)^2` and `(P^1)^3` does not establish a general scheme construction. Examples verify implemented branches. The mathematical domain is determined by the definition; executable coverage is separately stated.

A correct design may expose the general operation and dispatch to gated special cases. It may also keep a one-off coordinate computation private. What it should not do is publish a special-case wrapper as though modest reuse had made it foundational.

### 9.4 Research foresight is mathematical leverage

Before adding a public abstraction, ask whether nearby research will use the same standard construction. A correct general primitive can support blowups, K3 surfaces, Enriques surfaces, toric varieties, and projective products through different backends. A class named after the first backend offers no such leverage.

This does not require implementing all schemes immediately. It requires choosing a public mathematical boundary that does not obstruct later cases.

## 10. Modality VIII: coordinate computation as transport

Coordinates are necessary and valuable. The error is not using them; it is failing to show how the computation enters and leaves coordinates.

A research-quality coordinate computation should visibly contain:

1. the intrinsic source object;
2. the chosen presentation or chart;
3. the comparison morphism or isomorphism;
4. the coordinate computation;
5. the invariant result;
6. any transport back to the original object;
7. the choices on which the coordinate output depends.

This pattern applies to polynomial sections, local equations, matrices of maps, affine-chart points, quotient rings, and projective embeddings.

When this transport is explicit, coordinate code becomes evidence. When it is implicit, the code silently changes the mathematical claim.

## 11. Modality IX: Sage code as a mathematical ledger

### 11.1 Code should display the dependency graph of the argument

The notebook is not merely an executable program. It is a research record. Its visible structure should read as:

- define the objects;
- define the maps;
- state the theorem or universal property;
- choose the presentation;
- compute;
- verify the proof obligation;
- state the conclusion and remaining gap.

Procedural headings such as “next compute the matrix” are not a substitute for explaining why that matrix represents the needed map.

### 11.2 Name mathematical components

The user's tuple-unpacking correction is a pure Sage style rule grounded in the same mathematical modality. Given

```sage
tau_coordinates = tau.defining_polynomials()
first_factor_image = tuple(tau_coordinates[0:2])
second_factor_image = tuple(tau_coordinates[2:4])
```

anonymous slices conceal the decomposition of the morphism into named homogeneous coordinate functions. In a research notebook, write

```sage
f0, f1, g0, g1 = tau.defining_polynomials()
```

and use `f0,f1,g0,g1` in the matrices and explanations. The point is not a generic style preference for longer variable names. The named variables are the components of the morphism being studied.

Likewise:

- name projections and structure morphisms;
- name the comparison isomorphism;
- name the chosen chart and open immersion;
- name the line bundle and its section space;
- name the theorem certificate;
- avoid positional indexes when the positions have mathematical meanings.

### 11.3 Preserve information; improve organization

When a basis or defining map is printed, the user may need the full data. The appropriate response to unreadable output is structured TeX, not suppression. Objects own their displays; morphisms use the displays of their domain and codomain and add the arrow and defining map.

This is another instance of compositional mathematical design: dependent displays should be assembled from the objects, not from a parallel naming system.

### 11.4 Separate argument from regression infrastructure

Assertions that a basis length equals a dimension, constructors round-trip, or internal coordinate blocks have expected sizes belong in framework regressions unless they are genuine mathematical obligations of the current proof. The visible research narrative should contain the assertions that justify the argument.


### 11.5 Concrete Sage discipline is a consequence, not a competing layer

The report that proposed a “mathematician-friendly interface” contains both useful evidence and mathematically immature remedies. Its valid observation is that the notebook repeatedly fell from schemes, morphisms, line bundles, representations, and local rings to raw tuples and polynomial calculations. Its first proposed repair—create a freestanding class or method for each observed computation—was still engineering-first.

The corrected Sage rules follow from the modalities above.

1. **Parents before elements.** Construct or reuse the actual parent: `Pic(X)`, `X.Hom(Y)`, `X(R)`, a section space, a local ring, a linear system, or a representation. Do not invent an element class without its ambient structure.
2. **Functorial maps before element operations.** A section pullback is an application of the induced map on section spaces; an isotypic decomposition belongs to the induced representation; an evaluation matrix represents a restriction or evaluation morphism.
3. **Native operations before aliases.** `image()`, `inverse()`, `X(R)`, product components, domains, codomains, and ordinary composition should be used before adding qualified aliases such as `scheme_theoretic_image()`, `inverse_morphism()`, `points_over()`, or `factor_dimensions()`. Existing Sage globals and constructor aliases should not be shadowed for cosmetic syntax.
4. **Primary outputs before backend artifacts.** Return the morphism, pullback diagram, closed subscheme, local ring, linear-system object, or cyclic-cover morphism. Equations, matrices, tuples, and chart dictionaries are presentations of those outputs.
5. **Private backend plumbing.** Coordinate blocks, saturation, flattened coefficient rings, dispatch tests, and positional slices belong behind the interface. Duplicate coordinate rings should not be created merely to rename variables or restate an action already carried by a stored morphism.
6. **Named research data.** When a tuple contains mathematically meaningful components, unpack and name them. `f0,f1,g0,g1 = tau.defining_polynomials()` is better research code than anonymous slices because it exposes the component morphisms used next.
7. **Accurate partial parents.** A tested linear subgroup is not automatically `Aut(X)`; a hyperplane-class subgroup is not `Pic(X)`; a restricted singularity recognizer is not a total `ADE_type()` implementation.
8. **Explicit relative bases.** Base change takes a morphism, affine covers consist of open immersions, and global schemes or families require gluing and descent rather than side metadata or chart collections.
9. **Research assertions versus framework tests.** The notebook narrative keeps proof obligations; API round trips and backend invariants move to regressions.
10. **Full mathematical display.** Organize bases and maps in TeX without suppressing the information being inspected.

These are genuinely Sage-specific requirements. They do not replace object-first and morphism-first reasoning; they are what that reasoning looks like in Sage code.

## 12. Modality X: standard-reference recognition

A mature researcher assumes that common constructions—relative `Spec`, projectivization, evaluation, pullback, quotient, linearization, isotypic decomposition, cyclic cover, local ring, completion—have standard formulations. Before coining a noun or building a bespoke helper, the assistant should consult:

- standard texts or references such as the Stacks Project;
- Sage's category, parent/element, and morphism architecture;
- existing methods and source;
- established external systems or reference implementations when Sage lacks the backend.

The transcript's “universal section” sequence lasted several rounds because the assistant kept refining an invented abstraction rather than recognizing the relative-spectrum construction over a point and the evaluation counit. Reference consultation is not an optional afterthought here. It is part of mathematical recognition.

## 13. Modality XI: epistemic research discipline

### 13.1 Do not use the expected answer as an oracle

The initial fixed-point cell guessed the four points, asserted that they satisfy the equations, and reported a computation. A researcher distinguishes:

- proposing candidates;
- verifying candidates;
- proving completeness;
- computing a scheme;
- enumerating rational points;
- deducing a result from a theorem.

The notebook and report must say which occurred.

### 13.2 Preserve the gap

When a full locus, classification, quotient, or family has not been constructed, state what remains. A correct dimension obtained indirectly is useful, but it should not be narrated as an explicit computation of the locus.

### 13.3 Artifact state is part of evidence

Wrong kernels, duplicate cells, stale prose, unpersisted edits, and live-kernel-only definitions undermine the mathematical record. Reopening and cleanly executing the persisted notebook is the computational analogue of checking that a proof actually contains every cited lemma.

This is procedural in implementation, but its governing modality is ordinary evidentiary discipline: claim only what the durable argument supports.

## 14. Correction trajectories and the modalities they reveal

### 14.1 Fixed loci

Trajectory:

1. guessed coordinate points;
2. chartwise ideals;
3. determinant equations;
4. generic projective-product helper;
5. diagonal and graph methods;
6. pullback diagram and equalizer.

Underlying modalities:

- computation must derive the result rather than verify an oracle;
- points and fixed subschemes are different objects;
- equations should arise from the diagonal;
- the equalizer is the governing construction;
- a method on a morphism is not enough if the complete diagram is absent.

### 14.2 Section parameters

Trajectory:

1. polynomial ring in unknown coefficients;
2. “general element”;
3. “universal section” object;
4. affine section space;
5. recognition of relative `Spec` over a point and the evaluation counit.

Underlying modalities:

- recognize standard constructions before inventing nouns;
- distinguish affine parameters, projective linear systems, and total spaces;
- use adjunctions and functorial maps;
- coordinates are expressions of canonical maps after a basis choice.

### 14.3 Cox rings and sections

Trajectory:

1. sections represented directly as polynomials;
2. `polynomial()` conversion;
3. fixed-degree isomorphism;
4. one global graded-algebra isomorphism and its restrictions;
5. recognition that the Cox ring itself is the abstract algebra of sections, not the polynomial algebra.

Underlying modalities:

- isomorphism is not equality;
- comparison maps are first-class;
- fixed-degree maps derive from the graded map;
- structure such as grading must be preserved.

### 14.4 Sage-native interface

Trajectory:

1. freestanding utility class;
2. methods monkey-patched onto Sage objects;
3. removal of redundant aliases and backend bookkeeping;
4. ambient-category operations and compositional recovery.

Underlying modalities:

- object-oriented placement is not mathematical ownership;
- backend data are not public objects;
- standard categorical names need no engineering qualifiers;
- composition should recover derived data.

### 14.5 Universal covers and families

Trajectory:

1. local equations reported as a cover;
2. cyclic-cover datum;
3. global projective-bundle realization;
4. projective parameter family claimed;
5. discovery of the missing square root of the parameter `O(1)`;
6. affine parameter family with covered-scheme gluing.

Underlying modalities:

- input data, local realization, global object, and family are different levels;
- fiberwise constructions require descent;
- projectivization can discard data required by the construction;
- global claims require gluing and compatibility.

### 14.6 Toric rerouting

Trajectory:

1. mixed product failed in current Sage classes;
2. toric realization called the mathematically correct ambient;
3. user supplied non-toric scope witnesses;
4. assistant announced a categorical dispatch design;
5. user required native defect repair or a faithful shadow.

Underlying modalities:

- the mathematical construction determines the interface;
- a convenient presentation is one backend;
- examples witness the intended domain;
- abstract terminology is not a design;
- software defects should be repaired at the semantic layer when feasible.

## 15. Positive regression anchors

The transcript also contains examples of the desired mode of thought.

### 15.1 Refuting an overstrong equivalence

When asked to prove that passing through exactly one fixed point was equivalent to having exactly one `A_1` singularity, the assistant tested the converse, produced an `A_3` counterexample, and stated the corrected criterion with a Hessian and global-singularity condition. This is theorem-seeking rather than compliance.

### 15.2 Distinguishing direct and indirect dimension arguments

The assistant eventually separated the explicitly constructed smooth open locus from the larger ADE locus and derived the dimension by inclusions. This preserved the uncomputed discriminant as an explicit gap.

### 15.3 Detecting a descent obstruction

Before changing the universal-family section, the assistant noticed that the universal branch line bundle over the projective parameter space had an `O(1)` parameter factor without a canonical square root. It stopped rather than forcing a false family. This is the appropriate local-to-global reflex.

These examples should remain visible in contributor review so that guidance does not turn the assistant into a passive follower of user suggestions.

## 16. The compact internal research checklist

Before proposing or modifying Sage code for algebraic geometry, the assistant should internally ask:

1. **Object:** What is the standard mathematical object? Is the current datum the object, a class, a representative, or a presentation?
2. **Place:** In which category, parent, Hom-set, or fiber does it live? What is its base?
3. **Maps:** What named morphisms, functors, or natural transformations produce the operation?
4. **Construction:** Is this a standard limit, colimit, relative spectrum, projectivization, quotient, image, restriction, or descent construction?
5. **Relation:** Are two objects equal, isomorphic, equivalent, or merely related after forgetting structure? Where is the comparison map?
6. **Levels:** Am I confusing local with global, affine with projective, absolute with relative, family with fiber, or object with invariant?
7. **Proof:** What theorem proves the exact claim, and have its hypotheses been established?
8. **Generality:** What is the natural mathematical domain? Is the current implementation a backend branch or a private one-off?
9. **Presentation:** Which choices enter the computation, and how is the result transported back to the intrinsic object?
10. **Ledger:** Would a mathematician reading the notebook see the objects, maps, theorem, computation, and conclusion without reconstructing them from tuple indexes or helper state?
11. **Evidence:** Was the claimed result computed, theorem-deduced, merely checked on candidates, or not yet completed?

If these questions are answered first, most of the observed errors do not arise.

## 17. Consequences for guidance design

The assistant-facing guide should emphasize the modalities above, then use a limited number of Sage-specific examples to make them operational. It should not become a ban list containing every observed method name.

Contributor review should distinguish:

- **modality:** the generative mathematical habit;
- **operational consequence:** what the assistant must do in Sage or prose;
- **regression example:** a source incident showing the rule is strong enough.

For example:

- modality: think in named morphisms and functors;
- consequence: base change requires `T -> S`, and section pullback derives from the parent-level map;
- regression examples: `base_extend(field)` and `f.pullback_section(s)`.

Or:

- modality: recognize standard universal constructions;
- consequence: construct the equalizer through the diagonal and pullback;
- regression example: hand-written determinant equations for the fixed locus.

This organization teaches mathematical judgment and still permits precise testing against the transcript.
