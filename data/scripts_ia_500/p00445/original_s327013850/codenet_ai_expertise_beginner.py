import sys

for line in sys.stdin:
    parts = []
    length = len(line)
    for i in range(length - 2):
        parts.append(line[i:i+3])
    count_joi = parts.count("JOI")
    count_ioi = parts.count("IOI")
    print(count_joi)
    print(count_ioi)