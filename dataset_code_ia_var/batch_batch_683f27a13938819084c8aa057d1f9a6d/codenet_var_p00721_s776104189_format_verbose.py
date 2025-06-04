from heapq import heappush, heappop

INFINITY_DISTANCE = 10 ** 10

ADJACENT_DIRECTION_DELTAS = (
    (0, -1),  # Up
    (0, 1),   # Down
    (-1, 0),  # Left
    (1, 0)    # Right
)

def calculate_shortest_path_distance(start_coordinate, target_coordinate, map_matrix):
    priority_queue = []
    heappush(priority_queue, (0, start_coordinate))
    
    row_count = len(map_matrix)
    column_count = len(map_matrix[0])
    visited_grid = [[False] * column_count for _ in range(row_count)]
    visited_grid[start_coordinate[1]][start_coordinate[0]] = True
    
    while priority_queue:
        current_distance, current_position = heappop(priority_queue)
        current_x, current_y = current_position
        
        for delta_x, delta_y in ADJACENT_DIRECTION_DELTAS:
            next_x = current_x + delta_x
            next_y = current_y + delta_y
            
            if (next_x, next_y) == target_coordinate:
                return current_distance + 1
            if not visited_grid[next_y][next_x] and map_matrix[next_y][next_x] != "x":
                visited_grid[next_y][next_x] = True
                heappush(priority_queue, (current_distance + 1, (next_x, next_y)))
    else:
        return -1

def generate_hash_from_positions(remaining_positions_set):
    hash_value = 0
    for index in remaining_positions_set:
        hash_value += 10 ** index
    return hash_value

def compute_minimum_total_distance(current_index, unvisited_indices_set, adjacency_distance_edges, memoization_cache):
    if not unvisited_indices_set:
        return 0

    hashed_state = generate_hash_from_positions(unvisited_indices_set)
    if hashed_state in memoization_cache[current_index]:
        return memoization_cache[current_index][hashed_state]

    minimum_total_distance = INFINITY_DISTANCE
    for edge_distance, neighbor_index in adjacency_distance_edges[current_index]:
        if neighbor_index in unvisited_indices_set:
            total_distance = edge_distance + compute_minimum_total_distance(
                neighbor_index,
                unvisited_indices_set - {neighbor_index},
                adjacency_distance_edges,
                memoization_cache
            )
            if total_distance < minimum_total_distance:
                minimum_total_distance = total_distance
    memoization_cache[current_index][hashed_state] = minimum_total_distance
    return minimum_total_distance

def main():
    while True:
        map_width, map_height = map(int, input().split())
        if map_width == 0:
            break

        # Read and pad the map to simplify boundary checks
        padded_map_rows = ["x" + input() + "x" for _ in range(map_height)]
        horizontal_border = "x" * (map_width + 2)
        map_with_borders = [horizontal_border] + padded_map_rows + [horizontal_border]

        stain_coordinates_list = []
        for y in range(1, map_height + 1):
            for x in range(1, map_width + 1):
                if map_with_borders[y][x] == "*":
                    stain_coordinates_list.append((x, y))
                elif map_with_borders[y][x] == "o":
                    robot_start_index = len(stain_coordinates_list)
                    stain_coordinates_list.append((x, y))

        total_special_positions = len(stain_coordinates_list)
        adjacency_list_of_edges = [[] for _ in range(total_special_positions)]
        path_impossible_due_to_obstacle = False

        for from_index in range(total_special_positions):
            for to_index in range(from_index + 1, total_special_positions):
                from_position = stain_coordinates_list[from_index]
                to_position = stain_coordinates_list[to_index]
                distance_between_positions = calculate_shortest_path_distance(from_position, to_position, map_with_borders)
                if distance_between_positions == -1:
                    path_impossible_due_to_obstacle = True
                adjacency_list_of_edges[from_index].append((distance_between_positions, to_index))
                adjacency_list_of_edges[to_index].append((distance_between_positions, from_index))

        if path_impossible_due_to_obstacle:
            print(-1)
            continue

        memoization_cache = [{} for _ in range(total_special_positions)]
        indices_of_stains_to_clean = {i for i in range(total_special_positions) if i != robot_start_index}
        print(compute_minimum_total_distance(robot_start_index, indices_of_stains_to_clean, adjacency_list_of_edges, memoization_cache))

main()