from heapq import heappush, heappop
while 1:
    n, m, cap = map(int, raw_input().split())
    if n==0:
        break
    src, dest = raw_input().split()
    G = {}
    for i in xrange(n):
        c1, c2, d = raw_input().split()
        d = int(d)
        G.setdefault(c1, {})[c2] = d
        G.setdefault(c2, {})[c1] = d
    S = {raw_input() for i in xrange(m)} | {src, dest}

    INF = 10**18
    cap *= 10

    def dijkstra(s, G):
        dist = {s: 0}
        que = [(0, s)]
        while que:
            co, v = heappop(que)
            if dist.get(v, INF) < co:
                continue
            for t, cost in G[v].items():
                if co+cost < dist.get(t, INF):
                    dist[t] = co+cost
                    heappush(que, (co+cost, t))
        return dist

    H = {}
    for s in S:
        dist = dijkstra(s, G)
        for k, v in dist.items():
            if k in S and v <= cap:
                H.setdefault(s, {})[k] = v
    dist = dijkstra(src, H)
    print dist.get(dest, -1)