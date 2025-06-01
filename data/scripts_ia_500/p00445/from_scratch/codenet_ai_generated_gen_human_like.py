import sys

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    joi_count = 0
    ioi_count = 0
    for i in range(len(s)-2):
        tri = s[i:i+3]
        if tri == "JOI":
            joi_count += 1
        elif tri == "IOI":
            ioi_count += 1
    print(joi_count)
    print(ioi_count)