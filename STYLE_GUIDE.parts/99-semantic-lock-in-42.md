
## 42. Prevent prolonged semantic lock-in

The most dangerous abstraction failure is not the first mistaken noun. It is continuing for a long time after that noun has begun to organize the work, while every new class, method, test, and progress report assumes the noun is meaningful. Local implementation success can make an incoherent premise increasingly difficult to see.

Do not treat an abstraction as validated merely because:

- methods can be attached to it;
- its fields can be populated;
- examples execute;
- downstream classes compose with it;
- tests written in its own vocabulary pass;
- the same coined terminology now appears throughout the notebook or framework.

All of those facts are conditional on the original semantic claim. They can establish internal software consistency while the public mathematics remains meaningless.

### 42.1 Revalidate abstractions during long work, not only at introduction

A one-time naming audit is insufficient. Reopen the mathematical definition whenever a new abstraction begins to accumulate downstream consequences.

Mandatory revalidation triggers include:

- a coined noun acquires a second public method, subclass, or dependent construction;
- several progress updates use the noun without restating its mathematical type;
- tests verify only operations internal to the new vocabulary;
- the class begins bundling construction data, theorem consequences, certificates, and algorithms;
- a method name cannot be translated immediately into a well-typed mathematical sentence;
- implementation effort is growing while no standard source has been found;
- the abstraction is being used to justify further architecture;
- a user or collaborator asks what kind of mathematical thing it is.

At each trigger, suspend extension work and reconstruct the abstraction from first principles. Do not postpone the audit until the current method or notebook section is complete.

### 42.2 Apply the vocabulary-erasure test

Temporarily forbid use of every term coined by the implementation. Restate the construction using only established mathematical objects, morphisms, diagrams, properties, theorems, proof data, and algorithms.

The reconstruction must identify:

1. the ambient category or type;
2. the actual objects and maps;
3. every input and output of each public operation;
4. the equations, universal properties, or propositions involved;
5. which data are mathematical and which are backend state or provenance;
6. the standard source or independently recognizable construction.

If the public interface cannot be described without its private noun, the noun has no established independent meaning. Keep the implementation private or delete the abstraction.

The test must be performed from the mathematics outward, not by paraphrasing the class fields. Search the local source corpus and standard references using the underlying diagrams and operations rather than the coined class name.

### 42.3 Falsify the abstraction adversarially

Do not ask only how to make the abstraction work. Ask how it might fail to denote anything coherent.

Try to show that:

- its fields have different mathematical types and no standard object bundles them;
- its methods have no common mathematical owner;
- its equality convention is unspecified or changes by backend;
- its instances cannot be characterized independently of the constructor;
- its morphisms cannot be stated;
- its apparent theorem is merely a property of another object;
- its tests are tautological consequences of how the wrapper was built;
- the same functionality is already expressed by ordinary maps, diagrams, predicates, or proof records.

An abstraction intended for research mathematics must survive this hostile reconstruction before substantial downstream work continues.

### 42.4 Never use self-generated structure as semantic evidence

Documentation, tests, type annotations, method dispatch, and downstream reuse may verify that code conforms to its own contract. They do not show that the contract corresponds to a coherent mathematical concept.

Do not reason:

\[
\text{the class exists}
\Longrightarrow
\text{the mathematical object exists}
\Longrightarrow
\text{later methods are meaningful}.
\]

External mathematical grounding must enter before the second implication. Evidence must come from a standard definition, a precise reconstruction in accepted mathematics, or an explicitly typed new structure with independently stated objects and morphisms.

### 42.5 Use a semantic stop-loss

When an abstraction fails revalidation, treat the failure as foundational, regardless of the time already invested.

Immediately:

1. freeze all dependent work;
2. identify the earliest point where the invented noun entered the design;
3. discard claims whose statements depend on that noun;
4. decompose the implementation into valid computations, maps, predicates, certificates, and backend routines;
5. reassign those pieces to standard mathematical owners;
6. delete the public pseudo-object rather than preserving compatibility;
7. rerun the downstream mathematical audit from the corrected foundation.

Do not summarize the event as a naming cleanup or a small interface repair. If the original noun had no coherent meaning, hours of work performed inside that vocabulary do not constitute progress on the claimed mathematics. Only the independently reclassified components may be retained.

### 42.6 Surface semantic uncertainty before it compounds

Progress reports must not normalize unvalidated vocabulary. When a proposed abstraction is provisional, say exactly which mathematical type or standard construction remains unresolved. If the ambiguity affects downstream correctness, pause and present the issue before building further layers.

The user should not need to discover semantic incoherence after a large implementation has accumulated. The assistant is responsible for repeatedly challenging its own ontology, especially when local coding progress is easiest and mathematical meaning is least independently checked.

## 43. Preserve the established categorical level and reuse prior abstractions

A research framework must accumulate mathematics rather than repeatedly restart from a weaker local language. Once the project has fixed an ambient categorical universe and implemented constructions such as arrow categories, slices or coslices, mapping objects, limits, colimits, and comparison cells, later work must be expressed through those foundations unless an explicit theorem justifies changing level.

Do not replace an established higher or structured formulation by a parallel set-level or bare-morphism formulation merely because the current example is ordinary, strict, or computationally convenient. Ordinary categories and strict constructions should appear as truncated or strict special cases of the declared framework, not as a second foundation that bypasses it.

### 43.1 Conserve categorical level

