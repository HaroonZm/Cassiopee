import sys
from sys import stdin
input = stdin.readline

INF = 0x7fffffff
n,m = map(int,input().split())
d = [int(input()) for _ in range(n)]
c = [int(input()) for _ in range(m)]
dp = [[INF]*(n+1) for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    for j in range(n+1):
        dp[i+1][j] = dp[i][j]
    for j in range(n):
        if dp[i][j] != INF:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+c[i]*d[j])
print(dp[m][n])