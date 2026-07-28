# Contributing

This document is for human and agent contributors who edit this repository. It is not part of the prompt uploaded to the Algebraic Geometry Research Assistant.

## Repository audiences

The repository serves two primary audiences:

1. **The Algebraic Geometry Research Assistant.** It consumes `STYLE_GUIDE.md` as forward-facing operational guidance for mathematical reasoning, Sage computation, implementation, and reporting.
2. **Repository contributors and maintainers.** They consume `CONTRIBUTING.md`, `MAINTENANCE.md`, `INCIDENTS.md`, `CHANGELOG.md`, and `README.md` to decide how to extract, write, review, preserve, and deploy guidance.

Do not mix these audiences. Instructions about editing, version control, prompt maintenance, provenance, changelogs, or repository workflow belong in contributor-facing documentation, not in `STYLE_GUIDE.md`.

## Classify the input before editing

Every proposed correction must first be classified by both **target audience** and **failure class**.

### Target audience

Ask which actor the instruction governs:

- **AG-assistant instruction:** changes how the deployed assistant should reason, compute, implement, verify, or report.
- **Contributor instruction:** changes how editors should analyze incidents, formulate rules, maintain files, review diffs, or manage the repository.
- **Both:** requires separate wording in separate files. Do not write one hybrid clause.

The fact that an instruction was addressed to the current editing agent does not make it an AG-assistant instruction. Conversation-level directions such as “commit directly to main,” “do not store this in memory,” or “generalize beyond the literal incident” govern contributors unless they independently imply a forward-facing behavior for the deployed AG assistant.

### Failure class

Distinguish at least:

- **AG-assistant failures:** mathematical or computational defects in the deployed assistant, such as failing to define ambient objects, replacing intrinsic constructions with coordinates, inventing unsupported Sage APIs, reporting mental derivations as executed computations, or narrowing a general task to an easy presentation.
- **Editor/maintainer failures:** defects in producing or maintaining the guide, such as vague rules, reactive incident patching, destructive consolidation, audience confusion, overfitting to one example, loss of concrete algebraic geometry or Sage content, or placing repository process in the assistant prompt.

Record these classes explicitly in incident documentation. Do not infer that a maintainer failure should be copied into the assistant prompt.

## File routing

Use the following routing rules:

- `STYLE_GUIDE.md`: only instructions that the AG assistant should directly follow while doing algebraic geometry or Sage work.
- `CONTRIBUTING.md`: editorial principles, audience classification, rule extraction, writing standards, and review criteria for contributors.
- `MAINTENANCE.md`: mechanical repository operations, version control, deployment, and canonical-storage procedure.
- `INCIDENTS.md`: source failures, classified by actor, with regression evidence and mappings to resulting rules.
- `CHANGELOG.md`: concise revision history.
- `README.md`: repository orientation, audience map, and file map.

Only `STYLE_GUIDE.md` should be uploaded as operational guidance to the custom GPT unless deployment documentation explicitly states otherwise.

## Writing assistant-facing rules

Assistant-facing rules must be:

- forward-facing and imperative;
- mathematically substantive;
- usable without knowing the originating conversation;
- specific enough to alter future behavior;
- general enough to cover nearby algebraic-geometric and Sage cases;
- grounded by examples only when the examples sharpen the rule.

Do not include:

- incident chronology;
- admissions, apologies, or explanations of previous mistakes;
- repository-management instructions;
- changelog language;
- claims about canonical files or prompt deployment;
- editor-facing advice about how to formulate rules.

Examples in `STYLE_GUIDE.md` are regression anchors, not provenance narratives. State what the assistant must do, not how the rule was discovered.

## Extract mathematical thought modalities before symptom rules

The primary editorial question is not “which observed behavior should be banned?” It is “which ordinary research-mathematical habit would have prevented the error before it appeared?”

For each correction trajectory, identify the positive mode of thought first. Do not begin by enumerating bad method names or procedural mistakes. Reconstruct how a careful researcher would have approached the mathematics before any code existed, and make that order of thought the governing rule.

Typical modalities include:

- ontological typing: determine what the object is and where it lives;
- morphism-first reasoning: name the comparison maps rather than identifying objects informally;
- functorial reasoning: construct parent-level induced maps before element-level convenience syntax;
- universal-property recognition: identify limits, colimits, relative spectra, quotients, projectivizations, and descent constructions before writing equations;
- level discipline: distinguish object and presentation, class and representative, local and global, absolute and relative, affine and projective, family and fiber;
- theorem-mediated proof: establish the exact hypotheses and proof obligation rather than substituting matching invariants;
- natural mathematical generality: expose the standard construction and treat supported Sage presentations as backends;
- research-ledger exposition: make objects, named maps, choices, computations, and deductions legible in the notebook.

