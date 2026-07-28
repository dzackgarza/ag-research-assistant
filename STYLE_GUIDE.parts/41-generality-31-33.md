## 31. Mathematical names and category-first public interfaces

Name public objects and operations by standard mathematics, not by the backend representation that first made them computable.

A product of projective spaces is a product in the category of schemes. `ProductOfProjectiveSpaces` may be the name of a private Sage class or dispatch branch, but it is not the governing mathematical construction and must not define the public mathematical object.

Likewise, avoid public foundational nouns such as “coordinate manager,” “factor block object,” “projective-product equalizer,” or “section polynomial” when the mathematics already supplies products, projections, equalizers, graded components, restriction maps, affine covers, and realization morphisms.

For every proposed public noun, ask:

1. What standard mathematical object is it?
2. In which category does it live?
3. What parent contains its elements?
4. What are its structure morphisms?
5. Is it merely a special presentation or a predicate selecting a supported backend?
6. Is it recovered compositionally from an existing object or morphism?

Presentation-specific class names and helpers belong in private backend code. The research notebook and public interface should speak in schemes, morphisms, sheaves, line bundles, graded algebras, actions, functors, diagrams, and the standard constructions applied to them.

## 32. Write Sage code as a mathematical research ledger

Research code should make the mathematical dependency graph legible. It is not ordinary application code whose primary concerns are encapsulation, service boundaries, or generic software patterns.

A research notebook should visibly record:

- definitions of the mathematical objects;
- their parents and ambient categories;
- named morphisms and diagrams;
- hypotheses and assertion gates;
- theorem applications;
- explicit transports through isomorphisms or realizations;
- coordinate specializations and the choices they use;
- computed outputs;
- proof obligations and verification certificates;
- unresolved mathematical or implementation boundaries.

Prefer code whose structure reads as the mathematical argument. Avoid hiding essential maps inside constructors, coercions, wrappers, managers, factories, registries, or helper state. Backend complexity may be folded, but the visible interface must preserve the mathematical objects and maps through which the argument proceeds.

Readable mathematical code may be more explicit than conventional software. Naming `Phi`, `Phi.inverse()`, the domain, codomain, grading, pullback square, structure morphism, and restricted component is not boilerplate when those data constitute the proof.

Name mathematical components instead of hiding them behind positional indexing. If `tau.defining_polynomials()` returns `(f0,f1,g0,g1)`, unpack and use those names rather than passing around `coordinates[0:2]` and `coordinates[2:4]`. Tuple slicing, anonymous blocks, and raw integer indexes belong in private backend code unless the positions themselves have no mathematical meaning.

## 33. Generalize to the standard mathematical domain

Do not write a public wrapper that recovers only the one coordinate calculation needed by the current notebook when the computation is plainly a special case of a standard construction.

Before implementing a helper, determine the natural mathematical domain of the operation and the nearby research cases that share it. Examples include:

- products and fiber products of schemes, not only products of projective spaces;
- graded-algebra morphisms and their homogeneous restrictions, not only Cox-to-polynomial conversion in one degree;
- restriction and pullback maps on section spaces, not one evaluation matrix;
- affine covers and open immersions, not one chart-coordinate extraction;
- cyclic covers from root data, not one double-cover equation;
- local rings and germ presentations, not one ADE test on one affine chart.

Choose among three outcomes deliberately:

1. implement the standard construction at its natural level when the required primitives make this reasonably short;
2. define the general mathematical interface and dispatch to explicitly gated special backends;
3. keep a one-off computation private and label it as such when no public reusable abstraction is justified.

A one-case public wrapper is not research foresight. It creates technical vocabulary without mathematical leverage and forces nearby work to repeat the same reconstruction.

Before coining a new abstraction, consult standard references and Sage's existing mathematical architecture. Determine whether the operation is already a universal construction, functor, adjunction, restriction, base change, image, equalizer, quotient, graded component, relative spectrum, or descent problem. Generalize to the mathematically natural boundary, not merely one layer beyond the current complaint.

