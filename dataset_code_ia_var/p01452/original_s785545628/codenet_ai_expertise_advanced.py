import sys
from functools import lru_cache
from operator import mul
from itertools import accumulate

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    MOD = 10**9 + 7
    N, M, K = map(int, readline().split())
    L = N + M + 2 * K

    # Precompute factorials and inverse factorials using accumulate and pow
    fact = [1, *accumulate(range(1, L + 1), lambda x, y: x * y % MOD)]
    rfact = [1] * (L + 1)
    rfact[L] = pow(fact[L], MOD - 2, MOD)
    for i in range(L, 0, -1):
        rfact[i - 1] = rfact[i] * i % MOD

    # Combinatorial with precautions for k > n
    def C(n, k):
        if not 0 <= k <= n:
            return 0
        return fact[n] * rfact[k] % MOD * rfact[n - k] % MOD

    # Optimized formula avoiding negative indexes
    def F(n, k):
        if k < 0 or n < k:
            return 0
        return fact[n + k] * (n - k + 1) % MOD * rfact[k] % MOD * rfact[n + 1] % MOD

    ans = sum(
        C(N + 2 * a + M + 2 * (K - a), N + 2 * a) *
        F(N + a, a) *
        F(M + (K - a), K - a) % MOD
        for a in range(K + 1)
    ) % MOD

    write(f"{ans}\n")
solve()