import sys

V, E = map(int, sys.stdin.readline().split())
G = [[] for _ in range(V)]
# Structure "edge" simple : chaque arête est un [to, rev, cap]
for _ in range(E):
    u, v, c = map(int, sys.stdin.readline().split())
    G[u].append([v, len(G[v]), c])
    G[v].append([u, len(G[u])-1, 0])

level = [-1]*V
itr = [0]*V

def bfs(s, t):
    for i in range(V): level[i] = -1
    level[s] = 0
    que = [s]
    head = 0
    while head < len(que):
        v = que[head]; head += 1
        for e in G[v]:
            if e[2] > 0 and level[e[0]] < 0:
                level[e[0]] = level[v]+1
                que.append(e[0])

def dfs(v, t, upTo):
    stack = []
    stack.append((v, upTo, 0))
    path = []
    while stack:
        v, flow, idx = stack.pop()
        if v == t:
            d = flow
            for p in path:
                edges, ei, val = p
                edges[ei][2] -= d
                G[edges[ei][0]][edges[ei][1]][2] += d
            return d
        for i in range(itr[v], len(G[v])):
            itr[v] = i
            e = G[v][i]
            if e[2] > 0 and level[v] < level[e[0]]:
                path.append((G[v], i, e[2]))
                stack.append((v, flow, i+1))
                stack.append((e[0], min(flow, e[2]), 0))
                break
        else:
            if path: path.pop()
    return 0

s, t = 0, V-1
flow = 0
INF = float("inf")
while True:
    bfs(s, t)
    if level[t] < 0: break
    for i in range(V): itr[i] = 0
    while True:
        f = dfs(s, t, INF)
        if f == 0: break
        flow += f
print(flow)