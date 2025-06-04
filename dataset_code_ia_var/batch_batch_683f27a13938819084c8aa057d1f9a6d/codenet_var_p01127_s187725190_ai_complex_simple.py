from functools import reduce
from itertools import product, chain, groupby
try:
    xrange
except NameError:
    xrange = range
try:
    raw_input
except NameError:
    raw_input = input

for _ in xrange(int(raw_input())):
    h, w = map(int, raw_input().split())
    A = list(map(list, [raw_input() for _ in xrange(h)]))
    coords = list(product(xrange(h), xrange(w)))
    chars = set(chain.from_iterable(A))
    chars.discard('.')
    bounds = {c: list(zip(*[(i, j) for i, j in coords if A[i][j] == c])) for c in chars}
    getbound = lambda v, f, d: (f(v[0]) if v else d, f(v[1]) if v else d)
    box = {c: (
            min(bounds[c][0]) if bounds[c] else 99,
            max(bounds[c][0]) if bounds[c] else -1,
            min(bounds[c][1]) if bounds[c] else 99,
            max(bounds[c][1]) if bounds[c] else -1)
        for c in chars}
    if not chars:
        print("SAFE")
        continue
    # Build graph as adjacency sets and indegree counts using copmlex comprehensions
    suspicious = False
    def check(q):
        xr = lambda c: (box[c][2], box[c][3]+1)
        yr = lambda c: (box[c][0], box[c][1]+1)
        allcoords = ((i, j) for i in range(*yr(q)) for j in range(*xr(q)))
        data = [(A[i][j], i, j) for i, j in allcoords]
        if any(v == '.' for v, *_ in data): return False, None
        return True, set(v for v, *_ in data if v != q)
    rel = dict((c, check(c)) for c in chars)
    if any(not k for k, _ in rel.values()):
        print("SUSPICIOUS")
        continue
    g = dict((k, v) for k, (_, v) in rel.items())
    deg = {c: sum([c in v for v in g.values()]) for c in chars}
    used = set()
    # Exotic reduction for topological-like check
    cnt = [len(chars)]
    def topo(_):
        for e in chars:
            if deg[e] == 0 and e not in used:
                for t in g[e]: deg[t] -= 1
                used.add(e); cnt[0] -= 1
                return False
        return True
    while cnt[0] and not topo(None): pass
    print("SUSPICIOUS" if cnt[0] else "SAFE")