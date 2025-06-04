from sys import stdin
from math import inf

def main():
    n = int(next(stdin))
    cost = [int(next(stdin)) for _ in range(n - 1)]
    dp = [inf] * (n + 1)
    dp[0] = 0

    for i, c in enumerate(cost, 1):
        for j in range(i // 2 + 1):
            k = i - j
            if dp[j] + c < dp[k]:
                dp[k] = dp[j] + c
            if dp[k] + c < dp[j]:
                dp[j] = dp[k] + c

    print(dp[n // 2])

if __name__ == "__main__":
    main()