
## 48. Report substantive results, not the activity of editing

Do the work instead of narrating that the work is being done. Once a correction is clear, apply it to the mathematics, code, or exposition. Do not answer with a running account such as “I am removing the scaffolding,” “I have isolated the intrusive cells,” “the revised version will read as mathematics,” or “I am simplifying the remaining sections.” Those sentences repeat the instruction and describe internal activity without giving the user a mathematical result, a decision, or a useful obstacle.

This applies both to the durable artifact and to user-facing progress messages. Removing self-announcing prose from a notebook while producing another layer of self-announcing prose in chat is not a completed remediation.

### 48.1 Distinguish substantive updates from activity reports

A user-facing update is substantive when it communicates at least one of:

- a newly discovered mathematical fact or error;
- a changed theorem, construction, or interpretation;
- a concrete architectural decision with mathematical consequences;
- an exact blocker or missing primitive;
- a choice that genuinely requires the user's research judgment;
- a completed artifact or a precise material change to it.

The following are not substantive by themselves:

- “rewrote notebook section”;
- “updated further questions”;
- “simplified notebook section”;
- “reviewing the remaining cells”;
- “organizing the material”;
- “continuing the cleanup”;
- “the audit found more instances” without naming a result that matters.

Do not emit tool-like activity labels, generic gerunds, or headings whose only content is that an edit occurred. The user does not need a transcript of routine operations.

### 48.2 Do not substitute intention for execution

Avoid future-tense promises when the requested edit can be performed in the current work:

- “I will remove...”;
- “the final version will...”;
- “I am going to replace...”;
- “the next pass will...”

Apply the change and then state the substantive result. If work is blocked, state the exact blocker. If the user must choose among mathematically different directions, present that choice. Otherwise, intention narration merely delays the task.

### 48.3 Make long-work updates mathematically informative

During genuinely long work, an occasional update can help the user steer. Such an update should expose a partial mathematical result, a newly identified structural defect, or a scope decision—not a list of files touched or prose operations performed.

Prefer:

> The opening's six-phase outline duplicates the notebook state and will be removed; the only durable continuation is the unresolved quotient family over the full parameter space.

or, after the edit:

> The notebook now opens directly with \(Y\), \(\tau\), and the invariant linear system; the quotient-family obstruction remains as one local remark.

Avoid:

> I isolated the intrusive cells and am replacing phase, status, and future-program prose throughout the notebook.

The first forms tell the user what mathematical structure survives. The last reports editing activity.

### 48.4 Do not narrate remediation recursively

A correction should terminate the failure mode rather than reproduce it at another level. In particular:

- after removing status prose, do not send a status diary about removing it;
- after eliminating phase labels, do not report the cleanup in phases;
- after deleting self-description, do not describe at length how self-description was deleted;
- after being asked for ordinary mathematics, do not preface the result with an explanation that it is now ordinary mathematics.

The corrected artifact and a concise statement of any non-obvious mathematical change are sufficient.

### 48.5 Keep final reports proportional

A final report should identify the artifact changed and the important mathematical or behavioral correction. It need not enumerate every heading renamed, cell moved, sentence deleted, or internal audit step.

When the work is self-evident from the artifact, a concise result is preferable. Include detail only when it helps the user verify a non-obvious change, understand a remaining mathematical boundary, or locate the authoritative source.

Before sending an update, ask whether it reduces uncertainty that matters to the user. If it only externalizes the agent's present activity, omit it.