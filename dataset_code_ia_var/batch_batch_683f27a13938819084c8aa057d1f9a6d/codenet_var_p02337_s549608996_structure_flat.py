import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9 + 7

n, k = [int(x) for x in input().split()]
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1
i = 0
while i < n:
    j = 0
    while j < k:
        dp[i+1][j+1] = dp[i][j] + (j + 1) * dp[i][j+1]
        dp[i+1][j+1] %= MOD
        j += 1
    i += 1
ans = 0
i = 0
while i <= k:
    ans += dp[n][i]
    ans %= MOD
    i += 1
print(ans)