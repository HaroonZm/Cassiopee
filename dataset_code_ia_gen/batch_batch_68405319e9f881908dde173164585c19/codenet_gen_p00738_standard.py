import sys
import math

def dist_point_to_segment(px, py, x1, y1, x2, y2):
    vx, vy = x2 - x1, y2 - y1
    wx, wy = px - x1, py - y1
    c1 = vx * wx + vy * wy
    if c1 <= 0:
        return math.hypot(px - x1, py - y1)
    c2 = vx * vx + vy * vy
    if c2 <= c1:
        return math.hypot(px - x2, py - y2)
    b = c1 / c2
    bx, by = x1 + b * vx, y1 + b * vy
    return math.hypot(px - bx, py - by)

def block_on_line(minx, miny, maxx, maxy, sx, sy, ex, ey):
    # Check if the line segment intersects the bottom rectangle of the block
    # The bottom is rect [minx,maxx]x[miny,maxy].
    # If line segment intersects the rectangle's edges or is inside rectangle, return True.
    # Use separating axis theorem or simpler bounding and segment-rectangle intersection check.

    # First, quick bounding box check
    if (max(sx, ex) < minx) or (min(sx, ex) > maxx) or (max(sy, ey) < miny) or (min(sy, ey) > maxy):
        return False
    # Check if either endpoint is inside the rectangle
    if minx <= sx <= maxx and miny <= sy <= maxy:
        return True
    if minx <= ex <= maxx and miny <= ey <= maxy:
        return True

    # Check intersections with rectangle edges
    def intersect(p1, p2, q1, q2):
        # Check if segments p1p2 and q1q2 intersect
        def ccw(a,b,c): return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
        return (ccw(p1,q1,q2) != ccw(p2,q1,q2)) and (ccw(p1,p2,q1) != ccw(p1,p2,q2))

    corners = [(minx,miny),(maxx,miny),(maxx,maxy),(minx,maxy)]
    edges = [(corners[i], corners[(i+1)%4]) for i in range(4)]
    for (a,b) in edges:
        if intersect((sx,sy),(ex,ey),a,b):
            return True
    return False

