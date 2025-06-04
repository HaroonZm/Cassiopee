from sys import stdin
from itertools import repeat

def knapsack(n, max_weight):
    dp = [0] * (max_weight + 1)
    for _ in repeat(None, n):
        v, w = map(int, stdin.readline().split())
        for ww in range(w, max_weight + 1):
            if (new := dp[ww - w] + v) > dp[ww]:
                dp[ww] = new
    return dp[max_weight]

if __name__ == "__main__":
    n, max_w = map(int, stdin.readline().split())
    print(knapsack(n, max_w))