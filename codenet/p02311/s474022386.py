from math import acos, atan2, cos, hypot, isclose, pi, sin
from typing import List, Tuple

def tangent_points(c1x: float, c1y: float, c1r: float,
                   c2x: float, c2y: float, c2r: float) -> List[Tuple[float, float]]:
    c1c2 = hypot(c2x - c1x, c2y - c1y)
    t0 = atan2(c2y - c1y, c2x - c1x)
    ps: List[Tuple[float, float]] = []

    r1r2 = c1r + c2r
    if isclose(c1c2, r1r2):
        ps.append((c1x + c1r * cos(t0), c1y + c1r * sin(t0)))
    elif c1c2 > r1r2:
        t1 = acos(r1r2 / c1c2)
        ps.append((c1x + c1r * cos(t0 + t1), c1y + c1r * sin(t0 + t1)))
        ps.append((c1x + c1r * cos(t0 - t1), c1y + c1r * sin(t0 - t1)))

    r1r2 = c1r - c2r
    if isclose(c1c2, abs(r1r2)):
        if r1r2 > 0.0:
            t1 = 0.0
        else:
            t1 = pi
        ps.append((c1x + c1r * cos(t0 + t1), c1y + c1r * sin(t0 + t1)))
    elif c1c2 > abs(r1r2):
        if r1r2 > 0.0:
            t1 = acos(r1r2 / c1c2)
        else:
            t1 = pi - acos(-r1r2 / c1c2)
        ps.append((c1x + c1r * cos(t0 + t1), c1y + c1r * sin(t0 + t1)))
        ps.append((c1x + c1r * cos(t0 - t1), c1y + c1r * sin(t0 - t1)))

    return ps

if __name__ == "__main__":
    c1x, c1y, c1r = map(lambda x: float(x), input().split())
    c2x, c2y, c2r = map(lambda x: float(x), input().split())

    ps = tangent_points(c1x, c1y, c1r, c2x, c2y, c2r)

    for p in sorted(ps):
        print("{:.6f} {:.6f}".format(*p))