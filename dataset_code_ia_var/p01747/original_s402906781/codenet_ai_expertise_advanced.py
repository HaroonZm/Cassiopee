from sys import stdin, stdout
from math import hypot
from operator import itemgetter

readline = stdin.readline
write = stdout.write

def dot3(p0, p1, p2):
    x0, y0 = p0; x1, y1 = p1; x2, y2 = p2
    return (x1 - x0) * (x2 - x0) + (y1 - y0) * (y2 - y0)

def cross3(p0, p1, p2):
    x0, y0 = p0; x1, y1 = p1; x2, y2 = p2
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)

def dist2(p0, p1):
    x0, y0 = p0; x1, y1 = p1
    dx, dy = x0 - x1, y0 - y1
    return dx * dx + dy * dy

def solve():
    N = int(readline())
    P = [tuple(map(int, readline().split())) for _ in range(N)]

    ok = True
    for i in range(N - 1):
        p0, p1 = P[i], P[i+1]
        d0 = hypot(p0[0] - p1[0], p0[1] - p1[1])
        el0, el1, er0, er1 = [-d0, d0], [-d0, d0], [-d0, d0], [-d0, d0]

        for q0 in P[:i]:
            d1 = hypot(p0[0] - q0[0], p0[1] - q0[1])
            d2 = hypot(p1[0] - q0[0], p1[1] - q0[1])
            sv = cross3(p0, p1, q0)
            cv0 = dot3(p0, p1, q0) / d1 if d1 else 0.0
            cv1 = dot3(p1, p0, q0) / d2 if d2 else 0.0
            if sv > 0:
                el0[0] = max(el0[0], cv0)
                el1[0] = max(el1[0], -cv1)
            else:
                er0[1] = min(er0[1], -cv0)
                er1[1] = min(er1[1], cv1)

        for q1 in P[i+2:]:
            d1 = hypot(p1[0] - q1[0], p1[1] - q1[1])
            d2 = hypot(p0[0] - q1[0], p0[1] - q1[1])
            sv = cross3(p1, p0, q1)
            cv0 = dot3(p1, p0, q1) / d1 if d1 else 0.0
            cv1 = dot3(p0, p1, q1) / d2 if d2 else 0.0
            if sv > 0:
                er1[0] = max(er1[0], cv0)
                er0[0] = max(er0[0], -cv1)
            else:
                el1[1] = min(el1[1], -cv0)
                el0[1] = min(el0[1], cv1)

        if not (max(el0[0], er0[0]) <= min(el0[1], er0[1]) and
                max(el1[0], er0[0]) <= min(el1[1], er1[1])):
            ok = False
            break

    write("Possible\n" if ok else "Impossible\n")

solve()