import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10 ** 9 + 7

N = int(input())

A = [tuple(map(int, input().split())) for _ in range(N)]

dp = [-1] * (1 << N)
dp[(1 << N) - 1] = 1

def dfs(group, count):
    if dp[group] != -1:
        return dp[group]
    res = 0
    for i in range(N):
        if (group >> i) & 1 == 0 and A[count][i] == 1:
            res += dfs(group + (1 << i), count + 1)
    dp[group] = res % MOD
    return dp[group]

tmp = dfs(0, 0)

print (tmp)