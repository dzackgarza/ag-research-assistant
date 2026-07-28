# Changelog

This document is for repository contributors and users tracking revisions. It is not part of the prompt consumed by the Algebraic Geometry Research Assistant.

## 0.6.7 — 2026-07-28

Split the deployed style guide into canonical source fragments and a generated committed artifact.

- Added ordered `STYLE_GUIDE.parts/*.md` source files grouped by mathematical and Sage concerns.
- Added `scripts/build_style_guide.py`, which concatenates the fragments byte-for-byte and supports a `--check` mode.
- Kept `STYLE_GUIDE.md` as the single deployable custom-GPT artifact while making the fragments the canonical editable source.
- Added a GitHub Actions workflow that verifies the generated artifact on pull requests and rebuilds and commits it on `main`.
- Added an hourly scheduled fallback for connector- or API-authored fragment updates that do not trigger ordinary push workflows.
- Updated contributor guidance to prohibit memory-based whole-file reconstruction and to prefer publishing small reviewed fragments through repository APIs.

## 0.6.6 — 2026-07-28

Added backend-friction self-auditing and mathematical reformulation guidance.

- Required repeated repair around a Sage limitation to trigger reconsideration of the mathematical formulation, not merely another backend patch.
- Distinguished genuine Sage deficiencies from cases where the chosen notion is unnecessarily strict, presentation-bound, or at the wrong categorical level.
- Required searches of the local corpus and appropriate modern references for intrinsic formulations that may make the relevant witness first-class and obviate the deficient operation.
- Required explicit comparison maps, equivalences, universal properties, or strictification results before a reformulation may replace the original statement.
- Added safeguards against backend fixation, semantic foreclosure, and theory laundering.
- Retained equality of morphism composites as one regression example rather than the governing rule.
- Added contributor review criteria requiring proof that a reformulation preserves the research target and actually reduces the implementation burden.

## 0.6.5 — 2026-07-28

Added a contributor workflow for publishing reviewed changes when direct Git push access is unavailable.

- Required contributors to clone or materialize the exact current repository baseline before editing, with the upstream commit recorded.
- Prohibited reconstructing complete files from memory, chat history, partial connector snippets, or stale local copies.
- Required all corrections to be applied and reviewed locally as ordinary Git diffs before connector or REST publication.
- Added remote blob-SHA precondition checks immediately before whole-file overwrites.
- Required connector/API writes to transmit the exact reviewed local bytes and remote verification by comparison with local `git hash-object` values.
- Added explicit fallbacks for whole-file contents APIs and lower-level blob/tree/commit APIs.
- Required failed publication machinery to be removed from the canonical branch and partial remote completion to be reported precisely.

## 0.6.4 — 2026-07-28

Added reference-backed mathematical classification as a prerequisite to public abstraction design.

- Required the assistant to search the local research corpus and appropriate standard references before coining foundational nouns, categories, or method families.
- Made reference use operational: extract the established objects, morphisms, ambient category, variance, universal property, hypotheses, and functorial constructions that constrain the implementation.
- Added a completion test preventing a wrapper from being categorically laundered one abstraction layer upward without reduction to standard arrows, diagrams, refinements, and category constructors.
- Required comparison with Sage and formal-library architecture before declaring a construction absent or inventing a parallel ontology.
- Added contributor checks for source-free reconstruction, categorical laundering, and citation laundering.
- Clarified that local textbooks, papers, notes, and prior project decisions may be the governing sources; external references supplement rather than replace the local corpus.

## 0.6.3 — 2026-07-28

Extended the anti-reinvention guidance to functorial category constructions and diagram objects.

- Required slice, coslice, arrow, comma, functor, action, graded, filtered, equivariant, and similar categories to be generated from the ambient category when the construction is functorial, rather than introduced as independent top-level category families.
- Required public APIs to preserve ownership and variance: construct or refine the ambient category first, then apply its category constructor.
- Added an abstraction-completion check against correctly naming a standard diagram category but reifying it as a bespoke class instead of using Sage's native functorial-construction mechanism.
- Required arrows, spans, cospans, actions, functors, and other diagrams to remain the semantic objects; wrapper parents are backend realizations and must preserve the defining maps and commutative conditions.
- Added contributor checks for construction reification and wrapper substitution.
- Retained ring-extension and relative-scheme examples only as regression witnesses for the general category-construction rule.

