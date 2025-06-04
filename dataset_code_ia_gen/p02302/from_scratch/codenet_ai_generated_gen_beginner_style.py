n = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(n)]

q = int(input())

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def area_poly(poly):
    area = 0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1) % len(poly)]
        area += cross(x1, y1, x2, y2)
    return abs(area) / 2

for _ in range(q):
    p1x, p1y, p2x, p2y = map(int, input().split())

    left_poly = []

    for i in range(n):
        cx, cy = polygon[i]
        nx, ny = polygon[(i+1) % n]

        # Vector from p1 to p2
        vx, vy = p2x - p1x, p2y - p1y
        # Vector from p1 to current point and next point
        v1x, v1y = cx - p1x, cy - p1y
        v2x, v2y = nx - p1x, ny - p1y

        # Cross products to check if points are on left side
        cross1 = cross(vx, vy, v1x, v1y)
        cross2 = cross(vx, vy, v2x, v2y)

        if cross1 >= 0:
            left_poly.append((cx, cy))

        # If edge crosses the line (one point on left, one on right)
        if cross1 * cross2 < 0:
            # Line segment between points
            dx, dy = nx - cx, ny - cy
            # Parameter t for intersection point
            # Solve: p = (cx, cy) + t*(dx, dy)
            # line: (p - p1) cross (p2 - p1) = 0
            numerator = cross(vx, vy, p1x - cx, p1y - cy)
            denominator = cross(vx, vy, dx, dy)
            t = numerator / denominator
            ix = cx + dx * t
            iy = cy + dy * t
            left_poly.append((ix, iy))

    if len(left_poly) < 3:
        # No polygon formed on the left side
        print("0.00000000")
    else:
        a = area_poly(left_poly)
        print("{0:.8f}".format(a))