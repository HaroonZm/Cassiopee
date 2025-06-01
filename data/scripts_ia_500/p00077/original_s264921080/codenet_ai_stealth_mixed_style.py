import sys
import re

def process_line(line):
    parts = re.split('(@.{2})', line)
    res = []
    for segment in parts:
        if segment.startswith('@'):
            count = int(segment[1])
            char = segment[2]
            res.append(char * count)
        else:
            res.append(segment)
    return "".join(res)

for line in sys.stdin:
    output = process_line(line)
    print(output, end='')