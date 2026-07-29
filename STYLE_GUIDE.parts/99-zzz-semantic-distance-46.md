
## 46. Minimize semantic distance between mathematical claims and Sage code

Visible research code should read as executable mathematical prose. A mathematician who understands the source claim but knows little Sage or Python should be able to identify the objects, maps, hypotheses, intermediate constructions, and conclusions line by line, assuming the advertised methods are correctly implemented.

The semantic distance of a computation is the amount of reconstruction needed to recover the mathematics from the visible code. Keep this distance small. Do not translate a paper's schemes, divisors, linear systems, covers, lifts, quotients, local rings, or singularity strata into generic software nouns, detached arrays, utility pipelines, or backend operations when the standard mathematical objects can remain visible.

### 46.1 Preserve the mathematical nouns, verbs, and ownership

Use the same mathematical vocabulary in the code that appears in the theorem or paper. Prefer interfaces whose visible operations say, in substance:

- form a product, quotient, pullback, fixed locus, or singular locus;
- construct a line bundle, section space, or linear system;
- take a generic member or specialize a family;
- form a cyclic cover from its base and covering data;
- lift an automorphism through a covering morphism;
- compute a canonical divisor, ramification divisor, local ring, or germ;
- ask for ampleness, Cartier or \(\mathbf Q\)-Cartier structure, degree, intersection numbers, or singularity type.

Do not replace these by programming-language phrases that merely describe storage or control flow. A public noun such as `LinearSystems`, `CoverData`, `FactorBlocks`, or `SurfaceTools` is not preferable to the ordinary mathematical object merely because it packages several operations.

Object-oriented syntax is useful for discoverability only when the receiver is the mathematical owner. A line bundle may produce its section space or linear system; a linear system may produce its generic member; a morphism may produce its image or graph morphism; a covering morphism or the appropriate arrow category may own its lifts and deck transformations. A construction involving several named arrows may instead belong to their ambient category or diagram. Do not force every operation onto one argument merely to obtain method syntax.

### 46.2 Use mathematical sugar only when it expands to a standard construction

Concise syntax is desirable when it has a clear mathematical expansion. Products, quotients, line bundles such as \(\mathcal O(a,b)\), generated subgroups, and restrictions may admit familiar sugar. The underlying semantic objects and maps must remain recoverable: product projections, quotient morphisms, structure maps, subgroup inclusions, and comparison cells.

Do not invent specialized public classes or constructors merely to imitate notation. Before proposing sugar, identify the standard construction it abbreviates, the object that owns it, and the exact result it returns. The notation must not conceal noncanonical choices, omitted hypotheses, or loss of categorical data.

### 46.3 Name ambient parents and categories in the visible argument

Research notebooks should contain deliberate lines showing where objects live. For example, schematic code may name a line bundle, its Picard parent, the resulting linear system, and a member:

```sage
L = Y.O(4, 4)
assert L in Y.Pic()

Lambda = L.linear_system()
assert Lambda.line_bundle() == L

B_eta = Lambda.generic_member()
assert B_eta in Lambda
show(B_eta)
```

The exact Sage spelling is not prescribed by this example. The style is: construct the semantic object, name its parent, assert its location, and display the mathematical result.

Use assertions as mathematical checkpoints in the notebook narrative. Appropriate assertions include:

- membership in a parent or certified category;
- domain and codomain of a morphism;
- dimensions, degrees, ranks, and intersection numbers;
- equality or commutativity in the correct Hom-object;
- group order or isomorphism type;
- divisor classes and pullback or pushforward identities;
- ampleness, Cartier properties, smoothness, and singularity classifications when proved or certified.

These assertions must test actual computations, comparison maps, or theorem-backed certificates. Do not hard-code the desired conclusion, attach an expected label by construction, or use a weaker numerical coincidence as a proxy for the asserted theorem.

### 46.4 Hide canonical ceremony while exposing mathematical dependencies

Compose routine canonically induced stages inside semantic methods, and keep the mathematical intermediate objects visible whenever they participate in the argument. A line bundle may internally construct its complete linear system, and a group action may internally induce the action on a section space; the notebook should still name the line bundle, section space, linear system, invariant subsystem, branch divisor, covering morphism, quotient map, local ring, germ, or parameter stratum used in the proof.

Hide coercion plumbing, coordinate-block indexing, saturation helpers, ring flattening, and backend dispatch. Expose parentage, named maps, equations, and intermediate conclusions. Mathematical auditability, not minimum line count, determines the visible granularity.

### 46.5 Distinguish universal, generic, general, and specialized objects

A semantic interface must not collapse the following:

- the parameter space of a linear system;
- the universal divisor over that parameter space;
- the generic member over its function field;
- a statement about members on a dense open subset;
- a chosen specialization obtained by fixing coefficients.

