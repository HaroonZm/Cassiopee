from itertools import starmap
from collections import deque

def solve():
    try:
        while True:
            N, M = map(int, raw_input().split())
            dp = [[0] * (M + 1) for _ in range(3)]
            for _ in range(N):
                name = raw_input()
                C, V, D, L = map(int, raw_input().split())
                VDL = (V, D, L)
                if C > M:
                    continue
                for i, val in enumerate(VDL):
                    dp_i = dp[i]
                    # Forward traversal to avoid overcounting in 0/1 knapsack
                    for j in range(M, C - 1, -1):
                        if dp_i[j - C] or j == C:
                            dp_i[j] = max(dp_i[j], dp_i[j - C] + val if j - C >= 0 else val)
            print(max(starmap(max, dp)))
    except Exception:
        pass

solve()