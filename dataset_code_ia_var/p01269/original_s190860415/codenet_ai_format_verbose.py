import heapq

while True:

    number_of_nodes, number_of_edges, initial_energy = map(int, raw_input().split())

    if number_of_nodes == 0:
        break

    adjacency_list = {}

    for node_index in xrange(number_of_nodes):
        adjacency_list[node_index] = []

    minimum_cost = [[10**9] * (initial_energy + 1) for _ in xrange(number_of_nodes)]
    minimum_cost[0][initial_energy] = 0

    for _ in xrange(number_of_edges):
        node_u, node_v, energy_required, edge_cost = map(int, raw_input().split())
        node_u -= 1
        node_v -= 1
        adjacency_list[node_u].append((node_v, energy_required, edge_cost))
        adjacency_list[node_v].append((node_u, energy_required, edge_cost))

    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, initial_energy))
    # (current_total_cost, current_node, remaining_energy)

    while len(priority_queue) > 0:

        current_total_cost, current_node, remaining_energy = heapq.heappop(priority_queue)

        for neighbor, energy_needed, traversal_cost in adjacency_list[current_node]:

            # Case 1: Traverse using traversal_cost (do not guard)
            new_cost = current_total_cost + traversal_cost
            if minimum_cost[neighbor][remaining_energy] > new_cost:
                minimum_cost[neighbor][remaining_energy] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor, remaining_energy))

            # Case 2: Traverse guarded, consuming energy, at no cost
            if remaining_energy - energy_needed >= 0:
                if minimum_cost[neighbor][remaining_energy - energy_needed] > current_total_cost:
                    minimum_cost[neighbor][remaining_energy - energy_needed] = current_total_cost
                    heapq.heappush(priority_queue, (current_total_cost, neighbor, remaining_energy - energy_needed))

    print min(minimum_cost[number_of_nodes - 1])