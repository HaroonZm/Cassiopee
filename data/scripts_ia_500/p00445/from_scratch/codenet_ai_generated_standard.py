import sys

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    joi = ioi = 0
    for i in range(len(s) - 2):
        triplet = s[i:i+3]
        if triplet == "JOI":
            joi += 1
        elif triplet == "IOI":
            ioi += 1
    print(joi)
    print(ioi)