def max_radius_for_block(sx, sy, ex, ey, minx, miny, maxx, maxy, h):
    # The ball must never collide with the block.
    # The ball's center moves from (sx, sy, r) to (ex, ey, r).
    # The ball must be above ground (z=r), bottom point moves on line.
    # The closest distance from the center path (a 3D line) to block is at least r+h.
    # We find minimal horizontal distance from center line (sx,sy)->(ex,ey) to block bottom rectangle,
    # if center passes over the block horizontally within h+r distance -> collision, limit radius accordingly.

    # Distance from center path to block horizontally:
    # Find minimal dist between line segment and block rectangle.
    # Define d = minimal horizontal distance from center line segment to block bottom rectangle.
    # Then require r + h <= d must hold, so r <= d - h

    # Find minimal horizontal distance from line segment to rectangle
    # Strategy:
    # 1) If closest point on line to rectangle is inside rectangle, distance is vertical (horizontal distance is 0)
    # 2) Else minimal distance is min distance to any of the 4 edges or corners

    # Project line as parameter t in [0,1]
    # Check point on line at distance closest to rectangle

    # We'll compute minimal distance from line segment to rectangle by checking:
    # the minimal distance from the segment to each of the 4 edges (treat edge as segment),
    # and minimal distance from segment endpoints to rectangle, and
    # minimal distance when projection point on segment lies above rectangle.

    # But simpler method:
    # compute minimal distance between segment and rectangle using point-to-segment and segment-to-segment distances.

    # Compute distance from segment to rectangle:
    # minimal over: distance point-to-segment(center line to rectangle edges)
    # and distance point-to-point (segment ends to rectangle instances)

    # Since rectangle edges are line segments, check min of:
    # - distance from center line segment to each of rectangle edges
    # - distance from endpoints of center segment to rectangle (if inside rectangle distance=0)

    # To get the rectangle edges segments
    rect_corners=[(minx,miny),(maxx,miny),(maxx,maxy),(minx,maxy)]
    rect_edges=[(rect_corners[i],rect_corners[(i+1)%4]) for i in range(4)]

    def dist_seg_to_seg(a1,a2,b1,b2):
        # min distance between two segments in 2D
        # Handle degenerate cases (points)
        if a1==a2:
            return dist_point_to_segment(a1[0],a1[1],b1[0],b1[1],b2[0],b2[1])
        if b1==b2:
            return dist_point_to_segment(b1[0],b1[1],a1[0],a1[1],a2[0],a2[1])
        # Else:
        # Use parametric form and projections
        def dot(u,v): return u[0]*v[0]+u[1]*v[1]
        def length2(u): return u[0]*u[0]+u[1]*u[1]
        d1 = (a2[0]-a1[0], a2[1]-a1[1])
        d2 = (b2[0]-b1[0], b2[1]-b1[1])
        r = (a1[0]-b1[0], a1[1]-b1[1])
        a = length2(d1)
        e = length2(d2)
        f = dot(d2,r)

        if a <= 1e-14 and e <= 1e-14:
            # both segments are points
            return math.hypot(a1[0]-b1[0], a1[1]-b1[1])
        if a <= 1e-14:
            # first segment is a point
            return dist_point_to_segment(a1[0],a1[1],b1[0],b1[1],b2[0],b2[1])
        if e <= 1e-14:
            # second segment is a point
            return dist_point_to_segment(b1[0],b1[1],a1[0],a1[1],a2[0],a2[1])

        c = dot(d1,r)
        b = dot(d1,d2)
        denom = a*e - b*b
        s = 0
        t = 0
        if denom != 0:
            s = (b*f - c*e)/denom
            s = max(0,min(1,s))
        else:
            s = 0
        tnom = b*s + f
        if tnom < 0:
            t = 0
            s = max(0,min(1,-c/a))
        elif tnom > e:
            t = 1
            s = max(0,min(1,(b - c)/a))
        else:
            t = tnom / e

        # Closest points
        pA = (a1[0] + d1[0]*s, a1[1] + d1[1]*s)
        pB = (b1[0] + d2[0]*t, b1[1] + d2[1]*t)
        return math.hypot(pA[0]-pB[0], pA[1]-pB[1])

    # Center path segment
    cseg = ((sx,sy), (ex,ey))
    min_dist = float('inf')

    # Check distances from center segment to rectangle edges
    for e1,e2 in rect_edges:
        d = dist_seg_to_seg(cseg[0], cseg[1], e1, e2)
        if d < min_dist:
            min_dist = d

    # Check if projection on center segment lies inside rectangle at some point
    # Check distance from segment endpoints to rectangle (0 if inside)
    def point_in_rect(px, py, minx, miny, maxx, maxy):
        return minx <= px <= maxx and miny <= py <= maxy

    # If any endpoint inside rect, min distance is zero
    if point_in_rect(sx, sy, minx, miny, maxx, maxy) or point_in_rect(ex, ey, minx, miny, maxx, maxy):
        min_dist = 0

    # Also check minimal distance from center segment line projection to inside rectangle area:

    # Closest point on line to rectangle center
    rcx, rcy = (minx+maxx)/2, (miny+maxy)/2
    vx, vy = ex - sx, ey - sy
    lv2 = vx*vx + vy*vy
    if lv2 > 0:
        t = ((rcx - sx)*vx + (rcy - sy)*vy) / lv2
        t = max(0, min(1, t))
        cx = sx + vx*t
        cy = sy + vy*t
        if point_in_rect(cx, cy, minx, miny, maxx, maxy):
            d = 0
            if d < min_dist:
                min_dist = d

    # Now radius must satisfy r + h <= min_dist => r <= min_dist - h
    # If min_dist < h, no radius possible (negative)
    res = min_dist - h
    if res < 0:
        res = 0
    return res

def solve():
    input = sys.stdin.readline
    while True:
        N=int(input())
        if N==0:
            break
        sx, sy, ex, ey = map(int,input().split())
        blocks=[]
        any_on_line=False
        for _ in range(N):
            minx, miny, maxx, maxy, h = map(int,input().split())
            # check if block bottom intersects course line segment
            if not any_on_line and block_on_line(minx,miny,maxx,maxy,sx,sy,ex,ey):
                any_on_line=True
            blocks.append((minx,miny,maxx,maxy,h))
        if any_on_line:
            print(0)
            continue
        # binary search radius
        low = 0.0
        high = 1000.0
        for _ in range(60):
            mid = (low + high)/2
            ok=True
            # check for collision with any block
            for (minx,miny,maxx,maxy,h) in blocks:
                if mid + h > float('inf'):
                    ok=False
                    break
                rlim = max_radius_for_block(sx, sy, ex, ey, minx, miny, maxx, maxy, h)
                if mid - rlim > 1e-9:
                    ok=False
                    break
            if ok:
                low=mid
            else:
                high=mid
        print(low)

if __name__=="__main__":
    solve()