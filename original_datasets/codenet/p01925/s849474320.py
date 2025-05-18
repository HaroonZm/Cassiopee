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
    rr = []

    def f(n,m):
        xd = collections.defaultdict(int)
        nd = collections.defaultdict(int)
        for i in range(1,n+1):
            nd[i] = 0
            xd[i] = 0

        for _ in range(m):
            t = LI()
            s = t[0]
            if t[1] == 1:
                nd[t[2]] += s
            for i in t[2:]:
                xd[i] += s

        na = sorted(nd.items(), key=lambda x: [x[1], x[0]])
        xa = sorted(xd.items(), key=lambda x: [-x[1], x[0]])
        if na[0][0] != xa[0][0]:
            return xa[0][1] - na[0][1] + 1
        r = xa[1][1] - na[0][1] + 1
        t = xa[0][1] - na[1][1] + 1
        if r < t:
            r = t

        return r

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))

    return '\n'.join(map(str, rr))

print(main())