Then derive operational rules and regression checks from that modality. A specific prohibition is justified when it is needed to make the modality executable in Sage, but it must not replace the modality.

Use the following review test:

1. Could the rule guide the assistant on a nearby problem whose method names and varieties are different?
2. Would a careful mathematician naturally derive the source correction by following the rule?
3. Does the rule teach what to construct or ask, rather than merely list what not to write?
4. Are concrete examples retained as consequences or regression cases rather than treated as the governing ontology?
5. Could the assistant obey the wording while continuing to think in backend classes, coordinate containers, or numerical proxies? If so, the rule is too superficial.

For example, “do not expose `factor_blocks()`” is too narrow. The governing modality is that a product's factors are mathematical objects and coordinate blocking is derived private bookkeeping. Likewise, “unpack this tuple” is a style consequence of naming the components of a morphism, not an independent theory of tuple syntax.

## Extracting rules from incidents

Do not reflexively append a literal prohibition for every noun or phrase appearing in an incident.

For each incident:

1. reconstruct the intended mathematical or operational task;
2. identify the actor that failed;
3. identify the underlying cognitive or process defect;
4. determine the likely neighboring tasks in which the same defect would recur;
5. formulate the smallest set of rules that blocks that failure class without erasing important concrete constraints;
6. retain Sage-specific or algebraic-geometric examples when they materially improve future behavior;
7. store detailed chronology and regression criteria in `INCIDENTS.md`, not in the assistant prompt.

Avoid both extremes:

- **incident overfitting:** encoding a catalogue of named examples instead of the governing failure mode;
- **destructive abstraction:** replacing operational mathematical constraints with slogans such as “be rigorous” or “think mathematically.”

A valid generalization must still prevent the source incident and nearby variants.

## Decompose incidents before generalizing

A single incident may expose several causally independent defects. Do not assume that every correction has one “smallest invariant principle,” or that the best edit is the shortest possible sentence. The goal is the smallest **sufficient** rule set: every material failure must be blocked without duplicating rules that truly have the same cause.

Analyze at least the following dimensions when they are present:

- the mathematical-semantic defect;
- the Sage representation, API, or source-audit defect;
- the implementation-coverage defect;
- the computation, evidence, or status-reporting defect;
- the defect in the assistant’s response to correction;
- the editor’s own extraction, drafting, or preservation defect.

Combine dimensions only when one operational rule genuinely prevents all of them. Do not erase a separate requirement merely because the failures occurred in the same paragraph.

Avoid oscillating between two invalid editing modes:

1. **incident transcription:** copying every named variety, backend, phrase, or counterexample into the standing guide;
2. **slogan compression:** reacting to that overfit by replacing all concrete requirements with one broad principle.

Concrete examples can have different roles:

- a **scope witness** showing that the intended domain is broader than the implementation;
- a **regression case** against which a rule must be tested;
- evidence that reveals an underlying cognitive defect;
- an incidental detail that need not appear in the assistant-facing guide.

Classify each example by its role. Do not automatically preserve every example as a rule, and do not automatically discard every example after stating an abstraction.

Before claiming that an incident has been incorporated, maintain a coverage map from each material source failure to at least one resulting clause or regression criterion. The edit underfits when any original defect could recur while all new wording is technically obeyed.

## Preserve semantic generality without forcing total implementation

Do not encode a blanket prohibition on assertion gates, case dispatch, `NotImplementedError`, or other explicit implementation boundaries. These mechanisms are often required to keep a mathematically general interface while Sage only computes special cases.

When an incident concerns limited computational coverage, require the assistant-facing rule to distinguish:

1. the most general mathematical object or construction to which the operation applies;
2. the special cases Sage already handles and can route directly;
3. whether existing Sage primitives compose into the general case with modest effort;
4. whether an established bridge to GAP, Singular, Macaulay2, Magma, Julia, PARI/GP, or another system already supplies the missing primitive or algorithm;
5. whether a general reference implementation can be followed or reproduced without substantial new design;
6. whether a paper, book, or citable theorem gives a direct algorithm or reduction;
7. whether implementing that route now is proportionate to the active research task and likely reuse.

The resulting guide should favor a principled escalation ladder:

- route verified native Sage cases first;
- compose existing Sage primitives when the generalization is short and reusable;
- use a clean existing bridge when it already owns the needed mathematics;
- adapt a reliable reference implementation when integration is straightforward;
- implement a literature algorithm when the translation is sufficiently bounded and valuable;
- otherwise preserve the general interface, gate unsupported backends explicitly, and record a backlog item with a concrete implementation strategy.

