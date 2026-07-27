# Incident and Regression Record

This document is for contributors, editors, and reviewers. It preserves source failures, classifies the actor that failed, and records regression evidence. It is not part of the prompt consumed by the Algebraic Geometry Research Assistant.

## Classification

Every incident must identify one of the following primary failure classes.

- **AG-assistant failure:** a defect in the deployed assistant’s mathematical reasoning, Sage work, computation, implementation, verification, or reporting. Its forward-facing correction must appear in `STYLE_GUIDE.md`.
- **Editor/maintainer failure:** a defect in extracting, writing, organizing, preserving, versioning, or deploying guidance. Its correction belongs in `CONTRIBUTING.md` or `MAINTENANCE.md`.

One conversation may reveal both classes. Record them separately rather than writing a hybrid rule for both audiences.

# Part I — Failures of the AG assistant

## P-0002 — Presentation-driven product construction and rhetorical pseudo-generality

**Failure class:** AG assistant

### Failure

The assistant asserted that Sage did not support a mixed product in its projective and affine scheme classes, then selected a toric realization because the motivating factors happened to be toric. It called this the “mathematically correct toric ambient” and announced that factor projections were being constructed as a decisive next step, without evidence that the Sage limitation had been audited or that the construction had been executed.

After being challenged with non-toric examples, the assistant immediately announced a new architecture based on the “categorical product” `X ×_S T`, a dispatch list for affine and projective cases, and assertion gates for unsupported presentations. Assertion-gated partial coverage was not itself the error. The response did not specify the defining cospan, establish whether an ordinary product or fiber product was intended, define the general semantic operation and its supported predicates, inspect the existing Sage primitives, implement the dispatch, or analyze whether broader coverage was cheaply obtainable through native primitives, bridges, reference implementations, or literature algorithms.

### Underlying defects

The response contained several independent failures:

- selecting a convenient computational presentation before reconstructing the governing mathematical construction;
- treating the existence of a toric realization as evidence that toric geometry was the canonical or “mathematically correct” semantic ambient;
- claiming a Sage limitation without source inspection or executed evidence;
- invoking a fiber product notation without its two structural morphisms or ambient category;
- replacing one special backend with a speculative list of special backends and calling the result general;
- using abstract words such as “categorical” and “semantic” as rhetorical substitutes for complete mathematical data and implementation;
- proposing assertion gates without distinguishing the general semantic domain, mathematical preconditions, implemented backend coverage, and research-scope boundaries;
- failing to check whether native Sage composition, an existing bridge, a general reference implementation, or a literature algorithm made broader coverage straightforward;
- presenting plans, headings, and intended next actions as designed or active computational work.

### Governing correction

Start from the complete mathematical construction, including all objects, morphisms, ambient category, hypotheses, and universal property. Keep that semantic interface general even when executable coverage is partial. Audit Sage before claiming support or absence. Route verified special cases beneath the general operation and gate unsupported representations explicitly.

Before deferring the general implementation, check in order whether it follows from a short composition of Sage primitives, an established bridge to another system, a reliable general reference implementation, or an explicit algorithm or theorem in the literature. Implement a broader route when it is bounded, mathematically controlled, and likely to improve reuse. When it is substantial and unnecessary for the current supported computation, record an actionable backlog strategy and continue the research task.

### Regression criteria

A future response must:

1. distinguish an ordinary product from a fiber product;
2. name every structural morphism and the ambient category;
3. state precisely what Sage representation or operation was inspected and what failed;
4. avoid calling a convenient presentation the mathematically correct ambient;
5. inspect existing Sage primitives before inventing a replacement architecture;
6. define the general semantic operation independently of current backend coverage;
7. case-route verified supported representations and assertion-gate unsupported representations precisely;
8. distinguish mathematical preconditions, implementation preconditions, and research-scope boundaries;
9. treat user counterexamples as scope witnesses rather than a backend menu;
10. determine whether existing Sage primitives compose into the general case with modest effort;
11. inspect relevant bridges to established external systems;
12. search for a general reference implementation or citable literature algorithm before deferral;
13. weigh implementation complexity, integration risk, immediate necessity, and likely reuse;
14. record substantial deferred work as an actionable backlog item with a concrete route;
15. distinguish a mathematical correction from a proposed implementation;
16. label work as proposed, written, executed, or verified according to evidence;
17. avoid status headings that imply completed design or computation without an artifact.

### Rule destination