Use separate operations or return objects for these levels. If a method called `general_member()` produces a symbolic equation with indeterminate coefficients, document whether it is actually returning the universal member or the generic member. Specialization should be an explicit map from the parameter space or an explicit choice of coefficients, and the specialized divisor should retain its relation to the universal family.

Likewise, a condition such as “the member has one \(A_n\) singularity at \(q\)” should ordinarily produce or describe a locally closed parameter stratum, including closed equations, open nonvanishing conditions, and a certificate or theorem identifying the local type. It is not merely a Boolean attached to an anonymous polynomial.

### 46.6 Keep morphisms and diagrams primary

Represent an involution as an actual endomorphism or automorphism in the appropriate Hom-object. Represent a fixed subscheme as the equalizer with the identity. Represent a quotient by its quotient object together with the quotient morphism. Represent a cyclic cover by its covering morphism and the line-bundle, algebra, or branch-section data that define it.

A lift of an automorphism through a cover is not merely another map with a suggestive name. It is a solution of a commutative square

\[
\begin{CD}
X @>{\widetilde\tau}>> X\\
@V{\pi}VV @VV{\pi}V\\
Y @>{\tau}>> Y,
\end{CD}
\]

and should be returned or certified as the corresponding comparison datum. The covering morphism, its automorphism object, or the ambient arrow category is a natural owner; a phrase such as `tau.lifts_to(pi)` is suspect unless its mathematical grammar and return type are explicit.

Deck transformations belong to the automorphisms of the covering object over its base, such as \(\operatorname{Aut}_Y(X)\), not to an unrelated wrapper. Standard group operations—generated subgroup, cyclic subgroup, centralizer, commutator, identity, and isomorphism—should remain visible when they express the paper's claims.

### 46.7 Prefer certified category membership to flattened labels

When construction or a theorem proves that an object is a K3 surface, Enriques surface, del Pezzo surface of a specified degree, smooth proper family, or object with ADE singularities, record the corresponding certified category refinement when the framework supports it. The resulting category should supply uniform mathematical methods.

Do not replace this by an unchecked constructor label. When recognition is partial, return a proof-valued or three-valued predicate and refine the category only after a theorem, computation, or supplied certificate establishes membership. Unknown is not false.

Local classifications belong to the relevant point, germ, completed local ring, or singular subscheme together with their ambient scheme. A string such as `"A1"` detached from that local object is not the full mathematical result.

### 46.8 Treat equations as presentations of semantic objects

Equations are essential outputs, but they should be obtained from and remain attached to the schemes, divisors, sections, covers, or local germs they present. The notebook should be able to display:

- the full generic or specialized equation of a member;
- defining equations of a subscheme or quotient presentation;
- a local equation at a named point with its residue field and chart or local-ring map;
- equations defining a parameter stratum together with its open conditions.

Do not let the argument silently switch from a semantic section to a polynomial, from a point to a tuple, or from a scheme to an ideal. Name the realization map or presentation and return to the semantic object after backend computation.

### 46.9 Use hypothetical semantic pseudocode as a design probe, not an API claim

It is useful to sketch how a paper could be verified if the correct semantic interface existed. Label such code explicitly as hypothetical or schematic. Its purpose is to expose the mathematical objects and missing primitives, not to claim that Sage already implements the displayed methods or that the exact method names are settled.

Every line of hypothetical pseudocode must still type-check mathematically:

1. identify the receiver's mathematical ownership;
2. state the input and output objects;
3. preserve domains, codomains, parents, and structure maps;
4. expose required hypotheses and choices;
5. distinguish the full semantic object from a component or presentation;
6. avoid names whose ordinary mathematical grammar is incoherent;
7. use exact examples only as regression anchors for the general style.

Before promoting the sketch into implementation, audit native Sage conventions and the project's established foundations. A mathematician-friendly appearance does not excuse an ill-typed construction.

### 46.10 Apply the mathematical-auditor test

A visible verification should allow a mathematically competent reader to answer:

- What object from the paper is being constructed on each line?
- In which parent, category, Hom-object, or family does it live?
- Which named map realizes each relation or identification?
- Which statements are computed directly, which are theorem-derived, and which remain conjectural or unsupported?
- Where are genericity, specialization, local coordinates, and presentation choices introduced?
- Which assertions establish the paper's claimed degrees, identities, classifications, divisor properties, or singularities?
- Can the reader follow the proof without understanding tuple positions, coercion rules, private helper names, or Python control flow?

If the answer is no, the code is too far from the mathematics even when it executes. Refactor the visible notebook around standard mathematical objects and maps, and confine implementation-specific machinery to the backend.
