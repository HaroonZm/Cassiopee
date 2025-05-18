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
        e = [[0]*n for _ in range(n)]
        cs = []
        for _ in range(m):
            a,b,c = LI_()
            c += 1
            e[a][b] = c
            e[b][a] = c
            cs.append([a,b])

        r = 0
        while cs:
            ns = []
            for a in cs:
                t = 0
                for i in a:
                    m = inf
                    for j in a:
                        if i == j:
                            continue
                        if m > e[i][j]:
                            m = e[i][j]
                    t += m
                if r < t:
                    r = t
                for i in range(a[-1]+1,n):
                    f = True
                    for j in a:
                        if e[i][j] < 1:
                            f = False
                            break
                    if f:
                        ns.append(a + [i])
            cs = ns

        return r

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        # print('rr', rr[-1])
        break

    return '\n'.join(map(str,rr))

print(main())