Forward-facing corrections belong in `STYLE_GUIDE.md`, especially the sections on complete universal constructions, intrinsic objects versus presentations, general interfaces with partial backend coverage, Sage audit, evidence, and remediation.

## P-0004 — Engineering-first reconstruction of an algebraic-geometry interface

**Failure class:** AG assistant

### Source failure

A notebook report identified repeated coordinate-level workarounds in Sage and proposed a catalogue of new freestanding classes and factory functions: divisor-class objects without first establishing `Cl(X)` or `Pic(X)`, a representation object attached directly to sections, free-standing fixed-locus and evaluation-map constructors, an embedding-specific singular-locus operation, free-standing ADE classification, and a free-standing double-cover factory.

The first correction correctly objected that these proposals omitted ambient mathematical structures, attached operations to the wrong objects, and promoted derived constructions to primitives. The revised report then mostly converted functions into method syntax without fully reconstructing the mathematics. It still proposed several ill-defined or unsupported operations, including treating `H^0(X,L)` as an algebra, assigning a universal local equation or Tjurina algebra to every point, treating ADE type as an unconditional point invariant, and specifying double covers without all required cover data.

### Cognitive failure

The governing defect was engineering-first thought:

- reading notebook code as a list of missing software conveniences rather than evidence of missing mathematical structure;
- naming classes and methods before defining the objects, categories, functors, and universal properties involved;
- treating the current coordinate presentation as the ontology;
- promoting intermediate computational artifacts to primary mathematical objects;
- relocating a function onto a method receiver and mistaking that syntactic change for a semantic correction;
- accepting plausible mathematical vocabulary without checking definitions, hypotheses, variance, ownership, or return types;
- inventing a parallel API without auditing Sage’s existing implementation and partial support.

### Governing correction

The assistant must reconstruct the mathematics before designing or extending Sage interfaces:

1. identify the ambient category or structure;
2. identify the actual object or morphism represented by each datum;
3. distinguish primitive data from functorially derived data;
4. determine which constructions are intrinsic and which depend on a presentation;
5. state all hypotheses under which an invariant or method is defined;
6. choose the mathematically primary output;
7. only then map the construction to existing or proposed Sage ownership and syntax.

### Sage-specific regression cases

#### Divisors and line bundles

- A divisor, divisor class, invertible sheaf, and element of `Pic(X)` or `Cl(X)` are not interchangeable.
- Implement or use the ambient group before proposing isolated element classes.
- Intersection products, canonical classes, cohomology, linear systems, and section rings have different ownership and hypotheses.

#### Group actions

- A group action on the base and a linearization of a line bundle induce representations on cohomology.
- `H^0(X,L)` is generally a module or vector space, not an algebra.
- The graded section ring `\bigoplus_{n\ge 0} H^0(X,L^{\otimes n})` is an algebra when its multiplication is part of the construction.

#### Endomorphisms and fixed loci

- A fixed subscheme is the equalizer of an endomorphism and the identity.
- The endomorphism and ambient category must already exist.
- The graph morphism is primary; its codomain represents the graph subscheme. Do not add redundant convenience nouns when composition already exposes the object.

#### Linear systems and evaluation

- A line bundle does not automatically define a morphism to projective space.
- Global generation or basepoint-freeness must be established; otherwise the complete linear system gives a rational map with a base locus.
- Point evaluations and matrices are derived from the relevant section space and linear-system map, not independent primitive objects.

#### Singularities

- The singular locus is intrinsic to the scheme, not to a chosen embedding as a curve on a surface.
- Local invariants belong to the local ring or germ and may require a chosen local presentation.
- A single local equation exists only under appropriate hypersurface or Cartier hypotheses.
- Tjurina algebras, Milnor numbers, and ADE classification are partial constructions with characteristic, isolation, and singularity-class hypotheses. They must not be advertised as total methods on arbitrary points.

#### Double covers

- A double cover is primarily a morphism `pi: X -> Y`.
- Its construction requires the actual cover data, typically an invertible sheaf `L` and a section of `L^\otimes 2`, or equivalent branch data together with a chosen square root where required.
- Branch and ramification loci are derived from the covering morphism and its construction.
- A method such as `D.double_cover()` is valid only when the divisor object carries or canonically determines the missing data; otherwise the method must require them explicitly.

#### Existing Sage semantics

