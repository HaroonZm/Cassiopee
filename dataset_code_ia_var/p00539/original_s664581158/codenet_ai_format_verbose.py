from heapq import heappush, heappop

number_of_nodes, number_of_edges, cost_coefficient = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_nodes)]
edge_list = []

for edge_index in range(number_of_edges):
    node_u, node_v, edge_weight = map(int, input().split())
    node_u -= 1  # Convert to zero-based index
    node_v -= 1
    adjacency_list[node_u].append((node_v, edge_weight))
    adjacency_list[node_v].append((node_u, edge_weight))
    edge_list.append((node_u, node_v, edge_weight))

INFINITY = 10 ** 18
shortest_distances = [INFINITY] * number_of_nodes
shortest_distances[0] = 0
priority_queue = [(0, 0)]  # (distance, node)

while priority_queue:
    current_distance, current_node = heappop(priority_queue)
    if shortest_distances[current_node] < current_distance:
        continue
    for neighbor_node, edge_cost in adjacency_list[current_node]:
        new_distance = current_distance + edge_cost
        if new_distance < shortest_distances[neighbor_node]:
            shortest_distances[neighbor_node] = new_distance
            heappush(priority_queue, (new_distance, neighbor_node))

ordered_nodes_by_distance = list(range(number_of_nodes))
ordered_nodes_by_distance.sort(key=shortest_distances.__getitem__)

node_rank_by_distance = [0] * number_of_nodes
for rank, node in enumerate(ordered_nodes_by_distance):
    node_rank_by_distance[node] = rank

edge_weight_accumulation = [0] * number_of_nodes
total_edge_weight = 0

for node_u, node_v, edge_weight in edge_list:
    if node_rank_by_distance[node_u] < node_rank_by_distance[node_v]:
        edge_weight_accumulation[node_v] += edge_weight
    else:
        edge_weight_accumulation[node_u] += edge_weight
    total_edge_weight += edge_weight

minimum_total_cost = INFINITY
accumulated_weight = 0

for node in ordered_nodes_by_distance:
    node_distance = shortest_distances[node]
    accumulated_weight += edge_weight_accumulation[node]
    total_cost = cost_coefficient * node_distance + (total_edge_weight - accumulated_weight)
    minimum_total_cost = min(minimum_total_cost, total_cost)

print(minimum_total_cost)