import math

cx, cy, r = map(int, input().split())
q = int(input())

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1

    A = dx*dx + dy*dy
    B = 2*(dx*(x1 - cx) + dy*(y1 - cy))
    C = (x1 - cx)**2 + (y1 - cy)**2 - r*r

    discriminant = B*B - 4*A*C

    if discriminant < 0:
        # No intersection, but problem states at least one cross point, so ignore
        continue

    sqrt_disc = math.sqrt(discriminant)

    t1 = (-B + sqrt_disc) / (2*A)
    t2 = (-B - sqrt_disc) / (2*A)

    points = []

    # For each t, calculate the point on the line
    # Since line is infinite, both points are candidate
    # But problem expects all cross points, so print accordingly.

    # Sometimes both t are equal (tangent), then only one cross point
    x_1 = x1 + t1*dx
    y_1 = y1 + t1*dy
    x_2 = x1 + t2*dx
    y_2 = y1 + t2*dy

    # Add points and remove duplicates if any
    points.append((x_1, y_1))
    points.append((x_2, y_2))

    # Remove duplicates by rounding very small differences
    cleaned_points = []
    for p in points:
        is_new = True
        for cp in cleaned_points:
            if abs(cp[0] - p[0]) < 1e-12 and abs(cp[1] - p[1]) < 1e-12:
                is_new = False
                break
        if is_new:
            cleaned_points.append(p)

    # If only one point, print it twice
    if len(cleaned_points) == 1:
        p = cleaned_points[0]
        print(f"{p[0]:.8f} {p[1]:.8f} {p[0]:.8f} {p[1]:.8f}")
    else:
        p1, p2 = cleaned_points
        # Sort points by x then y
        if p2[0] < p1[0] or (abs(p2[0]-p1[0]) < 1e-12 and p2[1] < p1[1]):
            p1, p2 = p2, p1
        print(f"{p1[0]:.8f} {p1[1]:.8f} {p2[0]:.8f} {p2[1]:.8f}")