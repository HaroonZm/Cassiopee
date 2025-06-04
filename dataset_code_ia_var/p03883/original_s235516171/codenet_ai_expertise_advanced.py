import sys
import numpy as np
from functools import partial

def main():
    readline = sys.stdin.readline

    N = int(readline())
    LR = [tuple(map(int, line.split())) for line in sys.stdin]

    LR.sort(key=partial(lambda a, t: -(t[0]+t[1]), LR[0]))

    INF = np.iinfo(np.int64).max
    dp = np.full((2, N+1), INF, dtype=np.int64)

    dp[0, 0 if N & 1 else 1-1] = 0  # Set initial state: central not used or used depending on parity

    for n, (L, R) in enumerate(LR):
        length = L + R
        x = np.arange(n+1, dtype=np.int64)
        dp_new = np.full_like(dp, INF)

        # From not-fixed central
        np.minimum(dp[0, :n+1] + R + x * length, dp_new[0, 1:n+2], out=dp_new[0, 1:n+2])
        np.minimum(dp[0, :n+1] + L + (n - x) * length, dp_new[0, :n+1], out=dp_new[0, :n+1])
        np.minimum(dp[0, :n+1] + ((N-1)//2) * length, dp_new[1, :n+1], out=dp_new[1, :n+1])

        # From fixed central
        np.minimum(dp[1, :n+1] + R + x * length, dp_new[1, 1:n+2], out=dp_new[1, 1:n+2])
        np.minimum(dp[1, :n+1] + L + (n - x) * length, dp_new[1, :n+1], out=dp_new[1, :n+1])

        dp = dp_new

    print(int(dp[1, N//2]))

if __name__ == "__main__":
    main()