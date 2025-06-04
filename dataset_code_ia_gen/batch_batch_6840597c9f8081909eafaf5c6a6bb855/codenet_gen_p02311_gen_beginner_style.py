import math

def print_point(p):
    print(f"{p[0]:.10f} {p[1]:.10f}")

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def circle_tangents(x1, y1, r1, x2, y2, r2):
    # Function adapted from simple geometry approach for common tangents of two circles
    result = []
    dx = x2 - x1
    dy = y2 - y1
    d_squared = dx*dx + dy*dy
    if d_squared == 0:
        # Same centers, infinite tangents if circles differ, no tangents otherwise
        return []
    d = math.sqrt(d_squared)

    for sign1 in [+1, -1]:
        r = r2 * sign1
        c = (r1 - r) / d

        if c*c > 1.0:
            # no tangents with this configuration
            continue
        h = math.sqrt(max(0.0, 1.0 - c*c))

        # base vector (dx/d, dy/d)
        vx = dx / d
        vy = dy / d

        for sign2 in [+1, -1]:
            nx = vx * c - sign2 * h * vy
            ny = vy * c + sign2 * h * vx

            # tangent point on circle 1
            tx = x1 + r1 * nx
            ty = y1 + r1 * ny
            result.append((tx, ty))

    return result

c1x, c1y, c1r = map(int, input().split())
c2x, c2y, c2r = map(int, input().split())

points = circle_tangents(c1x, c1y, c1r, c2x, c2y, c2r)
if points:
    # Remove duplicates closer than 1e-8 (to handle very close points)
    unique_points = []
    for p in points:
        if not any(dist(p, q) < 1e-8 for q in unique_points):
            unique_points.append(p)
    unique_points.sort(key=lambda x: (x[0], x[1]))
    for p in unique_points:
        print_point(p)