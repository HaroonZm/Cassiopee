import re
import sys

def read_input():
    return sys.stdin

def split_line(line):
    return re.split('(@.{2})', line)

def is_encoded_segment(segment):
    return '@' in segment

def decode_segment(segment):
    if len(segment) < 3:
        return segment
    count = int(segment[1])
    char = segment[2]
    return char * count

def process_segment(segment):
    if is_encoded_segment(segment):
        return decode_segment(segment)
    else:
        return segment

def write_output(segment):
    sys.stdout.write(segment)

def process_line(line):
    segments = split_line(line)
    for segment in segments:
        processed = process_segment(segment)
        write_output(processed)

def main():
    for line in read_input():
        process_line(line)

if __name__ == "__main__":
    main()