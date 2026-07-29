
## 41. Require ontological coherence before naming public abstractions

A public mathematical noun is a mathematical claim. It asserts that a coherent object, morphism, diagram, property, structure, proof datum, or algorithm has been identified. Do not coin a class or method family merely because several implementation details need a common handle.

Before introducing a public abstraction, state:

1. its mathematical kind: object, morphism, diagram, subobject, property, structure, theorem, proof, certificate, algorithm, or presentation;
2. the ambient category, type, parent, or proposition in which it lives;
3. its defining data and axioms;
4. its morphisms or maps, when applicable;
5. its equality, equivalence, or proof-irrelevance convention;
6. the standard source or established construction that justifies the name;
7. its relation to the mathematical objects already present.

If these data are unresolved, keep the implementation private and describe it as backend state rather than as a mathematical primitive.

### 41.1 Type objects, statements, evidence, and algorithms separately

Keep distinct:

- the object, morphism, or diagram being constructed;
- a property it satisfies;
- a theorem or universal property characterizing it;
- a proof, certificate, or witness that the property holds;
- an algorithm that constructs a mediator or verifies a condition;
- provenance describing which backend or theorem supplied the result.

Proof and certificate data may be represented explicitly, but their type and relation to the characterized object must remain clear. They do not replace that object.

Factorization language must expose the diagram. Given

\[
X \xrightarrow{f} Z,
\qquad
X \xrightarrow{u} Y,
\]

a factorization of \(f\) through \(u\) is a morphism \(ar f:Y\to Z\) satisfying \(ar f\circ u=f\). The map being factored, the comparison arrow, and the mediator must all be visible in the interface.

Place operations on their mathematical owners. Mediator construction belongs to the universal arrow or diagram, or to the ambient category's universal-construction interface. Properties and uniqueness statements belong to predicates, theorems, or certificates. Derived structure belongs to the object on which it is defined. Provenance remains separate.

### 41.2 Reject implementation bundles that impersonate mathematical primitives

A wrapper is not made mathematical by collecting related implementation data under a sophisticated name. A class that simultaneously stores construction inputs, a canonical morphism, theorem consequences, normalization state, a partial induced-map algorithm, and certificates is probably bundling several mathematical types and owners.

Translate every field and method into ordinary mathematical data, maps, statements, and algorithms. Determine whether the proposed noun reduces to existing objects, a standard diagram category, an axiomatic refinement, a universal construction, or a private implementation record. Retain a new public noun only when irreducible mathematical data and morphisms remain.

A public abstraction should support ordinary mathematical sentences without reinterpretation. Its instances, maps, and operations must be independently describable without referring to the class that implements them.

### 41.3 Ground semantics independently of implementation success

The existence of a class, parent, wrapper, documentation page, or passing regression does not establish that its name denotes a coherent mathematical concept. Establish the semantics from standard mathematics and the project's existing foundations before using the noun as a premise in later reasoning or architecture.

When the abstraction cannot be reconstructed independently, replace it by the actual objects, morphisms, diagrams, predicates, proof data, and backend routines. Existing dependencies do not justify preserving a mathematically meaningless public interface.

### 41.4 Test the claimed mathematics

A reflexive, identity, empty, zero, or otherwise tautological case may test construction and dispatch plumbing. It does not by itself verify a universal property, classification theorem, factorization algorithm, or general interface.

Evidence for a universal construction should address the obligations appropriate to the setting:

- admissibility of the input diagram or map;
- construction of the mediator;
- commutativity of the required diagram;
- uniqueness or the relevant contractible comparison space;
- nontrivial independent examples;
- rejection or explicit gating of inadmissible inputs;
- compatibility with composition, base change, or other required functoriality.

A tautological case should remain a plumbing regression. If only that case is executable, the general construction remains unimplemented.
