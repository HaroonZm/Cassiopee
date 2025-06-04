from collections import deque

def calculate_number_of_paths(
    number_of_nodes,
    diameter_length,
    adjacency_list,
    node_degrees,
    starting_node_1,
    starting_node_2
):

    bfs_queue = deque([starting_node_1, starting_node_2])
    node_distance_from_sources = [-1] * number_of_nodes
    node_distance_from_sources[starting_node_1] = 0
    node_distance_from_sources[starting_node_2] = 0

    while bfs_queue:
        current_node = bfs_queue.popleft()
        for neighbor in adjacency_list[current_node]:
            if node_distance_from_sources[neighbor] == -1:
                node_distance_from_sources[neighbor] = node_distance_from_sources[current_node] + 1
                bfs_queue.append(neighbor)

    max_path_length = diameter_length // 2
    path_length_counts = [0] * (max_path_length + 1)

    if starting_node_1 == starting_node_2:
        path_length_counts[0] = node_degrees[starting_node_1]

    for node_index in range(number_of_nodes):
        path_length = node_distance_from_sources[node_index]
        if path_length >= 0:
            path_length_counts[path_length] = max(
                path_length_counts[path_length],
                node_degrees[node_index] - 1
            )

    number_of_tree_central_paths = 1

    for paths_at_level in path_length_counts[:-1]:
        number_of_tree_central_paths *= paths_at_level

    return number_of_tree_central_paths

number_of_nodes = int(input())
adjacency_list = [[] for _ in range(number_of_nodes)]
node_degrees = [0] * number_of_nodes

for _ in range(number_of_nodes - 1):
    input_node_a, input_node_b = map(int, input().split())
    adjacency_list[input_node_a - 1].append(input_node_b - 1)
    node_degrees[input_node_a - 1] += 1
    adjacency_list[input_node_b - 1].append(input_node_a - 1)
    node_degrees[input_node_b - 1] += 1

# BFS to find farthest node from root (node 0)
stack = [0]
distance_from_root = [-1] * number_of_nodes
distance_from_root[0] = 0

while stack:
    current_node = stack.pop()
    for neighbor in adjacency_list[current_node]:
        if distance_from_root[neighbor] == -1:
            distance_from_root[neighbor] = distance_from_root[current_node] + 1
            stack.append(neighbor)

max_distance_from_root = max(distance_from_root)
farthest_node_from_root = distance_from_root.index(max_distance_from_root)

# BFS from one endpoint of the diameter to find the other endpoint
stack = [farthest_node_from_root]
distance_from_first_endpoint = [-1] * number_of_nodes
distance_from_first_endpoint[farthest_node_from_root] = 0

while stack:
    current_node = stack.pop()
    for neighbor in adjacency_list[current_node]:
        if distance_from_first_endpoint[neighbor] == -1:
            distance_from_first_endpoint[neighbor] = distance_from_first_endpoint[current_node] + 1
            stack.append(neighbor)

diameter_length = max(distance_from_first_endpoint)
opposite_endpoint = distance_from_first_endpoint.index(diameter_length)

# BFS from the opposite endpoint to measure distances again
stack = [opposite_endpoint]
distance_from_second_endpoint = [-1] * number_of_nodes
distance_from_second_endpoint[opposite_endpoint] = 0

while stack:
    current_node = stack.pop()
    for neighbor in adjacency_list[current_node]:
        if distance_from_second_endpoint[neighbor] == -1:
            distance_from_second_endpoint[neighbor] = distance_from_second_endpoint[current_node] + 1
            stack.append(neighbor)

if diameter_length % 2 == 1:  # Diameter length is odd

    central_nodes = []
    half_diameter_plus_one = diameter_length // 2 + 1

    print(half_diameter_plus_one, end=' ')

    for node_index in range(number_of_nodes):
        if (distance_from_first_endpoint[node_index] <= half_diameter_plus_one and
            distance_from_second_endpoint[node_index] <= half_diameter_plus_one):
            central_nodes.append(node_index)

    answer = (
        calculate_number_of_paths(
            number_of_nodes,
            diameter_length,
            adjacency_list,
            node_degrees,
            central_nodes[0],
            central_nodes[1]
        ) * 2
    )

    print(answer)

else:  # Diameter length is even

    half_diameter = diameter_length // 2
    central_node = None

    print(half_diameter + 1, end=' ')

    for node_index in range(number_of_nodes):
        if (distance_from_first_endpoint[node_index] <= half_diameter and
            distance_from_second_endpoint[node_index] <= half_diameter):
            central_node = node_index

    minimum_number_of_paths = calculate_number_of_paths(
        number_of_nodes,
        diameter_length,
        adjacency_list,
        node_degrees,
        central_node,
        central_node
    )

    for neighbor in adjacency_list[central_node]:
        candidate = (
            calculate_number_of_paths(
                number_of_nodes,
                diameter_length,
                adjacency_list,
                node_degrees,
                central_node,
                neighbor
            ) * 2
        )
        minimum_number_of_paths = min(minimum_number_of_paths, candidate)

    print(minimum_number_of_paths)