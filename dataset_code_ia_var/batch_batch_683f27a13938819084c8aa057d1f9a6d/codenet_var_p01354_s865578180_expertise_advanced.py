import sys
from functools import lru_cache
from operator import itemgetter

def solve():
    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer
    readline = stdin.readline

    M, N = map(int, readline().split())
    P = [tuple(map(float, readline().split())) + (0.0,) for _ in range(M)]
    full = (1 << M) - 1

    dp = [ [0.0] * (N+1) for _ in range(1<<M) ]
    dp[0][N] = 1.0

    for state in range(1, 1 << M):
        dps = dp[state]
        for k in range(M):
            if not (state & (1<<k)):
                continue
            pk = P[k]
            prev = dp[state ^ (1<<k)]
            acc = 0.0
            # Compute backwards with in-place s
            for i in range(N, -1, -1):
                acc += prev[i] * (1 - pk[i])
                dps[i] = max(dps[i], acc)
                if i:
                    acc *= pk[i-1]
    stdout.write(f"{dp[full][0]:.16f}\n".encode())

solve()