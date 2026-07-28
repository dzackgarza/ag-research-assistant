## Audit meta-status narration, stale state prose, and reflexive editorial accretion

When a mathematical notebook contains headings or paragraphs about what the notebook records, what it has established, how its question evolved, or which stage of work has been reached, do not treat the problem as a preference for shorter prose. Review whether conversational corrections, internal status tracking, and the agent's desire to externalize its momentary state have displaced standard mathematical exposition.

First determine the artifact type. A status report, research log, implementation plan, or framework-wide outstanding-work document may legitimately discuss its own state. A notebook whose primary purpose is to develop mathematics should normally present the mathematical objects, constructions, calculations, theorems, and questions directly.

Require the analysis to identify:

1. sentences whose grammatical subject is the notebook, section, agent, investigation, current stage, or verification status rather than a mathematical object or claim;
2. headings that announce completion, scope, or editorial history instead of naming a mathematical construction or result;
3. user corrections that were memorialized as warnings or disclaimers rather than assimilated into corrected mathematics;
4. outlines that reproduce the chronology of the agent's work rather than the logical or geometric organization of the subject;
5. repeated statements of what was computed or theorem-derived even though code, assertions, proofs, or citations already make this evident;
6. prose, tables, matrices, phases, or inventories that manually mirror facts already recoverable from cells, source, tests, or capability gates;
7. statements whose expected useful lifetime is shorter than the mathematical artifact and which will become false after the next nearby edit;
8. information duplicated across introductions, roadmaps, status tables, section conclusions, and final summaries, creating several synchronization obligations;
9. limitations or future work repeated globally instead of placed once at the exact mathematical boundary where they matter;
10. whether a concise theorem, remark, footnote, local forward pointer, generated view, or separate operational artifact would preserve the substantive information without burdening the exposition;
11. whether the notebook remains readable as a mathematical document after all conversation-specific history and momentary state descriptions are erased;
12. which identifiable reader, other than the agent recording its own state, needs each surviving piece of status prose.

Flag **meta-epistemic narration** when prose reports the artifact's own state instead of presenting mathematics. Flag **reflexive editorial accretion** when each correction produces another explanatory paragraph. Flag **correction memorialization** when the history of a repaired mistake survives as a standing warning. Flag **state mirroring** when prose duplicates the current code or notebook state. Flag **synchronization burden** when the same volatile fact must be manually updated in several places. Flag **transient-plan fossilization** when a temporary next step remains after work has moved on. Flag **audience-free documentation** when text exists only to externalize the agent's current context and has no durable reader.

Do not prohibit ordinary mathematical introductions, section roadmaps, summary theorems, remarks, or explicit distinctions between computation and deduction. The criterion is substantive ownership and durability. A sentence such as “By Proposition 2.7, the quotient is Enriques” contributes to the argument. A heading such as “What this notebook has established” usually reports on the artifact instead of stating a theorem.

Use two complementary tests.

- **Assimilation test:** after a correction, identify the definition, claim, proof, code cell, or section organization that should change. Make that change and remove the conversational scaffolding.
- **Derivability and lifetime test:** when prose merely restates information recoverable from the artifact and will change whenever the artifact changes, delete it, generate it from the source of truth, or move it to an explicitly maintained status artifact.

A short forward note can be useful at the exact boundary of unfinished mathematics. It should state the next object, construction, or obstruction and should be removed or rewritten once that work begins. Version control owns historical snapshots; the mathematical notebook should not preserve a prose image of every intermediate state.

A valid assistant-facing rule should cause the agent to write a short mathematical setup such as “Let \(Y=\mathbf P^1\times\mathbf P^1\) with involution \(\tau\); we study invariant \((4,4)\)-divisors and the associated covers and quotients,” rather than an editorial account explaining that the notebook contains several evolving investigations, has no immutable central question, and currently occupies a particular phase.