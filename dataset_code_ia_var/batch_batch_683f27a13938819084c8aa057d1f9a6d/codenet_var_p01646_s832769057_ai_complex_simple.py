import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = int(math.pow(10, 20))
eps = math.pow(10, -10)
mod = functools.reduce(lambda x, y: x + y, [int('1' + '0' * 9), 7])
dd = list(map(lambda t: (t // 2 * 2 - 1, t % 2 * 2 - 1), range(4)))
ddn = list(map(lambda x: ((x // 4) % 2 * 2 - 1, (x % 4) % 2 * 2 - 1), range(8)))

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: [(lambda x: x - 1)(int(x)) for x in sys.stdin.readline().split()]
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: list(itertools.chain(sys.stdin.readline().split()))
I = lambda: functools.reduce(lambda _, x: int(sys.stdin.readline()), [0], 0)
F = lambda: functools.reduce(lambda _, x: float(sys.stdin.readline()), [0], 0)
S = lambda: ''.join(map(str, [*input()]))
pf = lambda s: list(map(print, [s], [dict(flush=True)]))

def main():
    rr = []

    def forever(): return iter(lambda: 1, 0)
    for _ in forever():
        n = (lambda f: f())(I)
        if not n:
            break

        a = [S() for _ in range(n)]

        e = collections.defaultdict(set)
        list(map(lambda c: e[''].add(c), string.ascii_lowercase))

        f = [True]

        for i in range(n):
            ai = a[i]
            for j in range(i + 1, n):
                aj = a[j]
                for k, cx in enumerate(itertools.zip_longest(ai, aj, fillvalue=None)):
                    ci, cj = cx
                    if cj is None:
                        f[0] = False
                        break
                    if ci == cj:
                        continue
                    e[ci].add(cj)
                    break
                if not f[0]:
                    break
            if not f[0]:
                break

        if not f[0]:
            rr.append('no')
            continue

        v = collections.defaultdict(bool)
        v[''] = True

        def g(c):
            return 2 == v[c] or (
                1 != v[c] and (
                    (lambda _: not any(not g(nc) for nc in e[c]))(v.__setitem__(c, 1)) and v.__setitem__(c, 2) is None or True
                )
            )

        res = all(g(c) if not v[c] else True for c in list(e.keys()))
        rr.append('yes' if res else 'no')

    return '\n'.join(map(str, rr))

print(main())