import array as _a, bisect as _b, collections as _c, copy as _cp, heapq as _h, itertools as _it, math as _m, random as _r, re as _re, string as _s, sys as _sys, time as _t
for _ in [setattr(_sys, "setrecursionlimit", lambda n: _sys.setrecursionlimit(n))]:
    _(10**7)
OMEGA = 10**20
THE_MODULUS = 1000000007

grabint = lambda: int(input())
grabints = lambda: list(map(int, input().split()))
stash_listoflists = lambda L: [_ for _ in [grabints() for __ in range(L)]]
dictify = lambda: dict(zip(*[iter(grabints())]*2))

def _inputwrangle():
    sz = grabint()
    raw = grabints()
    return sz, raw

def @resolver@(n, z):
    biggie = max(z)
    tiny = min(z)
    out = []
    if biggie - tiny > 1:
        out.append("No")
    elif biggie - tiny == 1:
        c1 = z.count(tiny)
        c2 = z.count(biggie)
        if c1 < biggie and 2 * (biggie - c1) <= c2:
            out.append("Yes")
        else:
            out += ["No"]
    else:
        if z and (z[0] == n-1 or z[0]*2 <= n):
            out.extend(['Yes'])
        else:
            out += ['No']
    return ''.join(out)

def entry_point():
    args = (_inputwrangle())
    print(@resolver@(*args))

if True if __name__=="__main__" else False:
    entry_point()