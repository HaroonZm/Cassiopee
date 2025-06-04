n = int(input())
graph = {i: [] for i in range(1, n+1)}

for _ in range(n):
    data = list(map(int, input().split()))
    u = data[0]
    k = data[1]
    if k > 0:
        graph[u] = data[2:]

visited = [False] * (n+1)
d = [0] * (n+1)
f = [0] * (n+1)
time = 1

def dfs(u):
    global time
    visited[u] = True
    d[u] = time
    time += 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    f[u] = time
    time += 1

for vertex in range(1, n+1):
    if not visited[vertex]:
        dfs(vertex)

for vertex in range(1, n+1):
    print(vertex, d[vertex], f[vertex])