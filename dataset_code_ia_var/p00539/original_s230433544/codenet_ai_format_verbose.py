import heapq

def dijkstra_shortest_paths(start_node, adjacency_list):
    """
    Calcule les plus courts chemins depuis le sommet start_node vers tous les autres sommets en utilisant l'algorithme de Dijkstra.
    """
    visited_status = [0] * number_of_nodes    # 0: non traité, 1: en file, 2: traité définitivement
    shortest_distances = {node_index: float('inf') for node_index in range(number_of_nodes)}
    shortest_distances[start_node] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start_node])

    while len(min_heap) != 0:
        current_distance, current_node = heapq.heappop(min_heap)
        visited_status[current_node] = 2
        if shortest_distances[current_node] < current_distance:
            continue
        for neighbor_node, edge_cost in adjacency_list[current_node]:
            if visited_status[neighbor_node] != 2:
                if shortest_distances[current_node] + edge_cost < shortest_distances[neighbor_node]:
                    shortest_distances[neighbor_node] = shortest_distances[current_node] + edge_cost
                    visited_status[neighbor_node] = 1
                    heapq.heappush(min_heap, [shortest_distances[neighbor_node], neighbor_node])
    return shortest_distances

number_of_nodes, number_of_edges, additional_cost_per_distance_unit = map(int, raw_input().split())
adjacency_list = [[] for _ in range(number_of_nodes)]
total_edge_cost = 0

for edge_index in range(number_of_edges):
    node_a, node_b, edge_distance = map(int, raw_input().split())
    adjacency_list[node_a - 1].append([node_b - 1, edge_distance])
    adjacency_list[node_b - 1].append([node_a - 1, edge_distance])
    total_edge_cost += edge_distance

min_cost_priority_queue = []
shortest_distances_from_source = dijkstra_shortest_paths(0, adjacency_list)
sorted_distances = sorted(shortest_distances_from_source.items(), key=lambda distance_tuple: distance_tuple[1])

minimal_total_cost = float('inf')
nodes_already_considered = [0] * number_of_nodes

for current_node, distance_from_source in sorted_distances:
    nodes_already_considered[current_node] = 1
    for neighbor_node, edge_cost in adjacency_list[current_node]:
        if nodes_already_considered[neighbor_node] == 1:
            total_edge_cost -= edge_cost
    minimal_total_cost = min(minimal_total_cost, total_edge_cost + additional_cost_per_distance_unit * distance_from_source)

print minimal_total_cost