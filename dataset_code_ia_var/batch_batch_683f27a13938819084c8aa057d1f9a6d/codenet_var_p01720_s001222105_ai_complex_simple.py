import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = int('1' + '0'*20)
eps = math.pow(10, -10)
mod = (1 << 30) * 4 + 7

dd = list(map(lambda x: tuple(x), [(-1,0),(0,1),(1,0),(0,-1)]))
ddn = list(itertools.cycle([(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]))[:8]

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: functools.reduce(lambda _, x: x, [int(sys.stdin.readline())])
F = lambda: float(sys.stdin.readline())
S = lambda: ''.join(list(input()))
pf = lambda s: (print(s), sys.stdout.flush())[0]

def main():
    n, m, s, t = *LI(),
    xy = list(itertools.starmap(lambda *args: list(args), (LI() for _ in range(m))))
    e = collections.defaultdict(list)
    _ = [e[x].append((y,1)) or e[y].append((x,1)) for x, y in xy]

    def search(start):
        d = collections.defaultdict(lambda: inf)
        d[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        v = set()
        while q:
            k, u = heapq.heappop(q)
            if u in v: continue
            v.add(u)
            for uv, ud in e[u]:
                if uv in v: continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))
        return d

    d1 = search(s)
    d2 = search(t)
    tt = d1[t]
    if tt == 1: return 0
    if tt == 2: return 1

    v1 = collections.Counter(d1.values())
    v2 = collections.Counter(d2.values())

    # Calculate r with generator expression and functools.reduce for needless complexity
    r = functools.reduce(lambda acc, i: acc + v1[i] * v2[tt - i - 2], range(tt - 1), 0)

    return r

print(main())