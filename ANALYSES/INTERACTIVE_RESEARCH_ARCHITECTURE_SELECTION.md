# Interactive Research-Architecture Selection

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** user analysis of Sage research workflows in which foundational gaps emerge during implementation reconnaissance.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

A foundation-sufficiency audit does not by itself determine what the assistant should build. Once the audit reveals that the requested semantic construction is not readily supported, several mathematically legitimate responses may remain. Choosing among them depends on the user's research program, desired artifact, tolerance for one-off code, and interest in reusable foundations.

The error is to treat that choice as an internal engineering decision. The assistant may default to coordinate calculations because they are executable, or silently begin a broad foundational project because it is principled. Both choices can be wrong even when the mathematics is competent.

The correct behavior is an interactive research-architecture checkpoint after reconnaissance and before deep implementation.

## 2. Three recurring architectural scales

### 2.1 Bounded coordinate work

A specific surface, involution, fixed locus, branch curve, singularity check, or double-cover equation may be computable directly in coordinates. This can be appropriate when the desired output is a quick witness or isolated calculation.

The route must be described honestly. It may not construct the product, sheaves, sections, actions, fixed subschemes, local rings, covering morphisms, or other objects as first-class mathematical entities. It may prove the requested numerical or equation-level fact without producing a reusable semantic artifact.

### 2.2 Semantic quarantine

A small synthetic or shadow layer can isolate the complication. It may own a coherent class of products, line bundles, sections, actions, fixed loci, localizations, or covers for a recognizable research domain while routing to existing coordinate backends.

This is not a compromise wrapper around one example. It is a bounded mathematical interface whose public operations match standard parlance and whose special representations are quarantined privately. It is useful when a total foundation is disproportionate but auditability and nearby reuse matter.

### 2.3 Foundational program

The task may expose a genuinely reusable missing substrate: coherent ring arrows, localizations, algebra structures, tensor products, affine spectra, scheme pullbacks, local rings, germs, or theorem propagation. Owning that layer can widen the base of an ongoing computational research program and support unrelated future problems.

This route changes project scope. Its value cannot be inferred solely from the current example. The user must decide whether the broader investment matches the research agenda.

## 3. Mathematical auditability changes the decision

The artifact is not merely its final answer. Research code should permit a mathematician unfamiliar with Sage or Python to inspect the argument.

Code such as

\[
X=\mathbf P^1\times\mathbf P^1,
\qquad
\iota:X\to X,
\qquad
\operatorname{Fix}(\iota),
\qquad
\pi:Y\to X
\]

communicates a mathematical proof structure when these are genuine objects and morphisms. A long sequence of coordinate-ring substitutions can compute equivalent equations while obscuring why the construction is correct and which hypotheses are used.

Therefore implementation cost is not the only axis. The assistant must compare auditability, theorem strength, semantic fidelity, reuse, and the amount of hidden backend trust.

## 4. The decision must occur before local-repair commitment

The assistant should perform enough source and Sage reconnaissance to identify the actual gaps. It should not immediately ask the user how to proceed before it can describe the alternatives. But once the alternatives are clear, it should not continue coding until one route has accumulated so much implementation that the choice is effectively made.

The checkpoint should state:

- what has already been established;
- which standard mathematical constructions are missing or defective;
- what each route would produce;
- what each route would not prove or represent;
- how each route affects auditability and reuse;
- which current experiments remain useful;
- the assistant's recommendation.

The final question should be a concrete scope choice, not an invitation for the user to manage the implementation process.

## 5. Opposite failure modes

**Ad-hoc defaulting** chooses coordinate work because it is closest to the current notebook. It hides semantic losses and often creates rigid code that is difficult to audit or reuse.

**Foundation maximalism** treats every discovered Sage defect as authorization to build a universal replacement. It can derail a task whose user only wanted a bounded computation.

**Silent quarantine** creates a local framework without explaining its mathematical domain, leading to another bespoke ontology.

**Auditability erasure** treats the production of correct equations as completion even when the research artifact no longer exposes the mathematical argument.

The style guide must block all four, not merely prefer the most abstract route.

## 6. Editorial consequence

Contributor guidance should require a scope-options table or equivalent comparison whenever these routes differ materially. Concrete motivating examples should remain regression cases, while the assistant-facing rule should apply across algebraic geometry, topology, representation theory, and other computational research domains.
