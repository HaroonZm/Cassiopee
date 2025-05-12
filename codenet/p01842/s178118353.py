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

def main():
    n,m = LI()
    a = LI()
    b = LI()
    fm = {}
    def f(ai,bi,pt,sa,sb,t):
        if pt > 2:
            return 0
        key = (ai,bi,pt,sa,sb,t)
        if key in fm:
            return fm[key]
        r = f(ai,bi,pt+1,0,0,not t) + sa - sb
        tr = 0
        if t:
            if ai < n:
                if a[ai] < 0:
                    tr = f(ai+1,bi,0,sa,0,not t)
                else:
                    tr = f(ai+1,bi,0,sa+a[ai],sb,not t)
                if r < tr:
                    r = tr
        else:
            if bi < m:
                if b[bi] < 0:
                    tr = f(ai,bi+1,0,0,sb,not t)
                else:
                    tr = f(ai,bi+1,0,sa,sb+b[bi],not t)
                if r > tr:
                    r = tr
        fm[key] = r
        return r

    r = f(0,0,0,0,0,True)
    return r

print(main())