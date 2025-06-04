import sys
import math

EPS = 1e-10

def eq(a, b):
    return abs(a - b) < EPS

def point_eq(a, b):
    return abs(a[0] - b[0]) < EPS and abs(a[1] - b[1]) < EPS

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def line_intersection(p1, p2, p3, p4):
    d = (p2[0]-p1[0])*(p4[1]-p3[1]) - (p2[1]-p1[1])*(p4[0]-p3[0])
    if abs(d) < EPS:
        return None
    t = ((p3[0]-p1[0])*(p4[1]-p3[1]) - (p3[1]-p1[1])*(p4[0]-p3[0]))/d
    s = ((p3[0]-p1[0])*(p2[1]-p1[1]) - (p3[1]-p1[1])*(p2[0]-p1[0]))/d
    if 0-EPS<=t<=1+EPS and 0-EPS<=s<=1+EPS:
        ix = p1[0] + t*(p2[0]-p1[0])
        iy = p1[1] + t*(p2[1]-p1[1])
        return (ix, iy)
    return None

def between(a,b,c): # test if b is between a and c
    return (a[0]-b[0])*(c[0]-b[0]) <= EPS and (a[1]-b[1])*(c[1]-b[1]) <= EPS

def on_segment(p1,p2,p):
    minx = min(p1[0], p2[0]) - EPS
    maxx = max(p1[0], p2[0]) + EPS
    miny = min(p1[1], p2[1]) - EPS
    maxy = max(p1[1], p2[1]) + EPS
    return minx <= p[0] <= maxx and miny <= p[1] <= maxy

def normalize_point(p):
    # Round coordinates to avoid floating point errors below EPS
    return (round(p[0]*1e10)/1e10, round(p[1]*1e10)/1e10)

def main():
    input = sys.stdin.readline
    square = [(-100,-100),(100,-100),(100,100),(-100,100)]
    edges = [(square[i],square[(i+1)%4]) for i in range(4)]
    while True:
        n = int(input())
        if n == 0:
            break
        lines = []
        # Each line is represented as sorted tuple of two points on square edge
        for _ in range(n):
            x1,y1,x2,y2 = map(int,input().split())
            p1 = (x1,y1)
            p2 = (x2,y2)
            # Sort points to normalize representation
            if p2 < p1:
                p1, p2 = p2, p1
            lines.append((p1,p2))

        # For each line find all intersection points: on boundary and with other lines
        segments_points = []
        for i in range(n):
            pA, pB = lines[i]
            pts = [pA,pB]
            for j in range(i+1, n):
                pC, pD = lines[j]
                inter = line_intersection(pA,pB,pC,pD)
                if inter is not None:
                    ip = normalize_point(inter)
                    if on_segment(pA,pB,ip) and on_segment(pC,pD,ip):
                        pts.append(ip)
            segments_points.append(pts)

        # Add intersections with square edges for each line
        for i in range(n):
            pA, pB = lines[i]
            pts = segments_points[i]
            for e0,e1 in edges:
                inter = line_intersection(pA,pB,e0,e1)
                if inter is not None:
                    ip = normalize_point(inter)
                    if on_segment(pA,pB,ip) and on_segment(e0,e1,ip):
                        pts.append(ip)
            # Remove duplicates and sort points on the line according to position from pA to pB
            pts_set = set()
            filtered = []
            for pt in pts:
                pt = normalize_point(pt)
                if pt not in pts_set:
                    pts_set.add(pt)
                    filtered.append(pt)
            def key_func(p):
                dx = p[0] - pA[0]
                dy = p[1] - pA[1]
                return dx*dx + dy*dy
            filtered.sort(key=key_func)
            segments_points[i] = filtered

        # Build graph

        # vertices: all intersection points (line-line or line-boundary)
        # edges: between consecutive points along lines and along square edges

        # Map points to ids for union-find
        # use dict with rounding to avoid fp errors

        points_map = dict()
        def get_id(p):
            p = normalize_point(p)
            if p not in points_map:
                points_map[p] = len(points_map)
            return points_map[p]

        # Add all points from line segments
        for pts in segments_points:
            for pt in pts:
                get_id(pt)

        # Add all square vertices
        for v in square:
            get_id(v)

        # Graph edges: along lines
        uf = UnionFind(len(points_map))

        for pts in segments_points:
            for i in range(len(pts)-1):
                a = get_id(pts[i])
                b = get_id(pts[i+1])
                uf.union(a,b)

        # Graph edges: along square edges (add segments between consecutive vertices, but also check for intersections)
        for e0, e1 in edges:
            # we must find all intersection points of square edge with lines to split edge into segments
            inters = [e0, e1]
            for i in range(n):
                pA, pB = lines[i]
                inter = line_intersection(e0,e1,pA,pB)
                if inter is not None:
                    ip = normalize_point(inter)
                    if on_segment(e0,e1,ip) and on_segment(pA,pB,ip):
                        inters.append(ip)
            # unique and sort points on edge
            inters = list(set(inters))
            inters.sort(key=lambda p: (p[0], p[1]) if abs(e1[0]-e0[0]) > abs(e1[1]-e0[1]) else (p[1], p[0]))
            # Union consecutive points
            for i in range(len(inters)-1):
                a = get_id(inters[i])
                b = get_id(inters[i+1])
                uf.union(a,b)

        # Count vertices V and edges E
        V = len(points_map)
        # Count edges
        # We count segments along lines plus segments along square edges after splitting by intersections.

        # Count edges along lines
        E = 0
        for pts in segments_points:
            E += len(pts)-1

        # Count edges along square edges
        for e0, e1 in edges:
            inters = [e0, e1]
            for i in range(n):
                pA, pB = lines[i]
                inter = line_intersection(e0,e1,pA,pB)
                if inter is not None:
                    ip = normalize_point(inter)
                    if on_segment(e0,e1,ip) and on_segment(pA,pB,ip):
                        inters.append(ip)
            inters = list(set(inters))
            inters.sort(key=lambda p: (p[0], p[1]) if abs(e1[0]-e0[0]) > abs(e1[1]-e0[1]) else (p[1], p[0]))
            E += len(inters)-1

        # Count number of connected components
        parent_set = set()
        for i in range(V):
            parent_set.add(uf.find(i))
        C = len(parent_set)

        # Euler's formula for planar graph:
        # F = E - V + C + 1
        # Faces = regions = number of pieces
        F = E - V + C + 1

        print(F)

class UnionFind:
    def __init__(self,n):
        self.p = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.p[x] = y
        else:
            self.p[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

if __name__ == "__main__":
    main()