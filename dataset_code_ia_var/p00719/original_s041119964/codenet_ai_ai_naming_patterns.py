while True:
    num_nodes, num_positions, num_edges, start_pos, end_pos = map(int, input().split())
    if not (num_nodes | num_positions | num_edges | start_pos | end_pos):
        break
    start_idx, end_idx = start_pos - 1, end_pos - 1
    speeds = [int(val) for val in input().split()]
    INF_COST = 1000
    dp_states = [[INF_COST] * num_positions for _ in range(1 << num_nodes)]
    dp_states[0][start_idx] = 0
    edge_list = []
    for _ in range(num_edges):
        from_pos, to_pos, cost = map(int, input().split())
        from_idx, to_idx = from_pos - 1, to_pos - 1
        edge_list.append((from_idx, to_idx, cost))
        edge_list.append((to_idx, from_idx, cost))
    min_total_cost = INF_COST
    for visit_mask in range(1 << num_nodes):
        for edge_from, edge_to, edge_cost in edge_list:
            for speed_idx in range(num_nodes):
                if (visit_mask >> speed_idx) & 1:
                    prev_mask = visit_mask & ~(1 << speed_idx)
                    current_cost = dp_states[prev_mask][edge_from] + edge_cost / speeds[speed_idx]
                    if dp_states[visit_mask][edge_to] > current_cost:
                        dp_states[visit_mask][edge_to] = current_cost
    min_total_cost = min(dp_states[visit_mask][end_idx] for visit_mask in range(1 << num_nodes))
    if min_total_cost == INF_COST:
        print("Impossible")
    else:
        print("{:.05f}".format(min_total_cost))