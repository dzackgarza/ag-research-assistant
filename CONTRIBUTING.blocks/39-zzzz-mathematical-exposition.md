## Audit meta-status narration and reflexive editorial accretion

When a mathematical notebook contains headings or paragraphs about what the notebook records, what it has established, how its question evolved, or which stage of work has been reached, do not treat the problem as a preference for shorter prose. Review whether conversational corrections and internal status tracking have displaced standard mathematical exposition.

First determine the artifact type. A status report, research log, implementation plan, or framework-wide outstanding-work document may legitimately discuss its own state. A notebook whose primary purpose is to develop mathematics should normally present the mathematical objects, constructions, calculations, theorems, and questions directly.

Require the analysis to identify:

1. sentences whose grammatical subject is the notebook, section, agent, investigation, current stage, or verification status rather than a mathematical object or claim;
2. headings that announce completion, scope, or editorial history instead of naming a mathematical construction or result;
3. user corrections that were memorialized as warnings or disclaimers rather than assimilated into corrected mathematics;
4. outlines that reproduce the chronology of the agent's work rather than the logical or geometric organization of the subject;
5. repeated statements of what was computed or theorem-derived even though code, assertions, proofs, or citations already make this evident;
6. limitations or future work repeated globally instead of placed once at the exact mathematical boundary where they matter;
7. prose that paraphrases a code cell merely to announce that the computation occurred;
8. whether a concise theorem, remark, footnote, or local qualification would preserve the substantive information without interrupting the exposition;
9. whether the notebook remains readable as a mathematical document after all conversation-specific history is erased;
10. whether status material should be moved to a separate contributor-facing or operational artifact.

Flag **meta-epistemic narration** when the prose repeatedly reports the artifact's own state instead of presenting mathematics. Flag **reflexive editorial accretion** when each user correction produces another explanatory paragraph in the notebook. Flag **correction memorialization** when the repaired artifact preserves the history of the mistake as a standing warning. Flag **status-prose intrusion** when progress reporting interrupts a mathematical argument. Flag **chronological organization** when session order replaces mathematical dependency. Flag **warning diffusion** when one precise limitation is restated throughout the artifact.

Do not prohibit ordinary mathematical introductions, section roadmaps, summary theorems, remarks, or explicit distinctions between computation and deduction. The criterion is substantive ownership. A sentence such as “By Proposition 2.7, the quotient is Enriques” contributes to the argument. A heading such as “What this notebook has established” usually reports on the artifact instead of stating a theorem.

Use the assimilation test: after a correction, ask what definition, claim, proof, code cell, or section organization should change. Make that change and remove the conversational scaffolding. The corrected notebook should preserve the mathematics that survived review, not a trace of every nudge required to obtain it.

A valid assistant-facing rule should cause the agent to write a short mathematical setup such as “Let \(Y=\mathbf P^1\times\mathbf P^1\) with involution \(\tau\); we study invariant \((4,4)\)-divisors and the associated covers and quotients,” rather than an editorial account explaining that the notebook contains several evolving investigations and has no immutable central question.