- Check Sage source, documentation, categories, parent/element ownership, and executed behavior before claiming an abstraction is absent.
- Extend or repair an existing general primitive where possible.
- Do not route around a Sage defect with a narrow special-purpose implementation merely because it solves the notebook’s current example.

### Acceptance criteria

A revised report passes only if it:

1. begins with the governing mathematics rather than a feature catalogue;
2. defines ambient structures before their elements;
3. identifies the primary object and functorial dependencies of each computation;
4. separates intrinsic constructions from coordinate presentations;
5. states hypotheses for partial invariants;
6. audits existing Sage functionality;
7. distinguishes mathematically justified method ownership from merely object-oriented syntax;
8. avoids inventing unsupported classes, methods, or return types;
9. preserves concrete Sage guidance where it is operationally important;
10. does not describe speculative API design as implemented computation.

### Rule destination

Forward-facing corrections belong in `STYLE_GUIDE.md`, especially the mathematical stance, ambient structures, ownership, primitive-versus-derived data, Sage audit, divisor theory, group actions, morphisms, linear systems, singularities, covers, return types, hypotheses, and evidence sections.

# Part II — Failures of contributors and maintainers

## P-0001 — Destructive prompt replacement and false preservation claims

**Failure class:** editor/maintainer

### Failure

Corrections were repeatedly written into a bounded replacement field as though it were append-only memory. New incident-specific clauses displaced or compressed earlier requirements, while the editor continued to claim that each correction had been incorporated.

### Governing correction

Maintain a complete external, version-controlled source. Treat bounded prompt fields as derived deployment artifacts. Never claim preservation without comparing the resulting source and deployment against the preceding version.

### Regression criteria

A future update must preserve prior clauses, identify destructive changes, and distinguish canonical storage from deployment state.

### Rule destination

Repository mechanics belong in `MAINTENANCE.md`; preservation and editorial review requirements belong in `CONTRIBUTING.md`.

## P-0003 — Unnecessary pull-request ceremony

**Failure class:** editor/maintainer

### Failure

A feature branch and pull request were created in an empty user-owned repository even though direct writes to the default branch were permitted and no review boundary had been requested.

### Governing correction

Use the least elaborate repository workflow that satisfies the actual requirements. Direct commits are preferred when authorized and sufficient.

### Rule destination

Repository workflow belongs in `MAINTENANCE.md`, not in the assistant-facing guide.

## P-0005 — Repository-maintenance prose placed in the assistant prompt

**Failure class:** editor/maintainer

### Failure

The assistant-facing style guide was dominated by explanations of its own purpose, versioning, prompt deployment, provenance, changelog, storage, and Git workflow. The assistant that consumes the guide did not need this material to perform algebraic geometry or Sage work.

### Governing correction

Separate artifacts by audience. `STYLE_GUIDE.md` contains only assistant behavior. Contributor rule-writing guidance belongs in `CONTRIBUTING.md`; repository procedure belongs in `MAINTENANCE.md`; source failures belong here; revision history belongs in `CHANGELOG.md`; repository orientation belongs in `README.md`.

### Regression criteria

No section may remain in `STYLE_GUIDE.md` solely to explain how that file is stored, updated, versioned, reviewed, or deployed.

## P-0006 — Instructions to the editor misrouted as instructions to the AG assistant

**Failure class:** editor/maintainer

### Failure

During repository construction, instructions addressed to the current editing agent were repeatedly treated as content for the deployed AG assistant. Directions about persistent storage, version control, direct commits, document maintenance, generalizing incidents, and separating audiences were initially mixed into the assistant-facing guide.

This conflated two distinct questions:

1. How should contributors write and maintain the behavioral specification?
2. How should the AG assistant reason and act while doing algebraic geometry and Sage computations?

### Underlying defect

The editor classified guidance by conversational proximity rather than by the actor whose future behavior it governed. Because both kinds of instructions arose in the same conversation, the editor assumed they belonged in one document.

### Governing correction

Classify every correction by target audience before writing it. An instruction addressed to the current editor belongs in contributor or maintenance documentation unless it independently describes behavior the deployed AG assistant must perform. When one incident yields both editor-facing and assistant-facing lessons, write separate clauses in separate files.

### Regression criteria

A future repository edit must:

1. name the actor whose behavior is being corrected;
2. route contributor instructions to `CONTRIBUTING.md`;
3. route mechanical repository instructions to `MAINTENANCE.md`;
4. route only forward-facing AG/Sage behavior to `STYLE_GUIDE.md`;
5. split mixed incidents into separate audience-specific rules;
6. verify that `README.md` accurately explains the audience map.

