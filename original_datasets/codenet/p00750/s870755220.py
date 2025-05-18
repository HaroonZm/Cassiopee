import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class Seg():
    def __init__(self, na, default, func):
        if isinstance(na, list):
            n = len(na)
        else:
            n = na
        i = 1
        while 2**i <= n:
            i += 1
        self.D = default
        self.H = i
        self.N = 2**i
        if isinstance(na, list):
            self.A = [default] * (self.N) + na + [default] * (self.N-n)
            for i in range(self.N-1,0,-1):
                self.A[i] = func(self.A[i*2], self.A[i*2+1])
        else:
            self.A = [default] * (self.N*2)
        self.F = func

    def find(self, i):
        return self.A[i + self.N]

    def update(self, i, x):
        i += self.N
        self.A[i] = x
        while i > 1:
            i = i // 2
            self.A[i] = self.merge(self.A[i*2], self.A[i*2+1])

    def merge(self, a, b):
        return self.F(a, b)

    def total(self):
        return self.A[1]

    def query(self, a, b):
        A = self.A
        l = a + self.N
        r = b + self.N
        res = self.D
        while l < r:
            if l % 2 == 1:
                res = self.merge(res, A[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.merge(res, A[r])
            l >>= 1
            r >>= 1

        return res

def main():
    rr = []

    def f(n,m,s,g):
        def _f(a):
            x,y,lab = a
            return [int(x),int(y),lab]
        a = [_f(LS()) for _ in range(m)]
        e = collections.defaultdict(list)
        for x,y,lab in a:
            e[y].append((x,1))

        def search(s):
            d = collections.defaultdict(lambda: inf)
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                for uv, ud in e[u]:
                    if v[uv]:
                        continue
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
        for x,y,lab in a:
            if d[x] == inf or d[y] == inf:
                continue
            e[x].append((y,lab))
            ee[x][y] = lab
        ml = 0
        for k,v in e.items():
            vl = max(map(lambda x: len(x[1]), v))
            ml += vl
        ml = ml * 2 + 2
        # print('a',a)
        # print('e',e)

        def search2(s, g):
            d = collections.defaultdict(lambda: None)
            d[(s,0)] = ''
            q = []
            heapq.heappush(q, ('', (s,0)))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                for uv, ud in e[u[0]]:
                    vd = k + ud
                    vl = len(vd)
                    if vl >= ml:
                        continue
                    uv = (uv,vl)
                    if v[uv]:
                        continue
                    if d[uv] is None or d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            # print('d',d)
            return min([d[(g, _)] for _ in range(ml) if not d[(g, _)] is None])

        dg = search2(s, g)
        # print(infs,dg)
        if len(dg) >= ml // 2:
            return 'NO'
        return dg

    while 1:
        n,m,s,g = LI()
        if n == 0:
            break
        rr.append(f(n,m,s,g))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))

print(main())