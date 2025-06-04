import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, x = map(int, sys.stdin.readline().split())
    graph[A].append((B, x))
    graph[B].append((A, 1 / x))

visited = [False] * (N + 1)
value = [0.0] * (N + 1)
ok = True

def dfs(u):
    global ok
    visited[u] = True
    for v, ratio in graph[u]:
        if not visited[v]:
            value[v] = value[u] * ratio
            dfs(v)
        else:
            # Check for inconsistency
            if abs(value[v] - value[u] * ratio) > 1e-9:
                ok = False

for i in range(1, N + 1):
    if not visited[i] and graph[i]:
        value[i] = 1.0
        dfs(i)

print("Yes" if ok else "No")