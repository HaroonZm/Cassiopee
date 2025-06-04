import sys
sys.setrecursionlimit(10**6)
read_line = sys.stdin.readline
infinity_value = float('inf')

node_count, edge_count = map(int, read_line().split())
adjacency_list_template = [{} for _ in range(node_count)]

for edge_index in range(edge_count):
    from_node, to_node, edge_weight = map(int, read_line().split())
    from_node -= 1
    to_node -= 1
    adjacency_list_template[from_node][to_node] = edge_weight
    adjacency_list_template[to_node][from_node] = edge_weight

import heapq
def run_dijkstra(graph_edges, source_node):
    distance_table = [[float('inf'), float('inf')] for _ in range(len(graph_edges))]
    distance_table[source_node][0] = 0
    priority_queue = [(0, source_node, 0)]
    heapq.heapify(priority_queue)
    while priority_queue:
        current_distance, current_node, has_flag = heapq.heappop(priority_queue)
        updated_flag = has_flag or (current_node % node_count == node_count - 1)
        if current_distance > distance_table[current_node][has_flag]:
            continue
        for neighbor_node, edge_cost in graph_edges[current_node].items():
            if distance_table[neighbor_node][updated_flag] <= current_distance + edge_cost:
                continue
            distance_table[neighbor_node][updated_flag] = current_distance + edge_cost
            heapq.heappush(priority_queue, (distance_table[neighbor_node][updated_flag], neighbor_node, updated_flag))
    return distance_table

random_seed = int(read_line())
random_a, random_b, random_c = map(int, read_line().split())
random_values_list = [random_seed]
current_value = random_seed
seen_values = set()
while True:
    current_value = (random_a * current_value + random_b) % random_c
    if current_value in seen_values:
        cycle_start_index = random_values_list.index(current_value)
        break
    random_values_list.append(current_value)
    seen_values.add(current_value)
cycle_length = len(random_values_list)

expanded_adjacency_list = [{} for _ in range(cycle_length * node_count)]
for base_node, neighbor_dict in enumerate(adjacency_list_template):
    for cycle_step, random_multiplier in enumerate(random_values_list):
        for neighbor, base_edge_weight in neighbor_dict.items():
            if cycle_step + 1 != cycle_length:
                expanded_adjacency_list[cycle_step * node_count + base_node][(cycle_step + 1) * node_count + neighbor] = base_edge_weight * random_multiplier
            else:
                expanded_adjacency_list[cycle_step * node_count + base_node][cycle_start_index * node_count + neighbor] = base_edge_weight * random_multiplier

all_distances = run_dijkstra(expanded_adjacency_list, 0)
minimum_result = float('inf')
for cycle_index in range(cycle_length):
    minimum_result = min(minimum_result, all_distances[cycle_index * node_count][1])
print(minimum_result)