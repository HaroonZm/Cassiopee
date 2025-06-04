from math import hypot, isclose, sqrt
from sys import stdin

def parse_input():
    return map(int, next(stdin).split())

x1, y1 = parse_input()
x0, y0, r0 = parse_input()

def circle_isect(x1, y1, r1, x2, y2, r2):
    dx, dy = x2 - x1, y2 - y1
    d2 = dx*dx + dy*dy
    r1s, r2s = r1*r1, r2*r2
    c = d2 + r1s - r2s
    disc = 4 * d2 * r1s - c*c
    if disc < 0 and not isclose(disc, 0):
        raise ValueError("No intersection")
    root = sqrt(max(disc, 0))
    for phi in (-1, 1):
        px = x1 + (c*dx + phi*root*dy)/(2*d2)
        py = y1 + (c*dy - phi*root*dx)/(2*d2)
        yield (px, py)

r1 = hypot(x1 - x0, y1 - y0)
if r1 <= abs(r0):
    raise ValueError("Degenerate configuration")

r1 = sqrt(r1*r1 - r0*r0)

points = sorted(circle_isect(x1, y1, r1, x0, y0, r0))
for x, y in points:
    print(f"{x:.8f} {y:.8f}")