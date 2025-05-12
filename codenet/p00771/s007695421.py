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

eps = 1e-7
def bs(f, mi, ma):
    mm = -1
    while ma > mi + eps:
        m1 = (mi*2+ma) / 3.0
        m2 = (mi+ma*2) / 3.0
        r1 = f(m1)
        r2 = f(m2)
        if r1 < r2:
            mi = m1
        else:
            ma = m2
    return f((ma+mi)/2.0)

def main():
    rr = []

    def f(n):
        a = [LI() for _ in range(n)]
        def _f(x,y):
            r = inf
            for px,py,l in a:
                r = min(r, l**2 - (x-px)**2 - (y-py)**2)
            return r
        def _fy(y):
            def _ff(x):
                return _f(x,y)
            return bs(_ff, -100, 100)
        r = bs(_fy,-100,100)

        return "{:0.7f}".format(r**0.5)

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))

print(main())