Before formulating a new universal construction, record the categorical level already in force:

- the ambient category or category of categories;
- the mapping objects and their truncation level;
- how arrows, squares, transformations, homotopies, and higher cells are represented;
- which equality, equivalence, or coherence relation the project uses;
- which truncation or strictification functors are available.

If the project treats ordinary categories inside an \(\infty\)-categorical universe, do not claim that a separate ambient \(2\)-category must first be invented before recognizing morphisms between arrows or coherent comparison data. Use the project's existing arrow and functor constructions. Conversely, do not invoke higher cells decoratively when the theorem genuinely requires strict equality in a Hom-set. The categorical level is determined by the established mathematics, not by whichever backend interface is easiest.

Any descent from mapping objects to sets, from cells to component maps, or from coherent equivalence to Boolean equality must be an explicit operation. Name the truncation, projection, component, or forgetful functor and state what data are lost. Never let a backend's inability to store higher structure perform that truncation silently.

### 43.2 Reuse the project's categorical constructors before defining parallel interfaces

Before adding a class, method family, or theorem wrapper, audit the abstractions already established in the project. Search prior notebook sections, local source files, project decisions, and existing implementations for:

- \(\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C)\);
- slice, coslice, comma, and full or replete subcategories;
- limits, colimits, initial and final objects;
- universal cones, cocones, mediators, and comparison cells;
- natural transformations, sections, adjunction data, and theorem certificates;
- previously chosen conventions for components, equality, and coherence.

State how the new construction is obtained by composition, restriction, refinement, or a universal construction from those primitives. A new public abstraction is justified only by irreducible data not already represented. Re-deriving a Hom-set bijection, factorization helper, or bespoke lift object when initiality in an existing slice or arrow category already supplies it is abstraction amnesia, not simplification.

### 43.3 Preserve the whole categorical witness

When the mathematical result is a morphism in an arrow category, a commutative square, a natural transformation, a homotopy, or another higher cell, return or store that semantic object. Lower-dimensional components remain accessible as derived data.

For a morphism of arrows, the target component may be the ring map or scheme map used in a concrete calculation, but it is not the entire comparison datum. The source component, commutative square, ambient arrow category, and coherence conditions must remain recoverable. Convenience syntax may return a component only when it delegates to the stored cell and clearly states the projection being applied.

Do not erase a universal structure while purging an incoherent wrapper. The correct remediation may be to replace the wrapper by an initial object, universal cone, or structured arrow already supported by the framework—not to collapse everything to its underlying morphism.

### 43.4 Express universal properties through the existing categorical foundation

Formulate a universal property first as the appropriate initial or final object, limit or colimit, adjunction, localization, or representability statement in the established category. Its mapping object expresses existence, uniqueness, and coherence at the ambient level.

For example, if a class of arrows out of \(R\) forms a full subcategory of the coslice \(\mathcal C_{R/}\), a universal arrow should be an initial object of that subcategory. For every admissible arrow \(\phi\), the relevant mapping object from the universal arrow to \(\phi\) is contractible. A chosen point is a morphism in the arrow category; its target component is the familiar factor map. In a truncated ordinary case this recovers the unique strict mediator, but the implementation should be obtained by specialization from the same construction.

Do not build a second API around a set-valued Hom bijection, an opaque `induced_morphism`, or a component-only lift when the project's initial-object and arrow-category machinery already gives the complete datum. Such formulas may be backend realizations or derived theorems, not competing foundations.

### 43.5 Maintain an abstraction dependency ledger

Foundational work must be cumulative. Before each substantial extension, identify:

1. which existing categories and categorical constructions the new work depends on;
2. which previously implemented objects and cells it reuses directly;
3. which new irreducible datum is being added;
4. which earlier interfaces become derived sugar rather than separate primitives;
5. which tests demonstrate compatibility with existing composition, limits, truncations, and coherence.

If a local implementation cannot answer these questions, pause before coding. Reopen the established foundation instead of reconstructing the theory from the current example.

### 43.6 Detect categorical regression and abstraction amnesia

Stop and re-audit when:

- an established arrow, slice, or limit construction disappears from the explanation of a later universal object;
- mapping spaces or mapping categories are replaced by sets without an explicit truncation;
- a cell is returned only through one component and the full diagram is discarded;
- new terminology duplicates an existing categorical construction;
- the agent says that an ambient higher category must be specified even though the project already fixed one;
- a weaker local formulation is presented as a correction of a richer coherent one;
- methods are reimplemented independently rather than inherited or composed from earlier abstractions.

These are not harmless expository changes. They break the cumulative mathematical architecture and cause later work to prove statements in a different, weaker framework than the one the project established.

### 43.7 Repair from the earliest categorical divergence

When categorical regression is found:

1. freeze downstream work based on the weaker parallel formulation;
2. identify the last point where the established categorical framework was still being used;
3. translate the local objects, maps, and tests back into that framework;
4. restore full cells and universal witnesses, retaining component computations as backends;
5. remove duplicate set-level or component-only interfaces unless they are explicit derived projections;
6. re-audit downstream claims for lost coherence, naturality, or functoriality;
7. add nontrivial regressions involving composition and comparison in the existing categorical layer.

The user should not need to remind the assistant that an arrow category, slice construction, limit interface, or higher-cell convention was already implemented. Reuse of the project's own mathematics is a correctness requirement, not merely code reuse.
