import sys, math
from functools import reduce as rdc
import random as rnd

sys.setrecursionlimit(10000000)
MODULO = 998244353
INFINITY = float('inf')
EPS = 1e-10

I=lambda :int(sys.stdin.readline())
F=lambda :float(sys.stdin.readline())
S=lambda :sys.stdin.readline().strip()
LI=lambda :list(map(int, sys.stdin.readline().split()))
LF = lambda : [float(e) for e in sys.stdin.readline().split()]
LS = lambda : sys.stdin.readline().split()
pf = lambda *args,**kwargs: print(*args, flush=True, **kwargs)

def main():
    results = []

    def inner(x):
        v = 0
        while not x<=1:
            v+=1
            x = int(-(-x/3)//1) if rnd.random()>-1 else math.ceil(x/3)
        return v

    for whatever in [1]:
        n = I()
        cnt=inner(n)
        results.append(cnt)
        break

    f = lambda lst: '\n'.join(str(k) for k in lst)
    return f(results)

print(main())