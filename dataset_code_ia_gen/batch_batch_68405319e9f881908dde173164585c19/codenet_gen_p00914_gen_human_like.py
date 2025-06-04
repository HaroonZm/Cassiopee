import sys

def count_sets(n, k, s):
    # dp[i][j][m] = number of ways to select j numbers from {1..i} that sum to m
    dp = [[[0]*(s+1) for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0][0] = 1

    for i in range(1, n+1):
        for j in range(k+1):
            for m in range(s+1):
                # not take i
                dp[i][j][m] = dp[i-1][j][m]
                # take i if possible
                if j > 0 and m >= i:
                    dp[i][j][m] += dp[i-1][j-1][m - i]

    return dp[n][k][s]

for line in sys.stdin:
    n,k,s = map(int, line.split())
    if n == 0 and k == 0 and s == 0:
        break
    print(count_sets(n,k,s))