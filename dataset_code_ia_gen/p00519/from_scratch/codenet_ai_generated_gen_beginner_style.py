import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, K = map(int, input().split())
C = [0]*(N+1)
R = [0]*(N+1)
for i in range(1, N+1):
    c, r = map(int, input().split())
    C[i] = c
    R[i] = r

graph = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = 10**15
dp = [INF]*(N+1)
dp[1] = 0

from collections import deque

for i in range(1, N+1):
    # BFS from i to find towns reachable with R[i] or less edges
    dist = [-1]*(N+1)
    dist[i] = 0
    que = deque()
    que.append(i)
    reachable = []
    while que:
        v = que.popleft()
        if dist[v] == R[i]:
            continue
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                que.append(nv)
    # For all reachable towns from i within R[i] edges, update dp
    for j in range(1, N+1):
        if dist[j] != -1 and dp[i] + C[i] < dp[j]:
            dp[j] = dp[i] + C[i]

print(dp[N])