from sys import stdin
from itertools import accumulate, repeat

def main():
    N, W = map(int, stdin.readline().split())
    items = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

    # Using a single list for dp, rolling array optimization
    dp = [0] * (W + 1)
    for value, weight in items:
        # iterate in reverse to prevent overwrite
        for w in range(W, weight - 1, -1):
            # using assignment expression (walrus operator) in Python 3.8+
            if (candidate := dp[w - weight] + value) > dp[w]:
                dp[w] = candidate

    print(dp[W])

if __name__ == '__main__':
    main()