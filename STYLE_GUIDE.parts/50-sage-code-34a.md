## 34. Sage-specific semantic code discipline

The mathematical modes of thought above must produce concrete Sage coding habits. Do not stop at correct prose while leaving the notebook structured around raw rings, anonymous tuples, coordinate factories, or backend-specific helpers.

### 34.1 Use Sage parents, elements, categories, and morphisms as mathematical structure

Construct or reuse the actual Sage parent before manipulating its elements. Prefer objects such as:

- `X`, `X(R)`, and `X.Hom(Y)` for schemes, points, and morphisms;
- `Pic(X)`, divisor groups, local rings, section spaces, linear systems, and representations when these are genuinely implemented;
- actual morphisms, embeddings, open immersions, projections, quotient maps, and pullback diagrams rather than detached coordinate data.

Elements must retain their parents. Do not copy a section into a raw polynomial ring, a point into a tuple, a morphism into a list of coordinate functions, or a divisor class into an untyped integer tuple and then continue the geometric argument on the copy. Do not construct a duplicate polynomial or coordinate ring solely to rename variables when the existing parent and a named realization or change-of-coordinates morphism already suffice.

A Sage `Parent` or category declaration does not certify the mathematics. Do not call a facade subset the full `Aut(X)`, a known embedded subgroup the full `Pic(X)`, or a restricted recognizer a total classification parent. Name the implemented object accurately and gate partial coverage.

### 34.2 Audit native Sage ownership before adding public methods

Before adding a public method, inspect the existing parent, category, element class, source, documentation, and composition patterns. Use native mathematical operations when they already express the construction.

In particular:

- use `X(R)` rather than inventing `X.points_over(R)`;
- use the existing factors or components of a product and compose their methods rather than exposing `factor_dimensions()`;
- keep coordinate blocks, saturation helpers, flattened rings, and dispatch predicates private;
- do not shadow established Sage globals or aliases merely to obtain prettier constructor syntax;
- when behavior is uniform for a mathematical category, prefer category mixins and justified category refinement; when a native class defect or constructor gap genuinely requires a targeted patch or shadow, preserve native behavior outside the exact supported branch and avoid installing a partial method whose name claims broader semantics;
- use `image()` when a scheme-morphism class has scheme-theoretic image as its documented image convention, rather than adding a redundant `scheme_theoretic_image()` alias;
- use `inverse()` or Sage's established inversion protocol rather than `inverse_morphism()`;
- recover a graph subscheme as the codomain of `f.graph_morphism()` rather than adding a second `f.graph()` noun;
- recover derived data through `domain()`, `codomain()`, projections, restrictions, images, and composition when those operations already provide it.

Method placement is justified only by mathematical ownership. Moving a helper onto a Sage class is not enough, and a compositional convenience should not become a new public primitive merely because it is discoverable there.

### 34.3 Generate categories compositionally before inventing new ones

Before defining a new category, named subcategory, wrapper parent, or parallel method hierarchy, determine whether Sage's existing category calculus already constructs the desired mathematical domain.

Audit at least:

- the existing base category and its super-categories;
- registered axioms and compositional refinements such as `C.Axiom1().Axiom2()`;
- joins or intersections of existing categories;
- slice, coslice, arrow, action, graded, filtered, equivariant, and other standard categorical constructions;
- functors whose essential image or structured objects already supply the proposed domain;
- existing named aliases that resolve to one of these generated categories.

A familiar compound mathematical name is not evidence that a new primitive category is required. If the proposed objects differ from an existing category only by properties, construct the corresponding axiomatic refinement. If they differ by additional structure or specified morphisms, use the standard structured-object or diagram category when available. A new primitive category is justified only when the required mathematical data, morphisms, or universal construction cannot be generated faithfully from existing Sage categories.

Before naming the object or category, perform a reference-backed mathematical classification. Search the local research corpus first: supplied textbooks, papers, project notes, extracted references, and prior mathematical decisions. Then consult appropriate standard sources such as the Stacks Project, Kerodon, official Sage and Mathlib documentation and source, established textbooks, arXiv or journal papers, and broad reference works such as nLab or Wikipedia for orientation. The purpose is not to collect decorative citations. Extract the established definition, ambient category, objects, morphisms, variance, universal property, hypotheses, and standard functorial constructions that constrain the implementation.