## 0.6.2 — 2026-07-28

Generalized the category-refinement guidance into a rule against categorical reinvention.

- Required proposed categories and wrapper hierarchies to be reduced first through existing Sage base categories, registered axioms, joins, slices, construction functors, and standard structured-object categories.
- Distinguished genuinely new structure or morphism data from mere conjunctions of properties.
- Required standard named categories to be aliases of compositionally generated categories when possible, rather than independent ontologies with duplicated methods and refinement paths.
- Added contributor review criteria for detecting category reinvention across algebraic, geometric, topological, graded, equivariant, relative, and finiteness settings.
- Retained specific examples only as regression witnesses for the general anti-reinvention principle.

## 0.6.1 — 2026-07-27

Added local-to-global construction and problem-space reconnaissance discipline.

- Required global scheme, family, cover, action, and quotient operations to be built from general local algebraic primitives rather than implemented top-down through specialized objects.
- Made pushouts and tensor products of explicit rings and algebras the foundational base-change primitive, with affine pullbacks obtained contravariantly by `Spec`.
- Required compatibility with quotient, localization, polynomial, Laurent, and principal-open presentations to be expressed through the same universal tensor-product construction.
- Required globalization by affine-cover descent or relative `Proj`, with family-specific methods delegating to general scheme pullbacks.
- Added a dependency-graph and complexity survey before implementation, including comparison of general foundational repairs against accumulated special-case cost.
- Required proactive searches of Sage source, tickets, external computer-algebra systems, bridges, reference implementations, and mathematical literature.
- Added rules against greedy implementation paths that descend into point-, chart-, overlap-, localization-, and family-specific local minima.
- Added contributor review criteria for reversed dependency implementation, greedy basin descent, and failure to survey the broader solution landscape.

## 0.6.0 — 2026-07-27

Added guidance against changing the mathematical problem to fit a failing Sage backend.

- Required every restriction from a full parameter space to a pencil, principal open, or fiber to be expressed as a named base change with its logical effect on the original theorem.
- Distinguished nonconstant equations from non-isotrivial families and required moduli-level or invariant-level evidence.
- Distinguished exact discriminants and smooth loci from conservative resultant or denominator certificates.
- Required relative schemes and families to be represented by structure morphisms or slice objects rather than attached side metadata such as an ad hoc `as_scheme_over`.
- Added a root-cause rule requiring repair of the earliest broken semantic primitive instead of successive patches to lifts, overlaps, charts, products, and specializations.
- Required overlap morphisms to arise functorially from restriction or localization of covered morphisms.
- Clarified that avoiding bespoke wrappers does not justify avoiding standard mathematical parents such as linear subsystems with ambient inclusions.
- Required affine base change to be implemented from \(R\otimes_A B\) and explicit algebra structure maps rather than coercion experiments.
- Required method and category scope to match the exact backend domain.
- Required final reports to preserve unresolved family-level work when only a pencil or rational fiber has been completed.
- Added contributor guidance for auditing pivot debt while retaining exact certification, source inspection, and diagram verification as positive practices.

## 0.5.1 — 2026-07-27

Added Sage-native category-refinement guidance for installing mathematically uniform capabilities on existing parents.

- Distinguished category-level axiom refinement via `C._with_axiom(A)` from object-level parent refinement via `P._refine_category_(D)`.
- Required object refinement to record an already-true mathematical category membership rather than act as an unchecked cast or method-installation trick.
- Directed uniform methods to Sage category `ParentMethods`, `ElementMethods`, or `SubcategoryMethods`, with installation code limited to routing parents at controlled construction boundaries.
- Preferred the smallest accurate existing Sage category, while allowing new categories only for genuinely missing mathematical structures and uniform method surfaces.
- Added clean-kernel, idempotency, category-join, dynamic-MRO, singleton-side-effect, and `@final` review requirements.
- Clarified when category refinement is preferable to concrete-class monkey-patching and when a targeted native repair, shadow, subclass, backend patch, or proper category hierarchy remains the honest mechanism.
- Added contributor checks preventing `_refine_category_` from being used as a false proof of membership.

## 0.5.0 — 2026-07-27

Reframed the Coble transcript guidance around positive research-mathematics modalities rather than an expanding catalogue of observed failures.

