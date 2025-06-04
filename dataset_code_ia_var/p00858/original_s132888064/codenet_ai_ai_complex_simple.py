from functools import reduce, lru_cache, cmp_to_key, partial
from collections import defaultdict, deque, Counter, namedtuple
from itertools import chain, combinations, product, permutations, tee, count, cycle, accumulate, starmap, islice, groupby
from heapq import heappush, heappop
import sys
from operator import itemgetter, mul, add
import math

readline = sys.stdin.readline
write = sys.stdout.write

def dot3(O, A, B):
    return reduce(add, map(mul, (A[0]-O[0],A[1]-O[1]), (B[0]-O[0],B[1]-O[1])))

def cross3(O, A, B):
    return (lambda a, b, c, d: a*d-b*c)(A[0]-O[0], A[1]-O[1], B[0]-O[0], B[1]-O[1])

def dist2(A, B):
    return sum(map(lambda u,v:(u-v)**2, A, B))

def is_intersection(P0, P1, Q0, Q1):
    V = [cross3(P0,P1,Q0), cross3(P0,P1,Q1), cross3(Q0,Q1,P0), cross3(Q0,Q1,P1)]
    if all(x==0 for x in V[:2]):
        E0,E1=dot3(P0,P1,Q0),dot3(P0,P1,Q1)
        E0,E1 = sorted((E0,E1))
        return E0 <= dist2(P0,P1) and 0 <= E1
    return V[0]*V[1] <= 0 and V[2]*V[3] <= 0

def solve():
    N = int(readline())
    if not N: return False
    S, G = (tuple(map(int,readline().split())) for _ in range(2))
    P=[tuple(map(int,readline().split())) for _ in range(N)]
    L=[(lambda a,b,c,d:((a,c),(b,d)))(*x) for x in P]

    def check(p0, p1, q):
        T = tuple(map(subtuple,p1,p0))
        S = tuple(map(subtuple,q,p0))
        cross = S[0]*T[1] - S[1]*T[0]
        if cross != 0: return False
        return all((min(a,b) <= c <= max(a,b)) for a,b,c in zip(p0,p1,q))

    subtuple = lambda a,b: a-b
    calc = lambda p0, p1, q: (d:=tuple(map(subtuple,p1,p0)), s:=tuple(map(subtuple,q,p0)), k:=(s[0],d[0]) if d[0] else (s[1],d[1])) if (s[0]*d[1]==s[1]*d[0]) else None

    ss = set()
    G0 = [[] for _ in range(N)]
    Q = [0]*N
    for i, (pi,qi) in enumerate(L):
        u0=u1=0
        for j, (pj,qj) in enumerate(L):
            if i==j: continue
            f0,f1=check(pj,qj,pi),check(pj,qj,qi)
            u0|=f0; u1|=f1
            if f0 or f1: G0[i].append(j)
        if u0 and u1: ss|={pi,qi};Q[i]=1

    ss0 = tuple(sorted(ss))
    mp = dict(zip(ss0, range(len(ss0))))
    l=len(ss0); Gf=[[] for _ in range(l)]

    for i, (pi,qi) in enumerate(L):
        if not Q[i]:continue
        x0,y0=pi;x1,y1=qi
        candidates = [ (0,0,pi), (1,0,qi) ]
        for j, (pj,qj) in enumerate(L):
            for argq in [pj,qj]:
                k=calc(pi,qi,argq)
                if not k: continue
                s0,t0=k[0],k[1]
                t_s = s0/t0 if t0 else 0
                if 0<=s0<=t0:
                    if Q[j]: candidates.append((t_s,0,argq))
                    else:
                        x2,y2=argq;x3,y3=(pj if argq==qj else qj)
                        v=(x1-x0)*(x3-x2)+(y1-y0)*(y3-y2)
                        candidates.append((t_s,1,v))
        candidates.sort()
        pr=None;a=b=1
        for e, t, v in candidates:
            if t:
                if v < 0: b=0
                elif v > 0: a=0
                else: a=b=0
                continue
            if pr!=None and pr!=v:
                d=math.hypot(*(a-b for a,b in zip(pr,v)))
                k0=mp[pr];k1=mp[v]
                if a: Gf[k0].append((k1,d))
                if b: Gf[k1].append((k0,d))
                a=b=1
            pr=v

    INF=1<<60
    prv=[-1]*l; dst=[INF]*l
    sp,gp=mp[S],mp[G]
    dst[sp]=0;que=[(0,sp)]
    while que:
        cost,v=heappop(que)
        if dst[v]<cost: continue
        for w,d in Gf[v]:
            if cost+d<dst[w]:
                dst[w]=cost+d;prv[w]=v
                heappush(que,(cost+d,w))

    if dst[gp]==INF:
        write("-1\n")
        return True

    path=list(iterate=lambda v=gp: prv[v], start=gp, stop=sp)
    def iterate(f,start,stop):
        res=[start]
        while res[-1]!=stop: res.append(f(res[-1]))
        return res[::-1]
    for x,y in map(ss0.__getitem__,path):
        write(f"{x} {y}\n")
    write("0\n")
    return True

while solve():
    ...