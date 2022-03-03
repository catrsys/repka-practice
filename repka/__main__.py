import argparse
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from . import extractor, selecter

REPKA_IMAGE = """\033[92m
               ░░░░
       ░░░░  ░░▓▓▓▓░░  ░░░░
       ░░▓▓░░░░▓▓▓▓░░░░▓▓░░
         ░░▓▓░░▓▓▓▓░░▓▓░░
           ░░▓▓▓▓▓▓▓▓░░\033[93m
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   ▒▒████████████████████████▒▒
 ▒▒████████████████████████████▒▒
 ▒▒██████▒▒▒▒████████▒▒▒▒██████▒▒
 ▒▒████▒▒████▒▒████▒▒████▒▒████▒▒
 ▒▒████████████████████████████▒▒
   ▒▒█████████▒████▒█████████▒▒
     ▒▒▒▒██████▒▒▒▒██████▒▒▒▒
         ▒▒▒▒████████▒▒▒▒
             ▒▒████▒▒
               ▒▒▒▒
                ▒▒\033[00m"""

REPKA_TEXT = r"""
 _____  _____  _____  __ ___ _____ 
/  _  \/   __\/  _  \|  |  //  _  \
|  _  <|   __||   __/|  _ < |  _  |
\__|\_/\_____/\__/   |__|__\\__|__/
"""

REPKA_LOGO = REPKA_IMAGE + REPKA_TEXT


def main() -> None:
    """main"""

    parser = argparse.ArgumentParser(
        description=f"{REPKA_LOGO}\n"
        "A tool for open-source software version detection by its repository.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-u", "--uri", help="URI of the target", required=True, type=str)
    parser.add_argument(
        "-p", "--path", help="path to the local copy of the repository", required=True, type=Path
    )
    parser.add_argument(
        "-f", "--folder", help="repository folder with files to compare with", type=Path
    )
    parser.add_argument("-e", "--extensions", help="file extensions. example: html,css,js")

    args = parser.parse_args()

    try:
        extensions = list(map(lambda x: x.lower(), args.extensions.split(",")))
    except AttributeError:
        extensions = []

    repo_folder = args.path
    if args.folder:
        repo_folder /= args.folder

    with TemporaryDirectory() as tempdir:
        tempdir_path = Path(tempdir)

        extractor.download_static_files(args.uri, tempdir_path, extensions)

        from_commit, to_commit = selecter.get_commits_range(tempdir_path, repo_folder)

        tags = selecter.get_tags_by_range(from_commit, to_commit, repo_folder)

    print(f"Commits range: {from_commit}..{to_commit}")
    if tags:
        print(f"Tags: {', '.join(tags)}")


if __name__ == "__main__":
    try:
        main()

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
