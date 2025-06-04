from sys import stdin
from functools import lru_cache
from operator import mul
from itertools import islice, accumulate

def main():
    MOD = 10 ** 9 + 7
    FACT_MAX = 5 * 10 ** 5 + 10

    # Precompute factorial and inverse factorial using itertools.accumulate for speed
    fact = [1] * FACT_MAX
    for i in range(1, FACT_MAX):
        fact[i] = fact[i-1] * i % MOD

    ifact = [1] * FACT_MAX
    ifact[-1] = pow(fact[-1], MOD-2, MOD)
    for i in range(FACT_MAX-2, -1, -1):
        ifact[i] = ifact[i+1] * (i+1) % MOD

    def comb(n, k):
        if not (0 <= k <= n): return 0
        return fact[n] * ifact[k] % MOD * ifact[n-k] % MOD

    def perm(n, k):
        if not (0 <= k <= n): return 0
        return fact[n] * ifact[n-k] % MOD

    # Fast integer reading
    n, m = map(int, stdin.readline().split())

    res = 0
    for i in range(n+1):
        c = comb(m, i)
        p = perm(n, i)
        rest = perm(m-i, n-i)
        temp = p * c % MOD * rest % MOD * rest % MOD
        if i & 1:
            res = (res - temp) % MOD
        else:
            res = (res + temp) % MOD
    print(res)

if __name__ == "__main__":
    main()