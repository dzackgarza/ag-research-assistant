## Audit computational-ecosystem and installation routing

When a transcript responds to a missing Sage capability by writing more Sage or ordinary Python code, review whether the assistant surveyed the broader computational ecosystem and distinguished installed tools from installable or connectable tools.

Require the analysis to identify:

1. the exact mathematical capability required;
2. the native Sage support and its semantic limitations;
3. relevant installed interfaces and kernels, including Singular, `libgap`, Macaulay2, PARI/GP, Julia/Oscar, or domain-specific tools where applicable;
4. project-local bridges and packages;
5. maintained external packages, formal libraries, reference implementations, and literature algorithms;
6. whether an absent but installable dependency is the mathematically preferable route;
7. the fidelity of conversions across system boundaries;
8. exactness, certificates, supported coefficient domains, and universal properties;
9. installation, licensing, reproducibility, performance, and maintenance costs;
10. the assistant's recommendation and the precise user decision needed before environment expansion.

Flag **environment capture** when the assistant treats the currently installed packages as the complete solution space. Flag **Sage confinement** when Sage familiarity determines the architecture despite a stronger available backend. Flag **installation avoidance** when the assistant begins reimplementing a maintained external capability without surfacing the installation or bridge option. Flag **bridge laundering** when data is transferred to another system while mathematically essential parentage, structure maps, gradings, localizations, or certificates are lost. Flag **dependency maximalism** when a large toolchain is proposed without showing that its capabilities and reuse justify the integration cost.

A CAS-agnostic semantic layer is useful only when it preserves one mathematical contract across backends. Do not require every backend to support every operation. Require capability routing, explicit gates, and verified adapters.

The current environment is evidence about immediate executability, not evidence that an algorithm, package, or principled implementation is unavailable. A valid assistant-facing rule should cause the agent to search, compare, and, when appropriate, recommend installing or connecting the correct tool before inventing a replacement.
