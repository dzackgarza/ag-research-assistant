# Repository Maintenance

This file governs maintenance of the repository. It is not part of the behavioral prompt consumed by the Algebraic Geometry Research Assistant.

## File roles

- `STYLE_GUIDE.md` contains only instructions that should directly shape the assistant's mathematical reasoning, Sage work, implementation choices, and reporting.
- `INCIDENTS.md` records source failures, corrections, and regression criteria.
- `CHANGELOG.md` records revisions to the assistant-facing guide and repository structure.
- `README.md` explains the repository and the role of each file.

Maintenance procedure, provenance, version-control policy, and historical narrative must not be placed in `STYLE_GUIDE.md` unless they directly govern the assistant's work on algebraic geometry or Sage computations.

## Update procedure

For each accepted correction:

1. Read the current tracked files.
2. Identify whether the correction changes assistant behavior, repository process, incident history, or more than one of these.
3. Patch the narrowest appropriate files.
4. Preserve all still-valid behavioral requirements.
5. Inspect the diff for accidental deletion, weakening, contradiction, duplication, and incident-specific overfitting.
6. Add or amend an incident record when the source failure supplies useful regression evidence.
7. Update the changelog when assistant-facing behavior or repository structure changes.
8. Commit the result before claiming that the correction has been incorporated.

Do not use chat history, model memory, summaries, or bounded GPT fields as the canonical store.

## Rule extraction

A concrete incident can support two distinct artifacts:

- a general or Sage-specific rule in `STYLE_GUIDE.md` that the assistant can act on;
- a detailed record in `INCIDENTS.md` that preserves the failure and tests whether the rule prevents recurrence.

Do not burden the assistant-facing guide with explanations of how the guide itself is maintained. Conversely, do not move substantive behavioral constraints into incident history where the assistant will not consume them.

A generalization is valid only when it preserves the operational content of the source correction. A compact slogan must not replace stronger concrete constraints. Named Sage examples should remain in the guide when they materially instruct the assistant's frequent Sage work; incidental details should remain only in the incident record.

## Repository workflow

Use the least elaborate workflow that satisfies the actual requirement.

When authenticated direct writes to `main` are permitted and no review or isolation boundary has been requested, commit accepted changes directly to `main`. Do not create branches or pull requests as ceremony.

Use a branch or pull request only when required by repository policy, review, continuous-integration gates, concurrent work, risk isolation, or an explicit request.

## Deployment

Any custom-GPT configuration generated from `STYLE_GUIDE.md` is a deployment artifact. The tracked file remains authoritative.

When a deployment field is bounded:

1. preserve the complete tracked guide;
2. generate the bounded representation deliberately;
3. record omissions or transformations outside the assistant-facing guide;
4. do not claim complete deployment coverage without checking it.
