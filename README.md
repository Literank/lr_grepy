# lr_grepy

Example project: grep-like CLI app implemented in Python.

PyPI: [https://pypi.org/project/lr-grepy/](https://pypi.org/project/lr-grepy/)

## Install

```bash
make install
```

## Usage

```txt
usage: grepy [-h] [-c] [-i] [-n] [-r] [-v] pattern [file_paths [file_paths ...]]

A grep-like command-line utility from LiteRank.

positional arguments:
  pattern             The pattern to search for
  file_paths          File paths to search in

optional arguments:
  -h, --help          show this help message and exit
  -c, --count         Only a count of selected lines is written to standard output.
  -i, --ignore-case   Perform case insensitive matching. By default, it is case sensitive.
  -n, --line-number   Each output line is preceded by its relative line number in the file, starting at line 1. This option is ignored if -c is specified.
  -r, --recursive     Recursively search subdirectories listed.
  -v, --invert-match  Selected lines are those not matching any of the specified patterns.
```

### Search

```bash
grepy pattern *txt

cat *py | grepy pattern
```

### Recursive Search

```bash
grepy -r pattern .
```

### Search Multiple Files

```bash
grepy pattern a.txt b.py c.cpp
```

### Show Line Numbers

```bash
grepy -n pattern *txt
```

See [project tutorial](https://literank.com/project/9/intro) here.
