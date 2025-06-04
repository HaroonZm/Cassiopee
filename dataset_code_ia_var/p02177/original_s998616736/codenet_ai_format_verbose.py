import sys

def read_input_line():
    return sys.stdin.readline()

def read_int_list_from_input():
    return list(map(int, read_input_line().split()))

number_of_vertices, number_of_edges = read_int_list_from_input()

directed_graph = [[] for _ in range(number_of_vertices)]
reverse_directed_graph = [[] for _ in range(number_of_vertices)]

for _ in range(number_of_edges):
    start_vertex, end_vertex = read_int_list_from_input()
    # Convert to zero-based index for internal representation
    directed_graph[start_vertex - 1].append(end_vertex - 1)
    reverse_directed_graph[end_vertex - 1].append(start_vertex - 1)

def strongly_connected_components(graph, reverse_graph):
    total_vertices = len(graph)
    
    finishing_time = 0
    vertices_by_finishing_time = [-1] * total_vertices
    vertex_visited = [False] * total_vertices
    vertex_component = [-1] * total_vertices

    def forward_depth_first_search(current_vertex):
        nonlocal finishing_time
        vertex_visited[current_vertex] = True
        for adjacent_vertex in graph[current_vertex]:
            if not vertex_visited[adjacent_vertex]:
                forward_depth_first_search(adjacent_vertex)
        vertices_by_finishing_time[finishing_time] = current_vertex
        finishing_time += 1

    def reverse_depth_first_search(current_vertex, component_id):
        vertex_component[current_vertex] = component_id
        for adjacent_vertex in reverse_graph[current_vertex]:
            if vertex_component[adjacent_vertex] == -1:
                reverse_depth_first_search(adjacent_vertex, component_id)

    # First DFS to compute finishing order
    for vertex in range(total_vertices):
        if not vertex_visited[vertex]:
            forward_depth_first_search(vertex)

    current_component_id = 0
    # Process vertices in reverse finishing time to assign components
    for vertex_index in range(total_vertices - 1, -1, -1):
        vertex_in_order = vertices_by_finishing_time[vertex_index]
        if vertex_component[vertex_in_order] == -1:
            reverse_depth_first_search(vertex_in_order, current_component_id)
            current_component_id += 1

    return vertex_component, current_component_id

vertex_to_component, number_of_components = strongly_connected_components(directed_graph, reverse_directed_graph)

component_to_vertices_list = [[] for _ in range(number_of_components)]

for vertex_index in range(number_of_vertices):
    component_id = vertex_to_component[vertex_index]
    # Use one-based indices for output as in the original
    component_to_vertices_list[component_id].append(vertex_index + 1)

for vertex_index in range(number_of_vertices):
    component_id = vertex_to_component[vertex_index]
    print(*component_to_vertices_list[component_id])