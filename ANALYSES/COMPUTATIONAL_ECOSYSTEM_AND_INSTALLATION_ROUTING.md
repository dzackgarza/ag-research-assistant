# Computational Ecosystem and Installation Routing

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** user correction concerning Sage confinement, external CAS systems, project-local bridges, and installable dependencies.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The assistant often treats the current Sage kernel and its installed Python packages as the computational universe. When Sage lacks a coherent commutative-algebra construction, it begins extending Sage parents, adding Python wrappers, or implementing specialized formulas. This can repeat the local-repair pattern even after the mathematics has been formulated correctly.

The missing research habit is computational-ecosystem reconnaissance. A mathematician choosing a computational route is not limited to one CAS. The relevant question is which system already represents and computes the required mathematics most faithfully, and how that system can participate in an auditable common interface.

The same error has a second form: the assistant may know that a more suitable package or CAS exists but ignore it because it is not currently installed. Installation state is then allowed to determine mathematical architecture.

## 2. Available versus appropriate tools

Three sets must be distinguished:

1. tools immediately available in the current process;
2. tools already accessible through installed interfaces, subprocesses, kernels, or project-local bridges;
3. tools that are not yet installed but are maintained, installable, and mathematically preferable.

Only the first set determines immediate execution. The union of all three determines the plausible implementation landscape.

A missing import therefore proves little. It may justify a short capability gate while the assistant researches installation, but it does not justify a new foundational implementation by itself.

## 3. External CAS systems as mathematical backends

Sage already interfaces with or can call systems such as Singular, GAP through `libgap`, Macaulay2, and PARI/GP. Julia and Oscar can supply additional commutative algebra and algebraic geometry. Specialized command-line tools and language libraries may own still other algorithms.

The user-provided `sage-julia-bridge` is a concrete regression case. It provides a long-lived Julia subprocess, can load Oscar, transfers supported rings, polynomial rings, finite fields, and matrices with parent-aware conversions, and retains unsupported results as opaque handles. The important lesson is not that every task should use Julia. It is that a maintained project-local bridge can change the available architecture and must be audited before new local infrastructure is designed.

## 4. Capability routing rather than backend ontology

The public mathematical object should not become `SingularIdeal`, `M2Scheme`, or `OscarRing` merely because one backend performs the computation. The semantic owner remains the ideal, scheme, algebra, morphism, localization, or diagram. Backend adapters implement capabilities.

A capability route must specify:

- accepted mathematical domain;
- conversion map into the backend representation;
- preservation of coefficient rings, generators, orderings, gradings, quotients, localizations, and structure maps;
- output conversion or a typed opaque handle;
- certificates or comparison checks;
- exact failure boundaries.

This permits one construction to use Singular for Gröbner bases, Macaulay2 for sheaf or scheme computations, GAP for group calculations, Oscar for commutative algebra, and Sage for orchestration without making the visible research artifact a sequence of unrelated backend calls.

## 5. Installation is a research-scope option

If the best route needs an uninstalled tool, the assistant should not silently install it and should not silently reject it. It should present a concrete proposal:

- what should be installed or connected;
- which mathematical operations it unlocks;
- why it is better than extending the current backend;
- installation size, version, platform, licensing, and maintenance implications;
- integration and conversion work still required;
- fallback route;
- expected reuse beyond the immediate example.

The decision can be small—for example, adding one Python package—or substantial, such as provisioning Julia/Oscar or Macaulay2. The user controls the research and environment scope, but the assistant is responsible for identifying and recommending the principled option.

## 6. Opposite failure modes

**Environment capture** mistakes current installation state for the available mathematics.

**Sage confinement** assumes every missing operation must be rebuilt inside Sage or ordinary Python.

**Installation avoidance** hides a good external route because raising the dependency question feels like scope expansion.

**Bridge laundering** passes strings or coefficient arrays across a process boundary and claims semantic interoperability without preserving the mathematical structure.

**Dependency maximalism** proposes a broad toolchain without comparing its concrete benefit, reproducibility, licensing, and maintenance cost.

The guide must block all five. It should not replace Sage confinement by indiscriminate dependency accumulation.

## 7. Editorial consequence

Contributor reviews should require a capability matrix or equivalent comparison whenever backend work becomes substantial. Concrete systems remain examples; the general rule is that mathematical requirements determine tool selection, and absent but installable tools must remain part of the architecture discussion.
