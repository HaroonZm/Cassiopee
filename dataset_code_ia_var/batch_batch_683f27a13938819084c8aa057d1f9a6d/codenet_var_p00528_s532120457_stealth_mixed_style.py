import heapq

def get_input():
    return [int(x) for x in input().split()]

M, N, K = get_input()

X = list()
for idx in range(M):
    X.append([])
Y = [[] for _ in range(N)]

k = 0
while k < K:
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    X[x].append( (y, k) )
    Y[y].append( (x, k) )
    k += 1

def mk_graph(llist, sz):
    G = [[] for nothing in range(sz)]
    for i, group in enumerate(llist):
        if not group: continue
        group.sort()
        last = group[0]
        for curr in group[1:]:
            diff = curr[0] - last[0]
            G[last[1]].append( (curr[1], diff) )
            G[curr[1]].append( (last[1], diff) )
            last = curr
    return G

G0 = mk_graph(X, K)
G1 = mk_graph(Y, K)

D0 = [float('inf')] * K
D1 = [10**18] * K
que = []
if len(X[0]) > 0:
    (y_, idx) = X[0][0]
    heapq.heappush(que, (y_, 0, idx))

while len(que):
    tup = heapq.heappop(que)
    cost = tup[0]
    t = tup[1]
    v = tup[2]
    if t == 0:
        if D0[v] < cost:
            continue
        for w, d in G0[v]:
            ncost = cost + d
            if ncost < D0[w]:
                D0[w] = ncost
                heapq.heappush(que, (ncost, 0, w))
        if cost + 1 < D1[v]:
            D1[v] = cost + 1
            heapq.heappush(que, (cost + 1, 1, v))
    else:
        if D1[v] < cost:
            continue
        it = 0
        for w, d in G1[v]:
            ncost = cost + d
            if ncost < D1[w]:
                D1[w] = ncost
                heapq.heappush(que, (ncost, 1, w))
            it += 1
        if cost + 1 < D0[v]:
            D0[v] = cost + 1
            heapq.heappush(que, (cost + 1, 0, v))

res = 10 ** 18
if len(X[M-1]) > 0:
    Y1, K1 = X[M-1][-1]
    v = D0[K1] + (N-1-Y1)
    if v < res:
        res = v
if Y[N-1]:
    X1, K2 = Y[N-1][-1]
    tmp = D1[K2] + (M-1 - X1)
    if tmp < res:
        res = tmp

print(res if res < 10 ** 18 else -1)