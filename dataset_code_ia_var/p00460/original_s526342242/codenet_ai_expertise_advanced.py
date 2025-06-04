from functools import lru_cache
from itertools import count

def main():
    import sys
    input_iter = (map(int, line.split()) for line in sys.stdin)
    for N, M, S in input_iter:
        if not (N or M or S):
            break
        print(solve(N, M, S))

def solve(N, M, S):
    MOD = 10**5
    p, q = N * N, M - N * N
    T = S - (p * (p + 1)) // 2
    if T < 0 or p == 0:
        return int(T == 0)

    dp = [0] * (T + 1)
    dp[0] = 1

    for i in range(1, p + 1):
        cumsum = [0] * (T + 2)
        for t in range(T + 1):
            cumsum[t + 1] = (cumsum[t] + dp[t]) % MOD

        for t in range(T + 1):
            left = t - q if t - q >= 0 else 0
            right = t - i + 1 if t - i + 1 > left else left
            dp[t] = (cumsum[right] - cumsum[left]) % MOD

    return dp[T] % MOD

main()