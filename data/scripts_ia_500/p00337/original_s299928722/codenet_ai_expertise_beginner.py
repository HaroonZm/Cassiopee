def dist2(A, B):
    dx = A[0] - B[0]
    dy = A[1] - B[1]
    return dx * dx + dy * dy

def cross(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])

def convex_hull(points):
    points_with_index = []
    for i in range(len(points)):
        points_with_index.append(points[i] + [i])
    points_with_index.sort()
    
    Q = []
    for i in range(len(points_with_index)):
        while len(Q) > 1 and cross(points_with_index[Q[-2]], points_with_index[Q[-1]], points_with_index[i]) >= 0:
            Q.pop()
        Q.append(i)
    k = len(Q)
    for i in range(len(points_with_index) - 2, -1, -1):
        while len(Q) > k and cross(points_with_index[Q[-2]], points_with_index[Q[-1]], points_with_index[i]) >= 0:
            Q.pop()
        Q.append(i)
    
    hull_indices = []
    for i in Q:
        hull_indices.append(points_with_index[i][2])
    return hull_indices

from math import sqrt

v, r = map(int, input().split())
points = []
for _ in range(v):
    x, y = map(int, input().split())
    points.append([x, y])

hull = convex_hull(points)

parent = list(range(v))

def find_root(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

answer = 0.0
for i in range(len(hull) - 1):
    union(hull[i], hull[i+1])
    answer += sqrt(dist2(points[hull[i]], points[hull[i+1]]))

edges = []
for _ in range(r):
    s, t = map(int, input().split())
    edges.append([s, t])

edges.sort(key=lambda edge: dist2(points[edge[0] - 1], points[edge[1] - 1]))

for s, t in edges:
    if find_root(s - 1) != find_root(t - 1):
        union(s - 1, t - 1)
        answer += sqrt(dist2(points[s - 1], points[t - 1]))

print(answer)