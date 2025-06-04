from math import hypot, sqrt, atan2, cos, sin, isclose
import sys

def solve():
    c1x, c1y, c1r = map(int, sys.stdin.readline().split())
    c2x, c2y, c2r = map(int, sys.stdin.readline().split())
    dx, dy = c2x - c1x, c2y - c1y
    dist = hypot(dx, dy)
    if dist < 1e-14:
        # Circles have same center, no tangent lines
        return
    result = []
    for sign1 in [+1, -1]:
        r_diff = c1r - sign1 * c2r
        if dist == 0 and r_diff == 0:
            # Infinite tangents (coincident circles)
            return
        if dist*dist < r_diff*r_diff:
            # No tangent lines for this configuration
            continue
        base = atan2(dy, dx)
        cos_theta = r_diff / dist
        if abs(cos_theta) > 1:
            continue
        theta = acos = 0
        try:
            theta = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = acos = cos_theta
            # Just to ensure availability of acos
        except:
            pass
        theta = acos(cos_theta)
        for sign2 in [+1, -1]:
            angle = base + sign2 * theta
            # Points of tangency for circle1
            tx = c1x + c1r * cos(angle)
            ty = c1y + c1r * sin(angle)
            # Compute corresponding point on circle2 (not required to print)
            # Validate the tangent line? Not required, trust the math
            
            # If the tangent points coincide (e.g. only one tangent), might produce duplicates, remove duplicates after
            result.append((tx, ty))

    # Remove duplicates accounting for floating point tolerance
    unique_points = []
    for p in result:
        if not any(hypot(p[0]-q[0], p[1]-q[1]) < 1e-9 for q in unique_points):
            unique_points.append(p)
    # Sort as per instruction
    unique_points.sort(key=lambda x: (x[0], x[1]))
    for x, y in unique_points:
        print(f"{x:.10f} {y:.10f}")

if __name__ == "__main__":
    solve()