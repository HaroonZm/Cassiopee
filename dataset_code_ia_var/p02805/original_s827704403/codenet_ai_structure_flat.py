from collections import combinations
from math import sqrt
import sys

sys.setrecursionlimit(2147483647)
INF = 10 ** 20

mod = 1000000007

n = int(sys.stdin.buffer.readline())
L = []
for _ in range(n):
    L.append(tuple(map(int, sys.stdin.buffer.readline().split())))

ans = INF

for idxs in combinations(range(n), 3):
    i, j, k = idxs
    x1, y1 = L[i]
    x2, y2 = L[j]
    x3, y3 = L[k]
    a2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
    b2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
    c2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    area = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    if area == 0:
        continue
    x = (a2 * (b2 + c2 - a2) * x1 + b2 * (c2 + a2 - b2) * x2 + c2 * (a2 + b2 - c2) * x3) / (16 * area * area)
    y = (a2 * (b2 + c2 - a2) * y1 + b2 * (c2 + a2 - b2) * y2 + c2 * (a2 + b2 - c2) * y3) / (16 * area * area)
    r = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    ok = True
    for d in range(n):
        if d == i or d == j or d == k:
            continue
        ax, ay = L[d]
        if (ax - x) ** 2 + (ay - y) ** 2 > r ** 2:
            ok = False
            break
    if ok:
        ans = min(ans, r)

for idxs in combinations(range(n), 2):
    l, m = idxs
    lx, ly = L[l]
    mx, my = L[m]
    mid_x = (lx + mx) / 2
    mid_y = (ly + my) / 2
    r_s = (mid_x - lx) ** 2 + (mid_y - ly) ** 2
    for i in range(n):
        if i == l or i == m:
            continue
        zx, zy = L[i]
        if (zx - mid_x) ** 2 + (zy - mid_y) ** 2 > r_s:
            break
    else:
        ans = min(ans, sqrt(r_s))

print(ans)