Do not label the last option as degradation or task narrowing. The semantic domain remains general; only current executable coverage is partial. Conversely, do not let a general method name conceal that the current input is unsupported.

Editors must preserve the research-scope judgment. A short, reusable foundational extension is often worth implementing immediately. A substantial backend project that is not needed for the present supported computation should not derail the research conversation; it should become an actionable backlog entry. If the current computation itself requires the unsupported branch, the assistant must either implement the minimum correct extension or report the block.

## Preserve mathematics and Sage specificity

This repository is not a generic software-engineering style guide. Contributor edits must preserve the fact that the assistant performs algebraic geometry research and detailed Sage computations.

When editing rules:

- prefer standard mathematical objects, morphisms, functors, diagrams, hypotheses, and universal properties;
- retain Sage parent/element ownership, existing API behavior, source inspection, execution, and backend constraints where operationally important;
- do not replace concrete algebraic-geometric guidance with generic object-oriented design language;
- do not invent terminology when standard mathematical language exists;
- verify nontrivial mathematical corrections before encoding them as standing guidance.


## Require concrete Sage operationalization

Positive mathematical modalities must be translated into concrete Sage-facing guidance whenever the incident concerns code. Do not use “think semantically” as a reason to omit specific operational rules.

For each Sage-related correction, review at least:

1. **Parent and element ownership:** Does the code construct or reuse the correct Sage parent, or does it manipulate an untyped proxy?
2. **Native architecture:** Were Sage categories, parents, elements, morphisms, existing methods, and source inspected before adding an abstraction?
3. **Functorial ownership:** Is an element-level operation actually induced by a parent-level map, action, linearization, restriction, or base change?
4. **Primary return object:** Does the interface return the morphism, diagram, scheme, local ring, linear system, or cover rather than only equations, matrices, or tuples?
5. **Compositional redundancy:** Is a proposed public method already recovered from domain, codomain, factors, image, inverse, projections, or ordinary composition?
6. **Public versus private data:** Have coordinate blocks, ring flattening, saturation, dispatch predicates, positional indexes, duplicate coordinate rings, and alias shadowing remained out of the public research interface?
7. **Naming and legibility:** Are mathematically meaningful tuple components, maps, and generators explicitly named in the research notebook?
8. **Relative structure:** Are base morphisms, open immersions, overlaps, and descent data explicit rather than stored as side metadata or inferred by coercion?
9. **Partial-parent honesty:** Does a Sage `Parent`, predicate, or method name claim exactly the mathematical object and domain actually implemented?
10. **Narrative separation:** Are proof obligations visible in research cells while API self-tests remain in framework regressions?

The report or incident may itself propose incorrect APIs. Contributors must retain its valid Sage-style evidence while correcting claims such as `H^0(X,L)` being an algebra, every point having a local equation or total ADE classifier, every divisor determining a double cover, or every method receiver being the mathematically correct owner.

A useful assistant-facing rule should normally pair:

- the governing mathematical modality;
- the concrete Sage behavior it requires;
- one or more regression examples demonstrating that the rule excludes the original failure.

## Audit category generation before category invention

When a transcript proposes a new category, named subcategory, wrapper parent, or hierarchy of specialized classes, first ask whether the proposal merely redescribes a category already generated by Sage's existing constructions.

Review in this order:

1. Identify the nearest existing base category.
2. Inspect the registered axiom refinements available on it and its super-categories.
3. Determine whether the proposed category is a composition of existing axioms, a join or intersection, a slice or coslice, an arrow or action category, a graded or filtered construction, or another standard category constructor.
4. Determine whether that constructor is itself a functorial operation on the ambient category and whether Sage already exposes the corresponding construction method.
5. Check that the proposed API preserves ownership and variance: the ambient category should generate the derived category, and refinements should compose before or after the construction according to the mathematics.
6. Determine whether a standard named category should be only an alias for that generated object.
7. Identify any genuinely additional object data, structure morphisms, or morphism compatibility that remain after this reduction.
8. Introduce a new primitive category only for that irreducible additional structure.

Flag **category reinvention** when the editor or assistant creates separate categories for conjunctions of properties, duplicates an existing axiom hierarchy, or implements methods independently on several named classes that Sage's category composition would already unify.

Flag **construction reification** when the assistant correctly names a slice, coslice, arrow, comma, action, functor, or related category but then implements it as an independent top-level family instead of applying a standard construction to the ambient category. This is premature abstraction closure at the category-constructor level.

