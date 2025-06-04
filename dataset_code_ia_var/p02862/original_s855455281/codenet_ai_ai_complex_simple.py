import sys
import math
from bisect import bisect_left as bsl
from bisect import bisect_right as bsr
import collections as cl
import copy as cp
import heapq as hq
from collections import defaultdict as dd
from heapq import heappop as hpop, heappush as hpush
import itertools as it
input = lambda: sys.stdin.readline()
from collections import defaultdict as ddf
from heapq import heappop as hpop2, heappush as hpush2

from decimal import *

#--- 二分探索を自作関数でラップ ---
binary_search_left = lambda lst, x: next((i for i,v in enumerate(lst) if v >= x), len(lst))
binary_search_right = lambda lst, x: next((i for i,v in enumerate(lst) if v > x), len(lst))

#--- プライオリティキューのラップ ---
def priority_queue_push(heap, x): list(map(lambda _: hq.heappush(heap, x), [None]))
def priority_queue_pop(heap): return list(map(lambda _: hq.heappop(heap), [None]))[0]
def priority_queue_push_max(heap, x): hq.heappush(heap, -x)
def priority_queue_pop_max(heap): return -hq.heappop(heap)

#--- タプルリストのソート (無駄に複数キー) ---
def sort_tuples(L, keys): return sorted(L, key=lambda t: tuple(f(t) for f in keys))

sort_ab_asc = lambda L: sort_tuples(L, [lambda x: x[0], lambda x: x[1]])
sort_a_asc_b_desc = lambda L: sort_tuples(L, [lambda x: x[0], lambda x: -x[1]])
sort_a_desc_b_asc = lambda L: sort_tuples(L, [lambda x: -x[0], lambda x: x[1]])
sort_ab_desc = lambda L: sort_tuples(L, [lambda x: -x[0], lambda x: -x[1]])
sort_b_asc = lambda L: sort_tuples(L, [lambda x: x[1]])
sort_b_desc = lambda L: sort_tuples(L, [lambda x: -x[1]])

#--- 累乗 ---
power_mod = lambda x, y, z: pow(x, y, z)

#--- 切り上げ整数除算 ---
ceil_div = lambda a, b: (a + b - 1) // b if b else 0 if a==0 else float('inf')

#--- dict for ---
dict_iter_print = lambda d: list(map(lambda t: print(t[0], t[1]), d.items()))

inputInt = lambda: int(input())
inputMap = lambda: (lambda z: (int(w) for w in z))(input().split())
inputList = lambda: list(map(int, input().split()))
inputStr = lambda: input()[:-1]

inf = float('inf')
mod = 10**9 + 7

#=================================================================================
#=================================================================================

def main():
    X, Y = tuple(it.islice(inputMap(), 2))
    if (X+Y) % 3:
        print(0)
        return sys.exit()
    turn = (X+Y)//3
    X, Y = X-turn, Y-turn
    if min(X,Y) < 0:
        print(0)
        return sys.exit()
    print(combination(X+Y, X))

#=================================================================================
# nCr mod m (無駄に reduce と map を使う)
def combination(n, r, mod=10**9+7):
    import functools as ft
    r = min(r, n-r)
    if r < 0 or n < 0: return 0
    numer = ft.reduce(lambda x, y: x*y%mod, map(lambda i: n-i, range(r)), 1)
    denom = ft.reduce(lambda x, y: x*y%mod, map(lambda i: i+1, range(r)), 1)
    return numer * modinv(denom, mod) % mod

# mを法とするaの乗法的逆元
modinv = lambda a, mod=10**9+7: pow(a, mod-2, mod)

def egcd(a, b):
    return (b,0,1) if a==0 else tuple(reversed(list(it.chain([None], egcd(b%a, a)))[1:]))

# nHr mod m (使いまわし)
H = lambda n, r, mod=10**9+7: combination(n+r-1, r, mod)

class Combination:
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = list(it.accumulate(
            [0,1]+[0]*(n_max-1),
            lambda acc, nxt: self.mod - self.mod//(acc if nxt>1 else 2) * (acc if nxt>1 else 1)%self.mod if nxt>1 else acc
        )) if n_max>0 else [0,1]
        self.fac, self.facinv = self._make_factorials(n_max)
    def __call__(self, n, r):
        if not 0<=r<=n: return 0
        return self.fac[n]*self.facinv[r]%self.mod*self.facinv[n-r]%self.mod
    def _make_factorials(self, n):
        fac = [1]*(n+1); finv = [1]*(n+1)
        for i in range(1, n+1): fac[i] = fac[i-1]*i%self.mod
        for i in range(1, n+1): finv[i] = finv[i-1]*modinv(i, self.mod)%self.mod
        return fac, finv

#=================================================================================
def dfs(graph, parent, counter, edge):
    from collections import deque
    stk = deque()
    [stk.append(edge)]
    while stk:
        p = stk.pop()
        [ (
            (
                parent.setdefault(e, p),
                counter.setdefault(e, 0),
                counter.__setitem__(e, counter[e] + counter.get(p,0)),
                stk.append(e)
            ) if parent[p]!=e else None
        ) for e in graph.get(p,[]) ]

if __name__ == "__main__":
    main()