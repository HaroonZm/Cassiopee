from sys import stdin

def can_arrange(dominoes):
    # Count degrees of each vertex (0-6)
    degree = [0]*7
    # Graph adjacency: edge count between vertices
    adj = [[0]*7 for _ in range(7)]
    edges_total = len(dominoes)

    for a,b in dominoes:
        degree[a] += 1
        degree[b] += 1
        adj[a][b] += 1
        if a != b:
            adj[b][a] += 1

    # Check connectivity ignoring vertices with degree 0
    def dfs(u, visited):
        visited[u]=True
        for v in range(7):
            if adj[u][v]>0 and not visited[v]:
                dfs(v, visited)

    start_vertex = next((i for i,d in enumerate(degree) if d>0), -1)
    if start_vertex == -1:
        return True  # no edges = vacuously yes

    visited = [False]*7
    dfs(start_vertex, visited)
    for i in range(7):
        if degree[i]>0 and not visited[i]:
            return False  # not connected

    odd_count = sum(d%2 for d in degree)
    # Eulerian path conditions:
    # 0 or 2 vertices of odd degree
    return odd_count==0 or odd_count==2


lines=stdin.read().strip().split('\n')
for i in range(0,len(lines),2):
    n = int(lines[i])
    data=lines[i+1].split()
    dominoes=[]
    for d in data:
        dominoes.append((int(d[0]), int(d[1])))
    print("Yes" if can_arrange(dominoes) else "No")