Flag **wrapper substitution** when an arrow or diagram is the mathematical object but a backend wrapper is promoted to the definition. The review must recover the actual diagram, its ambient category, its structure maps, and its commuting conditions, and then classify the wrapper only as a Sage realization or adapter.

Do not overfit the rule to one algebraic or geometric example. The same audit applies to finite, smooth, proper, graded, equivariant, relative, presented, connected, or otherwise refined objects throughout Sage. Concrete examples are regression witnesses for the general construction principle.

A valid new category should answer: what data or morphisms does an object possess that cannot be recovered by applying existing category constructors and axioms? If the answer is only a list of properties, the proposal is ordinarily a refinement, not a new primitive.

## Require reference-backed mathematical classification

Do not accept an abstraction merely because the assistant has moved the current wrapper into a category or supplied more mathematical-sounding terminology. Before a new foundational noun, category, or method family enters the guide, require evidence that the underlying mathematics has been classified against standard sources.

Review whether the assistant:

1. searched the local source corpus supplied for the research task, including textbooks, papers, notes, and prior project decisions;
2. consulted appropriate standard references and formal or computational libraries, such as the Stacks Project, Kerodon, official Sage or Mathlib documentation and source, established papers, and broad reference works for orientation;
3. extracted the actual objects, morphisms, ambient category, variance, universal property, hypotheses, and standard constructors rather than only a familiar phrase;
4. compared that classification with Sage's existing category and construction architecture;
5. discarded any wrapper-derived noun that sources reveal to be an ordinary arrow, diagram, refinement, functorial construction, or universal object;
6. documented disagreements or variant conventions precisely instead of silently choosing the wording nearest the implementation;
7. used citations as constraints on ontology and proof obligations, not as retrospective decoration.

Flag **source-free reconstruction** when the assistant tries to rediscover standard mathematics solely from the shape of current code or Sage failures. Flag **categorical laundering** when it preserves a bespoke engineering object by placing it in a newly coined category without first reducing it to standard objects, arrows, diagrams, and category constructors. Flag **citation laundering** when references are added after the design but do not determine or correct the mathematical interface.

The relevant source need not always be external. A project may provide the governing definition in its local corpus. The requirement is that the abstraction be grounded in the best available mathematical source before it becomes public architecture. Concrete algebraic, geometric, or topological examples remain regression witnesses for this general rule.

## Review Sage category refinement and dynamic method installation

When a correction proposes Sage category refinement, do not reduce the review to whether the new method becomes callable. Verify the mathematical assertion encoded by the refinement.

Distinguish explicitly:

- category-level axiom refinement, such as `C._with_axiom(A)`, which constructs or retrieves a more specific category;
- object-level parent refinement, such as `P._refine_category_(D)`, which records that an existing parent already belongs to `D` and changes its dynamic method resolution.

A contributor review must answer:

1. What mathematical property places `P` in `D`, and where is that property established?
2. Is `D` the smallest accurate existing Sage category, or has a redundant custom category been invented?
3. Are the methods uniform for every object of `D`, so that `ParentMethods` or `ElementMethods` is the correct owner?
4. Is the refinement performed at the correct construction boundary: a controlled singleton installation, a native-constructor interceptor, or immediately before returning a newly constructed parent?
5. Does the interceptor call the native implementation first and refine the result rather than replacing Sage arithmetic?
6. Does the category join preserve the object's previous memberships and produce a coherent dynamic MRO?
7. Is repeated installation safe under `%run`, module reload, and clean-kernel execution?
8. Does any `@final` method reflect a genuine semantic non-overridability requirement?
9. Are global mutations of cached Sage parents documented and isolated?
10. Would a class-specific repair, proper new category hierarchy, subclass, or shadow be more honest than object refinement?

Reject `_refine_category_` when it is being used as an unchecked cast or as a device for smuggling unrelated helper methods onto an object. Conversely, reject concrete-class monkey patches when the method is genuinely categorical and Sage's category mixins provide the compositional owner.

The review should preserve the distinction between **declaring a true category membership** and **proving the mathematics that makes the declaration true**. Dynamic dispatch supplies methods; it does not discharge the proof obligation.


## Audit local-to-global dependency direction and problem-space reconnaissance

When a transcript starts with a family, cover, quotient, or covered scheme and then accumulates chartwise backend patches, reconstruct the dependency graph before drafting guidance.

The review must identify:

1. the requested global construction;
2. the affine-local geometric construction;
3. the universal algebraic primitive, such as a tensor product or pushout;
4. the theorem that converts the local primitive into the global object;
5. the first layer at which Sage lacks correct semantics;
6. whether later patches merely compensate for that earlier loss;
7. whether a general local repair would eliminate several specialized patches;
8. whether Sage, another computer-algebra system, a reference implementation, or the literature already supplies the primitive;
9. the estimated complexity and reuse of at least two implementation paths;
10. the exact scope decision: implement now, dispatch and gate, bridge externally, or backlog with a concrete route.

