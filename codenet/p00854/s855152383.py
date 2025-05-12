import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

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

    while True:
        n,k,m = LI()
        if n == 0:
            break
        a = list(range(1,n+1))
        t = m - 1
        for i in range(n-1):
            a = a[:t] + a[t+1:]
            t = (t - 1 + k) % len(a)
        rr.append(a[0])

    return '\n'.join(map(str, rr))

print(main())