### Rule destination

Audience classification and editorial routing belong in `CONTRIBUTING.md`. Mechanical file and deployment routing belongs in `MAINTENANCE.md`.

## P-0007 — Literal incident patching followed by destructive single-principle compression

**Failure class:** editor/maintainer

### Failure

When the product-construction incident was first converted into guidance, the editor copied a catalogue of incident-specific nouns into the standing behavior: the notation `X ×_S T`, toric, affine, projective, and chartwise backends, blow-ups, K3 and Enriques surfaces, mixed affine/projective examples, and a list of prohibited progress phrases.

After the user identified this as massively overfit, the editor swung to the opposite extreme. It claimed that the real issue was simply to distinguish a mathematical construction from a computational presentation and to avoid promoting an example-specific backend into the semantic interface. It then asserted that the behavior had been revised accordingly.

That compressed away independent requirements exposed by the same source incident: complete diagram data for a fiber product, verification of Sage support claims, criteria distinguishing legitimate assertion-gated partial coverage from semantic narrowing, evidence-sensitive status reporting, the implementation-escalation ladder, and the need to test the revised construction against the user’s non-toric scope witnesses.

### Underlying defect

The editor treated rule extraction as a choice between transcription and maximal compression. It assumed one incident should yield one smallest invariant principle, rather than decomposing the source into all causally independent failure dimensions and finding the smallest sufficient set of rules.

It also failed to classify the role of concrete examples. Some details were incidental, while others were scope witnesses and regression cases. Treating all examples first as standing rules and then as disposable noise lost both generality and operational coverage.

### Governing correction

Decompose each incident before generalizing it. Separate mathematical-semantic, Sage/API, implementation-coverage, evidence-reporting, remediation, and editorial defects when they are independently actionable. Produce the smallest sufficient rule set, not necessarily one rule. Preserve concrete examples as scope witnesses or regression anchors when they are needed to test the general rule, without turning them into a literal feature catalogue.

Do not claim that a correction has been incorporated until every material source failure maps to a resulting clause or regression criterion and the edited files have been reviewed.

### Regression criteria

A future editor handling a mixed incident must:

1. identify all independent failure dimensions before drafting rules;
2. avoid copying every incident noun or phrase into `STYLE_GUIDE.md`;
3. avoid replacing the incident with one slogan that does not block every source failure;
4. classify examples as incidental details, scope witnesses, or regression cases;
5. preserve concrete Sage and algebraic-geometry constraints where they carry operational content;
6. create separate assistant-facing and contributor-facing corrections when both actors failed;
7. maintain a coverage map from each material defect to a rule or regression criterion;
8. verify the repository diff before claiming the behavior was revised.

### Rule destination

Rule-extraction and coverage requirements belong in `CONTRIBUTING.md`. The forward-facing AG-assistant corrections derived from the same source incident belong in `STYLE_GUIDE.md` and are tracked separately under P-0002.

## P-0008 — Assertion-gated backend coverage misclassified as semantic narrowing

**Failure class:** editor/maintainer

### Failure

The editor encoded blanket rules that assertions must not exclude examples required by the task and that unsupported functionality must not be placed behind an assertion. This treated assertion gates as evidence of degradation rather than as a standard mechanism for preserving a mathematically general interface with explicitly partial executable coverage.

The rule would force one of two bad outcomes: either define a narrow method specialized to the currently supported Sage presentation, or derail the active research task into a substantial general backend implementation before any supported computation could proceed.

### Underlying defect

The editor conflated:

- the mathematical domain of a construction;
- mathematical hypotheses under which it is defined;
- the representations currently handled by Sage;
- available implementation routes through native primitives, bridges, reference code, or literature;
- the scope appropriate to the active research conversation.

It also failed to distinguish a vague unsupported-case escape hatch from a precise case match or assertion gate beneath a correct general semantic operation.

### Governing correction

Keep the mathematical interface as general as the construction itself. Route supported Sage cases beneath that interface and gate unsupported representations explicitly. Before deferral, inspect native Sage compositions, established bridges, reference implementations, and citable algorithms or theorems. Implement the general route when it is short, reusable, and mathematically controlled; otherwise record an actionable backlog strategy and continue the supported research task.

The current input determines whether deferral is permissible. If it is supported, backend generalization may be deferred. If it is unsupported and required for the result, the assistant must implement the necessary extension or report the block.