Flag **reversed dependency implementation** when the assistant adds base change to a specialized family before establishing pullbacks for rings, algebras, affine schemes, or general schemes. Flag **greedy basin descent** when each backend failure produces a narrower parent or helper and the cumulative route is not compared against a more general foundational repair.

Do not demand maximal generality regardless of cost. Require a bird's-eye comparison. A slightly larger local-algebra or affine-scheme implementation is preferred when it is mathematically standard, bounded, and causes the requested global operations to specialize automatically. A major foundational project may still be deferred, but only after the existing Sage, bridge, reference-code, and literature routes have been surveyed.

A valid assistant-facing correction should teach the upward construction order:

\[
\text{rings/algebras}
\longrightarrow
\text{affine schemes}
\longrightarrow
\text{covered or projective schemes}
\longrightarrow
\text{families, covers, actions, and quotients}.
\]

The review should also preserve the useful evidence from a restricted global experiment. A pencil or fiber can remain a regression input, but it must no longer own the general implementation.

## Audit mathematical pivots under computational pressure

When a transcript changes the parameter space, family, or categorical level after a backend failure, reconstruct a diagram of the pivots rather than treating each workaround as independent progress.

For every pivot, record:

1. the original object, morphism, locus, or theorem sought;
2. the new base or restricted object and the morphism into the original base;
3. whether the new result implies the original claim, proves a weaker lemma, supplies a witness, or changes the problem;
4. the exact Sage defect that forced the pivot;
5. the earliest semantic primitive that lost the required structure;
6. whether the assistant repaired that primitive or merely routed around it.

Flag the following recurring substitutions:

- full parameter space to a pencil without recording the pullback square;
- relative family to one rational fiber;
- nonconstant equations to non-isotriviality;
- a sufficient resultant or denominator certificate to the exact discriminant;
- a structure morphism to side metadata on an absolute scheme;
- a general covered morphism to coordinate formulas for one involution;
- a missing standard parent to misuse of an existing but semantically different parent;
- affine tensor-product base change to trial-and-error coercion or ring-extension calls.

The review must identify **pivot debt**: original proof obligations that remain open after a useful restricted computation succeeds. A final response underfits when the assistant can technically obey every status label while leaving the user with a fiber or example in place of the requested family or locus.

Also preserve positive evidence. It is good when the assistant:

- distinguishes a backend exception from a geometric conclusion;
- rejects probabilistic output when exact certification is required;
- constructs parameter morphisms by exact linear algebra rather than hard-coded positions;
- verifies commutative squares, cocycles, and involutivity;
- states backend limits precisely.

The editor's task is to retain these practices while preventing them from legitimizing a change of theorem.

## Audit backend friction as a signal for mathematical reformulation

When a transcript becomes preoccupied with compensating for one Sage limitation, do not assume that the only issue is a missing method or defective comparison routine. Audit whether the limitation exposes a more principled mathematical formulation that would make the desired semantics first-class and remove much of the repair work.

Require the analysis to distinguish:

1. the original mathematical object, relation, and theorem;
2. the exact Sage limitation and the presentations in which it appears;
3. whether Sage is deficient relative to the correct mathematical notion;
4. whether the chosen notion is itself unnecessarily strict, coordinate-bound, representative-dependent, or at the wrong categorical level;
5. the standard alternative formulations found in the local corpus and appropriate references;
6. the explicit comparison map, equivalence, universal property, or strictification result relating those formulations;
7. whether the reformulation preserves the original theorem rather than silently changing the target;
8. whether it eliminates a family of local patches and yields a more reusable semantic interface;
9. the genuine backend work that remains after the mathematical reformulation.

Flag **backend fixation** when the assistant assumes that every Sage difficulty must be solved by implementing the exact missing operation in the current representation. Flag **semantic foreclosure** when it does not search for a standard intrinsic formulation before extending a repair chain. Flag **theory laundering** when it invokes higher, derived, homotopical, or other modern language without an explicit comparison to the original claim or without reducing the implementation burden.

Equality of composites is a regression example, not the governing rule. Repeated normalization may reveal that the mathematics requires a comparison 2-cell or transport along an isomorphism; it may also reveal only that Sage fails to prove a genuine strict equality. The contributor must determine which conclusion follows from the mathematics.

A valid assistant-facing rule should teach a self-nudge: after several repairs around one backend deficiency, pause and ask whether a standard mathematical reformulation would both improve semantic fidelity and obviate the deficient operation. Preserve the useful parts of the original implementation only after that audit.

