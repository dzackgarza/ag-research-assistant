# Mathematician-Facing Sage and Semantic Distance

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** exchange comparing hypothetical computational verification of an algebraic-geometry paper with Sage code written in ordinary mathematical parlance.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The exchange exposes a default style misalignment common to coding agents. The assistant correctly wanted a semantic interface, but translated the paper into the idiom of generic software design: utility-like constructors, multi-stage method pipelines, abstract container nouns, and operations placed according to convenient call syntax. The user instead expected Sage code to read as mathematics.

The difference is not cosmetic. The visible code is part of the research argument. If it speaks in schemes, morphisms, divisors, line bundles, linear systems, covers, lifts, quotients, local rings, and singularity strata, a mathematician can audit the computation by checking that each line implements a familiar construction. If it speaks in helper factories, positional data, generic `element` constructors, and ad hoc action pipelines, the reader must reverse-engineer both a software architecture and the mathematics.

The governing objective is therefore to minimize semantic distance:

\[
\text{paper claim}
\longleftrightarrow
\text{visible Sage statement}
\longleftrightarrow
\text{certified mathematical result}.
\]

Backend code may be complicated. The research-facing layer should preserve this short path.

## 2. Default agent style is generic-software style

Coding agents are strongly attracted to several conventions that are reasonable in ordinary application software but often poor for computational mathematics.

### 2.1 Generic nouns replace mathematical objects

A phrase such as `LinearSystems(L).element(V)` treats a standard mathematical object as an instance manufactured by a software collection. A mathematician instead asks for the linear system associated to a line bundle and then for a subsystem or member of it. Similarly, `line_bundle(4,4)`, `CoverData`, or `ProjectiveSchemeTools` can conceal the ordinary objects \(\mathcal O(4,4)\), a covering morphism, or the category of schemes.

The problem is not that descriptive constructors are always forbidden. It is that the implementation vocabulary begins to determine the ontology. The code ceases to mirror the paper.

### 2.2 Procedural pipelines replace induced mathematics

The assistant proposed manually passing through linearization, action on cohomology, invariant subspace extraction, and generic element construction. Those are mathematically meaningful stages, but when they are canonical consequences of the chosen object, requiring the user to orchestrate them is needless implementation ceremony.

The better interface lets the line bundle, linear system, action, or cover compose the standard steps. The notebook still names the mathematically relevant intermediate objects when they participate in the proof.

### 2.3 Object-oriented syntax is confused with mathematical ownership

A method call is not semantic merely because it has a receiver. `tau.lifts_to(pi)` reads as though the automorphism owns a vaguely named relation to a cover. The actual datum is a lift through a covering morphism, represented by a commutative square. The cover, its automorphism object, or the ambient arrow category is the more natural owner.

The same issue appears when code places a cover on the branch curve rather than on the base scheme with the line-bundle or algebra data that define the cover. Discoverability should follow mathematical ownership, not arbitrary receiver convenience.

### 2.4 Programmers suppress lines that mathematicians need

Application code often removes “redundant” assertions and intermediate variables. Research code benefits from them. Lines such as

```sage
assert L in Y.Pic()
assert B in Lambda
assert pi.degree() == 2
```

are not clutter. They state where objects live and which mathematical claims the computation has established. They turn the notebook into an auditable proof ledger rather than an opaque execution trace.

### 2.5 Booleans and labels flatten mathematical structure

A generic API tends to return `True`, `False`, or a string label. In research mathematics, a positive classification may refine an object into a category, carry a theorem or certificate, and make additional operations available. A singularity type belongs to a point, germ, or local ring; a K3 or del Pezzo assertion belongs to a certified surface object. Detached labels discard the structure needed for later deductions.

### 2.6 Equations displace the objects they present

Agents often treat the polynomial or ideal as the final output. The paper speaks about a curve, surface, quotient, branch divisor, or local germ. Equations should be displayed and computed, but they should remain presentations of those semantic objects through named realization maps.

## 3. Executable mathematical prose

The target style is not merely “use more mathematical names.” The visible notebook should preserve the logical architecture of the mathematical argument.

A typical segment should:

1. construct the ambient object;
2. construct and type the line bundle, divisor, action, or morphism;
3. name the relevant parent or category;
4. form the induced object through a standard mathematical method;
5. display equations or local presentations when useful;
6. assert the claimed dimension, degree, commutativity, divisor relation, ampleness, or classification;
7. state whether the conclusion is computed or theorem-derived.

