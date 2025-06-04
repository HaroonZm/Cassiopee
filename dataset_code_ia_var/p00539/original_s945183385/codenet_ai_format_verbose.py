from heapq import heappush, heappop

INFINITY_DISTANCE = 10 ** 20

number_of_nodes, number_of_edges, cost_per_unit = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_nodes)]
edge_weight_lookup = {}
total_edge_weight = 0

for _ in range(number_of_edges):
    node_start, node_end, edge_weight = map(int, input().split())
    node_start -= 1
    node_end -= 1
    adjacency_list[node_start].append((node_end, edge_weight))
    adjacency_list[node_end].append((node_start, edge_weight))
    edge_weight_lookup[(node_start, node_end)] = edge_weight
    total_edge_weight += edge_weight

shortest_distance_from_source = [INFINITY_DISTANCE] * number_of_nodes
shortest_distance_from_source[0] = 0
priority_queue = []
heappush(priority_queue, (0, 0))

while priority_queue:
    current_distance, current_node = heappop(priority_queue)
    for neighbor_node, neighbor_edge_weight in adjacency_list[current_node]:
        potential_distance = current_distance + neighbor_edge_weight
        if shortest_distance_from_source[neighbor_node] > potential_distance:
            shortest_distance_from_source[neighbor_node] = potential_distance
            heappush(priority_queue, (potential_distance, neighbor_node))

edge_removal_by_max_distance = {}

for (start_node, end_node), weight in edge_weight_lookup.items():
    maximum_distance = max(shortest_distance_from_source[start_node], shortest_distance_from_source[end_node])
    if maximum_distance in edge_removal_by_max_distance:
        edge_removal_by_max_distance[maximum_distance] += weight
    else:
        edge_removal_by_max_distance[maximum_distance] = weight

minimum_total_cost = total_edge_weight

for distance_threshold, removable_weight in sorted(edge_removal_by_max_distance.items()):
    total_edge_weight -= removable_weight
    current_total_cost = total_edge_weight + distance_threshold * cost_per_unit
    if current_total_cost < minimum_total_cost:
        minimum_total_cost = current_total_cost

print(minimum_total_cost)