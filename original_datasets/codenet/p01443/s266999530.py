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

class BIT():
    def __init__(self, n, p):
        self.p = p
        i = 1
        while 2**i <= n:
            i += 1
        self.H = i
        self.N = 2**i
        self.A = [0] * self.N

    def find(self, i):
        r = 0
        while i:
            r += self.A[i]
            r %= self.p
            i -= i & (i-1) ^ i
        return r

    def update(self, i, x):
        while i < self.N:
            self.A[i] += x
            self.A[i] %= self.p
            i += i & (i-1) ^ i

    def total(self):
        return self.find(self.N-1)

    def query(self, a, b):
        return self.find(b-1) - self.find(a-1)

def main():
    rr = []

    def f(a,b,p):
        aa = list(range(a,b+1))
        sa = sorted(map(str,aa))
        l = len(aa)
        d = {}
        for s,i in zip(sa, range(l)):
            d[int(s)] = i

        seg = BIT(l+2, p)
        for c in aa:
            t = seg.find(d[c]+1)
            seg.update(d[c]+1, (t+1) % p)

        return seg.total() % p

    while 1:
        n,m,l = LI()
        if n == 0:
            break
        rr.append(f(n,m,l))

    return '\n'.join(map(str, rr))

print(main())