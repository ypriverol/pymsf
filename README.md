# pymsf

Simple script in python to parse ProteomeDiscover msf files and convert them to Tab-delimited file.

- The script is based on the pyproteome library https://github.com/white-lab/pyproteome. The script support the following PD versions:
  - 2.1.X
  - 1.4.X
  - 2.2.X

The script allows to filter the result peptide table by using the Confidence Level `--filter` for High Confidence Peptides.

## Install

```
$> python setup.py
```

## Usage

```
$> pymsf --help
Unable to find any expected data directories relative to /Users/yperez/IdeaProjects/github-repo/BDP/pymsf: CAMV Output, Searched, MS RAW, Figures
Setting base path to /Users/yperez/IdeaProjects/github-repo/BDP/pymsf, consider calling paths.set_base_dir()
Usage: pymsf [OPTIONS]

Options:
  -i, --msf_file TEXT  msf file
  -o, --output TEXT    Output tab
  -f, --filter         Filter only High-confidence peptides
  --help               Show this message and exit.
```
