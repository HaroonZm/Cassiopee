import re
import sys

def read_input():
    return sys.stdin

def process_lines(lines):
    for line in lines:
        process_line(line)

def process_line(line):
    parts = split_line(line)
    for part in parts:
        process_part(part)

def split_line(line):
    return re.split('(@.{2})', line)

def process_part(part):
    if contains_at_symbol(part):
        expanded = expand_part(part)
        write_output(expanded)
    else:
        write_output(part)

def contains_at_symbol(text):
    return '@' in text

def expand_part(part):
    repeat_count = extract_repeat_count(part)
    char_to_repeat = extract_char_to_repeat(part)
    return char_to_repeat * repeat_count

def extract_repeat_count(part):
    return int(part[1])

def extract_char_to_repeat(part):
    return part[2]

def write_output(text):
    sys.stdout.write(text)

def main():
    lines = read_input()
    process_lines(lines)

main()