Do not coin a noun from the current wrapper, API, or informal research phrase and then search for justification afterward. If the first source search reveals that the proposed object is already an arrow, diagram, slice object, algebra object, action, refinement, localization, completion, or another standard construction, discard the bespoke noun and implement the standard construction. If terminology varies across sources, state the precise definitions and relations rather than silently selecting the wording closest to the current code.

Reference search is part of abstraction completion. A proposed category or public method is not mathematically classified merely because it has a plausible name or forms a valid Python/Sage category. The classification is complete only when its relation to standard mathematics and Sage's existing architecture has been established or the absence of a faithful existing construction has been demonstrated.

Recognize when the category construction itself is functorial in an ambient category. Slice, coslice, arrow, comma, functor, action, graded, filtered, equivariant, and similar constructions should ordinarily be obtained by applying the corresponding construction to the existing category, not by introducing an unrelated top-level category family for every base object or example. The public API should preserve this ownership and variance: refine or otherwise construct the ambient category, then apply its category constructor. A top-level helper may implement the mechanism privately, but it must not become the semantic owner.

Do not stop one abstraction rung too early. Identifying that objects form a slice, coslice, arrow, or other diagram category is incomplete if the implementation then reifies that category as an independent bespoke class instead of first inspecting and using Sage's native functorial-construction mechanism when available. Determine whether the desired category is already generated by the ambient category's construction methods and whether it composes correctly with its axiomatic refinements, joins, and super-categories.

When the mathematical object is already an arrow, span, cospan, cone, action, functor, or other diagram, keep that diagram as the semantic object. A wrapper parent may provide Sage element behavior or backend storage, but it is a realization of the diagram object, not a replacement definition. Its domain, codomain, structure maps, and commuting conditions must remain first-class and recoverable.

A named category may be useful as a standard alias, but it should resolve to the generated category rather than establish an independent ontology, duplicate method implementations, or introduce a second refinement path.

When a capability is uniform for every Sage parent satisfying the resulting mathematical structure, let that category own the methods. Prefer Sage's dynamic category mixins to attaching the same methods directly to concrete implementation classes.

Distinguish two mechanisms that are mathematically and operationally different:

- `C._with_axiom(A)` acts on a category and forms or retrieves the subcategory of objects of `C` satisfying the registered axiom `A`;
- `P._refine_category_(D)` acts on an existing Sage parent `P`, joins `D` with `P.category()`, and makes the joined category's `ParentMethods` and `ElementMethods` available through Sage's dynamic method resolution.

Object-level refinement is not a cast and does not prove membership. Use it only when `P` already satisfies the defining mathematics of `D`, and make the justification or certificate inspectable. Refining an object merely to acquire convenient methods creates a false categorical assertion.

Apply the following discipline:

1. **Use the smallest valid existing category.** If the object is already an `R`-module, refine it into Sage's existing `Modules(R)` rather than inventing a parallel category. Define a new category only when the mathematical structure and its uniform method surface are genuinely absent.
2. **Let the category own the implementations.** Uniform parent methods belong in `ParentMethods`; uniform methods on elements of those parents belong in `ElementMethods`; operations on refined subcategories belong in `SubcategoryMethods` when that is the appropriate Sage ownership. Installation code should route objects into the category, not contain the mathematical implementation itself.
3. **Refine at a construction boundary.** For known singleton parents, a documented post-initialization pass may refine them in bulk. For dynamically created parents, call the native constructor first and refine its result in a constructor interceptor or immediately before returning it. Do not reimplement the native arithmetic merely to obtain the desired category membership.
4. **Preserve all existing category information.** `_refine_category_` joins with the current category. Check that the join is mathematically consistent, that method resolution has no accidental conflicts, and that repeated installation is idempotent under notebook re-execution and module reload.
5. **Treat global refinement as a visible side effect.** Refining cached singletons such as standard base rings changes their available methods for the process. Isolate the installation layer, document its scope, and test from a clean Sage kernel.
6. **Use `@final` only for a mathematical contract.** Prevent downstream override only when the operation must be uniquely inherited for semantic correctness, not merely to win a method-resolution conflict.
7. **Do not refine individual elements as a substitute for a parent.** Normally the parent receives the refined category and its elements receive `ElementMethods` through that parent. Preserve Sage's parent/element model.

Choose the implementation mechanism by mathematical ownership. Use a category hierarchy for uniform structure, justified category refinement for an existing parent already satisfying that structure, and a targeted native repair, subclass, shadow, or backend patch for implementation-specific behavior. A method belongs to a category exactly when every object of that category possesses it with the stated semantics and hypotheses.
