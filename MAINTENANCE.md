# Repository Maintenance

This document is for repository maintainers and automation that performs storage, version-control, release, and deployment operations. It is not part of the prompt consumed by the Algebraic Geometry Research Assistant.

For editorial classification, rule extraction, and writing standards, use [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Canonical files

- `STYLE_GUIDE.md` is the assistant-facing operational prompt.
- `CONTRIBUTING.md` governs contributors and editors.
- `INCIDENTS.md` stores classified failures and regression evidence.
- `CHANGELOG.md` records revisions.
- `README.md` provides repository orientation and the audience map.

Chat messages, model memory, summaries, and bounded GPT configuration fields are not canonical storage.

## Update procedure

For each accepted correction:

1. Read the current tracked files.
2. Use `CONTRIBUTING.md` to classify the target audience and failure class.
3. Patch only the files appropriate to that classification.
4. Inspect the diff for accidental deletion, weakening, contradiction, duplication, and audience leakage.
5. Update `INCIDENTS.md` when the source failure supplies useful regression evidence.
6. Update `CHANGELOG.md` when assistant-facing behavior or repository structure changes.
7. Commit the result before claiming that the correction has been incorporated.

Do not use model memory or the current chat transcript as a substitute for reading the tracked files.

## Repository workflow

Use the least elaborate workflow that satisfies the actual requirement.

When authenticated direct writes to `main` are permitted and no review or isolation boundary has been requested, commit accepted changes directly to `main`. Do not create branches or pull requests as ceremony.

Use a branch or pull request only when required by repository policy, review, continuous-integration gates, concurrent work, risk isolation, or an explicit request.

## Preservation checks

Before committing:

1. verify that every changed file still serves its declared audience;
2. verify that no contributor or maintenance instruction entered `STYLE_GUIDE.md`;
3. verify that no substantive AG-assistant behavior exists only outside `STYLE_GUIDE.md`;
4. compare against the preceding revision for removed or weakened requirements;
5. verify that detailed incident evidence remains recoverable when rules are consolidated;
6. verify that `README.md` remains accurate after structural changes.

## Deployment

Only `STYLE_GUIDE.md` is intended for upload as operational guidance to the custom GPT unless a deployment manifest explicitly states otherwise.

Any prompt assembled from the repository is a deployment artifact. The tracked files remain authoritative.

When a deployment field is bounded:

1. preserve the complete tracked source;
2. generate the bounded representation deliberately;
3. record omissions or transformations outside `STYLE_GUIDE.md`;
4. do not claim complete deployment coverage without checking it.
