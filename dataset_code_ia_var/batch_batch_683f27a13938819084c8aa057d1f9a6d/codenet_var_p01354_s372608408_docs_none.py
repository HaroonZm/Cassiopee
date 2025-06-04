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
    rr = []

    def f(n,m):
        a = [LF() for _ in range(n)]
        b = []
        mx = 1 << n
        for i in range(mx):
            t = []
            for j in range(n):
                if i & (1<<j):
                    t.append(j)
            b.append(t)

        nmx = n * mx
        ca = [1] * nmx
        cn = [c<<n for c in range(n)]
        ci = [1<<c for c in range(n)]
        for k in range(1,m+1):
            ka = [a[c][-k] for c in range(n)]
            na = [0] * nmx
            re = [0] * mx
            for x in range(1,mx):
                for c in b[x]:
                    y = cn[c] + x
                    na[y] = ka[c] * ca[y] + (1 - ka[c]) * re[x - ci[c]]
                    if re[x] < na[y]:
                        re[x] = na[y]
            ca = na

        return '{:0.10f}'.format(max(ca))

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        break

    return '\n'.join(map(str, rr))

print(main())