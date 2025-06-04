import sys
from collections import deque

input_buffer_read = sys.stdin.buffer.read
input_buffer_readline = sys.stdin.buffer.readline
input_buffer_readlines = sys.stdin.buffer.readlines

number_of_vertices, number_of_edges = map(int, input_buffer_readline().split())

adjacency_list_per_vertex = [[] for vertex_index in range(number_of_vertices)]

for edge_index in range(number_of_edges):
    from_vertex, to_vertex = map(int, input_buffer_readline().split())
    from_vertex -= 1
    to_vertex -= 1
    adjacency_list_per_vertex[from_vertex].append(to_vertex)
    adjacency_list_per_vertex[to_vertex].append(from_vertex)

def count_all_hamiltonian_paths_starting_from_vertex_zero():
    total_hamiltonian_paths = 0
    path_candidates_queue = deque([[0]])  # Each element is the current path (list of visited vertices)

    while path_candidates_queue:
        current_path = path_candidates_queue.popleft()
        if len(current_path) == number_of_vertices:
            total_hamiltonian_paths += 1
            continue
        for adjacent_vertex in adjacency_list_per_vertex[current_path[-1]]:
            if adjacent_vertex not in current_path:
                path_candidates_queue.append(current_path + [adjacent_vertex])

    return total_hamiltonian_paths

print(count_all_hamiltonian_paths_starting_from_vertex_zero())