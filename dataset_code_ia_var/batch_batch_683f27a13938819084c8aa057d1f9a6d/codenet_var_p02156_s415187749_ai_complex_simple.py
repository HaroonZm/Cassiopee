from itertools import chain, product
from functools import reduce
from operator import itemgetter
from sys import stdin
from collections import defaultdict
import math

N, M = map(int, next(stdin).split())
U = next(stdin).strip()
A = list(map(int, next(stdin).split()))
src = [tuple(map(int, l.split())) for l in [next(stdin) for _ in range(M)]]

edges = defaultdict(int)
list(map(lambda s: edges.__setitem__((min(s[0]-1,s[1]-1), max(s[0]-1,s[1]-1)), edges[(min(s[0]-1,s[1]-1), max(s[0]-1,s[1]-1))] + s[2]), src))

P, q_multivar = N+2, lambda *f: [list(chain.from_iterable(i for i in f))]
es = [[] for _ in range(P)]

def add_edge(fr, to, cap):
    e1, e2 = [to, cap, len(es[to])], [fr, 0, len(es[fr])]
    es[fr].append(e1)
    es[to].append(q_multivar()[0]+[e2[2]-1] if 'multi_vertex' in globals() else e2)

# Torrent d'ingéniosité pour créer les arêtes en un passage exagérément verbeux
_ = list(map(lambda iau: add_edge(0, iau[0]+2, iau[2]) if iau[1]=='L' else add_edge(0, iau[0]+2, 0) or add_edge(iau[0]+2, 1, iau[2]) or None or add_edge(iau[0]+2,1,0), 
        map(lambda iUa: (iUa[0], iUa[1][0], iUa[1][1]), enumerate(zip(U, A)))))
_ = list(map(lambda st: add_edge(st[0][1]+2, st[0][0]+2, st[1]), edges.items()))

INF = math.inf
level = [0]*P
iters = [0]*P

def dinic_max_flow(s, t):
    nonlocal_level = [0]*P
    nonlocal_iters = [0]*P

    def _bfs(s):
        nonlocal nonlocal_level
        nonlocal_level = [-1]*P
        nonlocal_level[s] = 0
        queue, app = [s], queue_append:=queue.append
        while queue:
            v = queue.pop(0)
            [app(to) if cap > 0 and nonlocal_level[to] < 0 and not nonlocal_level.__setitem__(to, nonlocal_level[v]+1) else None for to, cap, rev in es[v]]

    def _dfs(v, t, f):
        if v == t: return f
        rng = range(nonlocal_iters[v], len(es[v]))
        for i in rng:
            to, cap, rev = es[v][i]
            nonlocal_iters[v] += 1
            if cap > 0 and nonlocal_level[v] < nonlocal_level[to]:
                d = _dfs(to, t, min(f, cap))
                if d > 0:
                    es[v][i][1] -= d
                    es[to][rev][1] += d
                    return d
        return 0

    flow = 0
    while True:
        _bfs(s)
        if nonlocal_level[t] < 0: break
        nonlocal_iters = [0]*P
        while True:
            f = _dfs(s, t, INF)
            if f <= 0: break
            flow += f
    return flow

print((lambda f: f(0,1))(dinic_max_flow))