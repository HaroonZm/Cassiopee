import sys
import math

def polygon_area(poly):
    area = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%n]
        area += x1*y2 - x2*y1
    return abs(area)/2

def inside_halfplane(p, a, b, c):
    # Half-plane: ax + by + c >= 0
    return a*p[0] + b*p[1] + c >= -1e-14

def line_through_points(p1, p2):
    # line ax + by + c = 0 passing through p1, p2
    a = p2[1]-p1[1]
    b = p1[0]-p2[0]
    c = -(a*p1[0] + b*p1[1])
    norm = math.hypot(a,b)
    return a/norm, b/norm, c/norm

def segment_line_intersection(a, b, c, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d1 = a*x1 + b*y1 + c
    d2 = a*x2 + b*y2 + c
    # Assure |d1 - d2| > 0
    t = d1/(d1 - d2)
    x = x1 + t*(x2 - x1)
    y = y1 + t*(y2 - y1)
    return (x,y)

def clip_polygon(polygon, a, b, c):
    new_poly = []
    n = len(polygon)
    for i in range(n):
        cur = polygon[i]
        nxt = polygon[(i+1)%n]
        cur_in = inside_halfplane(cur, a, b, c)
        nxt_in = inside_halfplane(nxt, a, b, c)
        if cur_in:
            new_poly.append(cur)
        if cur_in != nxt_in:
            inter = segment_line_intersection(a,b,c,cur,nxt)
            new_poly.append(inter)
    return new_poly

def voronoi_region(island, castles, idx):
    poly = island[:]
    n_castles = len(castles)
    cx, cy = castles[idx]
    for j in range(n_castles):
        if j == idx:
            continue
        ox, oy = castles[j]
        # bisector between (cx,cy) and (ox,oy)
        dx = ox - cx
        dy = oy - cy
        mx = (cx + ox)/2
        my = (cy + oy)/2
        # line: a x + b y + c = 0
        a = dx
        b = dy
        c = -(a*mx + b*my)
        # half-plane: a x + b y + c <= 0 on the side closer to (cx, cy)
        # check which side (cx,cy) lies: s = a*cx + b*cy + c
        s = a*cx + b*cy + c
        if s > 0:
            a = -a
            b = -b
            c = -c
        poly = clip_polygon(poly, a, b, c)
        if not poly:
            break
    return poly

input = sys.stdin.readline

while True:
    line = ''
    while line.strip()=='':
        line = sys.stdin.readline()
        if not line:
            sys.exit(0)
    N,M= map(int,line.strip().split())
    if N==0 and M==0:
        break
    island = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    castles = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    for i in range(M):
        region = voronoi_region(island, castles, i)
        area = polygon_area(region) if region else 0.0
        print(f"{area:.10f}")