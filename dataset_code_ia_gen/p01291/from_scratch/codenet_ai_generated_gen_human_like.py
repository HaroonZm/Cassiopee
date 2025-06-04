import sys
import math
from collections import deque

def dist_point_to_segment(px, py, x1, y1, x2, y2):
    # Compute distance from point (px, py) to segment (x1, y1)-(x2, y2)
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return math.hypot(px - x1, py - y1)
    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))
    closest_x = x1 + t * dx
    closest_y = y1 + t * dy
    return math.hypot(px - closest_x, py - closest_y)

def polygons_min_dist(poly1, poly2):
    # Compute the minimal distance between two polygons poly1 and poly2
    # Each polygon is list of (x, y) points
    min_dist = float('inf')
    n1 = len(poly1)
    n2 = len(poly2)
    
    # Segment to segment minimal distance helper
    def seg_seg_dist(a1, a2, b1, b2):
        # Minimal distance between segments a1-a2 and b1-b2
        # Uses helper function dist_point_to_segment for endpoints
        dists = []
        dists.append(dist_point_to_segment(a1[0], a1[1], b1[0], b1[1], b2[0], b2[1]))
        dists.append(dist_point_to_segment(a2[0], a2[1], b1[0], b1[1], b2[0], b2[1]))
        dists.append(dist_point_to_segment(b1[0], b1[1], a1[0], a1[1], a2[0], a2[1]))
        dists.append(dist_point_to_segment(b2[0], b2[1], a1[0], a1[1], a2[0], a2[1]))
        return min(dists)
    
    for i in range(n1):
        a1 = poly1[i]
        a2 = poly1[(i + 1) % n1]
        for j in range(n2):
            b1 = poly2[j]
            b2 = poly2[(j + 1) % n2]
            d = seg_seg_dist(a1, a2, b1, b2)
            if d < min_dist:
                min_dist = d
    return min_dist

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if line == '':
                return
        W, N = map(int, line.strip().split())
        if W == 0 and N == 0:
            break

        pillars = []
        for _ in range(N):
            while True:
                l = input()
                if l.strip():
                    break
            M = int(l.strip())
            poly = []
            for __ in range(M):
                while True:
                    l2 = input()
                    if l2.strip():
                        break
                x, y = map(int, l2.strip().split())
                poly.append((x,y))
            pillars.append(poly)

        # Build nodes assignment:
        # node 0: super source (left boundary)
        # node 1..N: pillars
        # node N+1: super sink (right boundary)
        # We'll create a graph and do max flow

        V = N + 2
        INF = 1e10

        # Adjacency list for max flow graph
        graph = [[] for _ in range(V)]
        # We'll use an adjacency list with forward and backward edges for Dinic
        
        def add_edge(u, v, cap):
            graph[u].append([v, cap, len(graph[v])])
            graph[v].append([u, 0.0, len(graph[u]) - 1])
        
        # Connect super source (0) to pillars near left wall (x near 0)
        # Connect super sink (N+1) to pillars near right wall (x near W)
        # Connect pillars to pillars with capacity = minimal distance between pillars
        # Wall is at x=0 and x=W, so the minimal gap between pillar and wall is distance from polygon to line x=0 or x=W
        # For super source (0) and super sink (N+1) connections:
        # capacity is the minimal distance from pillar polygon to the wall

        # First build polygon for the left wall and right wall: vertical lines at x=0 and x=W
        # But for distance calculation to wall, we can just find minimal x or (W - x) for all polygon vertices

        # left wall cap for pillar i: minimal x among polygon vertices
        # right wall cap for pillar i: minimal W - x among polygon vertices

        for i, poly in enumerate(pillars, start=1):
            min_x = min(p[0] for p in poly)
            dist_left = min_x
            min_dist_to_left = float('inf')
            for p in poly:
                d = p[0]  # distance to x=0
                if d < min_dist_to_left:
                    min_dist_to_left = d

            min_x_right = float('inf')
            for p in poly:
                d = W - p[0]  # distance to x=W
                if d < min_x_right:
                    min_x_right = d
            
            # connect super source (0) to pillar i with capacity min_dist_to_left
            # connect pillar i to super sink (N+1) with capacity min_x_right
            # Only connect if distance > 0 (pillars do not touch walls)
            if min_dist_to_left > 1e-15:
                add_edge(0, i, min_dist_to_left)
            if min_x_right > 1e-15:
                add_edge(i, N+1, min_x_right)

        # Connect pillars to each other
        for i in range(N):
            for j in range(i+1, N):
                d = polygons_min_dist(pillars[i], pillars[j])
                # The capacity is the minimal gap between the two pillars
                # Add edges both ways with capacity d
                # Only if distance > 1e-15 to avoid zero capacity edges for touching polygons
                if d > 1e-15:
                    add_edge(i+1, j+1, d)
                    add_edge(j+1, i+1, d)

        # Dinic's max flow implementation
        def bfs(s, t, level):
            q = deque()
            q.append(s)
            level[s] = 0
            while q:
                u = q.popleft()
                for i, (v, cap, rev) in enumerate(graph[u]):
                    if cap > 1e-14 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            return level[t] >= 0

        def dfs(u, t, f, level, it):
            if u == t:
                return f
            while it[u] < len(graph[u]):
                v, cap, rev = graph[u][it[u]]
                if cap > 1e-14 and level[v] == level[u] + 1:
                    d = dfs(v, t, min(f, cap), level, it)
                    if d > 0:
                        graph[u][it[u]][1] -= d
                        graph[v][rev][1] += d
                        return d
                it[u] += 1
            return 0.0

        flow = 0.0
        s, t = 0, N+1

        while True:
            level = [-1] * V
            if not bfs(s, t, level):
                break
            it = [0] * V
            while True:
                f = dfs(s, t, INF, level, it)
                if f <= 1e-14:
                    break
                flow += f

        print(flow)

if __name__ == "__main__":
    main()