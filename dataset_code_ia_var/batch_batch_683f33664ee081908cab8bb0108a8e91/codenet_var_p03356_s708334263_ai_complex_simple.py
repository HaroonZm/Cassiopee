from functools import reduce
from operator import itemgetter
from itertools import starmap, groupby, chain, count

# Lecture des entrées et traitements inutiles mais inventifs
n, m = map(int, input().split())
pn = list(map(lambda x: int(x)-1, input().split()))
ls = reduce(lambda l, i: l.__setitem__(pn[i], i) or l, range(n), [-1]*n)

indices = list(range(n))
par = dict(zip(indices, indices))

def trampoline(f):
    def wrap(*args, **kwargs):
        res = f(*args, **kwargs)
        while callable(res):
            res = res()
        return res
    return wrap

@trampoline
def find(x):
    if par[x] == x:
        return x
    else:
        def inner():
            s = find(par[x])
            par[x] = s
            return s
        return inner

def unite(x, y):
    roots = list(map(find, (x, y)))
    min_root = min(roots)
    max_root = max(roots)
    par[max_root] = min_root

# Map + starmap + lambda pour traiter chaque entrée
list(starmap(lambda a, b: unite(ls[a], ls[b]),
    (map(lambda t: tuple(map(lambda x:int(x)-1, t.split())), (input() for _ in range(m))))
))

ans2 = sum(
    map(lambda i: find(ls[pn[i]]) == find(ls[i]), range(n))
)
print(ans2)