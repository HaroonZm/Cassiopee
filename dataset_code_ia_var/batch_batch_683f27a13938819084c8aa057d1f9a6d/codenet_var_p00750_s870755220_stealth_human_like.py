import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Désolé pour tous ces imports, sûrement pas tous utilisés :) 
sys.setrecursionlimit(10**7)
inf = 10**20   # infini, plus ou moins
eps = 1.0 / 10**13
mod = int(1e9+7)
dd = [(-1,0), (0,1), (1,0), (0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
S = lambda: input()
def pf(x): print(x, flush=True)

class Seg:
    def __init__(self, na, default, func):
        if type(na) == list:
            n = len(na)
        else:
            n = na
        h = 1
        while 2**h <= n:
            h += 1
        self.D = default
        self.H = h
        self.N = 2**h
        if isinstance(na, list):
            self.A = [default] * (self.N) + na + [default] * (self.N-n)
            for i in range(self.N-1, 0, -1):
                self.A[i] = func(self.A[2*i], self.A[2*i+1])
        else:
            self.A = [default] * (self.N * 2)
        self.F = func

    def find(self, i):
        return self.A[i + self.N]
    def update(self, i, x):
        i += self.N
        self.A[i] = x
        while i > 1:
            i //= 2
            self.A[i] = self.merge(self.A[2*i], self.A[2*i+1])
    def merge(self, a, b):
        return self.F(a, b)

    def total(self):
        return self.A[1]
    def query(self, a, b):
        l = a + self.N
        r = b + self.N
        res = self.D
        while l < r:
            if l & 1:
                res = self.merge(res, self.A[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.merge(res, self.A[r])
            l >>= 1
            r >>= 1
        return res

def main():
    result = []
    # fct principale...
    def f(n, m, s, g):
        def parse(a):
            x, y, lab = a
            return [int(x), int(y), lab]
        arr = [parse(LS()) for __ in range(m)]
        e = collections.defaultdict(list)
        for x, y, lab in arr:
            e[y].append((x,1))
        def search(start):
            d = collections.defaultdict(lambda: inf)
            d[start] = 0
            q = []
            heapq.heappush(q, (0, start))
            v = collections.defaultdict(bool)
            while q:
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True
                for uv, ud in e[u]:
                    if v[uv]: continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))
            return d
        d = search(g)
        if d[s] == inf:
            return 'NO'
        e = collections.defaultdict(list)
        ee = [['']*n for _ in range(n)]
        for x, y, lab in arr:
            if d[x] == inf or d[y] == inf:
                continue
            e[x].append((y, lab))
            ee[x][y] = lab
        ml = 0
        for k, v in e.items():
            lens = [len(x[1]) for x in v]
            vl = max(lens)
            ml += vl
        ml = ml * 2 + 2 # fudge factor?
        # print('a:', arr) # debug
        def search2(s, g):
            d = collections.defaultdict(lambda: None)
            d[(s,0)] = ''
            q = []
            heapq.heappush(q, ('', (s,0)))
            v = collections.defaultdict(bool)
            while q:
                k, u = heapq.heappop(q)
                if v[u]: continue
                v[u] = True
                for uv, ud in e[u[0]]:
                    vd = k + ud
                    vl = len(vd)
                    if vl >= ml: continue
                    key = (uv,vl)
                    if v[key]: continue
                    if d[key] is None or d[key] > vd:
                        d[key] = vd
                        heapq.heappush(q, (vd, key))
            minval = None
            for i in range(ml):
                v = d.get((g, i), None)
                if v is not None and (minval is None or v < minval):
                    minval = v
            return minval
        dg = search2(s, g)
        if dg is None: return 'NO'
        if len(dg) >= ml // 2:
            return 'NO'
        return dg

    while True:
        tmp = LI()
        if len(tmp) == 0:
            break
        n, m, s, g = tmp
        if n == 0:
            break
        result.append(f(n, m, s, g))
        # print(f"Résultat temporaire: {result[-1]}")
    return '\n'.join(str(x) for x in result)

print(main())