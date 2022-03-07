<div align='center'>

![Repka logo](./assets/repka_logo.png "Repka")

</div>

# Repka

A tool for open-source software version detection by its repository.

## Installation

```bash
pip install .
```

## Usage

```text
python -m repka [-h] -u URI -p PATH [-f FOLDER] [-e EXTENSIONS]

optional arguments:
  -h, --help            show this help message and exit
  -u URI, --uri URI     URI of the target
  -p PATH, --path PATH  path to the local copy of the repository
  -f FOLDER, --folder FOLDER
                        repository folder with files to compare with
  -e EXTENSIONS, --extensions EXTENSIONS
                        file extensions. example: html,css,js
```

Target `URI` and `path` to the local copy of repository are the only required parameters.

If `folder` is specified, `Repka` will try to compare files from that subfolder of the repository.

`Extensions` argument is used to filter files being compared by their types.

## Example

```text
python3.9 -m repka -u "https://kot-pes.com/" -p "../wp-polls/"
[*] Extracting files...
[+] Extraction finished.
[*] Searching for commits and tags...
[+] Done.

[+] Commits range: 028a5e0407c63bce0771d6fe82cf6dded1076f9f..9b52a5ae7ded437d5744dcb4b1798752a6754e06
```
