import sys
sys.setrecursionlimit(10**6)

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        edges.append((x - 1, y - 1))
    return n, m, edges

def build_graph(n, edges):
    graph = []
    for _ in range(n):
        graph.append([])
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    return graph

def dfs(node, parent):
    deg[node] = len(graph[node])
    dp[node] = [0] * deg[node]
    result = 1
    for i in range(deg[node]):
        neighbor = graph[node][i]
        if neighbor == parent:
            par[node] = i
            continue
        dp[node][i] = dfs(neighbor, node)
        result = (result * (dp[node][i] + 1)) % M
    return result

def bfs(node, parent_value = 0, parent = -1):
    if parent != -1:
        dp[node][par[node]] = parent_value
    left_products = [1] * (deg[node] + 1)
    right_products = [1] * (deg[node] + 1)
    for i in range(1, deg[node] + 1):
        left_products[i] = (left_products[i - 1] * (dp[node][i - 1] + 1)) % M
        right_products[deg[node] - i] = (right_products[deg[node] - i + 1] * (dp[node][deg[node] - i] + 1)) % M
    ans[node] = right_products[0]
    for i in range(deg[node]):
        neighbor = graph[node][i]
        if neighbor == parent:
            continue
        bfs(neighbor, (left_products[i] * right_products[i + 1]) % M, node)

N, M, edges = read_input()
graph = build_graph(N, edges)
deg = [0 for _ in range(N)]
par = [0 for _ in range(N)]
dp = [None for _ in range(N)]
ans = [0 for _ in range(N)]

dfs(0, -1)
bfs(0)
for value in ans:
    print(value)