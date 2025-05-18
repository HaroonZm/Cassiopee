from collections import deque

N, M, *L = map(int, open(0).read().split())

E = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(L[:2 * M])] * 2):
    E[a].append(b)
    E[b].append(a)

colors = [0] * (N + 1)
visited = [-1] * (N + 1)

for v, d, c in reversed(tuple(zip(*[iter(L[2 * M + 1:])] * 3))):
    Q = deque([(d, v)])
    while Q:
        cnt, v = Q.popleft()
        if visited[v] >= cnt:
            continue
        if colors[v] == 0:
            colors[v] = c
        visited[v] = cnt
        if cnt > 0:
            Q.extend((cnt - 1, u) for u in E[v])

for c in colors[1:]:
    print(c)