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

def main():
    rr = []

    dd = [(0,-1),(1,0),(0,1),(-1,0)]

    while True:
        n = I()
        if n == 0:
            break
        a = [(0,0)]
        for _ in range(n-1):
            i,di = LI()
            ai = a[i]
            d = dd[di]
            a.append((ai[0]+d[0], ai[1]+d[1]))
        y = sorted(list(map(lambda x: x[0], a)))
        x = sorted(list(map(lambda x: x[1], a)))
        rr.append('{} {}'.format(x[-1]-x[0]+1, y[-1]-y[0]+1))

    return '\n'.join(map(str, rr))

print(main())