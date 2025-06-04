from functools import reduce, lru_cache
from operator import xor, or_
from itertools import product

n = int(input())
for _ in range(n):
    F = {*map(int, input().split())}
    fl, fr = min(F), max(F)
    G = set(range(1,14)).difference(F, {7})
    gl, gr = min(G), max(G)
    
    bounds = ((gl, gr), (fl, fr))
    sets = (G, F)

    @lru_cache(maxsize=None)
    def f(*a):
        s, t, u = a
        T, (l, r) = sets[u], bounds[u]
        e = 0
        seq = [(s-1, lambda x: x<=l and r<=t),
               (t+1, lambda x: s<=l and r<=x)]
        for idx, cond in enumerate(seq):
            pt, ok = idx*2-1 + 7, cond
            if pt in T:
                if ok([s-1,t+1][idx]):
                    e |= True
                else:
                    e |= xor(f(s-1 if idx==0 else s, t if idx==0 else t+1, u^1),1)
        if all(x not in T for x in [s-1, t+1]):
            e |= xor(f(s, t, u^1),1)
        return int(e)
    print(('no', 'yes')[f(7,7,1)])