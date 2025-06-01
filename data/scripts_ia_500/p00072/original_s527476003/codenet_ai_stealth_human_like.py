while True:
    n = input()
    if n == 0:
        break
    # create graph as adjacency matrix with big values (infinity substitute)
    graph = [[10**9]*n for _ in xrange(n)]
    for _ in xrange(input()):
        a,b,c = map(int, raw_input().strip().split(","))
        graph[a][b] = c
        graph[b][a] = c  # since undirected
    visited = [False]*n
    visited[0] = True
    ans = 0
    # basically prim's algorithm for mst but a bit clunky
    while not all(visited):
        edges = []
        for i in xrange(n):
            if visited[i]:
                for j in xrange(n):
                    if not visited[j]:
                        edges.append((i,j,graph[i][j]))
        t = min(edges, key=lambda x: x[2])
        ans += t[2]/100.0 - 1  # convert to something, not sure why minus 1 exactly
        visited[t[1]] = True
    print ans