import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9 + 7

N, A, B = map(int, read().split())

def solve(N, A, B):
    if A > B:
        A, B = B, A
    if A == 1:
        return pow(2, N, MOD)
    dp1 = np.zeros((N, B), dtype=np.int64)
    dp2 = np.zeros((N, B), dtype=np.int64)
    dp1_sum = np.zeros(N, dtype=np.int64)
    ans = 0
    for n in range(N):
        if n < A:
            dp1[n, 1] += 1
        else:
            if n + 1 < B:
                dp1[n, n + 1] += 1
        if n > 0:
            dp1[n, 1:] += dp1[n - 1, :-1]
        dp1[n, 1] += dp1_sum[max(0, n - A):n - 1].sum() % MOD
        if n >= A + 1 < B:
            dp1[n, A + 1:B] += dp2[n - A - 1, 0:B - (A + 1)]
        dp1[n] %= MOD
        dp1_sum[n] = dp1[n].sum() % MOD
        if (N - n - 1) < A:
            ans += dp1_sum[n]
        else:
            M = B - (N - n - 1)
            if M > 0:
                ans += dp1[n, :M].sum() % MOD
        dp2[n] += dp1[n]
        dp2[n, 1:] += dp2[n - 1, :-1]
        dp2[n] %= MOD
    x = pow(2, N, MOD) - ans
    return x % MOD

print(solve(N, A, B))