### Regression criteria

A future editor must verify that assistant-facing guidance:

1. distinguishes semantic scope from executable coverage;
2. permits explicit assertion-gated or case-matched dispatch beneath a general interface;
3. distinguishes mathematical preconditions from implementation predicates;
4. requires precise failure messages for unsupported representations;
5. requires inspection of native primitives, bridges, reference implementations, and literature routes;
6. weighs implementation complexity and reuse against the active research goal;
7. requires actionable backlog entries for substantial deferred generalization;
8. never permits claimed results from unsupported branches;
9. does not force unrelated large backend work merely to remove an honest implementation boundary.

### Rule destination

The forward-facing implementation ladder belongs in `STYLE_GUIDE.md`. Editorial safeguards against blanket anti-assertion rules and uncontrolled scope expansion belong in `CONTRIBUTING.md`.

## P-0009 — Answer-first computation and oracle assertions

**Failure class:** AG assistant

### Failure

The assistant reported that Sage had computed the four fixed points of an involution, but the notebook had hard-coded the four expected coordinate points and checked that they satisfied the fixed equations. The user correctly observed that this verified candidates without deriving the complete locus.

Related cells later used expected tuple orders, singularity labels, group identifications, and classification facts as assertions whose success was described as computation.

### Underlying defect

The assistant substituted a known or guessed mathematical answer for the construction it was asked to perform. The expected answer became an oracle for writing the code, and candidate verification was laundered into exhaustive computation.

It also failed to distinguish capability gates, theorem-backed regression assertions, mathematical postconditions, and hard-coded answer assertions.

### Governing correction

Classify every evidentiary step. A computation may construct an object, exhaustively compute a result, verify a supplied candidate, apply a theorem, or compare against a regression oracle. These roles must be stated separately.

Assertions are valid for mathematical and implementation preconditions, universal-property equations, backend regressions, and postconditions computed from the object. They must not supply the answer that the advertised computation was supposed to derive.

### Regression criteria

A future response must:

1. distinguish candidate verification from complete computation;
2. explain the source of every expected value used in an assertion;
3. keep oracle values out of the computational path;
4. compute the complete scheme, ideal, map, group, or classification certificate advertised;
5. label theorem deductions as theorem deductions;
6. keep backend regression assertions outside the mathematical narrative unless they express a proof obligation.

### Rule destination

Forward-facing evidence and assertion rules belong in Sections 17 and 21 of `STYLE_GUIDE.md`.

## P-0010 — Premature abstraction closure and one-rung remediation

**Failure class:** AG assistant

### Failure

Across the fixed-locus and framework work, the assistant repeatedly declared a design complete after moving only one abstraction level upward:

1. hard-coded points;
2. chart ideals;
3. determinant helpers;
4. a projective-product equalizer helper;
5. a free-standing utility namespace;
6. methods monkey-patched onto morphisms;
7. facade parents for automorphisms;
8. categorical pullbacks;
9. standard functorial and relative-spectrum constructions.

At each intermediate rung the assistant described the new layer as the natural reusable interface. The user then identified that the construction was still compositional, presentation-specific, missing its parent, or a special case of a standard universal construction.

### Underlying defect

The assistant used reusability and object-oriented discoverability as stopping criteria for mathematical reconstruction. It did not ask whether the current abstraction was itself merely a coordinate realization, functorial restriction, compositional convenience, or special case of a standard construction.

### Governing correction

After every refactor, repeat an abstraction-completion test. Continue until the public interface is governed by the standard parent, functor, diagram, universal property, and hypotheses. Presentation-specific helpers may remain private.

Moving a function onto an object or creating a reusable helper is not evidence that the semantic design is complete.

### Regression criteria

A future interface proposal must identify:

1. its ambient parent or category;
2. its primitive mathematical data;
3. its universal or functorial definition;
4. whether any public method is merely compositional;
5. whether the proposed object is a coordinate model of a more standard object;
6. why the abstraction chain legitimately stops at the proposed layer.

### Rule destination

Forward-facing abstraction-completion rules belong in Sections 3, 4, and 20 of `STYLE_GUIDE.md`.

## P-0011 — False canonicity and representation-sensitive verification

**Failure class:** AG assistant

### Failure

An evaluation assertion failed because Sage enumerated fixed points in a different order from the expected coefficient tuple. The assistant first proposed enforcing a canonical order on points and corner monomials. The user correctly observed that the mathematics supplied equality of sets, supports, ideals, and principal opens, not a preferred enumeration.