- Added `ANALYSES/COBLE_NOTEBOOK_MATHEMATICAL_THOUGHT_MODALITIES.md`, synthesizing the cumulative logs as one correction trajectory.
- Identified ontological typing, morphism-first reasoning, functoriality, universal-property recognition, level discipline, theorem-mediated proof, natural mathematical generality, coordinate transport, research-ledger exposition, reference recognition, and epistemic discipline as the governing modes of thought.
- Rewrote the opening assistant guidance as a compact set of researcher questions that should prevent the observed failures before API design begins.
- Added explicit distinctions between isomorphism classes and chosen representatives, and between known subobjects or recognized subsets and the full mathematical parents they might otherwise impersonate.
- Clarified that moving a helper onto a Sage class, constructing a `Parent`, or assigning a category does not by itself create a semantic interface.
- Added Sage-specific legibility guidance requiring mathematically meaningful tuple components and coordinate blocks to be named rather than hidden behind positional slices.
- Added contributor guidance requiring editors to extract positive mathematical thought modalities before drafting symptom-level prohibitions.
- Added a dedicated Sage semantic-code discipline covering parent/element ownership, native method auditing, parent-level functorial maps, primary return objects, private backend plumbing, named tuple components, explicit relative bases, notebook/regression separation, and full mathematical display.
- Added contributor review criteria requiring every mathematical modality to be operationalized concretely in Sage without blindly copying mathematically incorrect API proposals from source reports.
- Clarified that the governing workflow starts with a software-independent mathematical formulation and only afterward maps the construction into Sage; incident-specific prohibitions are consequences, not the primary guidance.

## 0.4.1 — 2026-07-27

Deepened the mathematical-precision analysis from representation discipline to explicit relation and proof-burden discipline.

- Added `ANALYSES/COBLE_NOTEBOOK_CHAT_RELATION_DISCIPLINE.md`.
- Required explicit distinctions among equality, isomorphism, canonical or chosen isomorphism, categorical equivalence, realization morphisms, and weaker invariant-level relations.
- Required convenience syntax to route through named stored morphisms and their inverses rather than implicit identifications or coercions.
- Added the Cox-ring case as a governing example: the abstract graded algebra of sections and a polynomial graded algebra are distinct objects connected by a named graded-algebra isomorphism and its degree restrictions.
- Prohibited using matching numerical or structural invariants as unproved proxies for isomorphism, equivalence, classification, or quotient identification.
- Added category-first mathematical naming rules against backend-shaped public nouns such as specialized product classes.
- Required Sage notebooks to function as legible mathematical ledgers of objects, maps, transports, hypotheses, computations, and theorem-derived conclusions.
- Added research-foresight rules requiring the natural mathematical generalization, explicit backend gating, or deliberately private one-off code instead of public single-workflow wrappers.
- Added contributor checks for vague identification language, missing comparison maps, accidental isomorphisms, and proof-burden evasion.

## 0.4.0 — 2026-07-27

Performed a longitudinal analysis of the full Coble-notebook assistant transcript and converted the recurring correction patterns into assistant-facing and contributor-facing guidance.

- Added `ANALYSES/COBLE_NOTEBOOK_CHAT.md`, covering 85 user turns and 84 assistant turns.
- Identified premature abstraction closure, representation capture, epistemic substitution, nounification, functorial blindness, local-global collapse, false canonicity, predicate inflation, artifact detachment, reactive remediation, scope dysregulation, and expository displacement as root cognitive failures.
- Added an abstraction-completion test requiring the assistant to continue beyond the first reusable helper or object-oriented wrapper to the standard parent, functor, diagram, or universal construction.
- Added a precise assertion taxonomy separating precondition gates, capability gates, mathematical postconditions, theorem-backed regressions, representation checks, and prohibited oracle assertions.
- Added invariant-verification requirements for noncanonical orderings, bases, charts, trivializations, coordinate models, and equality-up-to-isomorphism or scalar.
- Added local-to-global, gluing, cocycle, descent, and parameter-space requirements for schemes, covers, quotients, and families.
- Added certificate requirements for partial classification predicates such as ADE, K3, Enriques, and del Pezzo recognizers.
- Added notebook narrative, clean-execution, persisted-state, and downstream dependency-audit requirements.
- Added contributor guidance for analyzing correction trajectories, separating symptoms from causes, retaining positive counterexamples, and testing rule strength against every recurrence.
- Added incidents P-0009 through P-0013 for answer-first computation, one-rung remediation, false canonicity, local-to-global collapse, and persisted-notebook drift.
- Added `ANALYSES/` to the README audience and file-routing map.

