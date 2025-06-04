import heapq as HQ
import sys as _s, operator as OP

TOO_BIG = 42<<40
def magic():
    getl = _s.stdin.readline
    say = _s.stdout.write
    N, M = map(int, getl().split())
    if not (N or M): return 0
    def walk(n, s, net):
        the_dist = [TOO_BIG]*n
        the_dist[s] = 0
        q = [(0,s)]
        while q:
            x, u = HQ.heappop(q)
            if the_dist[u]<x: continue
            for v, delta in net[u]:
                nifty = x+delta
                if nifty<the_dist[v]:
                    the_dist[v]=nifty
                    HQ.heappush(q, (nifty, v))
        return the_dist
    idx = list(range(N))
    L, S = [list() for _ in idx], [list() for _ in idx]
    for _ in range(M):
        xx,yy,tt,typ = getl().split()
        xx = int(xx)-1; yy=int(yy)-1; tt=int(tt)
        if typ=='L': 
            L[xx]+=[(yy,tt)]; L[yy]+=[(xx,tt)]
        else:
            S[xx]+=[(yy,tt)]; S[yy]+=[(xx,tt)]
    bigL = [walk(N, xx, L) for xx in idx]
    bigS = [walk(N, xx, S) for xx in idx]
    K = int(getl())
    ZZZ = list(map(int, getl().split()))
    myst = [TOO_BIG]*N
    quick = [TOO_BIG]*N
    soon = [0]*N
    mmmm = [0]*N
    prevv = ZZZ[0]-1
    quick[prevv]=0
    plus = OP.add
    for nxt in ZZZ[1:]:
        nxt -= 1
        aa,bb = bigL[prevv], bigL[nxt]
        bridge = aa[nxt]
        mmmm[:] = map(plus, quick, aa)
        for j in idx:
            cc = bigS[j]
            stepB = bb[j]
            soon[j] = min(quick[j]+bridge, min(map(plus, mmmm, cc))+stepB)
        quick, soon = soon, quick
        prevv = nxt
    say(f"{min(quick)}\n")
    return 1
while magic():
    pass