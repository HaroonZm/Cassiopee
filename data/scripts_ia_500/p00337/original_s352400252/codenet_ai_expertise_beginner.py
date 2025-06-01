import sys
from math import atan2, hypot

def graham_scan(points):
    points = sorted(points, key=lambda p: p[1])
    base = points[0]
    rest = points[1:]
    rest.sort(key=lambda p: atan2(p[1]-base[1], p[0]-base[0]))
    stack = [base, rest[0]]

    for p in rest[1:]:
        while len(stack) > 1:
            x1, y1 = stack[-2][0], stack[-2][1]
            x2, y2 = stack[-1][0], stack[-1][1]
            x3, y3 = p[0], p[1]
            cross = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
            if cross > 0:
                break
            stack.pop()
        stack.append(p)
    return stack

def find_root(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, a, b):
    root_a = find_root(parent, a)
    root_b = find_root(parent, b)
    if root_a == root_b:
        return False
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
    return True

def kruskal(num_vertices, edges, border_edges):
    edges = sorted(edges, key=lambda e: e[0])
    parent = [i for i in range(num_vertices)]
    rank = [0]*num_vertices
    cost = 0

    for w, a, b in border_edges:
        if union(parent, rank, a, b):
            cost += w

    for w, a, b in edges:
        if union(parent, rank, a, b):
            cost += w

    return cost

if __name__ == "__main__":
    V, R = map(int, input().split())
    vertices = [list(map(int, sys.stdin.readline().split())) for _ in range(V)]
    edges = []
    for line in sys.stdin:
        s, t = map(int, line.split())
        s -= 1
        t -= 1
        x1, y1 = vertices[s]
        x2, y2 = vertices[t]
        dist = hypot(x1 - x2, y1 - y2)
        edges.append((dist, s, t))

    convex = graham_scan([(x, y, i) for i, (x, y) in enumerate(vertices)])
    border_edges = []
    n = len(convex)
    for i in range(n):
        x1, y1, idx1 = convex[i]
        x2, y2, idx2 = convex[(i+1)%n]
        dist = hypot(x1 - x2, y1 - y2)
        border_edges.append((dist, idx1, idx2))

    result = kruskal(V, edges, border_edges)
    print(result)