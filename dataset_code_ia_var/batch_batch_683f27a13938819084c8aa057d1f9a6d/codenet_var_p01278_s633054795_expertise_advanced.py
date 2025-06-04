import sys
from functools import reduce
from itertools import islice

readline = sys.stdin.readline
write = sys.stdout.write

EPS = 1e-9

def cross(o, a, b):
    (ox, oy), (ax, ay), (bx, by) = o, a, b
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)

def cross_point(p0, p1, q0, q1):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p0, p1, q0, q1
    dx0, dy0, dx1, dy1 = x1 - x0, y1 - y0, x3 - x2, y3 - y2
    s = (y0 - y2) * dx1 - (x0 - x2) * dy1
    det = dx0 * dy1 - dy0 * dx1
    if abs(det) < EPS: return None
    return (x0 + s * dx0 / det, y0 + s * dy0 / det)

def convex_cut(P, line):
    q0, q1 = line
    N = len(P)
    res = []
    cyclic_P = P[-1:] + P
    crosses = [cross(q0, q1, pt) for pt in cyclic_P]
    for i, (p0, p1) in enumerate(zip(cyclic_P, islice(cyclic_P, 1, None))):
        c0, c1 = crosses[i], crosses[i+1]
        if c0 * c1 < EPS:
            v = cross_point(q0, q1, p0, p1)
            if v: res.append(v)
        if c1 > -EPS:
            res.append(p1)
    return res

def polygon_area(P):
    return abs(sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1) in zip(P, P[1:]+P[:1]))) / 2

def solve():
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0: return False
    P = [tuple(map(int, readline().split())) for _ in range(N)]
    Q = [tuple(map(int, readline().split())) for _ in range(M)]
    for idx, (x0, y0) in enumerate(Q):
        clipped = P
        for jdx, (x1, y1) in enumerate(Q):
            if idx == jdx: continue
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            q0 = (mx, my)
            q1 = (mx - (y1 - y0), my + (x1 - x0))
            clipped = convex_cut(clipped, (q0, q1))
        write(f"{polygon_area(clipped):.16f}\n")
    return True

while solve():
    pass