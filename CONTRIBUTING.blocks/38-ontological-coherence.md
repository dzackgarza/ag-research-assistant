## Audit ontological coherence and invented mathematical terminology

When a transcript introduces a new public noun, wrapper, parent, certificate class, or method family, review whether it denotes a standard or explicitly defined mathematical entity rather than an implementation bundle promoted one abstraction layer upward.

Require the analysis to identify:

1. whether the proposed entity is an object, morphism, diagram, property, structure, theorem, proof, certificate, algorithm, or presentation;
2. the ambient category, type, parent, or proposition in which it lives;
3. its defining data, axioms, morphisms, and equality convention;
4. the standard source or established construction that supports the name;
5. which fields and methods belong instead to existing objects, morphisms, categories, predicates, or proof records;
6. whether several mathematically distinct things have been bundled solely because the backend needs shared state;
7. whether an internally coined term is already being used as evidence for later design decisions;
8. whether universal-property language names the characterized object and mediator maps, or reifies the theorem as an opaque domain object;
9. whether formal proof data is explicitly typed as evidence rather than allowed to impersonate the mathematical object it certifies;
10. whether regressions test substantive existence, commutativity, uniqueness, and admissibility rather than only an identity or reflexive case.

Flag **ontological coinage** when implementation pressure produces a mathematical-sounding noun before its type and standard meaning are established. Flag **theorem reification** when a proposition, universal property, or proof obligation is promoted to the primary domain object without an explicit proof-data role. Flag **bundle laundering** when distinct objects, consequences, algorithms, and provenance are hidden inside one wrapper. Flag **self-referential ontology** when later code treats the existence of the coined class as evidence that the mathematical concept exists. Flag **tautological certification** when a trivial regression is reported as verification of a general theorem or interface.

Do not respond merely by renaming the class. Reconstruct the ordinary mathematics, delete the pseudo-object when it dissolves into existing structures, reassign methods to their mathematical owners, and audit every downstream claim that depended on the invented noun.

Formal libraries may legitimately represent a universal property by a proposition, typeclass, or structure containing lifts, factorization equations, and uniqueness proofs. This is not an exception to the audit: the evidence object must have an explicit type and must remain distinct from the object or morphism characterized by it.

Concrete localization, quotient, product, adjunction, moduli, or descent examples are regression witnesses only. The governing rule applies whenever the assistant creates terminology from its current implementation and then begins reasoning inside that private vocabulary.
