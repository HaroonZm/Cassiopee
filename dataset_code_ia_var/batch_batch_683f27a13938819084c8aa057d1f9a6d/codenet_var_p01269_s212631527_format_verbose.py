from collections import defaultdict
import heapq

while True:
    number_of_nodes, number_of_edges, max_allowed_gold = map(int, input().split())

    if number_of_nodes == number_of_edges == max_allowed_gold == 0:
        break

    adjacency_with_cost_and_gold = defaultdict(lambda: defaultdict(lambda: float("inf")))

    for _ in range(number_of_edges):
        start_node, end_node, gold_required, edge_cost = map(int, input().split())
        adjacency_with_cost_and_gold[start_node][end_node] = (gold_required, edge_cost)
        adjacency_with_cost_and_gold[end_node][start_node] = (gold_required, edge_cost)

    initial_state = (1, 0)  # (current_node, gold_collected)

    shortest_distance_from_start = defaultdict(lambda: float("inf"))
    shortest_distance_from_start[initial_state] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, initial_state))

    while len(priority_queue) > 0:
        current_total_cost, (current_node, current_gold) = heapq.heappop(priority_queue)

        if shortest_distance_from_start[(current_node, current_gold)] < current_total_cost:
            continue

        if current_node == number_of_nodes:
            print(current_total_cost)
            break

        candidate_next_states_with_cost = {}

        for neighbor_node, (required_gold_for_edge, cost_to_neighbor) in adjacency_with_cost_and_gold[current_node].items():
            candidate_next_states_with_cost[(neighbor_node, current_gold)] = cost_to_neighbor
            if current_gold + required_gold_for_edge <= max_allowed_gold:
                candidate_next_states_with_cost[(neighbor_node, current_gold + required_gold_for_edge)] = 0

        for next_state, additional_cost in candidate_next_states_with_cost.items():
            if shortest_distance_from_start[next_state] > shortest_distance_from_start[(current_node, current_gold)] + additional_cost:
                shortest_distance_from_start[next_state] = shortest_distance_from_start[(current_node, current_gold)] + additional_cost
                heapq.heappush(priority_queue, (shortest_distance_from_start[next_state], next_state))