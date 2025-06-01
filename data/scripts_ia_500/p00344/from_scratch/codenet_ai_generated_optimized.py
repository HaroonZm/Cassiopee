import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [0]*N  # 0=unvisited, 1=can reach start, -1=cannot reach
visited = [False]*N

def dfs(i):
    if dp[i] != 0:
        return dp[i] == 1
    if visited[i]:
        dp[i] = -1
        return False
    visited[i] = True
    ni = (i + a[i]) % N
    if ni == i:
        dp[i] = 1
        visited[i] = False
        return True
    res = dfs(ni)
    dp[i] = 1 if res else -1
    visited[i] = False
    return dp[i] == 1

count = 0
for i in range(N):
    if dfs(i):
        count += 1

print(count)