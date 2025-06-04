import sys

def read_input():
    return sys.stdin.readline()

def floyd_warshall(distance_matrix, node_count):
    for intermediate_node in range(node_count):
        for start_node in range(node_count):
            for end_node in range(node_count):
                current_distance = distance_matrix[start_node][end_node]
                path_via_intermediate = distance_matrix[start_node][intermediate_node] + distance_matrix[intermediate_node][end_node]
                distance_matrix[start_node][end_node] = min(current_distance, path_via_intermediate)
    return distance_matrix

number_of_rows, number_of_columns = map(int, read_input().split())

grid_representation = [list(read_input().strip()) for _ in range(number_of_rows)]

total_cells = number_of_rows * number_of_columns

adjacency_matrix = [[float("inf")] * total_cells for _ in range(total_cells)]

for cell_index in range(total_cells):
    adjacency_matrix[cell_index][cell_index] = 0

for row_index in range(number_of_rows):
    for column_index in range(number_of_columns - 1):
        if grid_representation[row_index][column_index] == "." and grid_representation[row_index][column_index + 1] == ".":
            left_cell = number_of_columns * row_index + column_index
            right_cell = number_of_columns * row_index + (column_index + 1)
            adjacency_matrix[left_cell][right_cell] = 1
            adjacency_matrix[right_cell][left_cell] = 1

for row_index in range(number_of_rows - 1):
    for column_index in range(number_of_columns):
        if grid_representation[row_index][column_index] == "." and grid_representation[row_index + 1][column_index] == ".":
            upper_cell = number_of_columns * row_index + column_index
            lower_cell = number_of_columns * (row_index + 1) + column_index
            adjacency_matrix[upper_cell][lower_cell] = 1
            adjacency_matrix[lower_cell][upper_cell] = 1

shortest_paths_matrix = floyd_warshall(adjacency_matrix, total_cells)

maximum_shortest_path_length = 0

for start_cell_index in range(total_cells):
    for end_cell_index in range(total_cells):
        if shortest_paths_matrix[start_cell_index][end_cell_index] != float("inf"):
            maximum_shortest_path_length = max(maximum_shortest_path_length, shortest_paths_matrix[start_cell_index][end_cell_index])

print(maximum_shortest_path_length)