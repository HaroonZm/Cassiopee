from heapq import heappush, heappop
M, N, K = map(int, input().split())

X = [[] for i in range(M)]
Y = [[] for i in range(N)]

for i in range(K):
    x, y = map(int, input().split()); x -= 1; y -= 1
    X[x].append((y, i))
    Y[y].append((x, i))

G0 = [[] for i in range(K)]
G1 = [[] for i in range(K)]
for x in range(M):
    vs = X[x]
    if vs:
        vs.sort()
        prv = vs[0]
        for v in vs[1:]:
            d = v[0] - prv[0]
            G0[prv[1]].append((v[1], d))
            G0[v[1]].append((prv[1], d))
            prv = v
for y in range(N):
    vs = Y[y]
    if vs:
        vs.sort()
        prv = vs[0]
        for v in vs[1:]:
            d = v[0] - prv[0]
            G1[prv[1]].append((v[1], d))
            G1[v[1]].append((prv[1], d))
            prv = v

INF = 10**18
que = []
D0 = [INF]*K; D1 = [INF]*K
if X[0]:
    y0, k = X[0][0]
    que.append((y0, 0, k))
while que:
    cost, t, v = heappop(que)
    if not t:
        if D0[v] < cost:
            continue
        for w, d in G0[v]:
            if cost + d < D0[w]:
                D0[w] = cost + d
                heappush(que, (cost + d, 0, w))
        if cost + 1 < D1[v]:
            D1[v] = cost + 1
            heappush(que, (cost + 1, 1, v))
    else:
        if D1[v] < cost:
            continue
        for w, d in G1[v]:
            if cost + d < D1[w]:
                D1[w] = cost + d
                heappush(que, (cost + d, 1, w))
        if cost + 1 < D0[v]:
            D0[v] = cost + 1
            heappush(que, (cost + 1, 0, v))
ans = INF
if X[M-1]:
    y0, k = X[M-1][-1]
    ans = min(ans, D0[k] + (N-1-y0))
if Y[N-1]:
    x0, k = Y[N-1][-1]
    ans = min(ans, D1[k] + (M-1-x0))
if ans < INF:
    print(ans)
else:
    print(-1)