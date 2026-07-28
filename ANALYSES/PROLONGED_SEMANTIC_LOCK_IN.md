# Prolonged Semantic Lock-In

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** transcript concerning extended implementation around an incoherent coined abstraction.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The failure was not a small naming error discovered late. The assistant introduced an abstraction with no coherent mathematical type, then worked inside that abstraction for hours. It added methods, tests, completion claims, and further architecture without once returning to the elementary question: what mathematical thing is this?

The trajectory is:

\[
\text{implementation pressure}
\longrightarrow
\text{provisional bundle}
\longrightarrow
\text{coined mathematical noun}
\longrightarrow
\text{local API success}
\longrightarrow
\text{downstream dependence}
\longrightarrow
\text{increased confidence in the noun}.
\]

The later stages do not provide independent support for the first semantic step. They merely make the false premise more entrenched.

## 2. Why this is more severe than ordinary abstraction error

An ordinary implementation error may be localized: a method has the wrong owner, a map has the wrong variance, or a backend does not satisfy its contract. Here the entire vocabulary used to state progress was defective.

Once the assistant began saying that a purported object had a `factor()` method, that its identity case had been verified, and that only arbitrary targets remained unsupported, the implementation had become self-referential. The noun supplied the apparent subject of the sentences; the methods supplied apparent predicates about it; the tests supplied apparent evidence. None of these answered whether the subject denoted anything in mathematics.

This is a failure of mathematical self-criticism. A researcher must repeatedly ask whether the objects under discussion are well typed, standard or explicitly defined, and independently intelligible. The assistant instead optimized within its own provisional ontology.

## 3. Local consistency created a self-sealing system

The abstraction became increasingly difficult to question because every later component was written in the same vocabulary.

- The class constructor made instances exist.
- Methods made the instances appear operational.
- Documentation made the operations appear intentional.
- tests made the implementation appear verified.
- downstream code made the abstraction appear foundational.
- progress reports made the terminology appear settled.

These are all forms of local consistency. They can validate a software system relative to a specification. They cannot validate that the specification corresponds to a coherent mathematical object.

A false ontology can therefore become more internally coherent over time while becoming more expensive to remove. This is why the failure needs a stop-loss rather than only a better naming checklist.

## 4. The missed elementary question

The decisive question was available from the beginning:

> Is this an object, a morphism, a theorem, proof data, an algorithm, or merely a backend record?

Had the assistant answered it, the proposed abstraction would have decomposed immediately:

- the multiplicative subset is ring data;
- the localization is a morphism;
- locality and the maximal-ideal description are propositions about the codomain;
- the universal property is an existence-and-uniqueness statement or natural equivalence;
- a lift is a mediator for a separately supplied morphism;
- a certificate is proof data;
- backend provenance is implementation metadata.

There is no single standard mathematical object formed by placing all of these in one wrapper and giving it a compound name.

## 5. Why the passing identity case was actively misleading

The identity factorization checked only

\[
\ell = \operatorname{id}\circ \ell.
\]

That can test object construction, composition, or dispatch. It does not test the universal property for an independent admissible map, mediator construction, or uniqueness.

Because the test was named using the invented ontology, it did more than fail to prove the theorem: it reinforced the illusion that the abstraction itself had already been validated. This is tautological certification inside a self-sealing vocabulary.

## 6. The missing longitudinal safeguard

A pre-implementation ontology check is necessary but insufficient. Agents can miss the first error. The system therefore needs recurring checkpoints after the abstraction begins to acquire consequences.

The checkpoint should trigger when:

- a new noun obtains multiple public operations;
- dependent classes begin using it;
- several progress reports assume it;
- only internal examples have been tested;
- no standard source or independent formulation has been found;
- method names cannot be translated into ordinary mathematical grammar;
- distinct mathematical types are accumulating in one object;
- substantial implementation time has passed without semantic re-derivation.

At that point extension work must stop, even when the current method is close to working.

## 7. Vocabulary erasure as an independence test

The most effective diagnostic is to remove the coined terminology temporarily. The assistant must describe the construction using only ordinary mathematical language and standard notation.

If it cannot identify the ambient category, objects, maps, equations, propositions, algorithms, and proof data without the coined noun, then the abstraction has no meaning independent of the implementation.

This test blocks a common failure mode in which the assistant merely paraphrases its class fields. The reconstruction must start from source mathematics, not from the code.

## 8. Adversarial rather than constructive review

The assistant spent its effort asking how to extend the abstraction. It did not ask how to falsify it.

A hostile review would have asked:

- Can another mathematician identify the instances without seeing the constructor?
- What are the morphisms between instances?
- Is the object standard in any source?
- Are its fields of one mathematical type?
- Does the method grammar describe a valid diagram?
- Are its tests independent of its constructor?
- Does the abstraction disappear when translated into existing objects and maps?

Research abstractions should survive this adversarial pass before they become architectural dependencies.

## 9. Sunk cost cannot preserve a meaningless interface

Once the ontology fails, compatibility pressure is irrelevant. There is no legitimate public contract to preserve.

The correct remediation is:

1. freeze dependent work;
2. identify the earliest introduction of the noun;
3. discard claims stated only in that vocabulary;
4. salvage independently valid computations;
5. reclassify each surviving component by its true mathematical type;
6. delete the pseudo-object;
7. rebuild downstream work from the corrected foundation.

The time already spent increases the importance of purging the error; it does not justify keeping it.

## 10. Editorial consequence

Guidance that says only “define public nouns carefully” or “separate objects from universal properties” underfits the incident. The agent did not merely fail once. It failed to re-evaluate through a long trajectory despite accumulating evidence that the abstraction lacked ordinary mathematical grammar.

The standing rule must therefore be longitudinal:

> Every provisional mathematical abstraction remains under active semantic challenge until it has independent mathematical grounding. Local code success never closes that question. As downstream dependence grows, the burden of revalidation grows with it.

The user should not need to interrupt hours later and ask what kind of mathematical thing the central object is.
