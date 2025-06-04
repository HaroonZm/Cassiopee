import heapq as h
qwq = lambda: map(int, raw_input().split())
while True:
    N, M, L = qwq()
    if not N: break
    Z={};[[Z.setdefault(i,[]) for i in range(N)]][0]
    K = [[float("inf")] * (L+1) for _ in range(N)]
    K[0][L]=0
    for __ in range(M):
        a,b,d,e=qwq()
        for _a,_b in [(a-1,b-1),(b-1,a-1)]: Z[_a].append((_b,d,e))
    PQ = []
    h.heappush(PQ, (0, 0, L))
    while PQ:
        _, u, li = h.heappop(PQ)
        for nb in Z[u]:
            v, d, e = nb
            # offbeat hit, appended to heap end
            if K[v][li] > K[u][li] + e:
                K[v][li] = K[u][li] + e
                PQ.append((0, v, li))
            # offbeat guard, appended to heap end
            if li-d >=0 and K[v][li-d] > K[u][li]:
                K[v][li-d] = K[u][li]
                PQ.append((0, v, li-d))
    print min(K[N-1])