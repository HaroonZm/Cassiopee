import math

def intersection(circle, polygon):
    # Find the intersection area between a circle and a polygon.
    # Positive if polygon vertices are given counter-clockwise, negative otherwise.
    cx, cy, r = circle
    # Move polygon so circle is at the origin
    new_polygon = []
    for px, py in polygon:
        new_polygon.append((px - cx, py - cy))
    area = 0.0
    n = len(new_polygon)
    for i in range(n):
        p1 = new_polygon[i]
        p2 = new_polygon[(i+1)%n]
        inter_points = seg_intersection((0, 0, r), (p1, p2))
        # Prepare ordered segment points
        segs = [p1] + inter_points + [p2]
        for j in range(len(segs)-1):
            a = segs[j]
            b = segs[j+1]
            c = cross(a, b)
            if c == 0:
                continue
            d1 = math.hypot(a[0], a[1])
            d2 = math.hypot(b[0], b[1])
            if le(d1, r) and le(d2, r):
                area += c / 2
            else:
                # Both or one point outside
                dp = dot(a, b)
                if d1 == 0 or d2 == 0:
                    t = 0.0
                else:
                    t = math.acos(dp / (d1 * d2))
                if c >= 0:
                    sign = 1.0
                else:
                    sign = -1.0
                area += sign * r * r * t / 2
    return area

def cross(v1, v2):
    return v1[0]*v2[1] - v2[0]*v1[1]

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def seg_intersection(circle, seg):
    # Calculate the intersection points of a circle (with center at (x0, y0) and radius r)
    # and a segment (p1, p2)
    x0, y0, r = circle
    (x1, y1), (x2, y2) = seg
    dx = x2 - x1
    dy = y2 - y1
    fx = x1 - x0
    fy = y1 - y0
    a = dx * dx + dy * dy
    b = 2 * (fx * dx + fy * dy)
    c = fx * fx + fy * fy - r * r
    disc = b * b - 4 * a * c
    points = []
    if math.isclose(a, 0):
        return []
    if math.isclose(disc, 0, abs_tol=1e-9):
        t = -b / (2*a)
        if ge(t, 0.0) and le(t, 1.0):
            px = x1 + t * dx
            py = y1 + t * dy
            points.append((px, py))
    elif disc > 0:
        sqrt_disc = math.sqrt(disc)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        if ge(t1, 0.0) and le(t1, 1.0):
            px1 = x1 + t1 * dx
            py1 = y1 + t1 * dy
            points.append((px1, py1))
        if ge(t2, 0.0) and le(t2, 1.0):
            px2 = x1 + t2 * dx
            py2 = y1 + t2 * dy
            points.append((px2, py2))
    return points

def le(a, b):
    return a < b or math.isclose(a, b, abs_tol=1e-9)

def ge(a, b):
    return a > b or math.isclose(a, b, abs_tol=1e-9)

N, cx, cy, r = map(int, input().split())
total = 0.0
circle_area = math.pi * r * r
for _ in range(N):
    p, score = map(int, input().split())
    polygon = []
    for _ in range(p):
        x, y = map(int, input().split())
        polygon.append((x, y))
    inter_area = intersection((cx, cy, r), polygon)
    total += abs(inter_area) * score / circle_area
print("{:.10f}".format(total))