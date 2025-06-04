import sys
from heapq import heappush, heappop

sys.setrecursionlimit(100000)

INFINITY_DISTANCE = 10 ** 10

DIRECTION_OFFSETS = ((0, -1), (0, 1), (-1, 0), (1, 0))

def compute_minimum_distance_between_points(start_coordinates, target_coordinates, map_grid):
    priority_queue = []
    heappush(priority_queue, (0, start_coordinates))
    visited_cells = [
        [False] * len(map_grid[0]) 
        for _ in range(len(map_grid))
    ]
    visited_cells[start_coordinates[1]][start_coordinates[0]] = True

    while priority_queue:
        current_distance, current_point = heappop(priority_queue)
        current_x, current_y = current_point

        for direction_x, direction_y in DIRECTION_OFFSETS:
            next_x = current_x + direction_x
            next_y = current_y + direction_y

            if (next_x, next_y) == target_coordinates:
                return current_distance + 1

            if (
                not visited_cells[next_y][next_x] and 
                map_grid[next_y][next_x] != "x"
            ):
                visited_cells[next_y][next_x] = True
                heappush(priority_queue, (current_distance + 1, (next_x, next_y)))
    else:
        return -1

def encode_remaining_stains(remaining_stain_indices):
    return sum([10 ** index for index in remaining_stain_indices])

def compute_shortest_cleaning_path(
    current_stain_index, 
    remaining_stain_indices, 
    adjacency_list, 
    memoization_table
):
    if remaining_stain_indices == set():
        return 0

    encoded_remaining = encode_remaining_stains(remaining_stain_indices)
    if encoded_remaining in memoization_table[current_stain_index]:
        return memoization_table[current_stain_index][encoded_remaining]

    minimal_total_distance = INFINITY_DISTANCE

    for edge_distance, next_stain_index in adjacency_list[current_stain_index]:
        if next_stain_index in remaining_stain_indices:
            total_distance = (
                edge_distance + 
                compute_shortest_cleaning_path(
                    next_stain_index, 
                    remaining_stain_indices - {next_stain_index}, 
                    adjacency_list, 
                    memoization_table
                )
            )
            if total_distance < minimal_total_distance:
                minimal_total_distance = total_distance

    memoization_table[current_stain_index][encoded_remaining] = minimal_total_distance
    return minimal_total_distance

def main():
    while True:
        room_width, room_height = map(int, input().split())
        if room_width == 0:
            break

        room_map_grid = [
            "x" + input() + "x" 
            for _ in range(room_height)
        ]
        room_map_grid.insert(0, "x" * (room_width + 2))
        room_map_grid.append("x" * (room_width + 2))

        stain_positions = []
        robot_start_index = None

        for y in range(1, room_height + 1):
            for x in range(1, room_width + 1):
                if room_map_grid[y][x] == "*":
                    stain_positions.append((x, y))
                elif room_map_grid[y][x] == "o":
                    robot_start_index = len(stain_positions)
                    stain_positions.append((x, y))

        total_stains = len(stain_positions)

        adjacency_list = [[] for _ in range(total_stains)]
        distances_between_stains = [
            [None] * total_stains 
            for _ in range(total_stains)
        ]
        for i in range(total_stains):
            distances_between_stains[i][i] = 0

        stain_unreachable_flag = False

        for i in range(total_stains):
            for j in range(i + 1, total_stains):
                from_stain = stain_positions[i]
                to_stain = stain_positions[j]
                distance = compute_minimum_distance_between_points(from_stain, to_stain, room_map_grid)
                if distance == -1:
                    stain_unreachable_flag = True
                adjacency_list[i].append((distance, j))
                adjacency_list[j].append((distance, i))
                distances_between_stains[i][j] = distance
                distances_between_stains[j][i] = distance

        if stain_unreachable_flag:
            print(-1)
            continue

        memoization_table = [{} for _ in range(10)]
        remaining_stain_indices = {i for i in range(total_stains) if i != robot_start_index}
        print(
            compute_shortest_cleaning_path(
                robot_start_index, 
                remaining_stain_indices, 
                adjacency_list, 
                memoization_table
            )
        )

main()