import sys

def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    for _ in range(n):
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

while True:
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
        if line == '':
            sys.exit(0)
    nmp = line.strip().split()
    if len(nmp) < 3:
        continue
    n, m, p = map(int, nmp)
    if n == 0 and m == 0 and p == 0:
        break
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    children = []
    for _ in range(p):
        c = int(sys.stdin.readline())
        children.append(c)

    dist_start = dijkstra(n, graph, 0)
    dist_end = dijkstra(n, graph, n-1)

    dist_shortest = dist_start[n-1]

    # count number of shortest paths from start to each node
    ways_start = [0] * n
    ways_start[0] = 1
    nodes_by_dist = sorted(range(n), key=lambda x: dist_start[x])
    for u in nodes_by_dist:
        for v, w in graph[u]:
            if dist_start[u] + w == dist_start[v]:
                ways_start[v] += ways_start[u]

    # count number of shortest paths from each node to end
    ways_end = [0] * n
    ways_end[n-1] = 1
    nodes_by_dist_end = sorted(range(n), key=lambda x: dist_end[x])
    for u in nodes_by_dist_end:
        for v, w in graph[u]:
            if dist_end[u] + w == dist_end[v]:
                ways_end[v] += ways_end[u]

    total_paths = ways_start[n-1]

    for c in children:
        if dist_start[c] + dist_end[c] == dist_shortest:
            count = ways_start[c] * ways_end[c]
            prob = count / total_paths
            print(float(prob))
        else:
            print(0.0)
    print()