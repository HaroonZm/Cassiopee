import sys
import math

def dist_point_to_segment(px, py, x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return math.hypot(px - x1, py - y1)
    t = ((px - x1) * dx + (py - y1) * dy) / (dx*dx + dy*dy)
    t = max(0, min(1, t))
    projx, projy = x1 + t*dx, y1 + t*dy
    return math.hypot(px - projx, py - projy)

def is_point_inside_convex_polygon(px, py, poly):
    # Since polygon is convex and CCW ordered
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%n]
        cross = (x2 - x1)*(py - y1) - (y2 - y1)*(px - x1)
        if cross < 0:
            return False
    return True

def distance_to_sea(px, py, poly):
    min_dist = float('inf')
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%n]
        d = dist_point_to_segment(px, py, x1, y1, x2, y2)
        if d < min_dist:
            min_dist = d
    return min_dist

def most_distant_point(poly):
    # Use ternary search on the polygon edges and inside the polygon
    # The max distance to sea is the radius of the largest inscribed circle
    # For a convex polygon, it is the maximal distance from a point inside to the polygon edges.
    # We find it via a geometric approach using ternary search over x and y inside bounding box.

    minx = min(p[0] for p in poly)
    maxx = max(p[0] for p in poly)
    miny = min(p[1] for p in poly)
    maxy = max(p[1] for p in poly)

    def f(x, y):
        if not is_point_inside_convex_polygon(x, y, poly):
            return -1
        return distance_to_sea(x, y, poly)

    # Ternary search on y for a fixed x
    def ternary_search_y(x):
        low, high = miny, maxy
        for _ in range(50):
            m1 = low + (high - low)/3
            m2 = high - (high - low)/3
            f1 = f(x, m1)
            f2 = f(x, m2)
            if f1 < f2:
                low = m1
            else:
                high = m2
        return f(x, (low+high)/2)

    # Ternary search on x
    low, high = minx, maxx
    for _ in range(50):
        m1 = low + (high - low)/3
        m2 = high - (high - low)/3
        f1 = ternary_search_y(m1)
        f2 = ternary_search_y(m2)
        if f1 < f2:
            low = m1
        else:
            high = m2
    return ternary_search_y((low+high)/2)

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        poly = [tuple(map(int,input().split())) for _ in range(n)]
        ans = most_distant_point(poly)
        print(f"{ans:.6f}")

if __name__=="__main__":
    main()