The same tendency appeared with bases, chart choices, coordinate blocks, polynomial models, and display symbols.

### Underlying defect

The assistant treated a convenient representation as canonical in order to make literal equality pass. It did not identify the choices involved or formulate the assertion at the invariant level.

### Governing correction

Name every choice of basis, chart, trivialization, ordering, normalization, grading, and coordinate model. Verify the invariant object supplied by the mathematics: schemes, ideals, maps, supports, sets, isomorphism classes, or equalities up to units and scalars.

Do not manufacture canonical orderings merely to stabilize tests.

### Regression criteria

A future computation must:

1. identify every noncanonical choice;
2. avoid order-sensitive assertions unless an order is part of the data;
3. compare ideals after the correct saturation or normalization;
4. distinguish equality from isomorphism and equality up to scalar;
5. expose coordinate realizations through explicit maps from intrinsic parents.

### Rule destination

Forward-facing rules belong in Sections 22 and 28 of `STYLE_GUIDE.md`.

## P-0012 — Local data promoted to global schemes and families

**Failure class:** AG assistant

### Failure

The assistant repeatedly described chart equations, chart dictionaries, or local quotient presentations as global covers, families, quotients, or morphisms before constructing overlaps and verifying compatibility.

The universal double-cover work also initially treated the projective linear system as carrying a canonical universal cover. Only later did the assistant notice that the parameter-space `O(1)` twist has no canonical square root, so the cover datum does not descend to the projective parameter space.

### Underlying defect

The assistant collapsed local construction, gluing, and descent into one step. It assumed that correct fiberwise or chartwise equations automatically assembled into a global object.

It also conflated affine parameter spaces of sections, projective linear systems of divisors, total spaces, incidence schemes, and moduli-like quotients.

### Governing correction

A global claim requires affine pieces, overlap isomorphisms, cocycle identities, compatible local morphisms, and descent of every line bundle, section, action, and root datum. A fiberwise construction must be checked for descent over the parameter base.

Before introducing “universal” or “generic” objects, identify the represented functor and the exact parameter scheme.

### Regression criteria

A future family construction must:

1. distinguish local equations from the global object;
2. construct and verify all overlap maps and cocycles;
3. verify compatibility of local morphisms;
4. track parameter-space twists and root line bundles;
5. distinguish affine sections from projective divisors;
6. state whether scalar multiplication has been quotiented;
7. refuse a universal-family claim when required data do not descend.

### Rule destination

Forward-facing local-to-global and parameter-space rules belong in Sections 23 and 24 of `STYLE_GUIDE.md`.

## P-0013 — Persisted-notebook state drift and expository displacement

**Failure class:** AG assistant

### Failure

The assistant repeatedly placed substantial theory in chat while leaving the notebook with procedural headings and opaque computation cells. Later, after service outages and refactors, it discovered:

- the framework notebook attached to a Python rather than Sage kernel;
- duplicated tail cells;
- stale regression cells;
- research-cell edits that had not persisted;
- prose claiming that a global cover was absent after later cells constructed one;
- chartwise computations still active after semantic replacements had supposedly landed.

Earlier completion claims had been based on live-kernel or intended state rather than the persisted artifact.

### Underlying defect

The assistant treated chat exposition, live kernel definitions, persisted notebook source, and executed notebook state as equivalent. It also failed to propagate semantic changes through downstream code, prose, displays, and tests.

### Governing correction

The artifact is the deliverable. Theory needed to justify a computation must be written into the notebook near the relevant cells. Backend tests should be isolated from the mathematical narrative.

After any outage, restart, failed write, import change, or structural refactor, reopen the persisted artifact, inspect its kernel and cells, remove duplicates and stale prose, execute from a clean state, reopen again, and only then claim completion.

Every primitive semantic change requires a downstream dependency audit.

### Regression criteria

A future notebook-maintenance response must:

1. identify the persisted file as the source of truth;
2. verify kernel type, cell count, cell order, and imports;
3. inspect changed source and persisted outputs;
4. detect duplicate or stale cells;
5. update theorem narrative and all downstream callers;
6. clean-execute the relevant notebook;
7. reopen the saved file after execution;
8. distinguish chat explanation from material actually landed in the artifact.

### Rule destination

Forward-facing notebook and dependency-audit rules belong in Sections 26 and 27 of `STYLE_GUIDE.md`.