## Review checklist

Before committing a change, verify:

1. The intended audience of every changed paragraph is explicit.
2. No contributor instruction was placed in `STYLE_GUIDE.md`.
3. No substantive AG-assistant behavior exists only in contributor documentation.
4. The resulting assistant rule is forward-facing and independent of incident chronology.
5. The rule addresses the underlying failure class, not only the literal example.
6. Concrete mathematical and Sage constraints were not abstracted away.
7. Existing valid guidance was not weakened, contradicted, or silently removed.
8. Examples clarify behavior rather than dominate the rule.
9. Incident records identify whether the failure belongs to the AG assistant or to editors/maintainers.
10. Only files appropriate to the correction were changed.
11. Every independent source defect maps to a resulting rule or regression criterion.
12. The edit avoids both incident transcription and slogan compression.
13. Any claim that the correction is complete follows a coverage audit rather than verbal agreement.
14. Semantic scope and implemented Sage coverage are distinguished explicitly.
15. Assertion gates preserve a general interface rather than masquerading as mathematical nonexistence.
16. The native-Sage, bridge, reference-implementation, and literature routes were considered before substantial new backend work was deferred.
17. A deferred generalization has an actionable strategy, not a vague TODO.

<!-- BEGIN GENERATED: publication-workflow -->
## Single-command publication workflow

Do not choose a publication mechanism interactively after the edit is finished. Use the repository tooling to make the decision deterministic.

The standard local sequence is:

```bash
make build
make check
git add -A
git commit -m "<reviewed change>"
make publish-plan BASE=<reviewed-upstream-commit>
```

`make publish-plan` writes `.publication/manifest.json`. The manifest records the base and local commits, every changed path, the expected old blob SHA, the exact new `git hash-object` value, file mode and size, whether the path is generated, and the connector verification steps. It is the handoff artifact for connector-backed publication.

When `GITHUB_TOKEN` is available, publish the reviewed tree atomically through GitHub's Git Data API:

```bash
GITHUB_TOKEN=... make publish-api BASE=<expected-current-remote-commit>
```

`scripts/publish.py` refuses to publish a dirty worktree, refuses a moved remote base, creates blobs from the exact committed local bytes, verifies every returned blob SHA, creates one tree and commit, updates the branch without force, and verifies the resulting remote tree.

Use this fixed decision order:

1. Use ordinary `git push` when authenticated Git transport works.
2. Otherwise use `scripts/publish.py publish` when a GitHub token is available.
3. Otherwise use the connector with `.publication/manifest.json`: update only the changed canonical files with current-SHA preconditions and verify the returned blob identities. Publish source fragments before generated artifacts and allow the repository workflow to rebuild generated files.
4. Stop and report the exact missing transport capability if none of these routes is available.

Do not create temporary workflows, trigger files, transport pull requests, patch-chunk branches, or competing publication mechanisms merely because one API call failed. Those mechanisms require an explicit repository-level need and review; they are not the default fallback.
<!-- END GENERATED: publication-workflow -->

## Generated style-guide workflow

`STYLE_GUIDE.parts/` is the canonical editable source for the deployed guide. `STYLE_GUIDE.md` is the committed generated artifact uploaded to the custom GPT. Do not edit the generated file as the primary source.

The fragments are ordered by their two-digit filename prefixes and concatenated byte-for-byte by:

```bash
python scripts/build_style_guide.py
```

Before committing a style-guide change:

1. edit the smallest relevant fragment or fragments;
2. run `python scripts/build_style_guide.py`;
3. run `python scripts/build_style_guide.py --check`;
4. review both the fragment diff and the generated `STYLE_GUIDE.md` diff;
5. commit the fragments and generated artifact together.

The `Build style guide` workflow verifies the committed artifact on pull requests. On `main`, it rebuilds and commits `STYLE_GUIDE.md` when the source fragments are newer. An hourly scheduled run is a fallback for connector- or API-authored fragment updates that do not emit ordinary push-triggered workflow events.

When direct Git push access is unavailable, publish only the changed small fragments, build script, workflow, or contributor documents through the connector/API using current blob-SHA preconditions. Do not reconstruct or overwrite the monolithic generated guide from memory. Either publish the locally generated artifact exactly through a whole-file API call and verify its blob hash, or allow the workflow to assemble it from the committed fragments.

## Contributions and repository workflow

Follow `MAINTENANCE.md` for canonical storage, commits, branch policy, deployment, and preservation checks.

### Update the repository when direct Git publication is unavailable

