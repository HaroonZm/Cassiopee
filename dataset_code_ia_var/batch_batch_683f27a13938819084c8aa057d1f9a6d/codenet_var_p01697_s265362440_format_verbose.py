import sys
import operator

def solve():
    input_buffer = sys.stdin.buffer.readline
    output_write = sys.stdout.write

    number_of_nodes, number_of_edges, max_height, number_of_keys = map(int, input_buffer().split())

    if number_of_nodes == number_of_edges == max_height == number_of_keys == 0:
        return False

    total_key_states = (1 << number_of_keys)
    adjacency_list = [[] for _ in range(number_of_nodes)]

    for _ in range(number_of_edges):
        node_a, node_b, edge_cost, edge_height, required_key = map(int, input_buffer().split())
        node_a -= 1
        node_b -= 1
        key_mask = 1 << (required_key - 1)
        adjacency_list[node_a].append((node_b, edge_cost, edge_height * number_of_nodes, key_mask))
        adjacency_list[node_b].append((node_a, edge_cost, edge_height * number_of_nodes, key_mask))

    start_node, target_node = map(int, input_buffer().split())
    start_node -= 1
    target_node -= 1

    INFINITY = 10**18
    shortest_distance_for_key_state = [0] * total_key_states
    max_total_height = max_height * number_of_nodes

    for key_state in range(total_key_states):
        distance = [INFINITY] * (number_of_nodes * max_height + number_of_nodes)
        distance[start_node] = 0

        for height_accum in range(0, max_total_height, number_of_nodes):
            remaining_height = max_total_height - height_accum
            for current_node in range(number_of_nodes):
                current_cost = distance[height_accum + current_node]
                if current_cost == INFINITY:
                    continue
                for neighbor_node, edge_cost, edge_height_cost, required_key_mask in adjacency_list[current_node]:
                    if remaining_height < edge_height_cost:
                        continue
                    next_position = height_accum + edge_height_cost + neighbor_node
                    if key_state & required_key_mask:
                        if current_cost < distance[next_position]:
                            distance[next_position] = current_cost
                    else:
                        if current_cost + edge_cost < distance[next_position]:
                            distance[next_position] = current_cost + edge_cost

        shortest_distance_for_key_state[key_state] = min(
            distance[position] for position in range(target_node, max_total_height + number_of_nodes, number_of_nodes)
        )

    number_of_special_items = int(input_buffer())
    special_item_costs_for_key_state = [INFINITY] * total_key_states

    for _ in range(number_of_special_items):
        inputs = list(map(int, input_buffer().split()))
        location = inputs[0]
        cost_for_items = inputs[1]
        keys = inputs[2:]
        key_state = 0
        for key in keys:
            key_state |= 1 << (key - 1)
        special_item_costs_for_key_state[key_state] = cost_for_items

    special_item_costs_for_key_state[0] = 0

    for first_key_state in range(total_key_states):
        for second_key_state in range(first_key_state + 1, total_key_states):
            merged_key_state = first_key_state | second_key_state
            combined_cost = special_item_costs_for_key_state[first_key_state] + special_item_costs_for_key_state[second_key_state]
            if combined_cost < special_item_costs_for_key_state[merged_key_state]:
                special_item_costs_for_key_state[merged_key_state] = combined_cost

    minimum_combined_cost = min(
        map(operator.add, shortest_distance_for_key_state, special_item_costs_for_key_state)
    )

    if minimum_combined_cost < INFINITY:
        output_write("%d\n" % minimum_combined_cost)
    else:
        output_write("-1\n")

    return True


while solve():
    pass