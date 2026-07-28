## Deterministic local preparation and connector publication

Do not choose a publication mechanism interactively after the edit is finished. Use the repository tooling to validate the local state and prepare an exact connector handoff, but distinguish local preparation from remote publication.

The usable local sequence is:

```bash
make build
make check
git add -A
git commit -m "<reviewed change>"
make publish-plan BASE=<reviewed-upstream-commit>
```

`make publish-plan` writes `.publication/manifest.json`. The manifest records the base and local commits, every changed path, the expected old blob SHA, the exact new `git hash-object` value, file mode and size, whether the path is generated, and the required verification steps.

A connector-only assistant cannot run `make publish-api`: it cannot supply a `GITHUB_TOKEN`, and the GitHub connector cannot execute the local script or consume the manifest automatically. The token-backed command is optional tooling for a human, CI job, or agent environment that actually has GitHub credentials:

```bash
GITHUB_TOKEN=... make publish-api BASE=<expected-current-remote-commit>
```

For this assistant, the actual publication workflow is:

1. Run the local build, checks, commit, and publication-plan steps.
2. Read `.publication/manifest.json` and identify only the changed canonical source files. Prefer small files under `STYLE_GUIDE.parts/`, `CONTRIBUTING.blocks/`, and `CHANGELOG.entries/` over generated documents.
3. For each changed existing path, call `GitHub.fetch_file` immediately before writing and require its blob SHA to equal the manifest's `old_blob_sha`.
4. Send the exact complete local contents through `GitHub.update_file`; use `GitHub.create_file` for new paths and `GitHub.delete_file` for deletions.
5. Perform writes sequentially. The connector contents API may create several commits; do not describe them as one atomic local commit.
6. Refetch every changed source path and require its remote blob SHA to equal the manifest's `new_blob_sha`.
7. Allow the repository workflow to rebuild generated artifacts, then refetch and verify `STYLE_GUIDE.md`, `CONTRIBUTING.md`, and `CHANGELOG.md` as applicable.
8. Report the actual remote commit sequence and any generated follow-up commit.

Use this fixed decision order:

1. Use ordinary `git push` when authenticated Git transport works.
2. In an environment that genuinely has a GitHub token, `scripts/publish.py publish` may publish atomically.
3. In this connector-only environment, use the explicit connector sequence above.
4. Stop and report the exact missing transport capability if the connector cannot perform a required create, update, delete, or refetch operation.

Do not create temporary workflows, trigger files, transport pull requests, patch-chunk branches, or competing publication mechanisms merely because one connector call failed. Those mechanisms require an explicit repository-level need and review; they are not the default fallback.
