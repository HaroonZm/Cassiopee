while True:
    try:
        line = input()
        if not line:
            break
        N, M = map(int, line.split())
        edges = []
        for _ in range(M):
            s, t = map(int, input().split())
            edges.append((s, t))

        # According to the problem, the smallest subset size is always
        # M - (N - number_of_strongly_connected_components).
        # Since each component is strongly connected, total components are counted.
        # But in the problem it's given every component is strongly connected.
        # So the number of strongly connected components is at least 1.
        # Actually, the problem says "each component is strongly connected",
        # so the graph may be disconnected but components are strongly connected.

        # We need to find the number of strongly connected components.
        # Then answer is M - (N - number_of_scc)

        # Let's implement a simple Kosaraju's algorithm to find SCC count

        graph = [[] for _ in range(N+1)]
        rgraph = [[] for _ in range(N+1)]
        for s,t in edges:
            graph[s].append(t)
            rgraph[t].append(s)

        visited = [False]*(N+1)
        order = []

        def dfs(v):
            visited[v] = True
            for nxt in graph[v]:
                if not visited[nxt]:
                    dfs(nxt)
            order.append(v)

        for i in range(1, N+1):
            if not visited[i]:
                dfs(i)

        visited = [False]*(N+1)
        def rdfs(v, comp):
            visited[v] = True
            comps[v] = comp
            for nxt in rgraph[v]:
                if not visited[nxt]:
                    rdfs(nxt, comp)

        comps = [0]*(N+1)
        comp_num = 0
        for v in reversed(order):
            if not visited[v]:
                comp_num += 1
                rdfs(v, comp_num)

        # Calculate answer
        ans = M - (N - comp_num)
        print(ans)
    except EOFError:
        break