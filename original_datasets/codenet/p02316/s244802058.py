import sys
readline = sys.stdin.readline

def knapsack(N, weight):
    dp = [0] * (weight + 1)
    for _ in range(N):
        v, w = map(int, readline().split())
        ww = w
        while ww <= weight:
            dp[ww] = max(dp[ww], dp[ww - w] + v)
            ww += 1
    return dp[-1]

if __name__ == "__main__":
    n_goods, weight = map(int, input().split())
    print(knapsack(n_goods, weight))