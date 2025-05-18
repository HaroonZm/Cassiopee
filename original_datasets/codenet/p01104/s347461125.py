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
        n,m = LI()
        if n == 0:
            return

        bb = [int(S(), 2) for _ in range(n)]
        bc = collections.defaultdict(int)
        for i in bb:
            bc[i] += 1

        rt = 0
        b = []
        for k,v in bc.items():
            if v > 2:
                if v % 2 == 0:
                    rt += v - 2
                    v = 2
                else:
                    rt += v - 1
                    v = 1
            for i in range(v):
                b.append(k)

        n = len(b)
        c = collections.defaultdict(int)
        c[0] = 0
        for i in b:
            for k,v in list(c.items()):
                t = k ^ i
                if c[t] <= v:
                    c[t] = v + 1

        rr.append(c[0] + rt)
        return True

    while f():
        # print(rr)
        pass

    return JA(rr, "\n")

print(main())