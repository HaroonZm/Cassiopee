v, e = map(int, input().split())
edges = []
graph = [[10**9]*v for _ in range(v)]
degree = [0]*v

for i in range(v):
    graph[i][i] = 0

total_edge_length = 0
for _ in range(e):
    s, t, d = map(int, input().split())
    edges.append((s,t,d))
    total_edge_length += d
    degree[s] += 1
    degree[t] += 1
    if d < graph[s][t]:
        graph[s][t] = d
        graph[t][s] = d

# Floyd-Warshall for all pairs shortest paths
for k in range(v):
    for i in range(v):
        for j in range(v):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

odd_vertices = [i for i in range(v) if degree[i] % 2 == 1]

# If no odd vertices, answer is sum of edges
if len(odd_vertices) == 0:
    print(total_edge_length)
    exit()

n = len(odd_vertices)
# Precompute cost between odd vertices
cost = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        cost[i][j] = graph[odd_vertices[i]][odd_vertices[j]]

# DP to find minimum perfect matching on odd vertices
dp = [10**9]*(1<<n)
dp[0] = 0

for mask in range(1<<n):
    if bin(mask).count('1') % 2 == 1:
        continue
    if dp[mask] == 10**9:
        continue
    # find first unmatched vertex
    try:
        first = next(i for i in range(n) if not (mask & (1 << i)))
    except StopIteration:
        continue
    for j in range(first+1, n):
        if not (mask & (1 << j)):
            new_mask = mask | (1 << first) | (1 << j)
            new_cost = dp[mask] + cost[first][j]
            if dp[new_mask] > new_cost:
                dp[new_mask] = new_cost

print(total_edge_length + dp[(1<<n)-1])