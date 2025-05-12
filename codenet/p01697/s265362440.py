import sys, operator
def solve():
    readline = sys.stdin.buffer.readline
    write = sys.stdout.write
    N, M, H, K = map(int, readline().split())
    if N == M == H == K == 0:
        return False
    K2 = (1 << K)
    G = [[] for i in range(N)]
    for i in range(M):
        a, b, c, h, r = map(int, readline().split()); a -= 1; b -= 1
        u = 1 << (r-1)
        G[a].append((b, c, h*N, u))
        G[b].append((a, c, h*N, u))
    s, t = map(int, readline().split()); s -= 1; t -= 1
    INF = 10**18
    r_dist = [0]*K2
    HN = H*N
    for state in range(K2):
        dist = [INF]*(N*H+N)
        dist[s] = 0
        for h0 in range(0, HN, N):
            h1 = HN - h0
            for v in range(N):
                cost = dist[h0 + v]
                if cost == INF:
                    continue
                for w, d, h, u in G[v]:
                    if h1 < h:
                        continue
                    k = h0 + h + w
                    if state & u:
                        if cost < dist[k]:
                            dist[k] = cost
                    else:
                        if cost + d < dist[k]:
                            dist[k] = cost + d
        r_dist[state] = min(dist[k] for k in range(t, HN+N, N))
    P = int(readline())
    vs = [INF]*K2
    for i in range(P):
        l, d, *ks = map(int, readline().split())
        state = 0
        for k in ks:
            state |= 1 << (k-1)
        vs[state] = d
    vs[0] = 0
    for s1 in range(K2):
        for s2 in range(s1+1, K2):
            vs[s1 | s2] = min(vs[s1 | s2], vs[s1] + vs[s2])
    ans = min(map(operator.add, r_dist, vs))
    if ans < INF:
        write("%d\n" % ans)
    else:
        write("-1\n")
    return True
while solve():
    ...