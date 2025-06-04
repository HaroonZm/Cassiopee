import sys
sys.setrecursionlimit(10**7)

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def sub(a,b):
    return (a[0]-b[0], a[1]-b[1])

def dot(a,b):
    return a[0]*b[0] + a[1]*b[1]

def on_segment(p, q, r):
    # q is point, p-r is segment
    # check if q lies on segment pr (excluding ends)
    if min(p[0], r[0]) < q[0] < max(p[0], r[0]) and min(p[1], r[1]) < q[1] < max(p[1], r[1]):
        return True
    return False

def segments_intersect(p1, p2, p3, p4):
    # check if segment p1p2 and p3p4 intersect
    # includes intersecting at endpoints (here we exclude intersection only at end points)
    v1 = cross(sub(p3,p1), sub(p2,p1))
    v2 = cross(sub(p4,p1), sub(p2,p1))
    v3 = cross(sub(p1,p3), sub(p4,p3))
    v4 = cross(sub(p2,p3), sub(p4,p3))

    if v1*v2 < 0 and v3*v4 < 0:
        return True
    # also check if the segments are colinear and overlap inside segment
    if v1 == 0 and on_segment(p1,p3,p2):
        return True
    if v2 == 0 and on_segment(p1,p4,p2):
        return True
    if v3 == 0 and on_segment(p3,p1,p4):
        return True
    if v4 == 0 and on_segment(p3,p2,p4):
        return True
    return False

def point_in_polygon(point, polygon):
    # ray casting algorithm, but polygon boundary is not included as inside
    x, y = point
    cnt = 0
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%n]
        # check if point lies on edge: if yes, then it is not inside
        if (y2 - y1) * (x - x1) == (y - y1)*(x2 - x1):
            if min(x1,x2) <= x <= max(x1,x2) and min(y1,y2) <= y <= max(y1,y2):
                return False
        if (y1 <= y < y2) or (y2 <= y < y1):
            t = (y - y1) / (y2 - y1)
            xt = x1 + t*(x2 - x1)
            if xt > x:
                cnt += 1
    return cnt % 2 == 1

def segment_hits_polygon(p1, p2, polygon):
    n = len(polygon)
    for i in range(n):
        q1 = polygon[i]
        q2 = polygon[(i+1)%n]
        # if segments intersect at any interior point (not endpoints of polygon edges)
        # The polygon boundaries are not considered inside, so intersection on boundary is allowed?
        # The problem states polygon edge is not inside polygon, but if line crosses the obstacle boundary it is obstacle ? No.
        # Need to check if line segment crosses polygon edge in interior of segment (excluding endpoints)
        # But intersection on edge endpoints is allowed? It's better to exclude also endpoints to be safe.
        # Just check if intersection occurs at interior of segment p1p2 and interior of edge q1q2, excluding endpoints
        # So we check if intersect and intersection point is not endpoint of polygon edge
        
        # segments_intersect returns true if intersect including touching ends
        # We should ignore touching at polygon vertices if it is at p1 or p2, since line touches polygon vertex
        # But problem states obstacle edges are not inside, so any intersection blocks view.
        
        # So if intersection occurs (including touching), block the view
        if segments_intersect(p1, p2, q1, q2):
            # exclude if intersection only at p1 or p2?
            # But problem states edges are not obstacle. But the interior polygon is obstacle.
            # The problem says: edges are not inside obstacle, but line crossing edge counts as obstacle blocking.
            # So any intersection counts as blocked
            # Except if the intersection point is a vertex of polygon that coincides with p1 or p2?
            # Vertices of polygon and p1,p2 are different by problem statement.
            # So no confusion on coinciding points
            return True
    return False

def main():
    N, M = map(int, input().split())
    polygons = []
    for _ in range(N):
        L = int(input())
        poly = [tuple(map(int,input().split())) for __ in range(L)]
        polygons.append(poly)
    voters = [tuple(map(int,input().split())) for __ in range(M)]

    # Candidate's possible positions are unrestricted on 2D plane
    # But we look for a position that maximizes number of visible voters
    # Since obstacles are polygon, and voters are points, and number is small,
    # Try candidate positions at each voter positions and polygon vertices and midpoints?

    # Because problem size small, we consider all points in (voters + all polygon vertices) and
    # also midpoints of voters, and possibly some offset points.
    # Let's check for all voters' and polygon vertices' positions as candidate positions.

    candidates = []
    for voter in voters:
        candidates.append(voter)
    for poly in polygons:
        for v in poly:
            candidates.append(v)

    # To be more thorough, add midpoints between voters and polygon vertices (optional)
    # But problem small, only trying these candidates will probably suffice.

    max_seen = 0
    for cx, cy in candidates:
        # Check if candidate inside any polygon, if yes skip (cannot stand inside obstacle)
        inside = False
        for poly in polygons:
            if point_in_polygon((cx, cy), poly):
                inside = True
                break
        if inside:
            continue

        count = 0
        for vx, vy in voters:
            # check if line (candidate)-(voter) crosses polygon interior
            # skip if candidate == voter (visible, no obstacle)
            if (cx, cy) == (vx, vy):
                count += 1
                continue
            blocked = False
            for poly in polygons:
                # if either candidate or voter lies on polygon boundary? No, polygon vertices distinct from voters.
                # check intersection with polygon edges
                # also check if candidate or voter inside polygon? Given input that voters not inside polygon.
                # candidate inside polygon already filtered.
                if segment_hits_polygon((cx,cy), (vx,vy), poly):
                    blocked = True
                    break
            if not blocked:
                # also check that midpoint of segment is not inside polygon (to prevent crossing polygon interior)
                # segment_hits_polygon only checks edges intersections, but crossing polygon interior between edges is not an issue if no edges intersected
                # But since polygon is simple, line crossing polygon interior must cross an edge, so edge intersection check suffices
                count += 1
        if count > max_seen:
            max_seen = count

    print(max_seen)


main()