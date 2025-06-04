import sys

def count_sets(n, k, s):
    dp = [[[0]*(s+1) for _ in range(k+1)] for __ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1, n+1):
        for j in range(k+1):
            for x in range(s+1):
                dp[i][j][x] = dp[i-1][j][x]
                if j>0 and x>=i:
                    dp[i][j][x] += dp[i-1][j-1][x-i]
    return dp[n][k][s]

for line in sys.stdin:
    n,k,s = map(int,line.strip().split())
    if n==0 and k==0 and s==0:
        break
    print(count_sets(n,k,s))