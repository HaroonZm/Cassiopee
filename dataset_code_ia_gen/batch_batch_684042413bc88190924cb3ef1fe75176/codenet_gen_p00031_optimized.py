import sys

weights = [1 << i for i in range(10)]

for line in sys.stdin:
    w = line.strip()
    if not w:
        continue
    w = int(w)
    res = []
    for i in range(10):
        if w & (1 << i):
            res.append(str(weights[i]))
    print(" ".join(res))