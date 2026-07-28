### 34.4 Construct parent-level functorial maps before element-level sugar

When a morphism induces operations on associated structures, construct the parent-level map first. For `f:X -> Y`, the relevant primitives may include

\[
f^*:\operatorname{Pic}(Y)\to\operatorname{Pic}(X)
\]

and, for an invertible sheaf `L` on `Y`,

\[
f^*:H^0(Y,L)\to H^0(X,f^*L).
\]

Element syntax such as pulling back a section must apply these stored maps. Do not manually re-specify the action by polynomial substitution in a duplicate coordinate ring.

Likewise:

- a group action on `X` plus a linearization of `L` induces a representation on `H^i(X,L)`;
- invariants, eigenspaces, and isotypic components belong to that representation;
- a restriction matrix is the matrix of a restriction map after choices of bases and trivializations;
- a coordinate realization of sections is a named isomorphism or morphism, not an intrinsic `.polynomial()` operation.

### 34.5 Return the mathematically primary object

Sage operations should return the object that carries the construction, not merely the coordinate artifact used by one backend.

Prefer:

- a morphism or a universal diagram, not only its source, target, or equations;
- a pullback object with its apex, projections, cospan, commutativity, and universal map, not only the fiber-product scheme;
- a graph morphism whose codomain is the graph, not an unrelated equation list;
- a closed singular subscheme, not a list of chartwise solutions;
- a linear-system object and its associated rational or regular morphism, not only an evaluation matrix;
- a cyclic-cover datum or covering morphism with branch, ramification, deck action, and root data, not only an equation `z^n=f`;
- an affine cover consisting of actual open immersions, not chart indexes and coordinate tuples;
- a local ring or germ together with its presentation, not a free-standing local polynomial;
- an actual cohomology object with graded pieces, not only a tuple of dimensions;
- an induced representation and its isotypic decomposition, not only filtered basis lists;
- a classification certificate, not only an ADE label or Boolean predicate.

Coordinate equations, matrices, numerical invariants, and labels remain inspectable consequences or backend realizations of these objects.

### 34.6 Keep coordinate and backend plumbing private, but name mathematical components in research code

Private implementation code may slice coordinate arrays, flatten coefficient rings, compute multigraded blocks, saturate ideals, or dispatch on Sage classes. The visible notebook should not expose those mechanics as the mathematical argument.

When output from Sage has mathematically meaningful components, unpack and name them. For example, prefer

```sage
f0, f1, g0, g1 = tau.defining_polynomials()
```

to anonymous slices such as `tau_coordinates[0:2]`. Use the names in subsequent matrices, maps, and explanations.

The same rule applies to:

- projections of a product;
- source and target coordinate blocks;
- basis vectors and their images;
- chart embeddings and point lifts;
- generators of ideals or graded pieces;
- branch sections, root line bundles, and deck transformations.

Raw positional indexing is acceptable in folded backend code when the positions have no independent mathematical meaning. It is not acceptable as the visible language of the research argument.

### 34.7 Make bases and relative structures explicit

Base change is along a named morphism `T -> S`, not merely a target ring or field accepted through implicit coercion. Products and fiber products must retain their structure maps and base.

For relative affine schemes, vector bundles, parameter spaces, and families:

- construct the relative scheme over its actual base;
- retain the structure morphism natively rather than in side metadata;
- use actual affine-cover morphisms and overlap maps;
- verify compatibility and cocycles before claiming a global object;
- distinguish the affine space of sections from the projective linear system;
- do not projectivize away root, scaling, or linearization data required by a later construction.

If Sage's native constructor loses the correct relative base or cannot form the required morphism, repair it or provide a mathematically faithful shadow rather than compensating throughout downstream code.

### 34.8 Separate research narrative from framework regressions

The visible notebook should contain assertions that are mathematical obligations of the argument: hypotheses, commutative diagrams, universal-property equations, invariant conclusions, and theorem certificates.

Move implementation checks such as constructor round trips, basis-length identities, coordinate-block sizes, alias equivalence, and backend branch tests into a folded framework or regression notebook.

Do not make research cells monolithic. Expose intermediate semantic objects in the order a mathematician would inspect them: parent, element, morphism, induced map, coordinate realization, computation, and conclusion.

### 34.9 Preserve full mathematical information in Sage display

Improve unreadable Sage output by structuring it in TeX, not by suppressing the data that motivated the display. Objects own their own notation. Morphisms should use the ordinary displays of their domain and codomain and add their arrow and defining map.

When the full basis, generator images, coordinate substitutions, or ring map are mathematically relevant, display them in aligned or array form. Do not replace them by a compact label that hides the proof data.

