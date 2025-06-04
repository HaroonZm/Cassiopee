from sys import stdin
from itertools import islice

lines = iter(stdin.readline, '')
while True:
    try:
        m, nMin, nMax = map(int, next(lines).split())
        if m == 0 and nMax == 0 and nMin == 0:
            break
        P = list(map(int, islice(lines, m)))
        diffs = [P[n] - P[n+1] for n in range(nMin, nMax+1)]
        max_idx = max(range(len(diffs)), key=lambda i: diffs[i])
        print(nMin + max_idx)
    except (StopIteration, ValueError):
        break