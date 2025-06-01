from sys import stdin
from itertools import chain

lines = iter(stdin.read().splitlines())
for line in lines:
    n, m = map(int, line.split())
    if n == m == 0:
        break
    up = list(map(int, next(lines).split())) if n else []
    down = list(map(int, next(lines).split())) if m else []
    upDown = sorted(chain(up, down))
    maxlen = max(b - a for a, b in zip(upDown, upDown[1:])) if upDown else 0
    print(maxlen)