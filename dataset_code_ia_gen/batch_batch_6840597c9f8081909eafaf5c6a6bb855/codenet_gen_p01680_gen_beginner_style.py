import sys
sys.setrecursionlimit(10**7)

MOD = 1000000007

def dfs(u, graph, visited):
    stack = [u]
    size = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            size += 1
            for v in graph[node]:
                if not visited[v]:
                    stack.append(v)
    return size

for line in sys.stdin:
    if line.strip() == '':
        continue
    N, M = map(int, line.strip().split())
    if N == 0 and M == 0:
        break
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(N+1)
    ans = 1
    for i in range(1, N+1):
        if not visited[i]:
            size = dfs(i, graph, visited)
            ans = (ans * (pow(2, size) -1)) % MOD
    print(ans)