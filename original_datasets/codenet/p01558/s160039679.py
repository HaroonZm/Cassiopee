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

class ModInt():
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n+x) % mod)

    def __sub__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n-x) % mod)

    def __mul__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n*x) % mod)

    def __truediv__(self, x):
        x = ModInt.xn(x)
        return ModInt(self.n * pow(x, mod-2, mod) % mod)

    @classmethod
    def xn(cls, x):
        if isinstance(x, ModInt):
            return x.n
        return x

    def __str__(self):
        return str(self.n)

def M(n): return ModInt(n)

class RollingHash():
    def __init__(self, s):
        self.N = n = len(s)
        a = [ord(c) for c in s]
        self.A1 = a1 = [M(a[0])]
        self.A2 = a2 = [M(a[0])]
        for c in a[1:]:
            a1.append(a1[-1] * 997 + c)
            a2.append(a2[-1] * 991 + c)

    def get(self, l, r):
        if l == 0:
            return (self.A1[r].n, self.A2[r].n)
        t1 = (self.A1[r] - self.A1[l-1] * pow(997, r-l+1, mod)).n
        t2 = (self.A2[r] - self.A2[l-1] * pow(991, r-l+1, mod)).n
        return (t1, t2)

def main():
    rr = []

    def f(n,m):
        rs = set()
        s = S()
        qa = [S() for _ in range(m)]
        l = 0
        r = 0
        rh = RollingHash(s)
        for q in qa:
            if q == 'L++':
                l += 1
            elif q == 'L--':
                l -= 1
            elif q == 'R++':
                r += 1
            else:
                r -= 1
            rs.add((l,r))

        rrs = set()
        for l, r in rs:
            rrs.add(rh.get(l,r))
        return len(rrs)

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        # print('rr', rr[-1])
        break

    return '\n'.join(map(str,rr))

print(main())