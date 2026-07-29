
## 40. Choose computational tools by mathematical capability, not by the current environment

Do not treat Sage, Python, or the packages already installed in the current kernel as the boundary of the computational solution space. Start from the mathematically correct objects, morphisms, universal constructions, algorithms, and certificates. Then determine which available or installable system represents and computes them most faithfully.

The current environment answers only what can be executed immediately. It does not determine what should be implemented, which abstraction is natural, or which tools may be added.

### 40.1 Survey the computational ecosystem before reimplementation

Before implementing a substantial missing backend, inspect the relevant capabilities across:

- native Sage categories, parents, interfaces, and optional packages;
- systems already bridged from Sage, such as Singular, GAP through `libgap`, Macaulay2, PARI/GP, and other available kernels;
- Julia and Oscar through an existing bridge when their algebraic implementations are stronger;
- importable Python, C, C++, Julia, or command-line libraries;
- formal libraries and proof assistants when they supply the correct definitions, algorithms, or executable reference behavior;
- project-local repositories, packages, and bridges;
- reference implementations found in maintained research code, official documentation, papers, or textbooks.

Search the web, repository sources, issue trackers, package registries, and local source corpus when they can reveal an existing principled solution. Do not begin a long native Sage or ordinary-Python reimplementation merely because the first import or method lookup failed.

### 40.2 Compare systems by semantic capability

For serious alternatives, determine:

1. which mathematical objects and morphisms the system represents explicitly;
2. whether the required universal property, certificate, or comparison map is available;
3. which coefficient rings, presentations, gradings, localizations, and noncanonical structure maps are supported;
4. whether algorithms are exact, heuristic, probabilistic, or numerical;
5. how objects and certificates cross the system boundary without losing structure;
6. whether the implementation is maintained and has usable reference tests or literature support;
7. installation, licensing, version, performance, and reproducibility constraints;
8. whether the route supports only the current example or a useful class of nearby problems.

Select the system that preserves the structure required by the theorem and already owns the needed mathematics whenever it can be integrated faithfully. Familiarity, speed, and immediate availability are secondary to semantic correctness and reuse.

### 40.3 Keep one mathematical interface across heterogeneous backends

The visible research interface should remain organized by standard mathematics rather than by the selected CAS. Use adapters or bridges so that Sage, Singular, Macaulay2, GAP, Oscar, or another system acts as a computational backend for the same mathematical construction.

Preserve and verify:

- domains, codomains, base and coefficient maps;
- parentage, generators, term orders, gradings, and quotient or localization data;
- exactness and coercion conventions;
- canonical and noncanonical morphisms;
- certificates, universal mediators, and comparison maps;
- round-trip identities on supported objects.

Do not flatten a structured object into an untyped string, matrix, or coefficient list and then claim the bridge preserves the mathematics. Opaque remote handles may be useful, but their mathematical type and supported operations must remain explicit.

Use independent systems for cross-checking when this materially strengthens confidence. Agreement of outputs is evidence only after the comparison maps and conventions relating the two computations are established.

### 40.4 Surface environment expansion as a research option

When the mathematically preferable route requires a tool that is not installed or connected, present the installation or connection option before undertaking substantial reimplementation.

State concretely:

- the package, CAS, kernel, bridge, or external service proposed;
- the mathematical capability it supplies;
- why it is more faithful or reusable than the currently executable route;
- the installation or integration boundary and expected environment changes;
- version, platform, licensing, reproducibility, and maintenance considerations;
- which conversions or adapters are still required;
- the fallback if installation is declined or fails;
- the work avoided and the nearby computations unlocked.

Give a mathematical recommendation and one precise scope question. Obtain authorization before installing a large or consequential toolchain that materially changes the environment, project dependencies, licensing assumptions, or maintenance burden.

Absence from the current environment is a capability gate, not a mathematical impossibility claim.

### 40.5 Compare implementation routes in a consistent order

For a missing computational capability, consider:

1. a correct native implementation already available in the current system;
2. an established interface or bridge to a system that already implements it;
3. installation of the most appropriate maintained package or CAS and a faithful adapter;
4. adaptation of a reliable reference implementation or literature algorithm;
5. a framework-owned repair or shadow when existing systems cannot preserve the required semantics;
6. an explicit unsupported gate with a concrete backlog route.

Choose among these routes by mathematical fidelity, auditability, integration cost, and research reuse rather than by current installation state or Sage familiarity.
