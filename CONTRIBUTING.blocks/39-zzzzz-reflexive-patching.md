## Audit reflexive patching and editor-generated counterrules

A correction to the editor's interpretation is not automatically a new behavior rule for the Algebraic Geometry assistant. Distinguish the failure present in the source transcript from a failure introduced while editing the guide.

A characteristic bad sequence is:

\[
\text{user intends }X
\longrightarrow
\text{editor writes }X'
\longrightarrow
\text{user rejects }X'
\longrightarrow
\text{guide says }X\text{ and never }X'.
\]

The final clause about \(X'\) usually records only the editor's detour. Replace the mistaken formulation by the intended rule; do not append a permanent counterrule unless the underlying AG-assistant transcripts independently exhibit the opposite failure.

For every proposed corrective clause, ask:

1. Which actor made the error: the deployed AG assistant, the current editor, or both?
2. Would this rule have been written if the preceding user instruction had been understood correctly on the first pass?
3. Does the source material show the prohibited behavior, or is it only a reaction to the editor's own wording?
4. Is the substantive mathematical principle already present elsewhere in the guide?
5. Can one positive governing rule replace a paired instruction of the form “do \(X\), but never \(X'\)”?
6. Did a concrete example become a standing exception, disclaimer, or anti-example solely because the editor overread it?
7. Did a later section duplicate an earlier section instead of revising it at its natural location?

Flag **reflexive patching** when the editor answers a correction by appending a negation of its own previous mistake. Flag **counterrule fossilization** when a one-turn misunderstanding survives as permanent assistant guidance. Flag **editor-error leakage** when contributor mistakes are routed into `STYLE_GUIDE.md`. Flag **corrective accretion** when successive objections produce parallel sections rather than a coherent revision of the original rule.

Use the correction-chain audit:

1. reconstruct the user's original intended principle;
2. identify the first guide clause that departed from it;
3. replace or delete that clause at its canonical source;
4. remove later counterrules whose only purpose was to negate the departure;
5. consolidate genuinely independent mathematical constraints;
6. verify that the source incident is still prevented without mentioning the editor's detour;
7. rebuild the generated guide and review the resulting section as a standalone prompt.

Changelog entries and contributor analyses may preserve the editing history. The deployed guide should contain only durable forward-facing behavior required of the AG assistant.
