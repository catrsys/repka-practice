import re
from hashlib import md5
from pathlib import Path
from subprocess import PIPE, Popen


def get_commits_range(files_folder_path: Path, repo_folder_path: Path) -> tuple[str, str]:
    with Popen(
        ["git", "rev-list", "--reverse", "HEAD"], cwd=repo_folder_path, stdout=PIPE, stderr=PIPE
    ) as proc:
        out, errs = proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(f"Something went wrong: {errs.decode('utf-8')}")

    from_commit, *_, to_commit = out.decode("utf-8").split()

    for file in files_folder_path.iterdir():
        if not file.is_file():
            continue

        from_commit, to_commit = _get_file_commits_range(
            file, repo_folder_path, from_commit, to_commit
        )

    return from_commit, to_commit


def get_tags_by_range(from_commit: str, to_commit: str, repo_folder_path: Path) -> list[str]:
    with Popen(
        ["git", "log", f"{from_commit}^..{to_commit}", "--pretty=format:%d"],
        stdout=PIPE,
        stderr=PIPE,
        cwd=repo_folder_path,
    ) as proc:
        out, errs = proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(f"Something went wrong: {errs.decode('utf-8')}")

    return re.findall("tag: (.*?)(?:,|$)", out.decode("utf-8"))


def _get_file_commits_range(
    file_path: Path, repo_folder_path: Path, from_commit: str, to_commit: str
) -> tuple[str, str]:

    with Popen(
        [
            "git",
            "log",
            f"{from_commit}..{to_commit}",
            "--pretty=format:%H",
            "--follow",
            "--",
            file_path.name,
        ],
        cwd=repo_folder_path,
        stdout=PIPE,
        stderr=PIPE,
    ) as proc:
        out, errs = proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(f"Something went wrong: {errs.decode('utf-8')}")

    commits_with_changes = out.decode("utf-8").split()
    if not commits_with_changes:
        return from_commit, to_commit

    try:
        file_hash = md5(file_path.read_bytes()).digest()
    except MemoryError:
        return from_commit, to_commit

    prev_commit = to_commit
    for commit in commits_with_changes:
        with Popen(
            ["git", "show", f"{commit}:{file_path.name}"],
            cwd=repo_folder_path,
            stdout=PIPE,
            stderr=PIPE,
        ) as proc:
            out, errs = proc.communicate()
            if proc.returncode == 128:  # file have different location or name
                continue

            if proc.returncode != 0:
                raise RuntimeError(f"Something went wrong: {errs.decode('utf-8')}")

        commit_file_hash = md5(out).digest()

        if commit_file_hash == file_hash:
            return commit, prev_commit

        prev_commit = commit

    return from_commit, to_commit
