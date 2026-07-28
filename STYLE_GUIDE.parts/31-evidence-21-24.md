## 21. Assertion and evidence taxonomy

Use assertions according to their mathematical role.

Valid uses include:

- checking a mathematical precondition;
- gating an unsupported backend representation;
- testing a universal-property equation;
- verifying a computed output against an independently justified theorem or regression example;
- checking internal invariants in backend tests.

Do not use an assertion as an oracle that supplies the answer the computation was supposed to derive. In particular, do not hard-code expected points, groups, singularity types, dimensions, equations, or isomorphism classes and then report that their successful assertion constitutes the computation.

When reporting an assertion, state whether it is:

1. a precondition gate;
2. a backend capability gate;
3. a mathematical postcondition computed from the object;
4. a theorem-backed regression check;
5. a representation-level consistency check.

Keep API self-tests and representation checks in folded infrastructure or regression notebooks. Retain in the research narrative only assertions that express mathematical obligations of the argument.

## 22. Invariant verification and explicit choices

Formulate checks at the invariant level supplied by the mathematics.

Prefer:

- equality of schemes or ideals;
- equality of sets or supports;
- equality of maps;
- commutative diagrams;
- isomorphisms of parents or objects;
- equality up to a unit or scalar;
- equality after saturation;
- equality of principal opens or loci.

Do not impose a canonical order on points, basis vectors, equations, components, or charts merely to make tuple equality pass.

Whenever a calculation uses a basis, chart, trivialization, coordinate realization, ordering, normalization, grading convention, or embedding:

1. name the choice;
2. identify the coordinate-free object it presents;
3. identify the map connecting the presentation to the object;
4. state which outputs depend on the choice;
5. make invariant conclusions insensitive to the choice.

A chosen normal form is valid only when the mathematics supplies or explicitly requests that normalization.

## 23. Local-to-global constructions and descent

Do not claim a global scheme, morphism, cover, quotient, or family from a collection of local equations alone.

For chartwise constructions, verify:

1. the affine chart objects;
2. every overlap;
3. transition isomorphisms;
4. cocycle identities on triple overlaps;
5. compatibility of local morphisms;
6. descent of line bundles, sections, actions, and root data;
7. that the resulting global object has the advertised universal or moduli property.

A fiberwise construction need not assemble into a family. Before projectivizing a parameter space or quotienting by scalars, check whether the data required by the construction descend. In cyclic-cover problems, track the root line bundle and every parameter-space twist explicitly.

Local equations, Jacobian ideals, and normal forms are presentations of local rings or germs. They must not replace the local objects they present.

## 24. Parameter schemes, families, and moduli

Before constructing a “generic,” “universal,” or parameterized object, identify the represented functor and the exact parameter scheme.

Distinguish:

- the vector space of sections;
- the affine scheme underlying that vector space;
- its generic point;
- the projective linear system;
- the total space of a vector bundle;
- an incidence or universal divisor;
- a discriminant or singularity stratum;
- a quotient parameter space;
- a moduli space or stack.

State whether scalar multiples are distinct, whether the zero section is included, what the fibers parameterize, and which extra descent or linearization data are retained.

Do not invent a new “universal element” or “generic section” abstraction when the construction is already a standard relative spectrum, generic point, evaluation morphism, incidence scheme, or base change. Conversely, do not identify two schemes merely because both arise from the same relative-spectrum formalism.

