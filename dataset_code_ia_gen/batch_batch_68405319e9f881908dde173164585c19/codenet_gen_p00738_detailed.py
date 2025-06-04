import sys
import math

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def dist_point_point(a, b):
    # distance between two points a,b each a tuple (x,y)
    return math.hypot(a[0]-b[0], a[1]-b[1])

def dist_point_segment(px, py, ax, ay, bx, by):
    # Distance from point p=(px,py) to segment ab=((ax,ay),(bx,by))
    # Compute projection t of p on ab, clamp between 0 and 1
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return dist_point_point((px,py), (ax,ay))
    t = ((px - ax)*dx + (py - ay)*dy) / (dx*dx + dy*dy)
    t = max(0, min(1, t))
    projx = ax + t*dx
    projy = ay + t*dy
    return dist_point_point((px,py), (projx, projy))

def dist_segment_segment(a1, a2, b1, b2):
    # distance between two 2D segments a1a2 and b1b2
    # check endpoints to other segment distances, plus segments intersecting consider 0
    if segments_intersect_2d(a1,a2,b1,b2):
        return 0.0
    d1 = dist_point_segment(a1[0],a1[1], b1[0],b1[1], b2[0],b2[1])
    d2 = dist_point_segment(a2[0],a2[1], b1[0],b1[1], b2[0],b2[1])
    d3 = dist_point_segment(b1[0],b1[1], a1[0],a1[1], a2[0],a2[1])
    d4 = dist_point_segment(b2[0],b2[1], a1[0],a1[1], a2[0],a2[1])
    return min(d1, d2, d3, d4)

def segments_intersect_2d(p1, p2, q1, q2):
    # Checks if 2 segments (p1-p2) and (q1-q2) intersect in 2D
    def ccw(a,b,c):
        return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
    A,B,C,D = p1,p2,q1,q2
    return (ccw(A,C,D) != ccw(B,C,D)) and (ccw(A,B,C) != ccw(A,B,D))

def point_in_rect(x,y, rx1, ry1, rx2, ry2):
    return rx1 <= x <= rx2 and ry1 <= y <= ry2

def line_segment_intersects_rect(ax, ay, bx, by, rx1, ry1, rx2, ry2):
    # Check if line segment ab intersects rectangle defined by corners rx1,ry1 and rx2,ry2
    # Check if either segment endpoint inside rect
    if point_in_rect(ax, ay, rx1, ry1, rx2, ry2) or point_in_rect(bx, by, rx1, ry1, rx2, ry2):
        return True
    # Rect edges
    rect_edges = [
        ((rx1, ry1), (rx2, ry1)),
        ((rx2, ry1), (rx2, ry2)),
        ((rx2, ry2), (rx1, ry2)),
        ((rx1, ry2), (rx1, ry1))
    ]
    for (ex1, ey1), (ex2, ey2) in rect_edges:
        if segments_intersect_2d((ax,ay), (bx,by), (ex1,ey1), (ex2,ey2)):
            return True
    return False

def vertical_distance_block(ball_x, ball_y, r, block):
    # Calculate the vertical clearance needed to roll the ball without collision with this block
    # The ball is a sphere radius r with bottom point on course line at (ball_x, ball_y)
    # Check 3D minimal distance between ball surface and block
    # Block bottom rectangle: (minx,miny), (maxx,maxy) and height h
    
    # Since both ball and block fixed on ground plane, 
    # minimal distance between ball center and block is horizontal distance to block + vertical part
    
    minx, miny, maxx, maxy, h = block
    
    # Clamp ball center x,y to block bottom rectangle for nearest horizontal point
    cx = ball_x
    cy = ball_y
    
    # Horizontal distance from ball center to block volume in xy projection:
    dx = 0
    if cx < minx:
        dx = minx - cx
    elif cx > maxx:
        dx = cx - maxx
    dy = 0
    if cy < miny:
        dy = miny - cy
    elif cy > maxy:
        dy = cy - maxy
    
    horizontal_dist = math.hypot(dx, dy)
    # Ball center is at (ball_x, ball_y, r) (since bottom at plane z=0)
    # Block from z=0 to z=h
    # Vertical distance between ball center and block vertical faces:
    # If horizontal_dist >= r, ball cannot touch block horizontally
    # Otherwise vertical distance must be > vertical overlap
    
    # If horizontal_dist >= r, minimal distance on z-axis is zero (ball does not horizontally overlap block)
    # Else ball horizontally overlaps, ball top point at height r+r=2r at max, ball bottom at 0
    # Block bottom at 0 top at h
    # For collision, sphere surface cannot intersect block volume:
    # Minimal vertical distance between ball center and block top is r - h if ball overlaps horizontally
    
    # Actually, the minimal distance between ball surface and block is minimal distance between sphere surface and block volume.
    # We want radius r such that:
    # sqrt(horizontal_dist^2 + vertical_dist^2) >= r
    # vertical_dist = max(0, h - r)
    # Because ball center at height r, block height h
    
    # So if horizontal_dist >= r: no horizontal overlap, vertical safe
    # If horizontal_dist < r: vertical space must satisfy (r - h) <= 0 -> r <= h
    
    # So the minimal radius r must satisfy:
    # horizontal_dist^2 + max(0,h - r)^2 >= r^2
    
    # We'll check feasibility in main function rather than here
    
    return horizontal_dist, h

