import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**3
eps = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    n, p, q = LI()
    c = [I() for _ in range(n)]
    s = sum(c)
    a = sorted([[c[i]+p*i, i] for i in range(n)])
    r = s
    for i in range(n):
        s -= c[a[i][1]] + p * a[i][1]
        t = s + p*i*(i+1) + p*q*(i+1)
        if t > r:
            r = t
    return r

print(main())