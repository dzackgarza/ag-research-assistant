# Incident and Regression Record

This document is for contributors, editors, and reviewers. It preserves source failures, classifies the actor that failed, and records regression evidence. It is not part of the prompt consumed by the Algebraic Geometry Research Assistant.

## Classification

Every incident must identify one of the following primary failure classes.

- **AG-assistant failure:** a defect in the deployed assistant’s mathematical reasoning, Sage work, computation, implementation, verification, or reporting. Its forward-facing correction must appear in `STYLE_GUIDE.md`.
- **Editor/maintainer failure:** a defect in extracting, writing, organizing, preserving, versioning, or deploying guidance. Its correction belongs in `CONTRIBUTING.md` or `MAINTENANCE.md`.

One conversation may reveal both classes. Record them separately rather than writing a hybrid rule for both audiences.

# Part I — Failures of the AG assistant

## P-0002 — Presentation-driven product construction and pseudo-generality

**Failure class:** AG assistant

### Failure

A mixed product involving a projective variety and an affine parameter space was routed through toric geometry because the motivating example happened to be toric. After challenge, the response replaced this with an announced dispatch list for affine, projective, and unsupported cases, and invoked a fiber product without specifying its defining cospan.

### Underlying defect

The assistant selected a computational presentation before reconstructing the governing mathematical construction. It then mistook a list of presentation-specific backends for a general implementation and described speculative architecture as active work.

### Governing correction

Start from the complete mathematical construction, including all objects, morphisms, ambient category, hypotheses, and universal property. Treat toric, affine, projective, and chartwise constructions only as implementations. A list of special backends is not a general implementation.

### Regression criteria

A future response must:

1. distinguish product from fiber product;
2. name every structural morphism;
3. inspect existing Sage primitives before inventing a replacement;
4. establish actual backend coverage;
5. preserve required non-special cases;
6. use assertions only for genuine preconditions;
7. distinguish proposed, executed, and verified work.

### Rule destination

Forward-facing corrections belong in `STYLE_GUIDE.md`, especially the sections on complete universal constructions, intrinsic objects versus presentations, backend coverage, evidence, and remediation.

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