def course_line_intersects_block(sx, sy, ex, ey, block):
    # Check if bottom sphere point trajectory line segment intersects block bottom rectangle (projection)
    minx, miny, maxx, maxy, h = block
    return line_segment_intersects_rect(sx, sy, ex, ey, minx, miny, maxx, maxy)

def max_radius_feasible(r, sx, sy, ex, ey, blocks):
    # For given radius r, check if ball can roll from start to end
    # without collision
    
    # The ball center path is offset r above bottom point on plane z=0,
    # but bottom point moves along straight line (sx,sy)-(ex,ey)
    
    # The ball bottom never leaves the course line segment.
    # Check the ball does not collide with any block
    
    # The ball center is at height r, its horizontal position is on the line from start to end
    
    # For continuous collision checking on path, since ball moves on straight line,
    # we can check the minimal distance between ball center path segment and block volume
    
    # Approach:
    # For each block, compute minimal horizontal distance from line segment (sx,sy)-(ex,ey)
    # to block bottom rectangle
    # Let this minimal horizontal distance be d_h
    # Let block height be h
    
    # The vertical distance between ball center and block top is r - h (ball center at height r)
    # The ball surface can not intersect the block, so:
    # minimal distance between ball center and block >= r
    # minimal distance^2 = d_h^2 + max(0, h - r)^2 >= r^2
    
    # Rearranged: d_h^2 >= r^2 - max(0,h - r)^2
    
    # Note max(0,h-r) = height distance if h > r, else 0
    
    # We must check this for all blocks
    
    ax, ay = sx, sy
    bx, by = ex, ey
    
    for block in blocks:
        minx, miny, maxx, maxy, h = block
        d_h = dist_segment_rectangle_2d((ax,ay),(bx,by), (minx,miny,maxx,maxy))
        
        # Compute vertical part
        vert_gap = max(0, h - r)
        lhs = d_h*d_h
        rhs = r*r - vert_gap*vert_gap
        # For feasibility rhs must be <= lhs
        # If rhs <= 0, automatically feasible (ball radius smaller than block height)
        # But if rhs > lhs -> no feasibility
        if rhs > lhs + 1e-14:
            return False
    return True

def dist_point_rectangle(px, py, rx1, ry1, rx2, ry2):
    # distance from point to rectangle
    dx = 0
    if px < rx1:
        dx = rx1 - px
    elif px > rx2:
        dx = px - rx2
    dy = 0
    if py < ry1:
        dy = ry1 - py
    elif py > ry2:
        dy = py - ry2
    return math.hypot(dx, dy)

def dist_segment_rectangle_2d(seg_a, seg_b, rect):
    # segment points: seg_a = (x1,y1), seg_b = (x2,y2)
    # rectangle: (minx, miny, maxx, maxy)
    minx, miny, maxx, maxy = rect
    
    x1,y1 = seg_a
    x2,y2 = seg_b
    
    # If segment intersects rectangle, dist=0
    if line_segment_intersects_rect(x1,y1,x2,y2,minx,miny,maxx,maxy):
        return 0.0
    
    # Else dist = minimal distance between segment and rectangle edges or vertices
    
    # 1) Check all segment points to rectangle:
    d1 = dist_point_rectangle(x1,y1,minx,miny,maxx,maxy)
    d2 = dist_point_rectangle(x2,y2,minx,miny,maxx,maxy)
    
    # 2) Check rectangle corners to segment
    corners = [(minx,miny), (maxx,miny), (maxx,maxy), (minx,maxy)]
    d3 = min(dist_point_segment(cx, cy, x1, y1, x2, y2) for cx,cy in corners)
    
    return min(d1,d2,d3)

def solve_dataset():
    while True:
        N_line = sys.stdin.readline()
        if not N_line:
            break
        N_line = N_line.strip()
        if N_line == '0':
            break
        N = int(N_line)
        sx, sy, ex, ey = read_ints()
        blocks = []
        for _ in range(N):
            minx, miny, maxx, maxy, h = read_ints()
            blocks.append((minx, miny, maxx, maxy, h))
        
        # First check if course line intersects any block's bottom surface
        # if yes, largest radius = 0
        intersects_line = False
        for block in blocks:
            if course_line_intersects_block(sx, sy, ex, ey, block):
                intersects_line = True
                break
        
        if intersects_line:
            print(0)
            continue
        
        # Binary search largest radius r in [0,1000]
        low = 0.0
        high = 1000.0
        
        for _ in range(100):
            mid = (low + high)/2
            if max_radius_feasible(mid, sx, sy, ex, ey, blocks):
                low = mid
            else:
                high = mid
        
        print(low)

if __name__ == '__main__':
    solve_dataset()