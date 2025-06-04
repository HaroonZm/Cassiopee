import sys
import math

input = sys.stdin.readline

def angle_normalize(a):
    # Normalize angle to [0,360)
    return a % 360

def interval_intersection(a1, a2, b1, b2):
    # Intersect two intervals on circle [0,360)
    # each is given as (start,end) with start<=end in [0,360)
    start = max(a1, b1)
    end = min(a2, b2)
    if start <= end:
        return (start, end)
    return None

def on_wall_points(w, d):
    # Return list of points on the walls: corners and integer points on edges
    points = []
    # corners
    points.append((0,0))
    points.append((0,d))
    points.append((w,0))
    points.append((w,d))
    # For simplicity, just corners are enough because continuous walls
    return points

def visible_intervals_from_point(x, y, f):
    # Facing directions:
    # N=90, E=0, S=270, W=180
    # Field of view: f +-45 degrees (inclusive)
    base = {'N':90, 'E':0, 'S':270, 'W':180}
    center = base[f]
    start = angle_normalize(center-45)
    end = angle_normalize(center+45)
    # field of view interval may wrap around 0
    if start <= end:
        return [(start,end)]
    else:
        return [(start,360), (0,end)]


def angle_from_point_to(x1, y1, x2, y2):
    # returns angle in degrees in [0,360)
    dx = x2 - x1
    dy = y2 - y1
    ang = math.degrees(math.atan2(dy, dx))
    return angle_normalize(ang)

def is_in_fov(xi, yi, f, px, py):
    # Check if point (px, py) is in the field of view of member i at (xi, yi) facing f
    intervals = visible_intervals_from_point(xi, yi, f)
    ang = angle_from_point_to(xi, yi, px, py)
    for start,end in intervals:
        if start <= ang <= end:
            return True
    return False

def main():
    n,w,d = map(int, input().split())
    members = []
    for _ in range(n):
        x,y,f = input().split()
        x = int(x)
        y = int(y)
        members.append((x,y,f))

    # Possible clock points: all corners and all wall integer points (for simplicity choose only corners and edges endpoints)
    # The problem hint: clocks can be hung even on corners.
    points = []
    # add corners
    points.append((0,0))
    points.append((0,d))
    points.append((w,0))
    points.append((w,d))
    # add points along edges at each member's projection on edges
    # for each member, put the projections on four walls
    for (x,y,_) in members:
        points.append((0,y))
        points.append((w,y))
        points.append((x,0))
        points.append((x,d))

    # remove duplicates
    points = list(set(points))

    # For each member, record which points are visible in their field of view
    member_points = []
    for (x,y,f) in members:
        visible_points = set()
        for (px,py) in points:
            # if point coincides with member position, skip (cannot put clock inside room)
            if px == x and py == y:
                continue
            if is_in_fov(x,y,f,px,py):
                visible_points.add((px,py))
        member_points.append(visible_points)

    # Now we want minimum number of points (clocks) that cover all members
    # This is minimum set cover problem
    # members are elements to cover, sets are points covering members
    # We transform the problem into sets:
    # For each point, find members it covers
    point_cover = {}
    for idx,mp in enumerate(member_points):
        for p in mp:
            if p not in point_cover:
                point_cover[p] = set()
            point_cover[p].add(idx)

    uncovered = set(range(n))
    clocks = 0
    while uncovered:
        # choose point covering most uncovered members
        best_point = None
        best_cover = set()
        for p, covered_members in point_cover.items():
            cover = covered_members & uncovered
            if len(cover) > len(best_cover):
                best_cover = cover
                best_point = p
        if not best_point:
            # no point covers any uncovered member (should not happen)
            break
        uncovered -= best_cover
        clocks += 1

    print(clocks)

if __name__ == '__main__':
    main()