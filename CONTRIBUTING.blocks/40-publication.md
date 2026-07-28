## Single-command publication workflow

Do not choose a publication mechanism interactively after the edit is finished. Use the repository tooling to make the decision deterministic.

The standard local sequence is:

```bash
make build
make check
git add -A
git commit -m "<reviewed change>"
make publish-plan BASE=<reviewed-upstream-commit>
```

`make publish-plan` writes `.publication/manifest.json`. The manifest records the base and local commits, every changed path, the expected old blob SHA, the exact new `git hash-object` value, file mode and size, whether the path is generated, and the connector verification steps. It is the handoff artifact for connector-backed publication.

When `GITHUB_TOKEN` is available, publish the reviewed tree atomically through GitHub's Git Data API:

```bash
GITHUB_TOKEN=... make publish-api BASE=<expected-current-remote-commit>
```

`scripts/publish.py` refuses to publish a dirty worktree, refuses a moved remote base, creates blobs from the exact committed local bytes, verifies every returned blob SHA, creates one tree and commit, updates the branch without force, and verifies the resulting remote tree.

Use this fixed decision order:

1. Use ordinary `git push` when authenticated Git transport works.
2. Otherwise use `scripts/publish.py publish` when a GitHub token is available.
3. Otherwise use the connector with `.publication/manifest.json`: update only the changed canonical files with current-SHA preconditions and verify the returned blob identities. Publish source fragments before generated artifacts and allow the repository workflow to rebuild generated files.
4. Stop and report the exact missing transport capability if none of these routes is available.

Do not create temporary workflows, trigger files, transport pull requests, patch-chunk branches, or competing publication mechanisms merely because one API call failed. Those mechanisms require an explicit repository-level need and review; they are not the default fallback.
