from collections import deque
import sys

standard_input_readline = sys.stdin.readline
standard_output_write = sys.stdout.write

def main():
    num_vertices, num_operations = map(int, standard_input_readline().split())
    operation_list = [list(map(int, standard_input_readline().split())) for _ in range(num_operations)]
    edge_status_map = {}
    block_size = int(num_operations**0.5) + 1

    def find_set(vertex, parent_list):
        if vertex == parent_list[vertex]:
            return vertex
        parent_list[vertex] = find_set(parent_list[vertex], parent_list)
        return parent_list[vertex]

    def union_sets(vertex_u, vertex_v, parent_list):
        root_u = find_set(vertex_u, parent_list)
        root_v = find_set(vertex_v, parent_list)
        if root_u < root_v:
            parent_list[root_v] = root_u
        else:
            parent_list[root_u] = root_v

    vertices_queue = deque()
    search_used_flags = [0] * num_vertices
    search_label_counter = 0
    parent_list = [0] * num_vertices

    for block_start in range(block_size):
        active_edges_set = set()
        for operation_index in range(block_start * block_size, min((block_start + 1) * block_size, num_operations)):
            operation_type, vertex_a, vertex_b = operation_list[operation_index]
            if operation_type == 3:
                continue
            current_edge = (vertex_a, vertex_b)
            if edge_status_map.get(current_edge, 0):
                active_edges_set.add(current_edge)
            edge_status_map[current_edge] = 0

        parent_list[:] = range(num_vertices)
        for (vertex_u, vertex_v), status in edge_status_map.items():
            if status == 1:
                union_sets(vertex_u, vertex_v, parent_list)

        adjacency_list = [[] for _ in range(num_vertices)]
        edge_to_adjacency_nodes = {}
        for vertex_a, vertex_b in active_edges_set:
            root_a = find_set(vertex_a, parent_list)
            root_b = find_set(vertex_b, parent_list)
            if root_a == root_b:
                continue
            ordered_edge = (root_a, root_b) if root_a < root_b else (root_b, root_a)
            if ordered_edge in edge_to_adjacency_nodes:
                node_list_1, node_list_2 = edge_to_adjacency_nodes[ordered_edge]
                node_list_1[1] = node_list_2[1] = node_list_1[1] + 1
            else:
                node_list_1 = [root_b, 1]
                node_list_2 = [root_a, 1]
                adjacency_list[root_a].append(node_list_1)
                adjacency_list[root_b].append(node_list_2)
                edge_to_adjacency_nodes[ordered_edge] = node_list_1, node_list_2

        for operation_index in range(block_start * block_size, min((block_start + 1) * block_size, num_operations)):
            operation_type, vertex_a, vertex_b = operation_list[operation_index]
            root_a = find_set(vertex_a, parent_list)
            root_b = find_set(vertex_b, parent_list)
            ordered_edge = (root_a, root_b) if root_a < root_b else (root_b, root_a)
            if operation_type == 1:
                edge_status_map[(vertex_a, vertex_b)] = 1
                if root_a == root_b:
                    continue
                if ordered_edge not in edge_to_adjacency_nodes:
                    node_list_1 = [root_b, 1]
                    node_list_2 = [root_a, 1]
                    adjacency_list[root_a].append(node_list_1)
                    adjacency_list[root_b].append(node_list_2)
                    edge_to_adjacency_nodes[ordered_edge] = node_list_1, node_list_2
                else:
                    node_list_1, node_list_2 = edge_to_adjacency_nodes[ordered_edge]
                    node_list_1[1] = node_list_2[1] = node_list_1[1] + 1
            elif operation_type == 2:
                edge_status_map[(vertex_a, vertex_b)] = 0
                if root_a == root_b:
                    continue
                node_list_1, node_list_2 = edge_to_adjacency_nodes[ordered_edge]
                node_list_1[1] = node_list_2[1] = node_list_1[1] - 1
            elif operation_type == 3:
                if root_a == root_b:
                    standard_output_write("YES\n")
                else:
                    search_label_counter += 1
                    vertices_queue.append(root_a)
                    search_used_flags[root_a] = search_label_counter
                    while vertices_queue:
                        current_vertex = vertices_queue.popleft()
                        for neighbor_vertex, is_active in adjacency_list[current_vertex]:
                            if is_active and search_used_flags[neighbor_vertex] != search_label_counter:
                                search_used_flags[neighbor_vertex] = search_label_counter
                                vertices_queue.append(neighbor_vertex)
                    if search_used_flags[root_b] == search_label_counter:
                        standard_output_write("YES\n")
                    else:
                        standard_output_write("NO\n")

main()