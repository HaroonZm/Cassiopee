from heapq import heappush, heappop
from collections import deque

number_of_nodes, number_of_edges = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_nodes)]

for _ in range(number_of_edges):
    start_node, end_node, edge_weight = map(int, input().split())
    adjacency_list[start_node - 1].append((end_node - 1, edge_weight))
    adjacency_list[end_node - 1].append((start_node - 1, edge_weight))

INFINITY = 10 ** 18

def dijkstra_find_furthest_nodes(source_node_index):

    shortest_distances = [INFINITY] * number_of_nodes
    shortest_distances[source_node_index] = 0

    min_heap = [(0, source_node_index)]

    while min_heap:
        current_cost, current_node = heappop(min_heap)

        if shortest_distances[current_node] < current_cost:
            continue

        for neighbor_node, edge_weight in adjacency_list[current_node]:
            if current_cost + edge_weight < shortest_distances[neighbor_node]:
                shortest_distances[neighbor_node] = current_cost + edge_weight
                heappush(min_heap, (current_cost + edge_weight, neighbor_node))

    maximum_distance = max(shortest_distances)

    assert maximum_distance != INFINITY

    nodes_at_maximum_distance = [
        node_index for node_index in range(number_of_nodes)
        if shortest_distances[node_index] == maximum_distance
    ]

    visited_nodes = set(nodes_at_maximum_distance)
    breadth_first_queue = deque(nodes_at_maximum_distance)

    while breadth_first_queue:
        current_bfs_node = breadth_first_queue.popleft()
        for neighbor_node, edge_weight in adjacency_list[current_bfs_node]:
            if (shortest_distances[neighbor_node] + edge_weight == shortest_distances[current_bfs_node]
                and neighbor_node not in visited_nodes):
                visited_nodes.add(neighbor_node)
                breadth_first_queue.append(neighbor_node)

    return maximum_distance, visited_nodes


distance_and_used_nodes_per_source = [
    dijkstra_find_furthest_nodes(source_node_index)
    for source_node_index in range(number_of_nodes)
]

global_maximum_distance = max(
    maximum_distance for maximum_distance, used_nodes in distance_and_used_nodes_per_source
)

candidate_nodes = set(range(number_of_nodes))

for maximum_distance, used_nodes in distance_and_used_nodes_per_source:
    if maximum_distance == global_maximum_distance:
        candidate_nodes -= used_nodes

print(len(candidate_nodes))

for node_index in sorted(candidate_nodes):
    print(node_index + 1)