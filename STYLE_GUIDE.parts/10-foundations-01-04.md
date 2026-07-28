## 1. Research-mathematics modes of thought

Reason as an algebraic geometer first and use software as a realization of the mathematics.

Before proposing code, classes, methods, or backends, work through the following questions.

1. **What is the object?** Determine whether each datum is an object, element, morphism, subobject, isomorphism class, chosen representative, or coordinate presentation.
2. **Where does it live?** Name the category, parent, Hom-set, base scheme, grading, action, or other structure that types it.
3. **What maps relate the objects?** Construct the actual morphisms, functors, natural transformations, isomorphisms, and structure maps rather than relying on informal identification.
4. **What standard construction is occurring?** Look first for a product, pullback, equalizer, image, quotient, relative spectrum, projectivization, restriction, base change, descent construction, or theorem from the standard literature.
5. **What is intrinsic and what is chosen?** Separate the mathematical object from coordinates, equations, bases, charts, embeddings, trivializations, and backend representations.
6. **What exactly proves the claim?** State the theorem, universal property, inverse map, or certificate required for the conclusion at the strength asserted.
7. **What is the natural mathematical domain?** Generalize to the standard construction, not merely one software layer beyond the current example; keep presentation-specific implementations as gated backends or private one-off code.
8. **What does the computation actually establish?** Distinguish construction, execution, candidate verification, theorem-derived deduction, and unresolved work.
9. **Would the artifact be legible to a researcher?** The notebook should expose the objects, named maps, hypotheses, choices, computations, and deductions as a mathematical argument.

Do not infer mathematical ontology from the shape of existing notebook code. Coordinate manipulations, matrices, affine charts, tuple slices, and helper functions may realize or witness a construction; they are not automatically the construction itself.

When a familiar operation appears in coordinates, assume first that it is an instance of standard mathematics and consult the relevant references and Sage architecture before inventing terminology or a public abstraction.

The remaining rules are operational consequences of these modes of thought, not a blacklist to apply mechanically. When an unfamiliar case arises, reconstruct the standard mathematics rather than matching surface vocabulary from earlier examples.

Use the ordinary research-mathematics order of thought:

1. formulate the construction without reference to Sage;
2. locate it in standard mathematical language and references;
3. identify the objects, morphisms, functors, universal properties, and hypotheses that define it;
4. determine what counts as a proof or computation of the desired conclusion;
5. only then inspect how Sage represents or computes the construction.

Do not infer the mathematics by reverse-engineering a desired API. The public Sage interface should be a transcription of the mathematical formulation, not a software design subsequently decorated with mathematical names.

## 2. Ambient structures before elements

Never propose isolated element types without identifying their parent mathematical object.

Examples:

- divisor classes belong to `Cl(X)`;
- line-bundle classes belong to `Pic(X)`;
- sections belong to `H^0(X,L)`;
- endomorphisms belong to `End_Sch(X)` or the relevant endomorphism object;
- local invariants belong to a local ring, germ, or point together with its ambient scheme;
- morphisms belong to a Hom-set or Hom-object with specified domain and codomain.

Do not conflate:

- a divisor with its divisor class;
- a Cartier divisor with an invertible sheaf;
- `Pic(X)` with `Cl(X)`;
- an equation with the subscheme it defines;
- a coordinate presentation with an intrinsic object;
- an object with a chosen basis, generating set, embedding, or chart.

When the ambient parent is absent from Sage, the missing abstraction is usually the parent and its mathematical structure, not a disconnected class for one convenient element representation.

Do not let an isomorphism class impersonate a chosen representative. An element of `Pic(X)` is a line-bundle class; operations requiring stalks, restrictions, local trivializations, total spaces, linearizations, or cyclic-cover multiplication require an actual invertible sheaf or a canonically tracked representative. Likewise, do not name a known subgroup, recognized subset, presentation, or certificate as the full mathematical object: an embedded hyperplane-class subgroup is not automatically `Pic(X)`, and a tested family of linear automorphisms is not automatically `Aut(X)`.

## 3. Mathematical ownership before object-oriented syntax

Place operations according to mathematical ownership, not merely according to which argument makes a convenient method receiver.

Determine whether a construction belongs to:

- an ambient category;
- an object;
- a morphism;
- a point or local ring;
- a group action or linearization;
- a line bundle or linear system;
- a diagram involving several named morphisms.

Changing `Construction(x)` into `x.construction()` is not a semantic correction by itself. Neither is wrapping the result in a Sage `Parent`, assigning it a category, or moving backend code onto a native class. The proposed operation must still be the standard mathematical construction owned by that object or diagram, with complete input data, correct hypotheses, a justified parent, and a mathematically meaningful return object.

Convenience methods may delegate to a more primitive construction, but do not duplicate compositional operations merely to create additional nouns. Prefer the primitive map or object already supplied by the mathematics and recover derived data through ordinary composition, domain, codomain, image, pullback, or other standard operations.

## 4. Primitive data versus derived constructions

Do not promote derived data to independent primitives.

Examples:

- a linearization of a line bundle induces representations on its cohomology;
- a morphism determines its graph morphism;
- an endomorphism determines a fixed subscheme as an equalizer with the identity;
- a covering morphism determines branch and ramification data under the appropriate hypotheses;
- a globally generated linear system determines a morphism to projective space;
- evaluation matrices are coordinate realizations of evaluation maps, not primary geometric objects;
- local normal forms and ADE labels are outputs of local singularity analysis, not arbitrary attributes available on every point.

When a construction is functorially induced, encode and explain the inducing data and the functorial passage. Do not attach the derived result directly to a lower-level object in a way that suppresses the dependency.

