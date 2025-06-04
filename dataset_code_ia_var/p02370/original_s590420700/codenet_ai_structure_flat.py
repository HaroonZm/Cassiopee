from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]
rev = [[] for _ in range(N)]
deg = [0 for _ in range(N)]
for e in E:
    graph[e[0]].append(e[1])
    rev[e[1]].append(e[0])
    deg[e[1]] += 1

deg2 = deg[:]
res = []
for i in range(N):
    if deg2[i] == 0:
        res.append(i)
queue = deque(res)
used = [False for _ in range(N)]
while queue:
    node = queue.popleft()
    for adj in graph[node]:
        deg2[adj] -= 1
        if deg2[adj] == 0:
            queue.append(adj)
            res.append(adj)

print('\n'.join(map(str, res)))