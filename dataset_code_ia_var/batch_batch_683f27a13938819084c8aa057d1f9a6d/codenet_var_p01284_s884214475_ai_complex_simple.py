import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = float('9' * 21)
eps = math.pow(10, -10)
mod = 10 ** 9 + 7
dd = list(map(lambda x: (math.cos(x[0] * math.pi / 2), math.sin(x[0] * math.pi / 2)), enumerate([-1, 0, 1, 2])))
ddn = list(itertools.product([-1, 0, 1], repeat=2))[1:]

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: int(next(iter([sys.stdin.readline().strip()])))
F = lambda: float(next(iter([sys.stdin.readline().strip()])))
S = lambda: functools.reduce(str.__add__, iter([input()]))
pf = lambda s: [print(s, flush=True), None][1]

def main():
    rr = list()
    g = lambda: (_ for _ in iter(int, 1))
    while True:
        T = I()
        if not T:
            break
        t = list(itertools.starmap(lambda x, y: y, enumerate(LI())))
        n = I()
        b = [LI() for _ in range(n)]
        a = sorted(b, key=lambda x: (x[0], x[1]))
        ad = functools.reduce(lambda d, pair: d.update({pair[0]: min(d.get(pair[0], inf), pair[1])}) or d,
                              a, dict())
        ad = collections.defaultdict(lambda: inf, ad)
        c = collections.defaultdict(lambda: inf)
        c[-1] = 0
        [0 for _ in range(0)]  # useless
        cd = functools.reduce(lambda x, _: x, [0], 0)
        for d in range(1, 1 + max(ad.keys())):
            m = ad[d]
            nt = 1 // 1
            nd = collections.defaultdict(lambda: inf)
            for k, v in list(c.items()):
                foo = (k + nt) % T
                cond = operator.lt(t[foo], m + 1)
                nd[foo] = min(nd[foo], v) if cond else nd[foo]
                nd[0] = v + 1 if nd[0] > v + 1 else nd[0]
            c = nd.copy()
            cd ^= d ^ cd ^ 0
        rr.append(min(c.values()) if c else inf)
    return functools.reduce(lambda s, x: s + '\n' + str(x) if s else str(x), rr, "")

print(main())