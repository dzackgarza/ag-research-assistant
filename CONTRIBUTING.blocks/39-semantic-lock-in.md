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

## Audit explicit categorical derivations without overfitting to one regression

When a transcript contains concrete higher-categorical mathematics, do not replace it by slogans such as “preserve categorical level” or “retain coherence.” Require an explicit derivation through the actual diagram category, admissible subcategory, universal object, mapping object, comparison cell, and projection or truncation used by the implementation.

A sufficiently detailed worked example may remain in the deployed guide when it anchors a recurring failure. Mark it explicitly as a regression example. Do not make its particular objects, symbols, or category chain the standing ontology for unrelated constructions.

For the localization regression, the derivation includes

\[
\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C),
\qquad
\mathcal C_{R/}
\simeq
\{R\}\times_{\mathcal C,\operatorname{ev}_0}\operatorname{Ar}(\mathcal C),
\]

a replete full subcategory \(\operatorname{Inv}_S(R)\), an initial object \(\ell:R\to L\), and contractible mapping objects \(\operatorname{Map}(\ell,\phi)\). A point \(\alpha_\phi:\ell\to\phi\) is the full comparison cell; the factor map \(\widetilde\phi:L\to T\) is its target component.

For another universal construction, require the analogous problem-specific derivation rather than copying the localization chain. The review should identify:

1. the ambient category and truncation convention;
2. the exact diagram, slice, coslice, comma, cone, or cocone category;
3. the subcategory or classifier expressing admissibility;
4. the initial, final, limit, colimit, adjoint, or representability object;
5. the mapping object containing universal comparison cells;
6. the components of those cells;
7. the evaluation, projection, truncation, or forgetful functor producing backend data;
8. the uniqueness, contractibility, naturality, or coherence retained by the full construction;
9. the prior project abstractions reused at each step;
10. the irreducible new datum.

Flag **categorical sloganization** when precise mathematics is compressed into advice too vague to reconstruct the objects or maps. Flag **example overfitting** when one regression derivation is promoted into a universal template whose symbols and special hypotheses dominate unrelated work. Flag **categorical-level regression**, **abstraction amnesia**, **component erasure**, and **parallel-foundation drift** when an existing structured construction is replaced by a weaker local interface.

The requirement is exact mathematical derivation plus an explicit statement of which parts are general and which parts belong only to the worked example.
