from collections import defaultdict
from heapq import heappush, heappop, heapify
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    INF = 10**9
    N, M = map(int, readline().split())
    if N == M == 0:
        return False
    H = [int(readline()) for i in range(N)]
    E = []
    G = [[] for i in range(N)]
    for i in range(M):
        a, b, c = map(int, readline().split())
        E.append((c, a-1, b-1))
        G[a-1].append((b-1, c))
        G[b-1].append((a-1, c))
    E.sort()

    mp = defaultdict(list)
    for i in range(N):
        mp[H[i]].append(i)

    def root(x):
        if x == prt[x]:
            return x
        prt[x] = y = root(prt[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px == py:
            return False
        if sz[px] > sz[py]:
            prt[py] = px
            sz[px] += sz[py]
        else:
            prt[px] = py
            sz[py] += sz[px]
        return True

    *prt, = range(N)
    sz = [1]*N

    *hs, = mp.keys()
    hs.sort(reverse=1)
    U = [0]*N
    c = 0
    h0 = -1
    k = -1
    for i, h in enumerate(hs):
        vs = mp[h]
        for v in vs:
            for w, _ in G[v]:
                if not U[w]:
                    continue
                unite(v, w)
            U[v] = 1
            c += 1
        v0 = root(vs[0])
        if sz[v0] != c:
            h0 = h
            k = i

    if k == len(hs)-1:
        write("0\n")
        return True

    ans = 0

    h = hs[k+1]
    *prt, = range(N); sz = [1]*N
    for c, a, b in E:
        if H[a] >= h and H[b] >= h:
            if unite(a, b):
                ans += c

    mc = [INF]*N
    U = [0]*N
    for v in range(N):
        if H[v] < h:
            continue
        U[v] = 1
        for w, d in G[v]:
            if H[w] < h:
                mc[w] = min(mc[w], d)

    que = []
    for v in range(N):
        if H[v] >= h:
            continue
        que.append((-H[v], mc[v], v))
    heapify(que)
    while que:
        _, cost, v = heappop(que)
        if U[v]:
            continue
        U[v] = 1
        h = H[v]
        ans += cost
        for w, d in G[v]:
            if not U[w] and H[w] <= h and d < mc[w]:
                mc[w] = d
                heappush(que, (-H[w], d, w))
    write("%d\n" % ans)
    return True
while solve():
    ...