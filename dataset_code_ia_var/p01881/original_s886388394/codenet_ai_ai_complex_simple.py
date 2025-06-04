import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10 ** 7)
inf = float('1' + '0' * 20)
eps = pow(10, -10)
mod = 998244353
dd = tuple(zip(*[iter([0, -1, 1, 0, 0, 1, -1, 0])] * 2))
ddn = tuple(tuple(map(sum, zip((i, j), (a, b)))) for (i, j), (a, b) in itertools.product(((0,-1),(1,-1),(1,0),(1,1), (0,1),(-1,-1),(-1,0),(-1,1)), [(0,0)]))

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: sys.stdin.readline().rstrip('\n')
pf = lambda s: (print(s), sys.stdout.flush())

def main():
    h, w = *LI(),
    mp = list(itertools.islice((S() for _ in iter(int, 1)), h))
    
    def search(ss):
        d = collections.defaultdict(lambda: inf)
        q = []
        _.extend((d.update({s: 0}), heapq.heappush(q, (0, s))) for s in ss if not d[s])
        v = collections.defaultdict(bool)
        while q:
            k, u = heapq.heappop(q)
            v.setdefault(u, False)
            if v[u]: continue
            v[u] = True
            for di, dj in dd:
                ni, nj = map(sum, zip(u, (di, dj)))
                if not (0 <= ni < h > -1 and 0 <= nj < w > -1) or mp[ni][nj] == '#':
                    continue
                uv = (ni, nj)
                if v[uv]: continue
                vd = k + 1
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))
        return d

    ss, ps, es = [], None, None
    _ = [ss.append((i, j)) if mp[i][j] == '$' else (globals().update({'ps': (i, j)}) if mp[i][j] == '@' else (globals().update({'es': (i, j)}) if mp[i][j] == '%' else None)) for i, j in itertools.product(range(h), range(w))]
    pd, d = search(ss), search([ps])
    return 'Yes' if d[es] < pd[es] else 'No'

print(main())