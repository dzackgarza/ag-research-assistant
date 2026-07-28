## Audit interactive research-architecture decisions

When reconnaissance reveals several materially different implementation architectures, review whether the assistant surfaced the choice before entering deep local work.

Require the analysis to distinguish at least:

1. the exact mathematical artifact and theorem requested;
2. the missing semantic or foundational operations discovered;
3. a bounded coordinate route and the weaker or less reusable artifact it would produce;
4. any small semantic quarantine that could isolate backend defects for a coherent research corner;
5. any reusable foundational detour and the broader dependency class it would unlock;
6. existing native, bridged, formal, or reference implementations;
7. the auditability of each resulting artifact to a mathematician unfamiliar with Sage or Python;
8. the proof obligations, reuse, and scope consequences of each route;
9. the assistant's mathematical recommendation;
10. the precise user decision required before costly implementation.

Flag **silent architecture selection** when the assistant chooses among these routes without exposing the choice. Flag **ad-hoc defaulting** when it chooses coordinates merely because they are immediately executable. Flag **foundation maximalism** when it launches a broad foundational program without establishing that the user wants that scope. Flag **auditability erasure** when the analysis treats a correct numerical or coordinate result as equivalent to a legible semantic research artifact.

A semantic quarantine is valid only when it captures standard objects and operations for a recognizable class of nearby problems. Reject wrappers whose only domain is the present example. Conversely, do not require a universal foundation when a bounded, explicitly disposable computation is the user's actual goal.

The assistant should ask after enough reconnaissance to describe concrete alternatives, but before implementation cost and patch accretion make the choice effectively irreversible. The question should include current valid work, exact gaps, expected deliverables, limitations, reuse, and a recommendation. It should not be a generic request for permission to continue.

A valid assistant-facing rule should make research architecture an explicit collaboration with the user while preserving the assistant's responsibility to investigate the mathematics and recommend the principled route.
