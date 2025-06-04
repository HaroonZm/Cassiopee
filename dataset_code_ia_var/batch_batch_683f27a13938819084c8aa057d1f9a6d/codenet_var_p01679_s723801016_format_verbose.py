from heapq import heappush, heappop
import sys

def main():
    read_line_input = sys.stdin.readline
    write_output = sys.stdout.write

    BIT_COUNT_LOOKUP_SIZE = 1 << 16
    bit_count_lookup = [0] * BIT_COUNT_LOOKUP_SIZE

    for index in range(1, BIT_COUNT_LOOKUP_SIZE):
        bit_count_lookup[index] = bit_count_lookup[index ^ (index & -index)] + 1

    INFINITY = 10 ** 18

    def solve_test_case():
        num_nodes, num_edges, num_special_nodes, start_node, max_time = map(int, read_line_input().split())

        if num_nodes == 0 and num_edges == 0:
            return False

        adjacency_list = [[] for _ in range(num_nodes)]
        for _ in range(num_edges):
            node_a, node_b, edge_cost = map(int, read_line_input().split())
            node_a -= 1
            node_b -= 1
            adjacency_list[node_a].append((node_b, edge_cost))
            adjacency_list[node_b].append((node_a, edge_cost))

        def dijkstra_shortest_paths(source_node):
            node_distances = [INFINITY] * num_nodes
            node_distances[source_node] = 0
            priority_queue = [(0, source_node)]
            while priority_queue:
                current_cost, current_node = heappop(priority_queue)
                if node_distances[current_node] < current_cost:
                    continue
                for neighbor_node, travel_cost in adjacency_list[current_node]:
                    total_cost = current_cost + travel_cost
                    if total_cost < node_distances[neighbor_node]:
                        node_distances[neighbor_node] = total_cost
                        heappush(priority_queue, (total_cost, neighbor_node))
            return node_distances

        special_nodes_graph = [[] for _ in range(num_special_nodes)]
        special_node_indices = []
        visiting_time_of_special_nodes = [0] * num_special_nodes

        for current_special_index in range(num_special_nodes):
            special_node_index, special_visit_time = map(int, read_line_input().split())
            special_node_index -= 1
            distance_from_this_special = dijkstra_shortest_paths(special_node_index)
            for previous_special_index, previous_node_index in enumerate(special_node_indices):
                cost_to_previous = distance_from_this_special[previous_node_index]
                if cost_to_previous + visiting_time_of_special_nodes[previous_special_index] <= max_time:
                    special_nodes_graph[current_special_index].append(
                        (previous_special_index, cost_to_previous + visiting_time_of_special_nodes[previous_special_index], 1 << previous_special_index)
                    )
                if cost_to_previous + special_visit_time <= max_time:
                    special_nodes_graph[previous_special_index].append(
                        (current_special_index, cost_to_previous + special_visit_time, 1 << current_special_index)
                    )
            special_node_indices.append(special_node_index)
            visiting_time_of_special_nodes[current_special_index] = special_visit_time

        max_num_of_special_visits = 0
        shortest_distances_from_start = dijkstra_shortest_paths(start_node - 1)
        bit_mask_range = 1 << num_special_nodes
        max_allowed_costs_for_special_nodes = [0] * num_special_nodes

        dp_next_states = [[{} for _ in range(num_special_nodes)] for _ in range(num_special_nodes + 1)]

        for special_index in range(num_special_nodes):
            distance_to_special = shortest_distances_from_start[special_node_indices[special_index]]
            total_start_cost = distance_to_special + visiting_time_of_special_nodes[special_index]
            max_allowed_costs_for_special_nodes[special_index] = max_time - distance_to_special + 1
            if total_start_cost < max_allowed_costs_for_special_nodes[special_index]:
                dp_next_states[1][special_index][1 << special_index] = total_start_cost
                max_num_of_special_visits = 1

        for num_collected in range(1, num_special_nodes):
            current_states_for_num_collected = dp_next_states[num_collected]
            next_states_for_num_collected = dp_next_states[num_collected + 1]
            if any(current_states_for_num_collected):
                max_num_of_special_visits = num_collected
            for current_special_index in range(num_special_nodes):
                current_states_dict = current_states_for_num_collected[current_special_index]
                for neighbor_special_index, travel_cost, special_bit_mask in special_nodes_graph[current_special_index]:
                    max_allowed_cost_for_neighbor = max_allowed_costs_for_special_nodes[neighbor_special_index]
                    neighbor_states_dict = next_states_for_num_collected[neighbor_special_index]
                    for collected_mask, current_cost in current_states_dict.items():
                        if collected_mask & special_bit_mask:
                            continue
                        total_cost = current_cost + travel_cost
                        updated_mask = collected_mask | special_bit_mask
                        if total_cost < neighbor_states_dict.get(updated_mask, max_allowed_cost_for_neighbor):
                            neighbor_states_dict[updated_mask] = total_cost

        if any(dp_next_states[num_special_nodes]):
            max_num_of_special_visits = num_special_nodes

        write_output(f"{max_num_of_special_visits}\n")
        return True

    while solve_test_case():
        pass

main()