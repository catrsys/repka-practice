<div align='center'>

![Repka logo](./assets/repka_logo.png "Repka")

</div>

# Repka
A tool for open-source software version detection by its repository.

## Usage

```
usage: repka.py [-h] -u URI -p PATH [-f FOLDER] [-e EXTENSIONS]

optional arguments:
  -h, --help            show this help message and exit
  -u URI, --uri URI     URI of the target
  -p PATH, --path PATH  path to the local copy of the repository
  -f FOLDER, --folder FOLDER
                        repository folder with files to compare with
  -e EXTENSIONS, --extensions EXTENSIONS
                        file extensions. example: html,css,js
```

Target ```URI``` and ```path``` to the local copy of repository are the only required parameters.

If ```folder``` is specified, ```Repka``` will try to compare files from that subfolder of the repository.

A list of ```extensions``` can be omitted if the ```URI``` provided points to the file to be compared. Otherwise, files from ```path``` (or ```folder```, if specified) with those extensions are selected for comparison.