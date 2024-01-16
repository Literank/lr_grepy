import re
from typing import List, Dict, Tuple, Union
import os
import sys

MatchResults = List[Tuple[int, str]]


def _filter_lines(pattern: Union[str, re.Pattern],
                  lines: List[str], flag: bool) -> MatchResults:
    return [
            (line_number, line.strip())
            for line_number, line in enumerate(lines, start=1)
            if bool(re.search(pattern, line)) == flag
        ]


def grep(pattern: Union[str, re.Pattern],
         file_path: str, options: List[str] = []):
    if not file_path:  # read from stdin, usually the pipe
        lines = sys.stdin.read().split('\n')
    else:  # read from files
        with open(file_path, 'r') as file:
            try:
                lines = file.readlines()
            except UnicodeDecodeError:  # filter out binary files
                return {file_path: []}

    if options:
        if 'i' in options:
            pattern = re.compile(pattern, re.IGNORECASE)
        if 'v' in options:
            matching_lines = _filter_lines(pattern, lines, False)
        else:
            matching_lines = _filter_lines(pattern, lines, True)
    else:
        matching_lines = _filter_lines(pattern, lines, True)

    return {file_path: matching_lines}


def grep_count(result: Dict[str, MatchResults]):
    return sum([len(v) for v in result.values()])


def grep_recursive(pattern: Union[str, re.Pattern],
                   directory_path: str, options: List[str] = []):
    results = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            results.update(grep(pattern, file_path, options))
    return results