Lack of Git push access does not justify editing from remembered content, partial excerpts, or chat history. Preserve the ordinary local-diff workflow and change only the publication transport.

Use this order:

1. **Materialize the exact current baseline.**
   - Prefer an ordinary clone or fetch of the repository, even when the checkout is read-only or no push credentials are available.
   - Record the upstream branch and commit SHA before editing.
   - If network Git transport is unavailable, use the connected repository API to fetch the exact current files or blobs needed for the edit. Fetch complete file contents, not only surrounding line ranges.
   - If several files or repository-wide checks matter, reconstruct a local checkout from connector-fetched contents and record the upstream commit from which it was reconstructed.

2. **Apply the correction locally as a diff.**
   - Write the fetched bytes to the local checkout without paraphrasing or reconstruction.
   - Apply a narrow patch to those files using normal editing or patch tools.
   - Inspect `git diff`, run `git diff --check`, run relevant tests or preservation checks, and commit the reviewed local state.
   - Compute `git hash-object <file>` for every file that will be published.

3. **Recheck the remote precondition immediately before writing.**
   - Fetch the current remote blob SHA for every target file.
   - Confirm that it still matches the baseline used by the local patch. If it changed, fetch the new file, rebase or reapply the local diff, and review again.
   - Never overwrite a changed remote file with the older local version merely because the intended edit is small.

4. **Publish the exact local files through the available API.**
   - When a connector provides whole-file replacement, send the complete reviewed local file and the current remote blob SHA to the update action.
   - When a lower-level Git data API is available, create blobs from the exact local bytes, assemble a tree against the verified base tree, create a commit, and update the branch ref.
   - Use connector or REST operations as the transport for the locally reviewed Git state; do not redraft the file inside the API call.
   - Perform sequential writes when the API requires one file per commit. Do not run concurrent updates against the same path.

5. **Verify publication by content, not by a success message.**
   - Compare every returned or refetched GitHub blob SHA with the corresponding local `git hash-object` value.
   - Refetch the changed files and inspect the changed sections.
   - Compare the remote base and final commits and confirm that only the intended files changed.
   - Report the actual remote commit sequence when a contents API necessarily created several commits; do not claim that it reproduced one local commit atomically.

6. **Leave the repository clean when publication fails.**
   - Remove or reset temporary workflows, trigger files, transport branches, patch chunks, and other publication machinery from the canonical branch.
   - Preserve the reviewed local commit and exportable patch so the work remains reproducible.
   - State precisely which files were updated remotely and which remain local.

Prohibited shortcuts include:

- composing a replacement file from memory, prior assistant messages, or partial search snippets;
- using a short `fetch_file` line range as though it were the complete source file;
- overwriting a whole remote file without an expected current blob SHA;
- claiming local and remote equality without comparing Git blob hashes;
- treating a connector's successful response as proof that the complete payload was stored;
- leaving temporary transport artifacts on the default branch after a failed publication attempt.

The invariant is: **the API publishes an already reviewed local repository state; it does not become the editing environment or the source of reconstructed file contents.**

## Analyze correction trajectories

For long transcripts, do not treat each user correction as an independent incident. Build a correction trajectory.

For each recurring topic:

1. record the assistant's initial abstraction level;
2. record each user correction;
3. record the assistant's attempted remediation;
4. determine whether the remediation removed the root defect or merely moved it one layer;
5. identify the first point at which the standard mathematical construction was reached;
6. identify stale downstream code or prose left by earlier rungs.

A repeated sequence of coordinate code, helper function, utility namespace, object method, parent method, and ambient-category construction is evidence of **premature abstraction closure**. Contributor guidance should require the assistant to complete the abstraction chain, not merely move one rung upward after each objection.

Analyze the whole trajectory before drafting a rule. The final assistant response may be correct while concealing a long-lived failure mode that will recur elsewhere.

## Distinguish surface symptoms from causal failures

A source complaint can name a symptom without naming the cause.

Examples:

- “This looks hard-coded” may indicate answer-first computation, representation capture, or failure to use a universal construction.
- “This API is not semantic” may indicate missing parents, functoriality, variance, compositionality, or local-to-global data.
- “The notebook is hard to follow” may indicate theory left in chat, monolithic cells, missing intermediate objects, or tests mixed into narrative.
- “The assertion is overfit” may indicate false canonicity rather than a general objection to assertions.
- “Sage should know this” may require a source audit, a native patch, a correct shadow, or a bridge rather than a new wrapper.

For every proposed rule, state the causal failure it prevents. Reject rules that merely prohibit the vocabulary of the source complaint.

## Preserve positive and negative evidence

Incident analysis should record not only failures but also turns where the assistant correctly resisted or corrected the user.

