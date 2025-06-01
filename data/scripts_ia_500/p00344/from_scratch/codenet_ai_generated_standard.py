import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

graph = [(i + a[i]) % N for i in range(N)]
state = [0] * N  # 0: unvisited, 1: visiting, 2: done
dp = [False] * N

def dfs(u):
    if state[u] == 1:
        # cycle detected
        dp[u] = True
        return True
    if state[u] == 2:
        return dp[u]
    state[u] = 1
    res = dfs(graph[u])
    dp[u] = res
    state[u] = 2
    return res

count = 0
for i in range(N):
    if dfs(i):
        count += 1

print(count)