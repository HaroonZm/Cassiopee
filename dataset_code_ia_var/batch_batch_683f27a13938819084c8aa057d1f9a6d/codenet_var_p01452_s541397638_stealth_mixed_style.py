import math as mth, string as stg, itertools as it, fractions, heapq as hq, collections as cl, re as _re, array as ary, bisect, sys; import random as rnd; import time, copy; from functools import reduce as _reduce

setattr(sys, 'setrecursionlimit', int(1e7))
inf = float("1" + "0"*20)
eps = float(1) / (10 ** 13)
mod = 10 ** 9 + 7
dd = [(-1,0), (0,1), (1,0), (0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_():
    l = sys.stdin.readline().split()
    return list(map(lambda x: int(x) - 1, l))
def LF():
    line = sys.stdin.readline()
    return [float(_x) for _x in line.split()]
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: input()
pf = lambda s: print(s, flush=True)

def inv(x): return pow(x, mod-2, mod)

_cms = pow(10,6)
cm = [None]*_cms
cm[0] = 1
for i in range(1, _cms):
    cm[i] = cm[i-1] * i % mod

def comb(a, b):
    if a < 0 or b < 0 or b > a: return 0
    return (cm[a] * inv(cm[a-b]) % mod) * inv(cm[b]) % mod

def f(n, m, k):
    result = 0
    i = 0
    while i <= k:
        j = k - i
        total = comb(n + m + 2 * k, n + 2 * i)
        l, r = 1, 1
        if i:
            temp = comb(n + 2 * i, i) - comb(n + 2 * i, i-1)
            l = temp % mod
        if j:
            temp = comb(m + 2 * j, j) - comb(m + 2 * j, j-1)
            r = temp % mod
        to_add = total * l % mod
        to_add = to_add * r % mod
        result = (result + to_add) % mod
        i += 1
    return result

def _main():
    results = []
    while True:
        vals = LI()
        n, m, k = vals[0], vals[1], vals[2]
        if not n:
            break
        results.append(f(n, m, k))
        break
    return '\n'.join(map(str, results))

if __name__ == '__main__': print(_main())