from functools import reduce
from itertools import product, accumulate, chain, count, takewhile, islice, repeat, groupby
import operator as op
from heapq import heapify, heappush as hpush, heappop as hpop
from collections import deque, defaultdict

def dijkstra(n, E, i0=0):
    pq = [(0, i0)]
    dists = [None] * n
    visited = set()
    dists[i0] = 0

    while pq:
        du, u = hpop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in E[u]:
            alt = du + w
            if dists[v] is None or alt < dists[v]:
                dists[v] = alt
                hpush(pq, (alt, v))
    return [(x if x is not None else -1) for x in dists]

def readints():
    return list(map(int, input().split()))

N = int(input())
A = readints()
B = readints()

M = 51

def make_edges(S=None):
    S = S or range(1, M)
    def mk(i): 
        return list(map(lambda j: [i%j, 1<<j], filter(lambda j: j>0, S if isinstance(S, list) else list(S))))
    return list(map(mk, range(M)))

def chk(S):
    X = make_edges(S)
    all_dijk = list(map(lambda i: dijkstra(M, X, i), range(M)))
    return min(map(lambda i: all_dijk[A[i]][B[i]]>=0, range(N)))

L1 = list(islice(count(1), 50))
L2 = []

if not chk(L1):
    print(-1)
else:
    while L1:
        while True:
            if chk(L1 + L2):
                if not L1: break
                L1.pop()
            else:
                nextval = (L1[-1]+1) if L1 else 1
                L2.append(nextval)
                L1 = list(islice(count(1), nextval-1))
                break
        if not L1: break
    print(sum(map(lambda l: 1<<l, L2)))