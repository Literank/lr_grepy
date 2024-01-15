import re
import os

def _filter_lines(pattern, lines, flag):
    return [(line_number, line.strip()) for line_number, line in enumerate(lines, start=1) if bool(re.search(pattern, line)) == flag]

def grep(pattern, file_path, options=None):
    with open(file_path, 'r') as file:
        try:
            lines = file.readlines()
        except UnicodeDecodeError: # filter out binary files
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

def grep_count(result):
    return sum([len(v) for v in result.values()])

def grep_recursive(pattern, directory_path, options=None):
    results = {}

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            results.update(grep(pattern, file_path, options))

    return results
