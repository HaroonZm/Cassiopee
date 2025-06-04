from sys import stdin
from collections.abc import Sequence

def knapsack(N: int, W: int, items: Sequence[tuple[int, int]]) -> int:
    dp = [0] * (W + 1)
    for v, w in items:
        for i in range(W, w - 1, -1):
            if (new := dp[i - w] + v) > dp[i]:
                dp[i] = new
    return dp[W]

if __name__ == "__main__":
    N, W = map(int, stdin.readline().split())
    items = [tuple(map(int, line.split())) for line in stdin.readlines()]
    print(knapsack(N, W, items))