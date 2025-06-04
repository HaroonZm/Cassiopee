import sys
import math
sys.setrecursionlimit(10**7)

def dist_point_to_segment(px, py, x1, y1, x2, y2):
    # calc distance squared from point to segment
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return (px - x1)**2 + (py - y1)**2
    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))
    cx = x1 + t * dx
    cy = y1 + t * dy
    return (px - cx)**2 + (py - cy)**2

def dist_polyline_to_polyline(p1, p2):
    # minimum squared dist between two polylines p1 and p2
    # p1 and p2 are list of points [(x,y),...]
    min_dist = float('inf')
    # check all vertices p1 to p2 segments
    for (px, py) in p1:
        for i in range(len(p2)-1):
            d = dist_point_to_segment(px, py, p2[i][0], p2[i][1], p2[i+1][0], p2[i+1][1])
            if d < min_dist:
                min_dist = d
    # check all vertices p2 to p1 segments
    for (px, py) in p2:
        for i in range(len(p1)-1):
            d = dist_point_to_segment(px, py, p1[i][0], p1[i][1], p1[i+1][0], p1[i+1][1])
            if d < min_dist:
                min_dist = d
    # now check segment to segment distance for closer cases
    # check all segment pairs
    for i in range(len(p1)-1):
        for j in range(len(p2)-1):
            d = dist_segments(p1[i], p1[i+1], p2[j], p2[j+1])
            if d < min_dist:
                min_dist = d
    return math.sqrt(min_dist)

def dist_segments(a1, a2, b1, b2):
    # min distance squared between segments a1-a2 and b1-b2
    # Use projection and check endpoints
    # Reference: https://stackoverflow.com/questions/2824478/shortest-distance-between-two-line-segments
    SMALL_NUM = 1e-15
    u = (a2[0]-a1[0], a2[1]-a1[1])
    v = (b2[0]-b1[0], b2[1]-b1[1])
    w = (a1[0]-b1[0], a1[1]-b1[1])
    a = u[0]*u[0] + u[1]*u[1]
    b = u[0]*v[0] + u[1]*v[1]
    c = v[0]*v[0] + v[1]*v[1]
    d = u[0]*w[0] + u[1]*w[1]
    e = v[0]*w[0] + v[1]*w[1]
    D = a*c - b*b
    sc, sN, sD = 0.0, 0.0, D
    tc, tN, tD = 0.0, 0.0, D

    if D < SMALL_NUM:
        sN = 0.0
        sD = 1.0
        tN = e
        tD = c
    else:
        sN = (b*e - c*d)
        tN = (a*e - b*d)
        if sN < 0.0:
            sN = 0.0
            tN = e
            tD = c
        elif sN > sD:
            sN = sD
            tN = e + b
            tD = c
    if tN < 0.0:
        tN = 0.0
        if -d < 0.0:
            sN = 0.0
        elif -d > a:
            sN = sD
        else:
            sN = -d
            sD = a
    elif tN > tD:
        tN = tD
        if (-d + b) < 0.0:
            sN = 0
        elif (-d + b) > a:
            sN = sD
        else:
            sN = (-d + b)
            sD = a
    sc = 0.0 if abs(sN) < SMALL_NUM else sN / sD
    tc = 0.0 if abs(tN) < SMALL_NUM else tN / tD

    dP = (w[0] + sc*u[0] - tc*v[0], w[1] + sc*u[1] - tc*v[1])
    return dP[0]*dP[0] + dP[1]*dP[1]

def main():
    input = sys.stdin.readline
    N1 = int(input())
    poly1 = []
    for _ in range(N1):
        x, y = map(int, input().split())
        poly1.append((x, y))
    N2 = int(input())
    poly2 = []
    for _ in range(N2):
        x, y = map(int, input().split())
        poly2.append((x, y))

    # Add boundary points as per problem statement
    poly1 = [(0,0)] + poly1 + [(1000,0)]
    poly2 = [(0,1000)] + poly2 + [(1000,1000)]

    # Compute minimal distance between polylines
    distance = dist_polyline_to_polyline(poly1, poly2)

    # The maximum diameter is exactly the minimal distance because circle can touch lines
    print(f"{distance:.10f}")

if __name__ == "__main__":
    main()