import sys
from math import atan2, hypot

def graham_scan(points):
    # Sort points by Y then process for convex hull
    points.sort(key=lambda p: p[1])
    base = points[0]
    # Sort the rest by polar angle relative to base point
    sorted_points = sorted(points[1:], key=lambda p: atan2(p[1] - base[1], p[0] - base[0]))
    pts = [base] + sorted_points + [base]  # wrap-around to close polygon
    hull = [pts[-1], pts[0]]  # start with last and first

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    for p in pts[1:]:
        while len(hull) > 1 and cross(hull[-2], hull[-1], p) < 0:
            hull.pop()
        hull.append(p)
    return hull[:-1]  # exclude the last point which is duplicate of first

def kruskal(vertex_count, edge_list, border_edges):
    parent = [-1] * vertex_count

    def find(x):
        while parent[x] >= 0:
            x = parent[x]
        return x

    def union(edge):
        a, b = find(edge[1]), find(edge[2])
        if a != b:
            if parent[a] > parent[b]:
                a, b = b, a
            parent[a] += parent[b]
            parent[b] = a
            return True
        return False

    total_cost = 0
    # Add the border edges first to guarantee the hull is connected
    for w, u, v in border_edges:
        total_cost += w
        union((0, u, v))

    # Adjust remaining edges count accordingly (small hack here)
    remaining = vertex_count - (len(border_edges) - 1)

    edges_sorted = sorted(edge_list)
    for w, u, v in edges_sorted:
        if union((0, u, v)):
            total_cost += w
            remaining -= 1
            if remaining == 1:
                break
    return total_cost

if __name__ == "__main__":
    V, R = map(int, input().split())
    vertices = []
    for i in range(V):
        x, y = map(int, sys.stdin.readline().split())
        vertices.append([x, y, i])

    edges = []
    for line in sys.stdin:
        s, t = map(int, line.split())
        s -= 1
        t -= 1
        dist = hypot(vertices[s][0] - vertices[t][0], vertices[s][1] - vertices[t][1])
        edges.append((dist, s, t))

    convex = graham_scan(vertices)
    border_edges = []
    for i in range(len(convex)):
        x1, y1, s = convex[i]
        x2, y2, t = convex[(i+1) % len(convex)]
        dist = hypot(x1 - x2, y1 - y2)
        border_edges.append((dist, s, t))

    cost = kruskal(V, edges, border_edges)
    print(cost)