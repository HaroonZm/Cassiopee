import sys
import numpy as np
from numba import njit, i8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

MOD = 10 ** 9 + 7

@njit(i8(i8, i8), cache=True, fastmath=True, inline='always')
def mpow(a, n):
    res = 1
    a %= MOD
    while n:
        if n & 1:
            res = res * a % MOD
        a = a * a % MOD
        n >>= 1
    return res

@njit((i8,), cache=True, fastmath=True)
def fact_table(N):
    fact = np.empty(N, np.int64)
    fact[0] = 1
    for i in range(1, N):
        fact[i] = fact[i-1] * i % MOD
    fact_inv = np.empty(N, np.int64)
    fact_inv[N-1] = mpow(fact[N-1], MOD-2)
    for i in range(N-2, -1, -1):
        fact_inv[i] = fact_inv[i+1] * (i+1) % MOD
    return fact, fact_inv

@njit((i8[:], i8), cache=True, fastmath=True, inline='always')
def is_colorful(A, K):
    n = len(A)
    if n < K:
        return False
    counts = np.zeros(K+1, np.int64)
    distinct = 0
    for i in range(K):
        x = A[i]
        if counts[x] == 0:
            distinct += 1
        counts[x] += 1
    if distinct == K:
        return True
    for i in range(K, n):
        y = A[i]; z = A[i-K]
        if counts[y] == 0:
            distinct += 1
        counts[y] += 1
        if counts[z] == 1:
            distinct -= 1
        counts[z] -= 1
        if distinct == K:
            return True
    return False

@njit((i8, i8, i8), cache=True, fastmath=True)
def compute_dp(N, K, n):
    dp = np.zeros((N, K), np.int64)
    dp[0, n] = 1
    for i in range(1, N):
        for k in range(K - 1, 0, -1):
            dp[i, k] = (dp[i, k] + dp[i-1, k]) % MOD
            dp[i, k-1] = (dp[i, k-1] + dp[i, k]) % MOD
        for k in range(1, K):
            dp[i, k] = (dp[i, k] + (K-k+1) * dp[i-1, k-1]) % MOD
        dp[i, 0] = 0
    return np.remainder(np.sum(dp, axis=1), MOD)

@njit((i8, i8, i8[:]), cache=True)
def main(N, K, A):
    M = len(A)
    pow_k = mpow(K, N - M)
    total = ((N - M + 1) * pow_k) % MOD

    if is_colorful(A, K):
        return total

    def f(X):
        seen = np.zeros(501, np.bool_)
        cnt = 0
        for a in X:
            if seen[a]:
                break
            seen[a] = True
            cnt += 1
        return cnt
    
    l, r = f(A), f(A[::-1])
    if l < M:
        dpl = compute_dp(N, K, l)
        dpr = compute_dp(N, K, r)
        for i in range(N - M + 1):
            j = N - M - i
            total = (total - dpl[i] * dpr[j] % MOD) % MOD
        return total

    dp1 = np.zeros((N + 1, K), np.int64)
    dp2 = np.zeros((N + 1, K), np.int64)
    dp1[0, 0] = 1
    for i in range(1, N + 1):
        for k in range(K - 1, 0, -1):
            dp1[i, k] = (dp1[i, k] + dp1[i-1, k]) % MOD
            dp1[i, k-1] = (dp1[i, k-1] + dp1[i, k]) % MOD
            dp2[i, k] = (dp2[i, k] + dp2[i-1, k]) % MOD
            dp2[i, k-1] = (dp2[i, k-1] + dp2[i, k]) % MOD
        for k in range(1, K):
            add = (K - k + 1) * dp1[i-1, k-1] % MOD
            dp1[i, k] = (dp1[i, k] + add) % MOD
            dp2[i, k] = (dp2[i, k] + (K - k + 1) * dp2[i-1, k-1]) % MOD
        dp1[i, 0] = 0
        dp2[i, 0] = 0
        for k in range(M, K):
            dp2[i, k] = (dp2[i, k] + dp1[i, k]) % MOD
    x = np.sum(dp2[-1]) % MOD
    fact, fact_inv = fact_table(200010)
    p = fact_inv[K] * fact[K - M] % MOD
    total = (total - x * p % MOD) % MOD
    return total

N, K, M = map(int, readline().split())
A = np.frombuffer(read(), dtype=np.int64, count=M)
print(main(N, K, A))