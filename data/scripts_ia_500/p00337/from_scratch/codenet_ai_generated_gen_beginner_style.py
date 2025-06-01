import math

V, R = map(int, input().split())
points = []
for _ in range(V):
    x, y = map(int, input().split())
    points.append((x, y))

edges = []
for _ in range(R):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    x1, y1 = points[s]
    x2, y2 = points[t]
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    edges.append((dist, s, t))

# クラスカル法で最小全域木を作る
parent = list(range(V))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        return True
    return False

edges.sort()
res = 0.0
for dist, s, t in edges:
    if union(s, t):
        res += dist

print("{0:.5f}".format(res))