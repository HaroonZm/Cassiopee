def compute_travel_time(total_weight, travel_distance):
    travel_time = travel_distance / (2000 / (70.0 + total_weight))
    return travel_time

def find_optimal_path():
    distance_matrix = [[None] * num_locations for _ in range(num_locations)]
    for from_idx in range(num_locations):
        for to_idx in range(num_locations):
            if from_idx == to_idx:
                distance_matrix[from_idx][to_idx] = float('inf')
            else:
                distance_matrix[from_idx][to_idx] = abs(location_distance[from_idx] - location_distance[to_idx])

    weight_at_state = [float('inf')] * (1 << num_locations)
    min_time_at_state = [[float('inf')] * num_locations for _ in range(1 << num_locations)]
    previous_location_at_state = [[0] * num_locations for _ in range(1 << num_locations)]

    for start_idx in range(num_locations):
        min_time_at_state[1 << start_idx][start_idx] = 0
        weight_at_state[1 << start_idx] = location_weight[start_idx] * 20

    for visited_mask in range(1, 1 << num_locations):
        for current_loc_idx in range(num_locations):
            if weight_at_state[visited_mask] == float('inf'):
                continue
            for next_loc_idx in range(num_locations):
                if not (visited_mask >> next_loc_idx) & 1:
                    next_visited_mask = visited_mask | (1 << next_loc_idx)
                    weight_at_state[next_visited_mask] = weight_at_state[visited_mask] + location_weight[next_loc_idx] * 20
                    computed_time = compute_travel_time(weight_at_state[visited_mask], distance_matrix[current_loc_idx][next_loc_idx]) + min_time_at_state[visited_mask][current_loc_idx]
                    if min_time_at_state[next_visited_mask][next_loc_idx] > computed_time:
                        min_time_at_state[next_visited_mask][next_loc_idx] = computed_time
                        previous_location_at_state[next_visited_mask][next_loc_idx] = current_loc_idx

    optimal_route = []
    current_state = (1 << num_locations) - 1
    current_location_index = min_time_at_state[current_state].index(min(min_time_at_state[current_state]))
    while current_state != 0:
        optimal_route.append(location_name[current_location_index])
        previous_index = previous_location_at_state[current_state][current_location_index]
        current_state = current_state ^ (1 << current_location_index)
        current_location_index = previous_index
    optimal_route.reverse()
    return optimal_route

num_locations = int(raw_input())
location_name = {}
location_distance = {}
location_weight = {}
for location_idx in range(num_locations):
    location_input_name, location_input_distance, location_input_weight = map(int, raw_input().split())
    location_name[location_idx] = location_input_name
    location_distance[location_idx] = location_input_distance
    location_weight[location_idx] = location_input_weight

optimal_result_route = find_optimal_path()
print(' '.join(map(str, optimal_result_route)))