import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
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

def bs(f, mi, ma):
    mm = -1
    while ma > mi + eps:
        mm = (ma+mi) / 2.0
        if f(mm):
            mi = mm + eps
        else:
            ma = mm
    if f(mm):
        return mm + eps
    return mm

def main():
    xy = sorted([LI() for _ in range(3)])
    x = list(map(lambda _: _[0] - xy[0][0], xy))
    y = list(map(lambda _: _[1] - xy[0][1], xy))
    a = []
    for i in range(3):
        a.append(((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2) ** 0.5)
    ma = max(a)
    s = abs(x[1]*y[2] - x[2]*y[1]) / 2
    r = 2 * s / sum(a)

    def f(i):
        return (1-i/r) * ma - 2*i > 0

    return bs(f, 0, ma)

print(main())