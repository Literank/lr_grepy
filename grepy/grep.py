import re

def grep(pattern, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matching_lines = [line.strip() for line in lines if re.search(pattern, line)]
        return matching_lines
