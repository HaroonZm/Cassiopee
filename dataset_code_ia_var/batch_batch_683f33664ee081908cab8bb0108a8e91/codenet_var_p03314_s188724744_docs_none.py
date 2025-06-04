import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 1_000_000_007

@njit((i8, i8), cache=True)
def mpow(a, n):
    p = 1
    while n:
        if n & 1:
            p = p * a % MOD
        a = a * a % MOD
        n >>= 1
    return p

@njit((i8, ), cache=True)
def fact_table(N):
    fact = np.empty(N, np.int64)
    fact[0] = 1
    for n in range(1, N):
        fact[n] = n * fact[n - 1] % MOD
    fact_inv = np.empty(N, np.int64)
    fact_inv[N - 1] = mpow(fact[N - 1], MOD - 2)
    for n in range(N - 1, 0, -1):
        fact_inv[n - 1] = fact_inv[n] * n % MOD
    return fact, fact_inv

@njit((i8[:], i8), cache=True)
def is_colorful(A, K):
    if len(A) < K:
        return False
    counts = np.zeros(K + 1, np.int64)
    n_color = 0
    for i in range(K):
        x = A[i]
        if counts[x] == 0:
            n_color += 1
        counts[x] += 1
    if n_color == K:
        return True
    for i in range(K, len(A)):
        x = A[i]
        if counts[x] == 0:
            n_color += 1
        counts[x] += 1
        x = A[i - K]
        if counts[x] == 1:
            n_color -= 1
        counts[x] -= 1
        if n_color == K:
            return True
    return False

@njit((i8, i8, i8), cache=True)
def compute_dp(N, K, n):
    dp = np.zeros((N, K), np.int64)
    dp[0, n] = 1
    for i in range(1, N):
        for k in range(K - 1, 0, -1):
            dp[i, k] += dp[i - 1, k]
            dp[i, k - 1] += dp[i, k]
        for k in range(1, K):
            dp[i, k] += (K - k + 1) * dp[i - 1, k - 1]
        dp[i, 0] = 0
        dp[i] %= MOD
    return dp.sum(axis=1) % MOD

@njit((i8, i8, i8[:]), cache=True)
def main(N, K, A):
    M = len(A)
    total = (N - M + 1) * mpow(K, N - M) % MOD
    if is_colorful(A, K):
        return total

    def f(A):
        ng = np.zeros(500, np.bool_)
        x = 0
        for a in A:
            if ng[a]:
                break
            ng[a] = 1
            x += 1
        return x

    l, r = f(A), f(A[::-1])

    if l < M:
        dpl = compute_dp(N, K, l)
        dpr = compute_dp(N, K, r)
        for i in range(N - M + 1):
            j = N - M - i
            total -= dpl[i] * dpr[j] % MOD
        return total % MOD

    dp1 = np.zeros((N + 1, K), np.int64)
    dp2 = np.zeros((N + 1, K), np.int64)

    dp1[0, 0] = 1
    for i in range(1, N + 1):
        for k in range(K - 1, 0, -1):
            dp1[i, k] += dp1[i - 1, k]
            dp1[i, k - 1] += dp1[i, k]
            dp2[i, k] += dp2[i - 1, k]
            dp2[i, k - 1] += dp2[i, k]
        for k in range(1, K):
            dp1[i, k] += (K - k + 1) * dp1[i - 1, k - 1]
            dp2[i, k] += (K - k + 1) * dp2[i - 1, k - 1]
        dp1[i, 0] = 0
        dp1[i] %= MOD
        dp2[i, 0] = 0
        dp2[i] %= MOD
        for k in range(M, K):
            dp2[i, k] += dp1[i, k]
        dp2[i] %= MOD

    x = dp2[-1].sum() % MOD
    fact, fact_inv = fact_table(200_010)
    p = fact_inv[K] * fact[K - M] % MOD
    total -= x * p % MOD
    return total % MOD

N, K, M = map(int, readline().split())
A = np.array(read().split(), np.int64)

print(main(N, K, A))