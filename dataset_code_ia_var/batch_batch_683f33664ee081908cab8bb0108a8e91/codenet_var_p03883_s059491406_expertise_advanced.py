import sys
import numpy as np
from functools import partial

def main():
    readline = sys.stdin.readline
    N = int(readline())
    LR = [tuple(map(int, line.split())) for line in sys.stdin]

    LR.sort(key=lambda x: -sum(x))

    INF = np.iinfo(np.int64).max
    dp_shape = (1,)
    dp = [np.full(dp_shape, INF, dtype=np.int64) for _ in (0, 1)]

    dp[0][0] = 0 if N & 1 else INF
    dp[1][0] = 0 if not N & 1 else INF

    for n, (L, R) in enumerate(LR):
        length = L + R
        prev_dp = [arr.copy() for arr in dp]
        dp_shape = (n + 2,)
        dp = [np.full(dp_shape, INF, dtype=np.int64) for _ in (0, 1)]
        x = np.arange(n + 1, dtype=np.int64)

        # Place on left
        np.minimum(prev_dp[0][:n+1] + R + x * length, dp[0][1:n+2], out=dp[0][1:n+2])
        np.minimum(prev_dp[1][:n+1] + R + x * length, dp[1][1:n+2], out=dp[1][1:n+2])
        # Place on right
        np.minimum(prev_dp[0][:n+1] + L + (n - x) * length, dp[0][:n+1], out=dp[0][:n+1])
        np.minimum(prev_dp[1][:n+1] + L + (n - x) * length, dp[1][:n+1], out=dp[1][:n+1])
        # Place at center
        np.minimum(prev_dp[0][:n+1] + ((N - 1)//2) * length, dp[1][:n+1], out=dp[1][:n+1])

    print(int(dp[1][N//2]))

if __name__ == "__main__":
    main()