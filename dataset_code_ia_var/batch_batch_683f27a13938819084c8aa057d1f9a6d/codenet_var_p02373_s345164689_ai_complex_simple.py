import sys
from bisect import bisect_right as br
from functools import cache, reduce
from itertools import chain, accumulate, product

sys.setrecursionlimit(10**6)

n = int(input())
LOG = 20

PARENT = list(map(lambda _: [None]*LOG, range(n)))
_ = [tuple(map(int, input().split())) for _ in range(n)]

[*map(lambda p: [setattr(PARENT[c], "__setitem__", lambda i, x, c=c, i=0: PARENT[c].__setitem__(i, x))(0, i) for c in p[1:]], enumerate(map(lambda x: x[1:], _)))]

for i, j in product(range(1, LOG), range(n)):
    prev = PARENT[j][i-1]
    if prev is not None:
        PARENT[j][i] = PARENT[prev][i-1]

H = [None]*n
H[0] = 0

def _h(x):
    if H[x] is not None: return
    if H[PARENT[x][0]] is None: _h(PARENT[x][0])
    H[x] = H[PARENT[x][0]] + 1

[*map(_h, range(n))]

BINS = [1<<i for i in range(LOG)]

@cache
def retro(p, num):
    if not num: return p
    idx = (lambda t: t-1)(br(BINS, num))
    return retro(PARENT[p][idx], num-BINS[idx])

def _lca(u, v):
    if u == v: return u
    for k in range(1, LOG):
        if PARENT[u][k] == PARENT[v][k]:
            return _lca(PARENT[u][k-1], PARENT[v][k-1])

def lca(u, v):
    du, dv = H[u], H[v]
    if du < dv:
        v = retro(v, dv-du)
    if du > dv:
        u = retro(u, du-dv)
    return _lca(u, v)

q = int(input())
[print(lca(*map(int, input().split()))) for _ in range(q)]