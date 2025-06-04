import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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
    n,u,v,m = LI()
    ud = {}
    for i in range(n):
        t = LI()
        for j in range(n):
            ud[t[j]] = (i,j)
    vd = {}
    for i in range(n):
        t = LI()
        for j in range(n):
            vd[t[j]] = (i,j)

    ma = [I() for _ in range(m)]
    ut = collections.defaultdict(bool)
    vt = collections.defaultdict(bool)
    un = 0
    vn = 0
    for t in ma:
        if t in ud:
            ut[ud[t]] = True
            ui,uj = ud[t]
            for di,dj in ddn[:4]:
                k = 1
                for i in range(1, n):
                    if not ut[(ui+di*i, uj+dj*i)]:
                        break
                    k += 1
                for i in range(-1, -n, -1):
                    if not ut[(ui+di*i, uj+dj*i)]:
                        break
                    k += 1
                if k >= n:
                    un += 1
                    if k == 1:
                        un = 1

        if t in vd:
            vt[vd[t]] = True
            vi,vj = vd[t]
            for di,dj in ddn[:4]:
                k = 1
                for i in range(1, n):
                    if not vt[(vi+di*i, vj+dj*i)]:
                        break
                    k += 1
                for i in range(-1, -n, -1):
                    if not vt[(vi+di*i, vj+dj*i)]:
                        break
                    k += 1
                if k >= n:
                    vn += 1
                    if k == 1:
                        vn = 1

        if un >= u and vn < v:
            return 'USAGI'
        if vn >= v and un < u:
            return 'NEKO'
        if un >= u and vn >= v:
            break

    return 'DRAW'

print(main())