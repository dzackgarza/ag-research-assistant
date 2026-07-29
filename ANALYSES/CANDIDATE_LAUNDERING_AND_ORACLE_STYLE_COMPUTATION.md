# Candidate Laundering and Oracle-Style Computation

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** transcript in which equations for a proposed Nikulin quotient were inserted first and then checked for dimension, degree, singular points, and étaleness.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The assistant did not compute the requested quotient from the involution. It supplied equations for a candidate surface and computed several properties of that candidate. It then reported the candidate as “the explicit Nikulin quotient” and described the property checks as establishing the quotient.

The failure is

\[
\text{expected or guessed answer}
\longrightarrow
\text{candidate entered into the notebook}
\longrightarrow
\text{properties of the candidate checked}
\longrightarrow
\text{candidate reported as computed output}.
\]

This is a stronger form of answer-first computation than a hard-coded assertion. The oracle has moved from the assertion into the construction of the object itself.

## 2. Candidate verification is mathematically different from construction

Let \(Q\) be a proposed answer. Computing

\[
\dim Q,
\qquad
\deg Q,
\qquad
\operatorname{Sing}(Q),
\]

or verifying that a map to another scheme is étale at selected points establishes those statements about \(Q\). It does not establish that \(Q\) is the requested categorical quotient, image, fixed locus, moduli object, or exhaustive solution set.

Many nonisomorphic objects can share dimensions, degrees, singularity counts, and other selected invariants. Even a long collection of correct consequences does not replace the defining comparison map or universal property.

## 3. What quotient computation would require

For a group action of \(G\) on \(X\), identifying a candidate \(Q\) with \(X/G\) requires the mathematical data defining that claim. Depending on the setting, this may include:

- a morphism \(q:X\to Q\);
- invariance \(q\circ g=q\) for every \(g\in G\);
- computation of the invariant algebra and construction of its spectrum or projective spectrum;
- an isomorphism from the independently constructed quotient to \(Q\);
- the appropriate categorical or geometric quotient universal property;
- orbit, stabilizer, or descent conditions required by the chosen quotient notion.

A computer algebra system may produce the quotient directly, or a displayed mathematical derivation may construct it. In either case, the notebook must expose the derivation from the action to the quotient. Starting with the final equations and checking downstream properties is not that derivation.

## 4. Internal model calculations are not research evidence

A language model may recognize a likely equation, remember a formula from a source, or derive a candidate internally. None of these is self-authenticating notebook evidence.

A useful candidate can be recorded if its origin is explicit:

- quoted from a paper or database;
- supplied by the user;
- derived in displayed mathematics;
- conjectured from examples;
- proposed for a regression comparison.

The candidate must remain separate from the computational path intended to reproduce it. If the derivation exists, write it down. If only the candidate is known, say that the notebook verifies properties of a supplied candidate and has not yet computed the requested object.

An unexplained correct answer is research-useless in the relevant sense: it cannot be audited, varied, generalized, debugged, or trusted as evidence that the implementation performs the advertised construction.

## 5. Completeness and identity claims require their own evidence

The same defect appears throughout computational mathematics:

- listing expected fixed points and checking that they are fixed does not compute the full fixed scheme;
- entering expected singular points and checking the Jacobian there does not compute the singular locus;
- assigning a known group and checking its order does not compute a fundamental group or deck group;
- entering an ADE label and checking a few invariants does not classify the germ;
- writing expected quotient equations and checking degree and singularities does not compute the quotient;
- matching invariants does not construct an isomorphism.

The evidence must match the claim. Exhaustive results need completeness arguments. Identification claims need maps or universal properties. Classification claims need the required normal form, theorem, or certificate.

## 6. Correct notebook structure

The visible argument should have the order

\[
\text{input data}
\longrightarrow
\text{executed algorithm or displayed derivation}
\longrightarrow
\text{output object}
\longrightarrow
\text{independent checks}.
\]

The final checks are valuable precisely because they are downstream and independent. Reversing the order turns expected answers into hidden inputs and makes successful checks circular or substantially weaker than the reported conclusion.

## 7. Editorial consequence

This transcript extends the existing answer-first-computation failure recorded in P-0009. It does not require a new operation-specific rule about Nikulin quotients. The durable correction belongs in the existing computation-and-evidence sections:

- distinguish computed output, theorem-derived output, supplied candidate, and candidate verification;
- require visible provenance from inputs to output;
- keep expected answers outside the computational path;
- require defining maps, completeness, or universal properties at the strength of the advertised result.
