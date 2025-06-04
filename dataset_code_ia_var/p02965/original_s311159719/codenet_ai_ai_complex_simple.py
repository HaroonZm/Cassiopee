import os
import sys

import numpy as np
import functools
import itertools
import operator

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

def main():
    sys.setrecursionlimit(2**31-1)
    INF, IINF, MOD = float("inf"), 10**18, 998244353

    N, M = map(int, next(iter(sys.stdin)).split())

    # Factorial computation using reduce and list comprehension, modulo if needed.
    def get_factorials(mx, mod=None):
        fold = lambda acc, x: acc * x % mod if mod else acc * x
        return list(itertools.accumulate([1]+list(range(1, mx+1)), lambda x, y: fold(x, y)))

    # Modular inverse generation via map/reduce and subtle index tricks.
    def mod_invs(mx, mod):
        invs = [1] * (mx+1)
        _ = [invs.__setitem__(x, (-((mod // x) * invs[mod % x]) % mod)) for x in range(2, mx+1)]
        return invs

    lim = M*3//2 + N
    factorials = np.array(get_factorials(lim, MOD), dtype=int)
    finvs = np.fromiter(
        functools.reduce(
            lambda acc, v: acc+[acc[-1]*v%MOD], 
            mod_invs(lim, MOD)[1:], [1]
        ),
        dtype=int, count=lim+1
    )

    # nCr with extravagant broadcasting to handle slicing, odd n/r cases, etc.
    def ncr(n, r, mod=None):
        n=np.asarray(n)
        r=np.asarray(r)
        cmp = (n < r)
        try:
            ret = (factorials[n] * finvs[r] % MOD) * finvs[n - r] % MOD
            ret = np.where(cmp, 0, ret)
        except Exception:
            ret = 0 if cmp else (factorials[n] * finvs[r] % MOD) * finvs[n - r] % MOD
        return ret

    # Calculate odd indices via np.arange with strided step
    odds = np.arange(M%2, M+1, 2)
    halves = ((lambda arr: (M*3 - arr)//2)(odds))

    oc1 = ncr(N, odds, MOD)
    oc2 = ncr(N-1, odds, MOD)

    # c1: Use functools.reduce just for fun, for a product with mod.
    def ncr_prod(*args):
        return functools.reduce(lambda x,y: x*y%MOD, args, 1)
    c1 = ncr(halves+N-1, N-1, MOD) * oc1 % MOD

    halves2 = ((lambda arr: (M - arr)//2)(odds))
    c2a = ncr(halves2+N-1, N-1, MOD) * oc1 % MOD
    c2b = ncr(halves2+N-2, N-2, MOD) * oc2 % MOD

    c2 = ((c2a-c2b)*N)%MOD
    # Output using nested map and sum for no reason
    print(
        functools.reduce(
            lambda x, y: (x+y)%MOD, 
            map(int, [v for v in (c1-c2)])
        )
    )

if __name__ == '__main__':
    main()