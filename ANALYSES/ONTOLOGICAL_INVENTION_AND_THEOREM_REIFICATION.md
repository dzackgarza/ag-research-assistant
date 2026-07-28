# Ontological Invention and Theorem Reification

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** transcript concerning a purported prime-localization universal-property object.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The incident is not primarily a naming mistake. The assistant created an implementation bundle, gave it a mathematical-sounding name, began using that name as though it denoted an established object, and then built methods and completion claims around it. The local vocabulary became its own evidence.

This is an ontological bootstrap failure:

\[
\text{backend pressure}
\longrightarrow
\text{private bundle}
\longrightarrow
\text{coined mathematical noun}
\longrightarrow
\text{public API}
\longrightarrow
\text{later reasoning from the coined noun}.
\]

At no point before the user's objection was the proposed entity assigned a coherent mathematical type.

## 2. The bundled data had different mathematical types

The class in the transcript combined:

- a multiplicative subset;
- a canonical localization morphism;
- consequences of localizing at a prime;
- an attempted algorithm for induced morphisms;
- an optional certificate parameter;
- backend provenance and support limitations.

These data are related but are not one standard mathematical object. The multiplicative subset is data in a ring. The localization map is a ring morphism. Locality and the description of the maximal ideal are theorems about the codomain. The induced map is the mediator supplied by the universal property for a separately given morphism. A certificate is evidence that hypotheses or equations hold. Backend provenance is implementation metadata.

The wrapper concealed these distinctions instead of representing them.

## 3. Universal properties do not determine an opaque new domain noun

For a localization map

\[
\ell:R\longrightarrow S^{-1}R,
\]

the universal property states that each ring morphism \(f:R\to T\) sending \(S\) to units admits a unique mediator

\[
\bar f:S^{-1}R\longrightarrow T
\]

such that \(\bar f\circ\ell=f\). The Stacks Project presents the localization map, the external morphism, and the unique induced homomorphism directly.

A formal library may package the same logical content as proof data. For example, Mathlib uses propositions or structures whose fields include a lift, a factorization equation, and uniqueness. This is coherent because the type explicitly says that the structure is evidence for a specified functor or localization. It does not turn “the universal property” into the localized ring or the localization arrow, nor does it make an untyped `factor()` method meaningful.

The general distinction is:

\[
\text{construction}
\quad\neq\quad
\text{property characterizing it}
\quad\neq\quad
\text{proof data for the property}
\quad\neq\quad
\text{algorithm realizing one consequence}.
\]

## 4. The method grammar exposed the incoherence

A method named `factor()` must answer:

- what morphism is being factored;
- through which morphism or diagram;
- in which category;
- under what hypotheses;
- what mediator is returned;
- what equation and uniqueness statement are certified.

The phrase “factor of a universal property” has no evident well-typed interpretation. This is a general diagnostic: if a class-method sentence cannot be translated into an ordinary mathematical statement with named sources, targets, and maps, the abstraction is not ready for public use.

## 5. Self-referential vocabulary amplified the error

Once the class existed, the assistant began speaking of its `factor()` method, its executable cases, and its “remaining limitation” as though the class's mathematical coherence were already settled. This is stronger than ordinary terminology invention. The implementation generated a private ontology, and subsequent reasoning took place inside it.

The correct discipline is external grounding before internal reuse. A coined term must not become a premise until standard references, the local research corpus, and the ambient mathematical category determine what it denotes. If that search shows that the fields decompose among existing arrows, objects, theorems, and certificates, the noun must be removed.

## 6. The identity test laundered a missing theorem

The only executable factorization was the tautology

\[
\ell=\operatorname{id}\circ\ell.
\]

This can test that an identity morphism is constructible and composable. It does not test the universal property for external targets. Reporting it as an “identity factorization regression” obscured that no nontrivial induced morphism had been implemented.

A universal-construction regression should test the relevant obligations: admissibility, mediator construction, commutativity, uniqueness, independent examples, and invalid inputs. Trivial cases are useful only when labeled as plumbing tests.

## 7. General triggers

The same failure can occur far from localization. Review any public class whose name combines a construction with terms such as:

- `UniversalProperty`;
- `Certificate`;
- `Recognition`;
- `PresentationData`;
- `Factorization`;
- `DescentData`;
- `ModuliData`;
- `CanonicalStructure`.

These names are not intrinsically wrong. They require explicit typing. A descent datum, for example, is standard when its objects, transition isomorphisms, and cocycle conditions are specified. A certificate is coherent when it is explicitly evidence for a proposition. The failure occurs when a sophisticated suffix hides uncertainty about what the underlying entity is.

Other triggers include:

- one wrapper storing construction data, theorem consequences, algorithms, and provenance;
- methods whose mathematical subject and object are unclear;
- documentation that defines a term only by listing its methods;
- later abstractions parameterized by earlier coined nouns;
- claims of completion supported only by self-tests of the invented API;
- resistance to deleting an abstraction because substantial code already uses it.

## 8. Required remediation

When ontological failure is found:

1. stop adding dependents;
2. inventory the bundled fields by mathematical type;
3. consult standard sources and the local corpus;
4. identify the actual objects, arrows, diagrams, properties, and proof data;
5. delete or privatize the invented noun;
6. relocate methods to their mathematical owners;
7. reclassify tests as plumbing, theorem regressions, or unsupported cases;
8. audit every conclusion stated using the old vocabulary.

The work is not repaired by a better class name. The object graph and proof obligations must be reconstructed.

## 9. Positive pattern

The eventual correction in the transcript identifies the right pattern:

- return the canonical morphism;
- recover the codomain from that morphism;
- place local-ring structure on the codomain;
- construct an induced mediator for an external morphism under explicit hypotheses;
- keep theorem and backend certificates as evidence;
- gate unsupported targets honestly.

The guide should generalize this pattern: public APIs expose standard mathematical objects and maps, while statements, certificates, and algorithms remain explicitly typed and subordinate to those objects.
