import sys
import math
import heapq

def star_points(x, y, a_deg, r):
    points = []
    a_rad = math.radians(a_deg)
    angle = a_rad
    for i in range(5):
        # outer point
        ox = x + r * math.sin(angle)
        oy = y + r * math.cos(angle)
        points.append((ox, oy))
        # inner point
        inner_angle = angle + math.radians(36)
        cr = r * math.sin(math.radians(18)) / math.sin(math.radians(54))
        ix = x + cr * math.sin(inner_angle)
        iy = y + cr * math.cos(inner_angle)
        points.append((ix, iy))
        angle += math.radians(72)
    return points

def segment_intersect(p1, p2, p3, p4):
    def ccw(a,b,c):
        return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
    return (ccw(p1,p3,p4) != ccw(p2,p3,p4)) and (ccw(p1,p2,p3) != ccw(p1,p2,p4))

def segments_intersect_any(pts1, pts2):
    n1 = len(pts1)
    n2 = len(pts2)
    for i in range(n1):
        for j in range(n2):
            p1 = pts1[i]
            p2 = pts1[(i+1)%n1]
            p3 = pts2[j]
            p4 = pts2[(j+1)%n2]
            if segment_intersect(p1,p2,p3,p4):
                return True
    return False

def point_in_polygon(pt, polygon):
    # ray casting method
    x, y = pt
    inside = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%n]
        if ((y1 > y) != (y2 > y)) and (x < (x2-x1)*(y - y1)/(y2 - y1) + x1):
            inside = not inside
    return inside

def polygons_intersect(pts1, pts2):
    # Check segment intersection
    if segments_intersect_any(pts1, pts2):
        return True
    # Check if any point of one polygon is inside the other
    for p in pts1:
        if point_in_polygon(p, pts2):
            return True
    for p in pts2:
        if point_in_polygon(p, pts1):
            return True
    return False

def solve():
    input = sys.stdin.readline
    while True:
        N, M, L = map(int, input().split())
        if N==0 and M==0 and L==0:
            break
        stars = []
        for _ in range(N):
            x, y, a, r = map(int, input().split())
            pts = star_points(x,y,a,r)
            stars.append((x,y,a,r,pts))

        # Build graph for Dijkstra
        # Edge weight: 0 if stars directly connected (the five-point star edges),
        # distance otherwise (Euclidean between centers)
        graph = [[] for _ in range(N)]

        for i in range(N):
            for j in range(i+1,N):
                # Check if stars are connected: polygons intersect (including touching),
                # means can move along the five-point star edges inside union,
                # so cost 0 between these stars.
                if polygons_intersect(stars[i][4], stars[j][4]):
                    graph[i].append((j,0))
                    graph[j].append((i,0))
                else:
                    # cost is distance between centers
                    dx = stars[i][0] - stars[j][0]
                    dy = stars[i][1] - stars[j][1]
                    dist = math.sqrt(dx*dx + dy*dy)
                    graph[i].append((j, dist))
                    graph[j].append((i, dist))

        # Dijkstra from M-1 to L-1
        dist = [math.inf]*N
        dist[M-1] = 0
        hq = [(0, M-1)]
        while hq:
            cd, u = heapq.heappop(hq)
            if dist[u]<cd:
                continue
            if u == L-1:
                break
            for v,w in graph[u]:
                nd = cd + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(hq, (nd,v))
        print("%.15f" % dist[L-1])

if __name__=="__main__":
    solve()