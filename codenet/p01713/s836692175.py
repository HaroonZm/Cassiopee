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
    w = I()
    a = LI()
    b = [0] * w
    c = [0] * w
    ti = 0
    for i in range(w):
        k = a[i]
        if k == 0:
            ti = -inf
        elif k < 0:
            if ti < k:
                ti = k
            elif ti < 0:
                ti += 1
        elif ti < 0:
            ti += 1
        b[i] = ti

    ti = 0
    for i in range(w-1,-1,-1):
        k = a[i]
        if k == 0:
            ti = -inf
        elif k < 0:
            if ti < k:
                ti = k
            elif ti < 0:
                ti += 1
        elif ti < 0:
            ti += 1
        c[i] = ti

    r = 0
    for i in range(w):
        if a[i] <= 0:
            continue
        r += min(abs(min(b[i], c[i])), a[i])

    return r

print(main())