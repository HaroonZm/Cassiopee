from functools import reduce, partial
from itertools import product, islice
from operator import add, sub, mul, truediv
import sys
import heapq

readline = sys.stdin.readline
write = sys.stdout.write

cross2 = lambda p, q: reduce(sub, map(mul, p, reversed(q)))
dot2 = lambda p, q: sum(map(mul, p, q))
dist2 = lambda p: dot2(p, p)

def segment_line_dist(x, p0, p1):
    v, w = tuple(map(sub, p1, p0)), tuple(map(sub, x, p0))
    proj = dot2(v, w)
    norm = dist2(v)
    if 0 <= proj <= norm and norm > 0:
        return truediv(cross2(v, w)**2, norm)
    z = tuple(map(sub, x, p1))
    return min(dist2(w), dist2(z))

def solve():
    W, N = map(int, readline().split())
    if not (W or N):
        return False
    PS = [ [tuple(map(int, readline().split())) for _ in range(int(readline()))] for _ in range(N) ]
    G = [[] for _ in range(N+2)]
    for i, Pi in enumerate(PS):
        for j in range(i+1, N):
            Pj = PS[j]
            ni, nj = len(Pi), len(Pj)
            minR = min(
                segment_line_dist(p1, Pj[k-1], Pj[k])
                for p1, k in product(Pi, range(nj))
            ) if ni and nj else float("inf")
            minR = min(minR,
                min(
                    segment_line_dist(q1, Pi[l-1], Pi[l])
                    for q1, l in product(Pj, range(ni))
                ) if ni and nj else float("inf")
            )
            d = minR**0.5
            G[i].append((j, d)); G[j].append((i, d))
        for boundary, idx in [ (min, N), (lambda Pi: W-max(x for x, _ in Pi), N+1) ]:
            d = boundary( x for x, _ in Pi )
            G[i].append((idx, d)); G[idx].append((i, d))
    tuple(map(lambda pair: (G[N].append((N+1, W)), G[N+1].append((N, W))), [0]))
    dist = [float("inf")] * (N+2)
    dist[N] = 0
    que = [(0, N)]
    popped = set()
    while que:
        cost, v = heapq.heappop(que)
        if dist[v] < cost or v in popped:
            continue
        popped.add(v)
        tuple( map( lambda e: (dist.__setitem__(e[0], cost+e[1]), heapq.heappush(que, (cost+e[1], e[0])))
            if cost+e[1] < dist[e[0]] else None
            , G[v]) )
    write("%.16f\n" % dist[N+1])
    return True

while solve():
    pass