from math import acos, hypot, isclose, sqrt, pi

def intersection(circle, polygon):
    """
    Calculates the area of intersection between a circle and a polygon.

    Parameters:
        circle (tuple): (x, y, r) representing the center (x, y) and radius r of the circle.
        polygon (list): List of vertices (tuples) of the polygon, given in order
                        (either counterclockwise or clockwise).

    Returns:
        float: The signed area of the intersection. Positive if vertices are given in counterclockwise order,
               negative if in clockwise order.
    """
    x, y, r = circle
    # Shift the polygon so that the circle center is at origin
    polygon = [(xp - x, yp - y) for xp, yp in polygon]
    area = 0.0
    # Loop over each edge of the polygon
    for p1, p2 in zip(polygon, polygon[1:] + [polygon[0]]):
        # Compute all intersection points of the circle with the current polygon edge
        ps = seg_intersection((0, 0, r), (p1, p2))
        # Partition the edge into parts: possibly split by intersection(s) with the circle
        for pp1, pp2 in zip([p1] + ps, ps + [p2]):
            c = cross(pp1, pp2)  # Twice the signed area of the triangle (origin, pp1, pp2)
            if c == 0:  # Points are colinear with origin, so area is zero
                continue
            d1 = hypot(*pp1)  # Distance from origin to pp1
            d2 = hypot(*pp2)  # Distance from origin to pp2
            if le(d1, r) and le(d2, r):
                # Both points are inside the circle: add triangle area
                area += c / 2
            else:
                # At least one point is outside: add sector area with sign
                t = acos(dot(pp1, pp2) / (d1 * d2))  # Angle at circle center between pp1 and pp2
                sign = 1.0 if c >= 0 else -1.0
                area += sign * r * r * t / 2  # Sector area is (1/2) * r^2 * angle
    return area

def cross(v1, v2):
    """
    Computes the cross product (2D) of two vectors.

    Parameters:
        v1 (tuple): The (x1, y1) vector.
        v2 (tuple): The (x2, y2) vector.

    Returns:
        float: The cross product v1 x v2 (scalar in 2D).
    """
    x1, y1 = v1
    x2, y2 = v2
    return x1 * y2 - x2 * y1

def dot(v1, v2):
    """
    Computes the dot product of two vectors.

    Parameters:
        v1 (tuple): The (x1, y1) vector.
        v2 (tuple): The (x2, y2) vector.

    Returns:
        float: The dot product v1 . v2.
    """
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2

def seg_intersection(circle, seg):
    """
    Finds intersection points (if any) between a line segment and a circle.

    Assumes the circle is centered at (x0, y0) with radius r.
    Solves the quadratic equation for intersection and checks if within segment bounds.

    Parameters:
        circle (tuple): (x0, y0, r) - center and radius of circle.
        seg (tuple): ((x1, y1), (x2, y2)) - endpoints of line segment.

    Returns:
        list: List of (x, y) tuples for intersection points between the segment and the circle.
              Could be empty, contain one point (tangent), or two points.
    """
    x0, y0, r = circle
    p1, p2 = seg
    x1, y1 = p1
    x2, y2 = p2

    # Compute coefficients for the quadratic equation
    p1p2 = (x2 - x1) ** 2 + (y2 - y1) ** 2  # Squared length of the segment
    op1 = (x1 - x0) ** 2 + (y1 - y0) ** 2   # Squared distance from p1 to circle center
    rr = r * r                               # Radius squared
    dp = dot((x1 - x0, y1 - y0), (x2 - x1, y2 - y1))   # (p1 - center) . (p2 - p1) 

    # Discriminant of the quadratic
    d = dp * dp - p1p2 * (op1 - rr)
    ps = []

    if isclose(d, 0.0, abs_tol=1e-9):
        # Tangent: exactly one intersection
        t = -dp / p1p2
        if ge(t, 0.0) and le(t, 1.0):
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            ps.append((x, y))
    elif d > 0.0:
        # Two points of intersection
        t1 = (-dp - sqrt(d)) / p1p2
        if ge(t1, 0.0) and le(t1, 1.0):
            x = x1 + t1 * (x2 - x1)
            y = y1 + t1 * (y2 - y1)
            ps.append((x, y))
        t2 = (-dp + sqrt(d)) / p1p2
        if ge(t2, 0.0) and le(t2, 1.0):
            x = x1 + t2 * (x2 - x1)
            y = y1 + t2 * (y2 - y1)
            ps.append((x, y))

    # All points found; return valid intersection points lying on the segment
    return ps

def le(f1, f2):
    """
    Returns True if f1 <= f2 up to a small tolerance.

    Parameters:
        f1 (float): value to check.
        f2 (float): threshold value.

    Returns:
        bool: True if f1 is less than or approximately equal to f2.
    """
    return f1 < f2 or isclose(f1, f2, abs_tol=1e-9)

def ge(f1, f2):
    """
    Returns True if f1 >= f2 up to a small tolerance.

    Parameters:
        f1 (float): value to check.
        f2 (float): threshold value.

    Returns:
        bool: True if f1 is greater than or approximately equal to f2.
    """
    return f1 > f2 or isclose(f1, f2, abs_tol=1e-9)

# --- Main execution starts here ---

# Read total number of polygons (N), circle center (cx, cy), and radius (r)
N, cx, cy, r = map(int, input().split())
ans = 0

# Precompute area of the circle for normalization
circle_area = pi * r * r

# Process each polygon with associated score
for _ in range(N):
    p, score = map(int, input().split())  # p = number of vertices, score = polygon score
    ps = []
    # Read vertices of the polygon
    for _ in range(p):
        x, y = map(int, input().split())
        ps.append((x, y))
    # Compute the area of intersection between this polygon and the circle
    area = intersection((cx, cy, r), ps)
    # Accumulate the normalized value: (|area| / circle_area) * score
    ans += abs(area) * score / circle_area

# Output the final accumulated result with 10 decimal places
print(f"{ans:.10f}")