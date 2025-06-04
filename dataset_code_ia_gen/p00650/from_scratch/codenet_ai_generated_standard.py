import sys
sys.setrecursionlimit(10**7)

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n)]
    redges = [[] for _ in range(n)]
    total = 0
    edges = []
    for _ in range(m):
        x, y, c = map(int, sys.stdin.readline().split())
        edges.append((x, y, c))
        total += c
        graph[x].append(y)
        redges[y].append(x)
    # Build residual graph for min cut
    # We'll find the min cut after partitioning rooms from 0 side
    # Use Dinic or BFS for min cut; here n<=100 so BFS + DFS is OK
    # But we only need to find vertices reachable from node 0 in original graph and reverse graph
    visited = [False]*n
    dfs(0)
    visited_r = [False]*n
    def dfs_r(u):
        visited_r[u] = True
        for v in redges[u]:
            if not visited_r[v]:
                dfs_r(v)
    dfs_r(0)
    res = 0
    for x,y,c in edges:
        # Edges from reachable(set S) to unreachable(set T) nodes are crossing the cut
        if visited[x] and not visited[y]:
            res += c
    print(res)