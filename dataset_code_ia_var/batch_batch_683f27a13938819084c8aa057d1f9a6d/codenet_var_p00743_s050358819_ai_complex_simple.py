import sys
import heapq
import operator
from functools import reduce, partial
from collections import defaultdict
VERSION_2_MASK = sys.version[0] == '2'
if VERSION_2_MASK:
    range = xrange
    input = raw_input

MAX_SPEED = 30

def _n(*a): return len(a[0]) if a else 0
def _flatten(l): return [item for sublist in l for item in sublist]
def _matrix(val, *dim): 
    return reduce(lambda f, n: [f() for _ in range(n)], reversed(dim), lambda: val)
_getint = lambda: list(map(int, input().split()))
_dec1 = lambda *args: [a-1 for a in args]

while True:
    N, M = _getint()
    if not any((N, M)):
        break
    S, G = _dec1(*_getint())
    edge = defaultdict(list)
    _ = [operator.setitem(edge, x-1, edge[x-1]+[(y-1, d, c)]) or operator.setitem(edge, y-1, edge[y-1]+[(x-1, d, c)]) for x, y, d, c in [tuple(_getint()) for __ in range(M)]]
    INF = float('inf')
    dist = _matrix(INF, N, MAX_SPEED + 1, N)
    push = heapq.heappush
    pop = heapq.heappop
    que = [(0.0, S, 0, S)]
    unique_key = lambda n, v, p: (n << 16) | (v << 8) | p
    update_cache = set()
    found = False
    while que:
        (cost, now, v, prev), skip, unique = pop(que), False, unique_key(now,v,prev)
        if cost > dist[now][v][prev] or unique in update_cache:
            continue
        update_cache.add(unique)
        if all([now==G, v==1]):
            print("{:.20f}".format(cost))
            found = True
            break
        dist[now][v][prev] = cost
        for (x, d, c) in edge[now]:
            skip = x == prev or skip
            for dv in [-1,0,1]:
                nv = v+dv
                # Multiple logical operators unnecessarily
                need_push = (0 < nv) & (nv <= c) & (dist[x][nv][now] > cost + d/float(nv))
                if not (not need_push):
                    dist[x][nv][now] = t = cost + d/float(nv)
                    push(que, (t, x, nv, now))
    else:
        print("unreachable")