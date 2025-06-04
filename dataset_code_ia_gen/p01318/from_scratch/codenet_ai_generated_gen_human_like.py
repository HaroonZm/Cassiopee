import sys
import math
from itertools import combinations

def dist_point_to_line(px, py, ax, ay, bx, by):
    # distance from point P(px,py) to line AB(ax,ay)-(bx,by)
    # line length squared
    lab = (bx - ax)**2 + (by - ay)**2
    if lab == 0:
        return math.hypot(px - ax, py - ay)
    # projection parameter t for projection of P onto AB line
    t = ((px - ax)*(bx - ax) + (py - ay)*(by - ay))/lab
    # distance from P to infinite line AB
    # distance = norm of vector (P - projection)
    px_proj = ax + t*(bx - ax)
    py_proj = ay + t*(by - ay)
    return abs((bx - ax)*(ay - py) - (ax - px)*(by - ay)) / math.sqrt(lab)

def does_line_intersect_circle(ax, ay, bx, by, cx, cy, r):
    # Check if line segment AB intersects circle C with radius r
    # Vector AB
    ABx = bx - ax
    ABy = by - ay
    # Vector AC
    ACx = cx - ax
    ACy = cy - ay
    # Projection length t of AC onto AB normalized by |AB|^2
    lab2 = ABx*ABx + ABy*ABy
    if lab2 == 0:
        # A and B are the same point
        return math.hypot(cx - ax, cy - ay) < r
    t = (ACx * ABx + ACy * ABy) / lab2
    # Clamp t between 0 and 1 to stay within segment
    t = max(0, min(1, t))
    # Closest point D on segment to C
    Dx = ax + t*ABx
    Dy = ay + t*ABy
    # Distance CD
    dist_CD = math.hypot(Dx - cx, Dy - cy)
    return dist_CD < r

def gem_surfaces_distance_line(cx, cy, r, m, ax, ay, bx, by):
    # Distance from circle surface to line:
    # distance from center to line minus radius
    # The actual distance d is >=0
    lab = math.hypot(bx - ax, by - ay)
    if lab == 0:
        # infinite line can't be defined by zero length segment
        # but we won't use this
        return float('inf')
    # distance from center to infinite line
    numerator = abs((by - ay)*cx - (bx - ax)*cy + bx*ay - by*ax)
    dist_center_line = numerator / lab
    d = dist_center_line - r
    if d < 0:
        # line penetrates circle
        return -1  # invalid, penetration
    return d

def check_gem_can_be_attracted(cx, cy, r, m, ax, ay, bx, by):
    # Determine if a gem can be attracted by metal rod line AB
    # Conditions:
    # 1) rod does NOT penetrate the gem (circle)
    # 2) distance from surface to line <= m (magnetic power)
    # Compute perpendicular distance from center to line:
    lab = math.hypot(bx - ax, by - ay)
    numerator = abs((by - ay)*cx - (bx - ax)*cy + bx*ay - by*ax)
    dist_center_line = numerator / lab
    # penetration if dist_center_line < r
    if dist_center_line < r:
        return False
    dist_to_surface = dist_center_line - r
    return dist_to_surface <= m

def get_candidate_directions(gems):
    # Candidate lines are:
    # - lines through centers of 2 different gems (infinite line)
    # - lines tangent to two gems from outside (where line touches each circle at one point)
    # - lines tangent to one gem at one point (vertical and horizontal at circle edge)
    # Because N ≤ 50, only consider center lines and tangent lines between gem pairs
    
    candidates = []
    n = len(gems)
    # Line through centers of gem pairs
    for i in range(n):
        for j in range(i+1, n):
            cx1, cy1, r1, m1 = gems[i]
            cx2, cy2, r2, m2 = gems[j]
            if cx1 == cx2 and cy1 == cy2:
                continue
            candidates.append((cx1, cy1, cx2, cy2))
    # Tangent lines to pairs of circles (outer tangents only)
    # There can be 4 multiple common tangents between 2 circles,
    # but we only need lines (infinite) that could maximize attraction.
    # We'll compute all outer tangent lines between two circles.
    # The formulas are from the geometric construction of tangent lines to two circles.
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1, m1 = gems[i]
            x2, y2, r2, m2 = gems[j]
            dx = x2 - x1
            dy = y2 - y1
            dist_centers = math.hypot(dx, dy)
            if dist_centers == 0:
                continue
            # External tangents (delta_r = r2 - r1)
            for side in [1, -1]:
                # angle between centers on axis:
                base = math.atan2(dy, dx)
                # distance between circles radii
                rdiff = (r2 - side * r1)
                # If dist_centers < abs(rdiff), no tangent
                if dist_centers < abs(rdiff):
                    continue
                # angle to tangent line
                try:
                    angle = math.acos(rdiff / dist_centers)
                except ValueError:
                    # floating point correction
                    val = rdiff / dist_centers
                    if val < -1:
                        angle = math.pi
                    elif val > 1:
                        angle = 0.0
                    else:
                        raise
                # two possible tangent lines directions
                theta1 = base + angle
                theta2 = base - angle
                for theta in [theta1, theta2]:
                    # The tangent line vector direction:
                    dxl = math.cos(theta)
                    dyl = math.sin(theta)
                    # A point on first circle tangent line:
                    # T1 = center1 + r1 * perpendicular vector with right orientation
                    # For outer tangent,
                    # the tangent points for each circle:
                    # For side=1: tangent touches circle1 at angle theta+pi/2
                    # For side=-1: tangent touches circle1 at angle theta-pi/2
                    # Using the direction vector, find point on circle perimeter:
                    if side == 1:
                        perp_angle = theta + math.pi/2
                    else:
                        perp_angle = theta - math.pi/2
                    x_point = x1 + r1*math.cos(perp_angle)
                    y_point = y1 + r1*math.sin(perp_angle)
                    # direction vector (dxl, dyl), point (x_point, y_point)
                    # Represent line as (x_point, y_point), (x_point + dxl, y_point + dyl)
                    candidates.append((x_point, y_point, x_point + dxl, y_point + dyl))
    # Add vertical/horizontal direction for each gem for completeness (pass through center)
    for (cx, cy, r, m) in gems:
        # Vertical line through center
        candidates.append((cx, cy, cx, cy + 1))
        # Horizontal line through center
        candidates.append((cx, cy, cx + 1, cy))
    return candidates

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N = int(line.strip())
        if N == 0:
            break
        gems = []
        for _ in range(N):
            x, y, r, m = map(int, input().split())
            gems.append((x, y, r, m))
        candidates = get_candidate_directions(gems)
        max_attracted = 1  # minimal: at least one gem can be attracted by line passing through it (if radii and m allows)
        # Also consider lines through a single gem vertically or horizontally from candidates
        # Also consider line through any single gem center only (degenerate line)?
        # Try all candidate lines
        for (ax, ay, bx, by) in candidates:
            if ax == bx and ay == by:
                # degenerate line: skip
                continue
            attracted = 0
            # Check all gems
            # 1) verify no penetration
            # 2) check distance from surface <= m
            ok = True
            for (cx, cy, r, m) in gems:
                lab = math.hypot(bx - ax, by - ay)
                numerator = abs((by - ay)*cx - (bx - ax)*cy + bx*ay - by*ax)
                dist_center_line = numerator / lab
                # penetration check
                if dist_center_line < r:
                    continue # cannot be attracted, gem breaks
                dist_surface = dist_center_line - r
                if dist_surface <= m:
                    attracted += 1
            if attracted > max_attracted:
                max_attracted = attracted
        print(max_attracted)

if __name__ == "__main__":
    main()