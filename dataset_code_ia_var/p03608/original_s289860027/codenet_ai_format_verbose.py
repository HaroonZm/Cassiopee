from itertools import permutations

def compute_all_pairs_shortest_paths(distance_matrix, number_of_nodes):

    for intermediate_node in range(number_of_nodes):
        for start_node in range(number_of_nodes):
            for end_node in range(number_of_nodes):
                distance_matrix[start_node][end_node] = min(
                    distance_matrix[start_node][end_node],
                    distance_matrix[start_node][intermediate_node] + distance_matrix[intermediate_node][end_node]
                )

    return distance_matrix

number_of_cities, number_of_roads, number_of_targets = map(int, input().split())

target_city_indices = list(map(int, input().split()))

adjacency_matrix = [
    [float('inf')] * number_of_cities
    for _ in range(number_of_cities)
]

for _ in range(number_of_roads):

    city_a_index, city_b_index, road_distance = map(int, input().split())

    adjacency_matrix[city_a_index - 1][city_b_index - 1] = road_distance
    adjacency_matrix[city_b_index - 1][city_a_index - 1] = road_distance

shortest_distance_matrix = compute_all_pairs_shortest_paths(adjacency_matrix, number_of_cities)

minimum_total_distance = float('inf')

for visiting_order in permutations(target_city_indices):

    current_total_distance = 0

    for current_stop_index in range(1, len(visiting_order)):
        previous_city_index = visiting_order[current_stop_index - 1] - 1
        current_city_index = visiting_order[current_stop_index] - 1

        current_total_distance += shortest_distance_matrix[previous_city_index][current_city_index]

    minimum_total_distance = min(minimum_total_distance, current_total_distance)

print(minimum_total_distance)