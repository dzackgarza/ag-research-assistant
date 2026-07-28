#!/usr/bin/env python3
"""Validate, plan, and publish an exact reviewed repository state.

The script preserves the ordinary Git workflow when direct ``git push`` is
unavailable.  It never reconstructs files from snippets: publication data is
read from the committed local checkout and verified with Git blob identities.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / ".publication" / "manifest.json"
GENERATED_OUTPUTS = {"STYLE_GUIDE.md"}


class PublicationError(RuntimeError):
    """A deterministic publication precondition failed."""


def run_git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if check and result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise PublicationError(f"git {' '.join(args)} failed: {message}")
    return result.stdout


def run_checked(command: list[str]) -> None:
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode != 0:
        raise PublicationError(f"command failed ({result.returncode}): {' '.join(command)}")


def git_rev(ref: str) -> str:
    return run_git("rev-parse", "--verify", ref).strip()


def git_blob(path: str, ref: str | None = None) -> str | None:
    spec = f"{ref}:{path}" if ref else path
    result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "--verify", spec],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def local_blob(path: str) -> str:
    return run_git("hash-object", "--", path).strip()


def git_mode(path: str, ref: str = "HEAD") -> str:
    line = run_git("ls-tree", ref, "--", path).strip()
    if not line:
        raise PublicationError(f"unable to determine Git mode for {path} at {ref}")
    return line.split(maxsplit=1)[0]


def require_clean() -> None:
    status = run_git("status", "--porcelain=v1", "--untracked-files=all")
    if status:
        raise PublicationError(
            "the worktree is not clean; commit the reviewed local state before publication:\n"
            + status
        )


def validate_repository(require_clean_tree: bool = False, base: str | None = None) -> None:
    run_git("rev-parse", "--is-inside-work-tree")
    run_checked([sys.executable, "scripts/build_style_guide.py", "--check"])
    run_git("diff", "--check")
    if base is not None:
        base_sha = git_rev(base)
        ancestor = subprocess.run(
            ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", base_sha, "HEAD"],
            check=False,
        )
        if ancestor.returncode != 0:
            raise PublicationError(f"base {base_sha} is not an ancestor of HEAD")
        run_git("diff", "--check", f"{base_sha}..HEAD")
    if require_clean_tree:
        require_clean()


@dataclass(frozen=True)
class ChangedFile:
    status: str
    path: str
    old_path: str | None
    old_blob_sha: str | None
    new_blob_sha: str | None
    mode: str | None
    size_bytes: int | None
    generated_output: bool
    content_base64: str | None = None


def _parse_name_status(raw: bytes) -> list[tuple[str, str | None, str]]:
    fields = raw.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()

    parsed: list[tuple[str, str | None, str]] = []
    index = 0
    while index < len(fields):
        status = fields[index].decode("utf-8", "surrogateescape")
        index += 1
        if status.startswith(("R", "C")):
            old_path = fields[index].decode("utf-8", "surrogateescape")
            new_path = fields[index + 1].decode("utf-8", "surrogateescape")
            index += 2
            parsed.append((status, old_path, new_path))
        else:
            path = fields[index].decode("utf-8", "surrogateescape")
            index += 1
            parsed.append((status, None, path))
    return parsed


def changed_files(base: str, include_content: bool = False) -> list[ChangedFile]:
    base_sha = git_rev(base)
    result = subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "diff",
            "--name-status",
            "-z",
            "--find-renames",
            f"{base_sha}..HEAD",
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise PublicationError(result.stderr.decode(errors="replace").strip())

    files: list[ChangedFile] = []
    for status, old_path, path in _parse_name_status(result.stdout):
        kind = status[0]
        old_lookup = old_path if old_path is not None else path
        old_sha = git_blob(old_lookup, base_sha)

        if kind == "D":
            files.append(
                ChangedFile(
                    status=status,
                    path=path,
                    old_path=old_path,
                    old_blob_sha=old_sha,
                    new_blob_sha=None,
                    mode=None,
                    size_bytes=None,
                    generated_output=path in GENERATED_OUTPUTS,
                )
            )
            continue

        file_path = ROOT / path
        if not file_path.is_file():
            raise PublicationError(f"changed path is not a regular file: {path}")
        payload = file_path.read_bytes()
        files.append(
            ChangedFile(
                status=status,
                path=path,
                old_path=old_path,
                old_blob_sha=old_sha,
                new_blob_sha=local_blob(path),
                mode=git_mode(path),
                size_bytes=len(payload),
                generated_output=path in GENERATED_OUTPUTS,
                content_base64=(base64.b64encode(payload).decode("ascii") if include_content else None),
            )
        )
    return files


def build_manifest(
    *,
    base: str,
    repository: str | None,
    branch: str,
    include_content: bool,
) -> dict[str, Any]:
    validate_repository(require_clean_tree=True, base=base)
    base_sha = git_rev(base)
    head_sha = git_rev("HEAD")
    files = changed_files(base_sha, include_content=include_content)
    if not files:
        raise PublicationError(f"no committed changes between {base_sha} and {head_sha}")
    return {
        "schema_version": 1,
        "repository": repository,
        "branch": branch,
        "base_commit": base_sha,
        "head_commit": head_sha,
        "head_subject": run_git("show", "-s", "--format=%s", "HEAD").strip(),
        "generated_outputs": sorted(GENERATED_OUTPUTS),
        "files": [asdict(item) for item in files],
        "connector_instructions": [
            "Fetch the current remote blob SHA for every target path immediately before writing.",
            "Require it to match old_blob_sha; otherwise rebase the local diff.",
            "Send the exact local file bytes, not reconstructed text.",
            "Publish source fragments before generated outputs; allow the repository workflow to rebuild generated outputs when possible.",
            "Refetch every changed path and compare its blob SHA with new_blob_sha.",
        ],
    }


def write_manifest(manifest: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class GitHubClient:
    def __init__(self, repository: str, token: str, api_url: str) -> None:
        self.repository = repository
        self.token = token
        self.api_url = api_url.rstrip("/")

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{self.api_url}{path}",
            data=data,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
                "User-Agent": "ag-research-assistant-publisher",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        try:
            with urllib.request.urlopen(request) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise PublicationError(f"GitHub API {method} {path} failed ({exc.code}): {body}") from exc
        except urllib.error.URLError as exc:
            raise PublicationError(f"GitHub API {method} {path} failed: {exc.reason}") from exc


def publish_atomic(
    *,
    manifest: dict[str, Any],
    token: str,
    api_url: str,
    message: str | None,
    dry_run: bool,
) -> dict[str, Any]:
    repository = manifest.get("repository")
    if not repository:
        raise PublicationError("--repo is required for publication")
    branch = str(manifest["branch"])
    base_sha = str(manifest["base_commit"])
    files = list(manifest["files"])

    if dry_run:
        return {
            "dry_run": True,
            "repository": repository,
            "branch": branch,
            "base_commit": base_sha,
            "files": files,
        }

    client = GitHubClient(str(repository), token, api_url)
    encoded_branch = urllib.parse.quote(branch, safe="")
    ref = client.request("GET", f"/repos/{repository}/git/ref/heads/{encoded_branch}")
    remote_sha = ref["object"]["sha"]
    if remote_sha != base_sha:
        raise PublicationError(
            f"remote {branch} moved: expected {base_sha}, found {remote_sha}; rebase and review again"
        )

    base_commit = client.request("GET", f"/repos/{repository}/git/commits/{base_sha}")
    base_tree_sha = base_commit["tree"]["sha"]
    tree_entries: list[dict[str, Any]] = []

    for item in files:
        status = str(item["status"])[0]
        path = str(item["path"])
        old_path = item.get("old_path")
        if status == "R" and old_path and old_path != path:
            tree_entries.append(
                {
                    "path": old_path,
                    "mode": git_mode(str(old_path), base_sha),
                    "type": "blob",
                    "sha": None,
                }
            )
        if status == "D":
            tree_entries.append(
                {
                    "path": path,
                    "mode": git_mode(path, base_sha),
                    "type": "blob",
                    "sha": None,
                }
            )
            continue

        payload = (ROOT / path).read_bytes()
        blob = client.request(
            "POST",
            f"/repos/{repository}/git/blobs",
            {"content": base64.b64encode(payload).decode("ascii"), "encoding": "base64"},
        )
        expected_blob = item["new_blob_sha"]
        if blob["sha"] != expected_blob:
            raise PublicationError(
                f"GitHub stored unexpected blob for {path}: expected {expected_blob}, got {blob['sha']}"
            )
        tree_entries.append(
            {
                "path": path,
                "mode": item["mode"],
                "type": "blob",
                "sha": blob["sha"],
            }
        )

    new_tree = client.request(
        "POST",
        f"/repos/{repository}/git/trees",
        {"base_tree": base_tree_sha, "tree": tree_entries},
    )
    commit = client.request(
        "POST",
        f"/repos/{repository}/git/commits",
        {
            "message": message or manifest["head_subject"],
            "tree": new_tree["sha"],
            "parents": [base_sha],
        },
    )
    client.request(
        "PATCH",
        f"/repos/{repository}/git/refs/heads/{encoded_branch}",
        {"sha": commit["sha"], "force": False},
    )

    final_commit = client.request("GET", f"/repos/{repository}/git/commits/{commit['sha']}")
    final_tree = client.request(
        "GET",
        f"/repos/{repository}/git/trees/{final_commit['tree']['sha']}?recursive=1",
    )
    by_path = {entry["path"]: entry["sha"] for entry in final_tree.get("tree", []) if entry["type"] == "blob"}
    for item in files:
        status = str(item["status"])[0]
        path = str(item["path"])
        if status == "D":
            if path in by_path:
                raise PublicationError(f"deleted path remains in remote tree: {path}")
        elif by_path.get(path) != item["new_blob_sha"]:
            raise PublicationError(
                f"remote verification failed for {path}: expected {item['new_blob_sha']}, got {by_path.get(path)}"
            )

    return {
        "repository": repository,
        "branch": branch,
        "base_commit": base_sha,
        "commit": commit["sha"],
        "tree": final_commit["tree"]["sha"],
        "verified_files": [item["path"] for item in files],
    }


def parser() -> argparse.ArgumentParser:
    top = argparse.ArgumentParser(description=__doc__)
    sub = top.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="run deterministic repository checks")
    validate.add_argument("--clean", action="store_true", help="also require a clean worktree")

    manifest = sub.add_parser("manifest", help="write a connector/API publication manifest")
    manifest.add_argument("--base", required=True, help="reviewed upstream/base commit or ref")
    manifest.add_argument("--repo", help="GitHub repository in owner/name form")
    manifest.add_argument("--branch", default="main")
    manifest.add_argument("--output", type=Path, default=DEFAULT_MANIFEST)
    manifest.add_argument("--include-content", action="store_true")

    publish = sub.add_parser("publish", help="atomically publish through GitHub's Git Data API")
    publish.add_argument("--base", required=True, help="expected current remote commit; must exist locally")
    publish.add_argument("--repo", required=True, help="GitHub repository in owner/name form")
    publish.add_argument("--branch", default="main")
    publish.add_argument("--token-env", default="GITHUB_TOKEN")
    publish.add_argument("--api-url", default="https://api.github.com")
    publish.add_argument("--message")
    publish.add_argument("--dry-run", action="store_true")

    return top


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "validate":
            validate_repository(require_clean_tree=args.clean)
            print("repository validation passed")
            return 0

        manifest = build_manifest(
            base=args.base,
            repository=args.repo,
            branch=args.branch,
            include_content=getattr(args, "include_content", False),
        )
        if args.command == "manifest":
            write_manifest(manifest, args.output)
            print(args.output)
            return 0

        token = os.environ.get(args.token_env, "")
        if not token and not args.dry_run:
            raise PublicationError(f"environment variable {args.token_env} is not set")
        result = publish_atomic(
            manifest=manifest,
            token=token,
            api_url=args.api_url,
            message=args.message,
            dry_run=args.dry_run,
        )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except PublicationError as exc:
        print(f"publication error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
