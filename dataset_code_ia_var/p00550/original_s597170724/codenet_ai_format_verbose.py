from collections import deque

def build_directed_acyclic_graph(source_node_index, total_nodes_count, adjacency_list):
    shortest_distances_from_source = [float("inf")] * total_nodes_count
    shortest_distances_from_source[source_node_index] = 0

    dag_adjacency_list = [[] for _ in range(total_nodes_count)]

    nodes_queue = deque([source_node_index])
    visited_nodes = [False] * total_nodes_count
    visited_nodes[source_node_index] = True

    indegree_counts = [0] * total_nodes_count

    while nodes_queue:
        current_node = nodes_queue.popleft()
        for neighbor_node in adjacency_list[current_node]:
            if shortest_distances_from_source[neighbor_node] >= shortest_distances_from_source[current_node] + 1:
                if not visited_nodes[neighbor_node]:
                    visited_nodes[neighbor_node] = True
                    nodes_queue.append(neighbor_node)
                dag_adjacency_list[current_node].append(neighbor_node)
                shortest_distances_from_source[neighbor_node] = shortest_distances_from_source[current_node] + 1
                indegree_counts[neighbor_node] += 1
    return dag_adjacency_list, shortest_distances_from_source, indegree_counts

def bfs_count_reachable_nodes_from(start_node_index, dag_adjacency_list, node_indegree_counts):
    global processed_edges_set

    node_indegree_counts[start_node_index] -= 1
    if node_indegree_counts[start_node_index] != 0:
        return 0
    traversal_queue = deque([start_node_index])
    reachable_nodes_count = 1

    while traversal_queue:
        current_node = traversal_queue.popleft()
        for neighbor_node in dag_adjacency_list[current_node]:
            if (current_node, neighbor_node) in processed_edges_set:
                continue
            processed_edges_set[(current_node, neighbor_node)] = True
            node_indegree_counts[neighbor_node] -= 1
            if node_indegree_counts[neighbor_node] == 0:
                reachable_nodes_count += 1
                traversal_queue.append(neighbor_node)
    return reachable_nodes_count

# Read input
total_nodes, total_edges, total_queries = map(int, input().split())
edges_list = []
undirected_graph_adjacency_list = [[] for _ in range(total_nodes)]
for _ in range(total_edges):
    node_u, node_v = map(int, input().split())
    node_u -= 1
    node_v -= 1
    undirected_graph_adjacency_list[node_u].append(node_v)
    undirected_graph_adjacency_list[node_v].append(node_u)
    edges_list.append((node_u, node_v))

dag_adjacency_list, shortest_distances, initial_indegrees = build_directed_acyclic_graph(
    0, total_nodes, undirected_graph_adjacency_list
)

cumulative_answer = 0
processed_edges_set = {}

for _ in range(total_queries):
    edge_query_index = int(input())
    edge_query_index -= 1
    node_a, node_b = edges_list[edge_query_index]

    if abs(shortest_distances[node_a] - shortest_distances[node_b]) == 0:
        print(cumulative_answer)
        continue

    if shortest_distances[node_a] < shortest_distances[node_b]:
        if (node_a, node_b) not in processed_edges_set:
            processed_edges_set[(node_a, node_b)] = True
            cumulative_answer += bfs_count_reachable_nodes_from(node_b, dag_adjacency_list, initial_indegrees)
    else:
        if (node_b, node_a) not in processed_edges_set:
            processed_edges_set[(node_b, node_a)] = True
            cumulative_answer += bfs_count_reachable_nodes_from(node_a, dag_adjacency_list, initial_indegrees)

    print(cumulative_answer)