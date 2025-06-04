import sys
import math
from functools import lru_cache
from itertools import islice

def readints():
    return list(map(int, sys.stdin.readline().split()))

def fast_input():
    for line in sys.stdin:
        yield line.rstrip('\n')

input_iter = fast_input()
next_line = input_iter.__next__

while True:
    try:
        n = int(next_line())
    except StopIteration:
        break
    if n == 0:
        break

    C = [readints() for _ in range(n)]
    P = [[tuple(C[0][:2])]]

    for i in range(n - 1):
        x0, y0, r0 = C[i]
        x1, y1, r1 = C[i + 1]
        dx, dy = x1 - x0, y1 - y0
        rr = dx * dx + dy * dy
        rd = math.hypot(dx, dy)
        rc = (r0 * r0 + rr - r1 * r1) / (2 * rd)
        discr = 4 * r0 * r0 * rr - (r0 * r0 + rr - r1 * r1) ** 2
        if discr < 0:  # robust: tangent circles or no intersection
            rs = 0.0
        else:
            rs = math.sqrt(discr) / (2 * rd)
        ex, ey = dx / rd, dy / rd
        bx, by = x0 + ex * rc, y0 + ey * rc
        ip1 = (bx + ey * rs, by - ex * rs)
        ip2 = (bx - ey * rs, by + ex * rs)
        P.append([ip1, ip2])
    P.append([tuple(C[-1][:2])])

    def calc(p0, p1):
        return math.hypot(p1[0] - p0[0], p1[1] - p0[1])

    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

    INF = float('inf')
    dist = {(0, 0): 0.0}

    for i, pts in enumerate(islice(P, len(P) - 1)):
        for j, (x, y) in enumerate(pts):
            left = p_left = right = p_right = None
            d = dist.get((i, j), INF)
            for k in range(i + 1, len(P) - 1):
                lp, rp = P[k]
                if left is None or cross((x, y), left, lp) >= 0:
                    left = lp
                if right is None or cross((x, y), rp, right) >= 0:
                    right = rp
                if cross((x, y), left, right) < 0:
                    break
                if p_left != left:
                    cur = dist.get((k, 0), INF)
                    dist[(k, 0)] = min(cur, d + calc((x, y), left))
                    p_left = left
                if p_right != right:
                    cur = dist.get((k, 1), INF)
                    dist[(k, 1)] = min(cur, d + calc((x, y), right))
                    p_right = right
            else:
                goal = P[-1][0]
                cond = (left is None and right is None) or \
                       (cross((x, y), left, goal) >= 0 and cross((x, y), goal, right) >= 0)
                if cond:
                    cur = dist.get((len(P) - 1, 0), INF)
                    dist[(len(P) - 1, 0)] = min(cur, d + calc((x, y), goal))

    print(f"{dist[(len(P) - 1, 0)]:.6f}")