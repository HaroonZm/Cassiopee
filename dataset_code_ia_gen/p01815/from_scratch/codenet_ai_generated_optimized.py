import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
w = list(map(int, input().split()))
g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

dp = [-1] * N  # dp[u] = 最大得点（頂点uから）
visited = [False] * N

def dfs(u):
    if dp[u] != -1:
        return dp[u]
    visited[u] = True
    res = 0
    for nv in g[u]:
        if not visited[nv]:
            res = max(res, dfs(nv))
    visited[u] = False
    dp[u] = res + w[u]
    return dp[u]

print(dfs(0))