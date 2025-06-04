from heapq import heappush, heappop

number_of_nodes, number_of_edges = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_nodes)]

for _ in range(number_of_edges):

    node_u, node_v, edge_weight = map(int, input().split())

    node_u -= 1
    node_v -= 1

    adjacency_list[node_u].append((node_v, edge_weight))
    adjacency_list[node_v].append((node_u, edge_weight))


start_node, end_node, number_of_queries = map(int, input().split())
start_node -= 1
end_node -= 1

def dijkstra_compute_shortest_distances_and_parents(source_node):

    INFINITY_DISTANCE = 10 ** 20

    distance_from_source = [INFINITY_DISTANCE] * number_of_nodes
    distance_from_source[source_node] = 0

    parent_nodes_on_shortest_paths = [set() for _ in range(number_of_nodes)]

    heap_priority_queue = []
    heappush(heap_priority_queue, (0, source_node))

    while heap_priority_queue:

        current_distance, current_node = heappop(heap_priority_queue)

        for neighbor_node, edge_cost in adjacency_list[current_node]:

            tentative_distance = current_distance + edge_cost

            if distance_from_source[neighbor_node] > tentative_distance:
                distance_from_source[neighbor_node] = tentative_distance
                parent_nodes_on_shortest_paths[neighbor_node] = {current_node}
                heappush(heap_priority_queue, (tentative_distance, neighbor_node))
            elif distance_from_source[neighbor_node] == tentative_distance:
                parent_nodes_on_shortest_paths[neighbor_node].add(current_node)

    return distance_from_source, parent_nodes_on_shortest_paths

def are_nodes_on_same_shortest_path_path(source_query_node, target_query_node, visited_nodes_set):

    if source_query_node == target_query_node:
        return True

    if target_query_node in visited_nodes_set:
        return False

    visited_nodes_set.add(target_query_node)

    if shortest_distances_from_start[source_query_node] >= shortest_distances_from_start[target_query_node]:
        return False

    for parent_node in shortest_path_parents[target_query_node]:
        if are_nodes_on_same_shortest_path_path(source_query_node, parent_node, visited_nodes_set):
            return True

    return False

shortest_distances_from_start, shortest_path_parents = dijkstra_compute_shortest_distances_and_parents(start_node)
shortest_distances_from_end, _ = dijkstra_compute_shortest_distances_and_parents(end_node)

minimal_shortest_path_length = shortest_distances_from_start[end_node]

for _ in range(number_of_queries):

    query_node_c, query_node_d = map(int, input().split())
    query_node_c -= 1
    query_node_d -= 1

    is_c_on_shortest_path = shortest_distances_from_start[query_node_c] + shortest_distances_from_end[query_node_c] == minimal_shortest_path_length
    is_d_on_shortest_path = shortest_distances_from_start[query_node_d] + shortest_distances_from_end[query_node_d] == minimal_shortest_path_length

    if is_c_on_shortest_path and is_d_on_shortest_path and are_nodes_on_same_shortest_path_path(query_node_c, query_node_d, set()):
        print("Yes")
    else:
        print("No")