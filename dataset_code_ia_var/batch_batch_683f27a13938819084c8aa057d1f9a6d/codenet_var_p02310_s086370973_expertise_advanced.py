from math import hypot, sqrt
from sys import stdin

(px, py), (cx, cy, r) = (map(int, stdin.readline().split()), map(int, stdin.readline().split()))

def solve():
    dx, dy = px - cx, py - cy
    d2 = dx * dx + dy * dy
    d = hypot(dx, dy)
    if d == 0 or d < r:
        print("No intersection")
        return

    sin2 = (r * r) / d2
    cos2 = 1 - sin2
    prod = r * sqrt(cos2 / sin2)
    mx, my = cx + dx * r / d, cy + dy * r / d
    norm = hypot(dx, dy)
    ux, uy = dx / norm, dy / norm
    vx, vy = -uy, ux
    x1 = mx + prod * vx
    y1 = my + prod * vy
    x2 = mx - prod * vx
    y2 = my - prod * vy
    if (x1, y1) > (x2, y2):
        print(f"{x2} {y2}")
        print(f"{x1} {y1}")
    else:
        print(f"{x1} {y1}")
        print(f"{x2} {y2}")

solve()