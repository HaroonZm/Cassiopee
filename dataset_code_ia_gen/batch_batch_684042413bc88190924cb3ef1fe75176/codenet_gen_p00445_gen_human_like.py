import sys

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    count_joi = 0
    count_ioi = 0
    for i in range(len(s) - 2):
        triple = s[i:i+3]
        if triple == "JOI":
            count_joi += 1
        elif triple == "IOI":
            count_ioi += 1
    print(count_joi)
    print(count_ioi)