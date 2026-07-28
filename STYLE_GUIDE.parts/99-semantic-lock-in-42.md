
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
