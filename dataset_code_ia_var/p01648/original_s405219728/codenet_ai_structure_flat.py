from heapq import heappush, heappop

while True:
    n_m = raw_input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0:
        break
    g = []
    for i in range(n):
        g.append([])
    i = 0
    while i < m:
        x = raw_input().split()
        a = int(x[0]) - 1
        b = int(x[1]) - 1
        c = int(x[2])
        g[a].append((b, c))
        g[b].append((a, c))
        i += 1
    heap = []
    visited = []
    edges = []
    for i in range(n):
        visited.append(False)
    heappush(heap, (0, 0))
    while len(heap) > 0:
        temp = heappop(heap)
        d = temp[0]
        v = temp[1]
        if visited[v]:
            continue
        visited[v] = True
        edges.append(d)
        for pair in g[v]:
            u = pair[0]
            dd = pair[1]
            if not visited[u]:
                heappush(heap, (dd, u))
    edges_sorted = sorted(edges)
    print edges_sorted[len(edges_sorted) // 2]