
## 41. Require ontological coherence before naming public abstractions

A public mathematical noun is a mathematical claim. It asserts that a coherent object, morphism, diagram, property, structure, or proof datum has been identified. Do not coin a class or method family merely because several implementation details need a common handle.

Before introducing any public abstraction, state:

1. whether it is an object, morphism, diagram, subobject, property, structure, theorem, proof, certificate, algorithm, or presentation;
2. the ambient category, type, parent, or proposition in which it lives;
3. its defining data and axioms;
4. its morphisms or maps, when applicable;
5. its equality, equivalence, or proof-irrelevance convention;
6. the standard source or established construction that justifies the name;
7. its relation to the existing mathematical objects already present in the computation.

If these questions do not have precise answers, do not expose the abstraction publicly. A private record may temporarily organize backend state, but it must be named and documented as implementation data rather than presented as a new mathematical primitive.

### 41.1 Separate mathematical objects from statements about them

Keep distinct:

- the object, morphism, or diagram being constructed;
- a property it satisfies;
- a theorem or universal property characterizing it;
- a proof, certificate, or witness that the property holds;
- an algorithm that constructs a mediator or verifies a condition;
- provenance describing which backend or theorem supplied the result.

A universal property ordinarily characterizes an object, morphism, functor, or diagram through an existence-and-uniqueness statement or a natural equivalence of Hom-objects. Formal systems may package that statement as a proposition, structure, typeclass, or record containing operations such as a lift together with factorization and uniqueness proofs. Such a package is coherent only when its role as proof data is explicit. It does not thereby replace the mathematical object it certifies, and it should not become the primary public return object unless the user is explicitly working with proof objects.

Factorization language must expose what is being factored and through which morphism. Given morphisms

\[
X \xrightarrow{f} Z,
\qquad
X \xrightarrow{u} Y,
\]

a factorization of \(f\) through \(u\) is a morphism \(\bar f:Y\to Z\) with \(\bar f\circ u=f\). The input is \(f\), the comparison arrow is \(u\), and the output is \(\bar f\). Do not attach an opaque `factor()` operation to a theorem bundle whose arguments and return type do not reveal this diagram.

Place operations on their mathematical owners. Mediator construction belongs to the universal arrow or diagram, or to the ambient category's universal-construction interface. Properties and uniqueness results belong to predicates, theorems, or certificates. Derived structure belongs to the object on which it is defined. Provenance remains separate from all of these.

### 41.2 Do not let coined vocabulary become mathematical evidence

The existence of a class, parent, wrapper, or passing regression does not establish that its name denotes a coherent mathematical concept. Do not use an internally coined term as a premise in later reasoning, documentation, or architecture until it has passed the ontological audit above.

When a new noun begins to organize several downstream classes or methods:

1. stop extending it;
2. search the local corpus and standard references for the established objects and constructions involved;
3. translate every field and method back into ordinary mathematical data, maps, statements, and algorithms;
4. determine whether the proposed noun dissolves into existing objects, a standard diagram category, an axiomatic refinement, a universal construction, or a private implementation record;
5. retain a new public noun only if irreducible mathematical data and morphisms remain.

Do not preserve an incoherent public abstraction merely because later code already depends on it. Delete or replace it and migrate the valid computations to the correct owners. Compatibility with a mathematically meaningless interface is not a design obligation.

### 41.3 Reject implementation bundles that impersonate mathematical primitives

A wrapper is not made mathematical by collecting several related facts under a sophisticated name. Be suspicious when one class simultaneously stores:

- construction inputs;
- a canonical morphism;
- consequences of a theorem;
- backend-specific normalization data;
- a partial algorithm for induced maps;
- certificates or provenance.

These items may be related, but they generally have different mathematical types and owners. Decompose the bundle. Preserve only a private backend record when the implementation genuinely needs a shared cache or transport object, and keep that record out of the visible research ontology.

A useful public abstraction should support ordinary mathematical sentences without reinterpretation. A reader should be able to say what its instances are, what maps between them are, and what its methods return. Names whose apparent grammar cannot be translated into a well-typed mathematical statement are redesign signals.

### 41.4 Test the claimed mathematics, not only the plumbing

A reflexive, identity, empty, zero, or otherwise tautological case may test construction and dispatch plumbing. It does not by itself verify a universal property, classification theorem, factorization algorithm, or general interface.

For a claimed universal construction, evidence should address the actual obligations appropriate to the setting:

- admissibility of the input diagram or map;
- construction of the mediator;
- commutativity of the required diagram;
- uniqueness or the relevant contractible comparison space;
- nontrivial independent examples;
- rejection or explicit gating of inadmissible inputs;
- compatibility with composition, base change, or other required functoriality.

Label tautological cases as plumbing regressions. Do not describe them as verification of a general theorem. If only a trivial case is executable, report the general construction as unimplemented rather than allowing the test name or class name to imply otherwise.

### 41.5 Remediate ontological failure before continuing downstream work

When an abstraction is found to be incoherent:

1. freeze new code that depends on it;
2. inventory every datum, map, theorem, certificate, and algorithm it bundled;
3. identify the standard mathematical owner of each item;
4. replace the public abstraction by the actual objects, morphisms, diagrams, predicates, and proof data;
5. relocate valid coordinate routines and backend state behind those interfaces;
6. re-audit all downstream claims that used the invented noun;
7. retain previous computations only as correctly labeled backends or regressions.

Do not treat a late semantic correction as a wording cleanup. If the old noun had no coherent type, work stated in terms of it has not yet established the mathematical claims suggested by its interface.
