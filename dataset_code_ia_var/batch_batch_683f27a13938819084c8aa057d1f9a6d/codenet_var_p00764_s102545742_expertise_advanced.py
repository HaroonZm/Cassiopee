from math import hypot, isclose, sqrt
from sys import stdin, stdout
from functools import lru_cache

readline = stdin.readline
write = stdout.write

def readints():
    return tuple(map(int, readline().split()))

def circle_intersections(c0, c1):
    x0, y0, r0 = c0
    x1, y1, r1 = c1
    dx, dy = x1 - x0, y1 - y0
    d = hypot(dx, dy)
    if isclose(d, 0):
        return ()
    rc = (r0**2 + d**2 - r1**2) / (2 * d)
    rs_sq = 4*r0**2*d**2 - (r0**2 + d**2 - r1**2)**2
    if rs_sq < 0:
        rs_sq = 0
    rs = sqrt(rs_sq) / (2*d)
    ex, ey = dx / d, dy / d
    bx, by = x0 + ex * rc, y0 + ey * rc
    return ((bx + ey * rs, by - ex * rs), (bx - ey * rs, by + ex * rs))

@lru_cache(maxsize=None)
def calc(p0, p1):
    return hypot(p1[0]-p0[0], p1[1]-p0[1])

def cross(o, a, b):
    return (a[0]-o[0]) * (b[1]-o[1]) - (b[0]-o[0]) * (a[1]-o[1])

while True:
    n = int(readline())
    if n == 0: break
    C = [readints() for _ in range(n)]
    P = {(0, 0): C[0][:2], (n, 0): C[-1][:2]}
    for i in range(n-1):
        inters = circle_intersections(C[i], C[i+1])
        P[(i+1, 0)], P[(i+1, 1)] = inters
    INF = float('inf')
    dist = {(0, 0): 0.0}
    goal = P[(n, 0)]
    keys = sorted((k for k in P if len(k) == 2), key=lambda x: (x[0], x[1]))
    for i, j in keys:
        cur = P[(i, j)]
        d = dist.get((i, j), INF)
        left = right = p_left = p_right = None
        for k in range(i+1, n):
            lpt, rpt = P[(k, 0)], P[(k, 1)]
            if left is None or cross(cur, left, lpt) >= 0:
                left = lpt
            if right is None or cross(cur, rpt, right) >= 0:
                right = rpt
            if cross(cur, left, right) < 0: break
            if p_left is not left:
                dist[(k, 0)] = min(dist.get((k, 0), INF), d + calc(cur, left))
                p_left = left
            if p_right is not right:
                dist[(k, 1)] = min(dist.get((k, 1), INF), d + calc(cur, right))
                p_right = right
        else:
            if (left is None and right is None) or (cross(cur, left, goal) >= 0 and cross(cur, goal, right) >= 0):
                dist[(n, 0)] = min(dist.get((n, 0), INF), d + calc(cur, goal))
    write(f"{dist[(n,0)]:.6f}\n")