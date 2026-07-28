## Audit prolonged semantic lock-in

When a transcript contains hours of work organized around a coined abstraction, do not reduce the incident to terminology, method ownership, or a missing preflight check. Reconstruct how the abstraction became self-sealing and why no later checkpoint forced the assistant to ask whether it denoted anything mathematically coherent.

Require the analysis to identify:

1. the first point at which the private noun entered the design;
2. the exact mathematical type that should have been assigned at that point;
3. every downstream class, method, test, and claim that assumed the noun was meaningful;
4. which local successes merely established internal consistency relative to the false premise;
5. when an external source or vocabulary-erasure audit first occurred;
6. which warning signs appeared earlier: mixed mathematical types, opaque method grammar, tautological tests, missing morphisms, absent standard references, or repeated bundling;
7. whether the assistant ever tried to falsify its abstraction rather than extend it;
8. whether sunk cost or compatibility pressure caused preservation of an incoherent interface;
9. which computations survive after being translated back into standard mathematics;
10. which downstream claims must be purged and re-established.

Flag **semantic lock-in** when a provisional abstraction becomes the unquestioned language of later work. Flag **self-sealing abstraction** when tests, documentation, and dependent code written in the same private vocabulary are treated as evidence that the vocabulary is meaningful. Flag **local-consistency substitution** when software coherence replaces mathematical coherence. Flag **sunk-cost preservation** when an incoherent object is retained because substantial code depends on it. Flag **semantic audit starvation** when no independent mathematical revalidation occurs during a long implementation trajectory.

The relevant prevention rule is longitudinal. A one-time ontological checklist at class creation is not enough. Require revalidation whenever a coined noun acquires substantial downstream dependence, when its methods cannot be expressed in ordinary mathematical sentences, before completion claims, and whenever progress has continued materially without external grounding.

Use the vocabulary-erasure test in review: restate the entire abstraction without any implementation-coined terminology. If the object, morphisms, operations, and proof obligations cannot then be recovered unambiguously, the public abstraction has no independent mathematical meaning.

Do not credit hours of work as mathematical progress merely because the code executed. Separate independently valid computations from claims formulated only inside the incoherent ontology. The latter must be discarded and rebuilt from the corrected mathematical foundation.

A valid assistant-facing rule should make it difficult for an agent to work for hours inside a false ontology without stopping itself. The user should not have to ask, late in the process, what kind of mathematical thing the central class is.

## Audit the actual \(\infty\)-categorical derivation, not a categorical slogan

When a transcript contains concrete higher-categorical mathematics, do not replace it in the guide by phrases such as “preserve categorical level,” “retain coherence,” or “reuse abstractions” without reproducing the construction that gives those phrases content.

For every universal construction, require the review to write an explicit derivation chain. In the localization regression case this must include:

\[
\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C),
\qquad
\mathcal C_{R/}
\simeq
\{R\}\times_{\mathcal C,\operatorname{ev}_0}\operatorname{Ar}(\mathcal C),
\]


a replete full subcategory

\[
\operatorname{Inv}_S(R)\subseteq\mathcal C_{R/},
\]

an initial object

\[
\ell:R\to L,
\]

and, for every admissible \(\phi:R\to T\), a contractible mapping object

\[
\operatorname{Map}_{\operatorname{Inv}_S(R)}(\ell,\phi).
\]

A point \(\alpha_\phi:\ell\to\phi\) is the full comparison cell. The familiar factor map \(\widetilde\phi:L\to T\) is its target component. The review must state which evaluation or truncation extracts it and what data are forgotten.

Require the analysis to identify:

1. the ambient \(\infty\)-category and the project’s truncation convention;
2. the exact diagram category, slice, coslice, comma category, or category of cones used;
3. the full or replete subcategory expressing admissibility;
4. the initial, final, limit, or colimit object that is the mathematical construction;
5. the mapping object whose points are universal comparison cells;
6. every source and target component of those cells;
7. the evaluation, truncation, or forgetful functor producing any bare map returned to a backend;
8. the contractibility, uniqueness, naturality, or coherence statement retained by the full construction;
9. the exact prior project abstractions reused at each step;
10. the irreducible new datum, if any.

Flag **categorical sloganization** when precise constructions are compressed into general advice that would not let a future agent reconstruct the objects or maps. Flag **categorical-level regression** when mapping objects are silently replaced by sets or higher cells by bare components. Flag **abstraction amnesia** when the assistant reimplements a Hom-set bijection, factorization helper, or local theorem wrapper instead of using an existing initial object, arrow category, slice, or limit. Flag **component erasure** when the target map survives but its square and ambient morphism of arrows do not. Flag **parallel-foundation drift** when a second strict or set-level API grows beside the established foundation.

Do not turn this into a generic demand for sophisticated language. The review must verify that the higher-categorical formulation actually determines the data being implemented. It must also preserve strict equalities when the theorem requires them. The requirement is exact derivation and explicit truncation, not abstraction for its own sake.

A valid guide entry should let a mathematically competent reader reconstruct the universal object, the comparison cell, its components, and the ordinary truncated statement without consulting the originating transcript.
