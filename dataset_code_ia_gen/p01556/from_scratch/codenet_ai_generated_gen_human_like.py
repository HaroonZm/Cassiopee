import sys
input = sys.stdin.readline

def polygon_area(points):
    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        area += x1*y2 - y1*x2
    return abs(area)/2

def line_intersection(p1, p2, q1, q2):
    # calculate intersection point of lines p1p2 and q1q2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q1
    x4, y4 = q2
    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom == 0:
        return None
    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    return (px, py)

def cut_polygon(polygon, a, b):
    # cut polygon by line through points a and b
    # returns the polygon on the left side of the line
    left = []
    n = len(polygon)
    for i in range(n):
        c = polygon[i]
        d = polygon[(i+1)%n]
        cross1 = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
        cross2 = (b[0]-a[0])*(d[1]-a[1]) - (b[1]-a[1])*(d[0]-a[0])
        
        if cross1 >= -1e-14:
            left.append(c)
        if cross1*cross2 < -1e-14:
            inter = line_intersection(c, d, a, b)
            if inter is not None:
                left.append(inter)
    return left

def area_split(polygon, p):
    # check if any cut line through p divides polygon into half area polygons
    # find edges on opposite sides of p
    n = len(polygon)
    total = polygon_area(polygon)
    for i in range(n):
        a = polygon[i]
        b = polygon[(i+1)%n]
        if abs(a[0]-p[0]) < 1e-15 and abs(a[1]-p[1]) < 1e-15 or abs(b[0]-p[0]) < 1e-15 and abs(b[1]-p[1]) < 1e-15:
            # If p is a vertex, no cut line through p other than edges. Checking those would give zero area
            continue
        vec = (b[0]-a[0], b[1]-a[1])
        # Use line perp to vector at p
        # since line through p divides Polygon into two halves, half area each
        # we can test cut polygons on left/right of line through p perp vec
        normal = (-vec[1], vec[0])
        
        left_poly = cut_polygon(polygon, p, (p[0]+normal[0], p[1]+normal[1]))
        area_left = polygon_area(left_poly)
        area_right = total - area_left
        if abs(area_left - area_right) < 1e-8:
            return True
    return False

N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]

total_area = polygon_area(points)

# The problem reduces to finding a point P inside polygon such that for ANY line crossing P,
# the polygon is split into two equal area parts.
# This is possible only if the polygon has a center of symmetry such that every chord through P divides polygon equally.
# For convex polygons, this point is the center of symmetry.
# But convex polygon may be asymmetric, so generally the point does not exist.
# From problem samples and reasoning, if polygon is centrally symmetric, such point P is unique and is the center of symmetry.
# We try to find center of symmetry by verifying if polygon is centrally symmetric about some point.
# The centroid is a candidate (the average of vertices), check if polygon is symmetric about centroid.

# Check center of symmetry candidate = average of points
cx = sum(p[0] for p in points)/N
cy = sum(p[1] for p in points)/N

def is_central_symmetric(points, c):
    n = len(points)
    used = [False]*n
    for i in range(n):
        if used[i]:
            continue
        p = points[i]
        found = False
        for j in range(n):
            if used[j]:
                continue
            q = points[j]
            if abs((p[0]+q[0])/2 - c[0]) < 1e-8 and abs((p[1]+q[1])/2 - c[1]) < 1e-8:
                used[i] = True
                used[j] = True
                found = True
                break
        if not found:
            return False
    return True

if is_central_symmetric(points, (cx,cy)):
    print(f"{cx:.5f} {cy:.5f}")
else:
    print("NA")