def solve(num_nodes, num_edges, edges):
    selected_edges = []
    visited = [False] * num_nodes
    visited[0] = True  # starting from node 0, obviously

    while True:
        min_edge_cost = float('inf')
        min_edge_index = -1
        start_node = -1
        end_node = -1

        for i in range(len(edges)):
            u, v, cost = edges[i]
            # check if this edge connects visited to unvisited node
            if (visited[u] and not visited[v]) or (not visited[u] and visited[v]):
                if cost < min_edge_cost:
                    min_edge_cost = cost
                    min_edge_index = i
                    start_node = u
                    end_node = v

        if min_edge_index == -1:
            # no connecting edge found; maybe graph disconnected?
            break

        selected_edges.append(min_edge_cost)
        visited[start_node] = True
        visited[end_node] = True
        edges.pop(min_edge_index)

        # try to clean up edges that connect already visited nodes
        i = 0
        while i < len(edges):
            u, v, _ = edges[i]
            if visited[u] and visited[v]:
                edges.pop(i)
                # don't increment i because list is shorter now
            else:
                i += 1

        if all(visited):
            break

    # The division by 100 and subtraction seems problem-specific...
    print(sum(selected_edges) / 100.0 - len(selected_edges))


while True:
    n = int(raw_input())
    if n == 0:
        break
    m = int(raw_input())
    edges_data = []
    for _ in range(m):
        line = raw_input()
        parts = line.split(",")
        edges_data.append(map(int, parts))
    solve(n, m, edges_data)