Positive examples are especially valuable when they demonstrate:

- testing a user conjecture rather than agreeing;
- producing a counterexample;
- distinguishing a theorem deduction from a computation;
- identifying a descent or gluing obstruction;
- correcting variance or functoriality;
- refusing to claim a global object from local data.

Use positive examples as regression anchors for desired behavior. Do not write guidance that would punish the assistant for correctly challenging the user.

## Audit rule strength against recurrence

Before committing an assistant-facing rule, test it against every recurrence of the failure in the source transcript.

A rule is too weak when the assistant could obey it while still:

- hard-coding the expected answer;
- stopping at a reusable but nonstandard wrapper;
- promoting local data to a global object;
- asserting representation-sensitive equality;
- leaving theory outside the artifact;
- failing to propagate a corrected primitive downstream.

A rule is too broad when it prohibits valid capability gates, useful coordinate specializations, requested full output, or theorem-backed deductions.

Record the result of this strength audit in the analysis or incident record.

## Treat artifact-state failures as substantive incidents

Notebook corruption, stale cells, wrong kernels, duplicate imports, nonpersisted edits, and prose/code contradiction are not merely operational inconveniences. They invalidate mathematical and computational claims.

When a transcript contains an outage or state discontinuity, contributors must inspect whether the assistant:

- relied on live-kernel state;
- reopened the persisted artifact;
- verified the kernel and dependency graph;
- performed a clean execution;
- audited stale narrative and duplicate cells;
- rechecked downstream conclusions.

Add assistant-facing artifact-discipline rules and regression criteria when these obligations were missed.


## Require relation-level mathematical precision

Contributor prose must not use vague words such as “model,” “identify,” “corresponds,” “regard as,” “represented by,” or “the same as” where the underlying mathematics supplies a more precise relation.

For every such statement, determine whether it means:

- literal equality;
- equality in a parent or Hom-set;
- a specified isomorphism;
- a canonical or natural isomorphism;
- a chosen coordinate-dependent isomorphism;
- an equivalence of categories;
- a realization or presentation morphism;
- equality only after applying a forgetful functor;
- agreement of invariants;
- a weaker birational, formal, analytic, derived, or numerical relation.

Write the actual relation and, when it is morphic, name its source, target, category, map, inverse, and hypotheses. Do not editorially compress an isomorphism into equality or a realization into an “identification.”

When assistant-facing sugar is proposed, require a routing audit: identify the stored morphism that the sugar applies, verify its inverse or component restriction, and ensure that no implicit coercion creates a second untracked identification.

## Audit proof burden and forbidden proxies

When a transcript claims an isomorphism, equivalence, classification, or quotient identification, contributors must list the actual proof obligation and the evidence supplied.

Flag the correction when the assistant substitutes:

- equal dimensions for an isomorphism;
- matching invariants for a classification;
- a numerical coincidence for equality of objects;
- a polynomial expression for a section;
- a tuple for a point;
- equations on one chart for a global scheme;
- an isomorphic underlying object for an object with its grading, action, base, topology, or other structure;
- a familiar accidental isomorphism for the defining construction.

A standing rule is insufficient if the assistant can obey it while continuing to omit the actual comparison map.

## Audit mathematical maturity and research foresight

Contributor review should ask whether the proposed code reflects the maturity expected of a research mathematician.

Check that the assistant:

1. consults standard mathematical references before inventing terminology;
2. determines where objects live before manipulating presentations;
3. names comparison maps rather than relying on hand-waved identifications;
4. preserves categorical structure, grading, base, action, and variance;
5. distinguishes necessary proof from convenient numerical evidence;
6. identifies the natural mathematical generality of the construction;
7. avoids public wrappers specialized to one notebook example;
8. writes the research notebook as a legible mathematical ledger rather than generic application software.

A public name such as `ProductOfProjectiveSpaces` should trigger review: is this genuinely a mathematical object needed by users, or merely an implementation class for one backend of the ordinary product of schemes?

## Additional review checks

Before committing relation- or representation-related guidance, verify:

18. Every claimed identification is classified as equality, isomorphism, equivalence, realization, or a weaker relation.
19. Every nontrivial isomorphism has a named morphism, category, inverse or theorem, and required structure.
20. No matching list of invariants is used as an unproved proxy for an isomorphism or classification.
21. Convenience syntax routes through explicit stored mathematical maps.
22. Backend class names do not determine the public mathematical ontology.
23. The proposed abstraction reaches the natural mathematical generality or remains explicitly private and one-off.
24. The visible code reads as a ledger of objects, maps, hypotheses, computations, and deductions.
