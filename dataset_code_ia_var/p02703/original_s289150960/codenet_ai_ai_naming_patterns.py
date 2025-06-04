import sys
import heapq

def graph_shortest_paths(adj_list, source_index):
    node_count = len(adj_list)
    min_distances = [float("inf")] * node_count
    min_distances[source_index] = 0
    priority_queue = [(0, source_index)]
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)
        if min_distances[curr_node] < curr_distance:
            continue
        for neighbor_node, edge_weight in adj_list[curr_node]:
            if min_distances[neighbor_node] > curr_distance + edge_weight:
                min_distances[neighbor_node] = curr_distance + edge_weight
                heapq.heappush(priority_queue, (min_distances[neighbor_node], neighbor_node))
    return min_distances

input_reader = sys.stdin.readline
vertex_count, edge_count, start_state = map(int, input_reader().split())
adjacency = [[] for _ in range(vertex_count)]

if start_state >= 2500:
    for _ in range(edge_count):
        src_node, dst_node, edge_val_a, edge_val_b = map(int, input_reader().split())
        src_node -= 1
        dst_node -= 1
        adjacency[src_node].append((dst_node, edge_val_b))
        adjacency[dst_node].append((src_node, edge_val_b))
    min_paths = graph_shortest_paths(adjacency, 0)
else:
    for _ in range(edge_count):
        src_node, dst_node, val_a, val_b = map(int, input_reader().split())
        src_node -= 1
        dst_node -= 1
        adjacency[src_node].append((dst_node, val_a, val_b))
        adjacency[dst_node].append((src_node, val_a, val_b))
    node_charge_data = [list(map(int, input_reader().split())) for _ in range(vertex_count)]
    expanded_graph = [[] for _ in range(vertex_count * 2500)]
    for node_index in range(vertex_count):
        charge_increment, charge_cost = node_charge_data[node_index]
        for charge_level in range(2500):
            for neighbor_index, require_charge, travel_cost in adjacency[node_index]:
                if charge_level >= require_charge:
                    expanded_graph[2500 * node_index + charge_level].append(
                        (2500 * neighbor_index + (charge_level - require_charge), travel_cost)
                    )
            if charge_level + charge_increment < 2500:
                expanded_graph[2500 * node_index + charge_level].append(
                    (2500 * node_index + (charge_level + charge_increment), charge_cost)
                )
    expanded_distances = graph_shortest_paths(expanded_graph, start_state)
    min_paths = [0] * vertex_count
    for node_index in range(vertex_count):
        min_paths[node_index] = min(expanded_distances[2500 * node_index:2500 * (node_index + 1)])
print(*min_paths[1:], sep="\n")