num_vertices, num_edges = map(int, input().split())
adjacency_matrix = [[0 for col_index in range(num_vertices)] for row_index in range(num_vertices)]

for edge_index in range(num_edges):
    source_vertex, dest_vertex = map(int, input().split())
    adjacency_matrix[source_vertex][dest_vertex] = 1

status_visited_vertices = [0 for vertex_index in range(num_vertices)]
cycle_found_flag = 0

def depth_first_search(current_vertex, start_vertex):
    for next_vertex in range(num_vertices):
        status_visited_vertices[current_vertex] = 1
        if adjacency_matrix[current_vertex][next_vertex] == 1 and next_vertex == start_vertex:
            global cycle_found_flag
            cycle_found_flag = 1
        if adjacency_matrix[current_vertex][next_vertex] == 1 and status_visited_vertices[next_vertex] == 0:
            depth_first_search(next_vertex, start_vertex)

for cycle_check_vertex in range(num_vertices):
    status_visited_vertices = [0 for vertex_reset_index in range(num_vertices)]
    depth_first_search(cycle_check_vertex, cycle_check_vertex)
    if cycle_found_flag == 1:
        print(1)
        break

if cycle_found_flag == 0:
    print(0)