import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random,resource

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
    rr = []

    def f():
        n = I()
        if n == 0:
            return

        m = I()
        xy = [LI_() for _ in range(m)]

        nn = n // 2
        aa = [[0] * n for _ in range(n)]
        wl = [[0] * 2 for _ in range(n)]
        for x, y in xy:
            aa[x][y] = aa[y][x] = 1
            wl[x][0] += 1
            wl[y][1] += 1

        for i in range(n):
            if wl[i][0] > nn or wl[i][1] > nn:
                rr.append(0)
                return True

        kh = []
        for x in range(n):
            for y in range(x+1, n):
                if aa[x][y] == 0:
                    kh.append((x,y))
        ks = len(kh)

        def ff(wl, i):
            if i == ks:
                return 1

            r = 0
            x,y = kh[i]
            if wl[x][0] < nn and wl[y][1] < nn:
                wl[x][0] += 1
                wl[y][1] += 1
                r += ff(wl, i+1)
                wl[x][0] -= 1
                wl[y][1] -= 1

            if wl[x][1] < nn and wl[y][0] < nn:
                wl[x][1] += 1
                wl[y][0] += 1
                r += ff(wl, i+1)
                wl[x][1] -= 1
                wl[y][0] -= 1

            return r

        rr.append(ff(wl, 0))

        return True

    while f():
        pass

    return JA(rr, "\n")

print(main())