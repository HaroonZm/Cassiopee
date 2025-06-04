from collections import deque

data = list(map(int, open(0).read().split()))
N = data[0]
M = data[1]
L = data[2:]

E = []
i = 0
while i <= N:
    E.append([])
    i += 1

i = 0
while i < 2*M:
    a = L[i]
    b = L[i+1]
    E[a].append(b)
    E[b].append(a)
    i += 2

colors = []
visited = []
i = 0
while i <= N:
    colors.append(0)
    visited.append(-1)
    i += 1

query_data = L[2*M+1:]
q_len = len(query_data) // 3
i = len(query_data) - 3
while i >= 0:
    v = query_data[i]
    d = query_data[i+1]
    c = query_data[i+2]
    Q = deque()
    Q.append((d, v))
    while Q:
        cnt, vv = Q.popleft()
        if visited[vv] >= cnt:
            continue
        if colors[vv] == 0:
            colors[vv] = c
        visited[vv] = cnt
        if cnt > 0:
            j = 0
            while j < len(E[vv]):
                u = E[vv][j]
                Q.append((cnt - 1, u))
                j += 1
    i -= 3

i = 1
while i <= N:
    print(colors[i])
    i += 1