## 0.3.3 — 2026-07-27

Corrected the treatment of partial Sage backend coverage.

- Replaced blanket anti-assertion rules with a distinction among mathematical preconditions, implementation preconditions, and research-scope boundaries.
- Required mathematically general semantic interfaces even when executable coverage is limited to special Sage representations.
- Made case routing, assertion gates, and `NotImplementedError` valid mechanisms for honest partial backend coverage.
- Added an implementation escalation ladder: native Sage routing, composition of Sage primitives, established external-system bridges, general reference implementations, and literature algorithms or theorems.
- Required an explicit scope decision based on implementation complexity, integration risk, immediate necessity, and likely reuse.
- Required substantial deferred generalizations to become actionable backlog entries with a concrete route, while supported research computations continue.
- Required unsupported current inputs either to receive the minimum correct extension or to be reported as blocked.
- Corrected P-0002 and P-0007 and added editor/maintainer incident P-0008 for misclassifying assertion-gated coverage as semantic narrowing.

## 0.3.2 — 2026-07-27

Separated the assistant and editor failures exposed by the product-construction correction sequence.

- Expanded P-0002 to record the independent AG-assistant failures: presentation-first reasoning, unsupported Sage claims, incomplete fiber-product data, rhetorical abstraction, speculative backend dispatch, assertion-based scope narrowing, and unevidenced status claims.
- Added forward-facing remediation rules requiring re-analysis of the mathematics and Sage implementation before announcing a revised architecture.
- Made headings and task-status labels subject to the same evidence standard as prose progress claims.
- Added contributor guidance against oscillating between literal incident transcription and destructive one-slogan compression.
- Required multi-defect incident decomposition, role classification for concrete examples, and coverage maps from each source defect to a resulting rule or regression criterion.
- Added editor/maintainer incident P-0007 for overfitted patching followed by underfitted “smallest invariant principle” compression.

## 0.3.1 — 2026-07-27

Clarified audiences, contributor responsibilities, and failure classification.

- Added the standard `CONTRIBUTING.md` entry point for contributor and editor guidance.
- Distinguished instructions to repository editors from instructions intended for the deployed AG assistant.
- Added an explicit README audience map and file-routing table.
- Required every correction to be classified by target actor and failure class before editing.
- Separated AG-assistant incidents from editor/maintainer incidents in `INCIDENTS.md`.
- Added incident P-0006 for misrouting conversation-level editor instructions into the assistant prompt.
- Reduced `MAINTENANCE.md` to repository mechanics and delegated editorial judgment to `CONTRIBUTING.md`.
- Made explicit that only `STYLE_GUIDE.md` is intended for upload as operational custom-GPT guidance.

## 0.3.0 — 2026-07-27

Restructured the repository by audience.

- Replaced the self-referential assistant prompt with an assistant-facing algebraic-geometry and Sage behavioral guide.
- Moved storage, version-control, deployment, and update procedure to `MAINTENANCE.md`.
- Moved source failures, provenance, and regression criteria to `INCIDENTS.md`.
- Added explicit mathematical-thinking rules against engineering-first API design.
- Added Sage-specific guidance for ambient parent structures, divisor and Picard data, group actions and linearizations, morphisms and graph constructions, linear systems, local singularity theory, double covers, backend audits, partial operations, and evidence-sensitive reporting.
- Recorded incident P-0004 for the notebook-interface report and incident P-0005 for placing repository-maintenance prose in the assistant prompt.

## 0.2.1 — 2026-07-27

- Preferred direct commits to the default branch when authorized and sufficient.
- Prohibited unrequested branch and pull-request ceremony.
- Added criteria for workflows that genuinely require review or isolation.

## 0.2.0 — 2026-07-27

- Required complete diagrams and ambient categories for universal constructions.
- Prohibited treating a finite backend list as mathematical generality.
- Required remediation to eliminate the original structural defect.
- Prohibited assertion gates that exclude required functionality.

## 0.1.1 — 2026-07-27

- Established repository-backed canonical storage.
- Prohibited chat or model memory as canonical storage.
- Required committed updates before preservation claims.

## 0.1.0 — 2026-07-27

- Created the initial behavioral guide.
