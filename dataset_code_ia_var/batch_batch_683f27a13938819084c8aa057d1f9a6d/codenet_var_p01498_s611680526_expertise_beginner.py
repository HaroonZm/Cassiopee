N, W, H = map(int, raw_input().split())

edges = []
for i in range(N):
    edges.append([])

points = []
ok = True

for i in range(N):
    x, y = map(int, raw_input().split())
    if x == 1 or y == 1 or x == W or y == H:
        ok = False
    points.append((x, y, i))

points.sort()
for i in range(N):
    if points[i][0] == points[i - 1][0]:
        a = points[i][2]
        b = points[i - 1][2]
        edges[a].append(b)
        edges[b].append(a)

points2 = []
for i in range(N):
    x, y, idx = points[i]
    points2.append((y, x, idx))

points2.sort()
for i in range(N):
    if points2[i][0] == points2[i - 1][0]:
        a = points2[i][2]
        b = points2[i - 1][2]
        edges[a].append(b)
        edges[b].append(a)

visited = [False] * N

def dfs(node, parent):
    if visited[node]:
        return
    visited[node] = True
    for nxt in edges[node]:
        if nxt != parent:
            dfs(nxt, node)

comp = 0
for i in range(N):
    if not visited[i]:
        dfs(i, -1)
        comp += 1

if comp > 1 and ok:
    comp += 1

print N - 2 + comp