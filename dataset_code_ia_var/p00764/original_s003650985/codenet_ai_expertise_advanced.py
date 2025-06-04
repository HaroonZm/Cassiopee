from math import hypot, sqrt
from functools import lru_cache
import sys

def input_gen():
    for line in sys.stdin:
        yield line.rstrip('\n')
inputs = input_gen()
next_input = lambda: next(inputs)

while True:
    n = int(next_input())
    if not n:
        break

    C = [list(map(int, next_input().split())) for _ in range(n)]
    P = [[tuple(C[0][:2])]]
    for i, (c0, c1) in enumerate(zip(C, C[1:])):
        x0, y0, r0 = c0
        x1, y1, r1 = c1
        dx, dy = x1 - x0, y1 - y0
        rr = dx * dx + dy * dy
        rd = sqrt(rr)
        rc = (r0**2 + rr - r1**2) / (2 * rd)
        rs = sqrt(max(0, 4 * r0**2 * rr - (r0**2 + rr - r1**2)**2)) / (2 * rd)
        ex, ey = dx / rd, dy / rd
        bx, by = x0 + ex * rc, y0 + ey * rc
        P.append([
            (bx + ey * rs, by - ex * rs),
            (bx - ey * rs, by + ex * rs)
        ])
    P.append([tuple(C[-1][:2])])

    @lru_cache(maxsize=None)
    def calc(a, b):
        return hypot(b[0] - a[0], b[1] - a[1])

    @lru_cache(maxsize=None)
    def cross(a, b, c):
        x0, y0 = a
        x1, y1 = b
        x2, y2 = c
        return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

    INF = float('inf')
    dist = {(0, 0): 0.0}

    for i, pts in enumerate(P[:-1]):
        for j, (x, y) in enumerate(pts):
            left = right = p_left = p_right = None
            d = dist.get((i, j), INF)
            for k in range(i+1, len(P)-1):
                lp, rp = P[k]
                if left is None or cross((x, y), left, lp) >= 0:
                    left = lp
                if right is None or cross((x, y), rp, right) >= 0:
                    right = rp
                if cross((x, y), left, right) < 0:
                    break
                if p_left != left:
                    idx = (k, 0)
                    dist[idx] = min(dist.get(idx, INF), d + calc((x, y), left))
                    p_left = left
                if p_right != right:
                    idx = (k, 1)
                    dist[idx] = min(dist.get(idx, INF), d + calc((x, y), right))
                    p_right = right
            else:
                goal = P[-1][0]
                lchk = left is None and right is None
                if lchk or (cross((x, y), left, goal) >= 0 and cross((x, y), goal, right) >= 0):
                    idx = (len(P)-1, 0)
                    dist[idx] = min(dist.get(idx, INF), d + calc((x, y), goal))

    print(f"{dist[len(P)-1, 0]:.6f}")