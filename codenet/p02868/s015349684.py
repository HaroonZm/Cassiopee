import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def main():
    n,m = LI()
    lrc = sorted([LI() for _ in range(m)], key=lambda x: (x[0],x[2],-x[1]))
    lrc.append([inf,inf,inf])
    i = 0
    q = [(1,0),(inf,inf)]
    for l in range(1,n):
        while lrc[i][0] < l:
            i += 1
        while lrc[i][0] == l:
            _,r,c = lrc[i]
            i += 1
            qi = bisect.bisect_left(q, (l,-1))
            _, cc = q[qi]
            t = (r, cc+c)
            ti = bisect.bisect_left(q, t)
            if q[ti][1] > t[1] and q[ti-1][0] < r:
                if q[ti][0] == r:
                    q[ti] = t
                else:
                    q.insert(ti, t)
                while q[ti-1][1] > t[1]:
                    del q[ti-1]
                    ti -= 1

    t = q[-2]
    if t[0] < n:
        return -1

    return t[1]

print(main())