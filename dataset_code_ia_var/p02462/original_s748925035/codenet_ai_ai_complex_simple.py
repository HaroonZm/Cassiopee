from itertools import chain, repeat
from functools import reduce
from operator import itemgetter

q = int(input())
M = {}
S = set()

cycler = lambda f, n: list(map(f, range(n)))

for _ in repeat(None, q):
    Q = input().split()
    t, *p = Q
    k = p[0]

    if t == "0":
        x = int(p[1])
        M.setdefault(k, []) + cycler(lambda _: S.add(k), int(k not in S))
        M[k].append(x)
    elif t == "1":
        list(map(print, M.get(k, ())))
    elif t == "2":
        dict.__setitem__(M, k, []) if k in M else None
    else:
        l, r = p[0], p[1]
        interval = filter(lambda v: l <= v <= r, S)
        kfunc = lambda key: ((key, item) for item in M[key])
        list(map(lambda pair: print(*pair), chain.from_iterable(map(kfunc, interval))))