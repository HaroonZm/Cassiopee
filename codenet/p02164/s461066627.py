from math import atan2, degrees
from itertools import permutations

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
px = py = 0
ans = float("inf")
for t in permutations(XY):
    a = 0
    deg = 0
    for x, y in t + ([0, 0],):
        d = degrees(atan2(y-py, x-px))
        delta = deg - d
        if delta < 0: delta += 360
        if delta > 180: delta = 360 - delta
        a += delta

        px, py = x, y
        deg = d
    ans = min(a, ans)
print(ans)