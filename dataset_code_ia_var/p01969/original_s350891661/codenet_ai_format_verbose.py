import re

def main():
    number_of_rows, number_of_columns, start_character, target_character = input().split()

    number_of_rows = int(number_of_rows)
    number_of_columns = int(number_of_columns)
    start_index = ord(start_character) - ord('A')
    target_index = ord(target_character) - ord('A')

    input_grid_rows = [input() for _ in range(number_of_rows)]

    # Transpose the grid to get columns for vertical pattern searching
    input_grid_columns = [
        ''.join([input_grid_rows[row_index][column_index] for row_index in range(number_of_rows)])
        for column_index in range(number_of_columns)
    ]

    # Regular expressions matching horizontal and vertical paths
    horizontal_path_pattern = re.compile(r'o[A-Z]o(?:-+o[A-Z]o)+')
    vertical_path_pattern = re.compile(r'o[A-Z]o(?:\|+o[A-Z]o)+')

    path_strings = []

    # Extract horizontal path strings from rows
    for row_string in input_grid_rows:
        path_strings.extend(horizontal_path_pattern.findall(row_string))

    # Extract vertical path strings from transposed columns
    for column_string in input_grid_columns:
        path_strings.extend(vertical_path_pattern.findall(column_string))

    # Remove all non-capital-letter characters to get only node labels
    node_paths = [re.sub(r'[^A-Z]+', '', path) for path in path_strings]

    # Initialize adjacency matrix for the graph
    MAXIMUM_DISTANCE = 50
    adjacency_matrix = [
        [MAXIMUM_DISTANCE for _ in range(26)]
        for _ in range(26)
    ]

    # Populate the adjacency matrix with direct connections
    for path in node_paths:
        for node_from_label, node_to_label in zip(path[:-1], path[1:]):
            node_from_index = ord(node_from_label) - ord('A')
            node_to_index = ord(node_to_label) - ord('A')
            adjacency_matrix[node_from_index][node_to_index] = 1
            adjacency_matrix[node_to_index][node_from_index] = 1

    # Floyd-Warshall algorithm to compute shortest path between all pairs of nodes
    for intermediate_node in range(26):
        for start_node in range(26):
            for end_node in range(26):
                shortest_path_distance = min(
                    adjacency_matrix[start_node][end_node],
                    adjacency_matrix[start_node][intermediate_node] + adjacency_matrix[intermediate_node][end_node]
                )
                adjacency_matrix[start_node][end_node] = shortest_path_distance

    print(adjacency_matrix[start_index][target_index])
    return 0

if __name__ == '__main__':
    exit(main())