This style intentionally uses more named lines than ordinary production software. The unit of readability is a mathematical step, not a compact expression.

## 4. Discoverability and ownership

Sage's parent/element and category design makes methods valuable for discovery. A user who has a line bundle should be able to inspect methods for sections and linear systems; a user who has a morphism should discover image, pullback, graph, and restriction operations; a user who has a cover should discover deck transformations and lifts.

This does not justify attaching every operation to every object. The ownership test remains mathematical:

- Does the receiver determine the construction?
- Is the result functorially induced from it?
- Does a multi-object diagram need to be named instead?
- Is the method merely derived syntax for an existing primitive?

The best public surface is both discoverable and mathematically typed.

## 5. Hide ceremony, not proof structure

The transcript reveals an important balance.

The interface should hide:

- coordinate-block slicing;
- coercion and normalization plumbing;
- saturation helpers;
- backend selection;
- standard induced-action machinery;
- canonical conversions among supported presentations.

The notebook should expose:

- the ambient scheme and base;
- the line bundle and section space;
- the linear system and its invariant subsystem;
- the branch divisor and covering morphism;
- the lifted automorphisms and their commutative squares;
- the quotient objects and quotient maps;
- the local rings, germs, and singularity strata;
- the divisor classes and numerical identities used in the proof.

Thus semantic compression is not maximal abstraction. It is removal of implementation ceremony while retaining the mathematical dependency graph.

## 6. Genericity and specialization are part of the interface

The source paper may discuss a general curve, a universal family, a generic member, or a special degeneration. These are distinct mathematical levels. An agent-generated API often collapses them into a method such as `general_member()` followed by raw coefficient substitution.

A mathematically legible interface should distinguish:

- the parameter scheme or projective space of sections;
- the universal divisor;
- the generic fiber over the function field;
- a dense open on which a property holds;
- a selected rational or geometric point;
- the specialized member and the base-change map producing it.

Conditions imposing an \(A_n\) singularity, tangency, fixed point, or divisor relation should appear as geometric loci in parameter space, not merely as solver constraints detached from the family.

## 7. Pseudocode is a semantic design instrument

Hypothetical pseudocode is useful when the current CAS lacks the desired interface. It lets the researcher ask what the computation should look like if the mathematics were represented faithfully. This can expose missing parents, morphisms, categories, universal constructions, or theorem propagation.

The danger is that visually mathematical pseudocode can still be incoherent. Each line must identify:

- the mathematical owner;
- the precise input and output;
- parentage and category;
- required hypotheses and choices;
- full diagrams versus projected components;
- whether the method is native, proposed, or purely schematic.

The transcript's individual method names are therefore not a specification. They are directional evidence for a style in which the semantic distance is small. The sketch also contains the line `assert pi in X.Aut()`, but the surrounding declarations make the intended line unambiguous: `assert i_dP in X.Aut()`. This is a transcription typo, not evidence that the user confused a covering morphism with an automorphism. Editorial analysis must reconstruct such sketches charitably from their local types and must not promote an obvious symbol slip into a conceptual failure mode.

## 8. The mathematical-auditor criterion

The strongest test is external to the software idiom.

Assume a reader understands algebraic geometry but not Sage or Python. Given the advertised meanings of the methods, can that reader:

- identify every object and map from the paper;
- determine where each object lives;
- follow the construction of covers, lifts, quotients, divisors, and singular loci;
- distinguish universal, generic, and specialized objects;
- see which equalities and numerical claims were actually checked;
- determine which conclusions use theorems;
- inspect the relevant equations and local presentations;
- identify the exact unsupported primitive if the computation stops?

If so, the notebook is close to executable mathematical prose. If not, the visible layer remains captured by generic software style.

## 9. General editorial rule

Do not encode the transcript as a list of mandatory method names. Preserve the underlying alignment:

- standard mathematical nouns and verbs;
- correct ownership and Sage-native discoverability;
- explicit parents, categories, and maps;
- visible mathematical checkpoints;
- canonical procedure hidden behind semantic methods;
- equations retained as presentations;
- categories and certificates retained instead of flattened labels;
- hypothetical pseudocode audited for mathematical typing;
- research code written for a mathematical auditor rather than a Python maintainer.

This principle applies beyond algebraic surfaces. It governs any computational mathematics notebook in which the code is intended to certify, reproduce, or extend a mathematical argument.