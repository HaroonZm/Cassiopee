def compute_strongly_connected_components(
    number_of_vertices,
    adjacency_list,
    reversed_adjacency_list
):
    topological_order = []
    visited_vertices = [False] * number_of_vertices
    component_labels = [None] * number_of_vertices

    def depth_first_search(current_vertex):
        visited_vertices[current_vertex] = True
        for neighbor_vertex in adjacency_list[current_vertex]:
            if not visited_vertices[neighbor_vertex]:
                depth_first_search(neighbor_vertex)
        topological_order.append(current_vertex)

    def reverse_depth_first_search(current_vertex, current_label):
        component_labels[current_vertex] = current_label
        visited_vertices[current_vertex] = True
        for neighbor_vertex in reversed_adjacency_list[current_vertex]:
            if not visited_vertices[neighbor_vertex]:
                reverse_depth_first_search(neighbor_vertex, current_label)

    for vertex_index in range(number_of_vertices):
        if not visited_vertices[vertex_index]:
            depth_first_search(vertex_index)

    visited_vertices = [False] * number_of_vertices
    total_components = 0

    for vertex_in_order in reversed(topological_order):
        if not visited_vertices[vertex_in_order]:
            reverse_depth_first_search(vertex_in_order, total_components)
            total_components += 1

    return total_components, component_labels


number_of_vertices, number_of_edges = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_vertices + 1)]
reversed_adjacency_list = [[] for _ in range(number_of_vertices + 1)]

for _ in range(number_of_edges):
    start_vertex, end_vertex = map(int, input().split())
    adjacency_list[start_vertex].append(end_vertex)
    reversed_adjacency_list[end_vertex].append(start_vertex)

component_count, vertex_component_label = compute_strongly_connected_components(
    number_of_vertices + 1,
    adjacency_list,
    reversed_adjacency_list
)

for target_label in vertex_component_label[1:]:
    connected_component_vertices = []
    for vertex_index, component_label in enumerate(vertex_component_label[1:], 1):
        if target_label == component_label:
            connected_component_vertices.append(vertex_index)
    print(" ".join(map(str, connected_component_vertices)))