import math
from itertools import permutations, combinations

def polygon_area(points):
    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def solve():
    N = int(input())
    r = [int(input()) for _ in range(N)]
    r.sort(reverse=True)

    # When N points lie on the convex hull, the largest area polygon they form,
    # with each point at distance r_i from origin,
    # is when they are equally spaced angles on the convex hull.

    # Because we can assign the angles arbitrarily to maximize area,
    # Let's consider the following:

    # Assign the largest r to largest angle gap to maximize area.
    # But since we don't know the angle gaps, and we want maximum polygon area,
    # the maximal polygon for points on circle with radius r_i arranged optimally
    # is to arrange points on convex polygon in order maximizing area.

    # Since N <= 8, we can permute the order of radii assigned to vertices.
    # Angles are fixed regularly spaced: 0, 2pi/N, 4pi/N, ..., so polygon is simple.

    # We'll check all permutations of radii assigned to these regular angles.

    max_area = 0
    angles = [2*math.pi*i/N for i in range(N)]

    for perm in permutations(r):
        points = [(perm[i]*math.cos(angles[i]), perm[i]*math.sin(angles[i])) for i in range(N)]
        hull = convex_hull(points)
        if len(hull) < 3:
            continue
        area = polygon_area(hull)
        if area > max_area:
            max_area = area

    print(max_area)

if __name__ == "__main__":
    solve()