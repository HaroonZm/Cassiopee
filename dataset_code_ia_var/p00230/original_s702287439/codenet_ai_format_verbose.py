from collections import deque

def adjust_floor_level(
    building_a_floors_list, 
    building_b_floors_list, 
    current_floor, 
    current_building, 
    total_number_of_floors
):
    if current_building == 0:
        building_floors_status_list = building_a_floors_list
    else:
        building_floors_status_list = building_b_floors_list

    if building_floors_status_list[current_floor] == 0:
        return current_floor

    if building_floors_status_list[current_floor] == 1:
        while (
            current_floor + 1 < total_number_of_floors and 
            building_floors_status_list[current_floor + 1] == 1
        ):
            current_floor += 1
        return current_floor

    if building_floors_status_list[current_floor] == 2:
        while (
            current_floor >= 0 and 
            building_floors_status_list[current_floor] == 2
        ):
            current_floor -= 1
        return current_floor

def find_minimum_moves_to_top_floor(
    building_a_floors_status, 
    building_b_floors_status, 
    total_number_of_floors
):
    bfs_queue = deque()

    initial_floor_in_building_a = adjust_floor_level(
        building_a_floors_status, 
        building_b_floors_status, 
        0, 
        0, 
        total_number_of_floors
    )
    initial_floor_in_building_b = adjust_floor_level(
        building_a_floors_status, 
        building_b_floors_status, 
        0, 
        1, 
        total_number_of_floors
    )

    target_top_floor_index = total_number_of_floors - 1

    if target_top_floor_index in (initial_floor_in_building_a, initial_floor_in_building_b):
        print(0)
        return

    bfs_queue.append((0, initial_floor_in_building_a, 0))
    bfs_queue.append((0, initial_floor_in_building_b, 1))

    visited_states_to_minimum_moves = {}
    visited_states_to_minimum_moves[(initial_floor_in_building_a, 0)] = 0
    visited_states_to_minimum_moves[(initial_floor_in_building_b, 1)] = 0

    while bfs_queue:
        current_moves_count, current_floor_index, current_building_index = bfs_queue.popleft()
        next_building_index = (current_building_index + 1) % 2

        for number_of_floors_to_move_up in range(3):
            intended_next_floor = current_floor_index + number_of_floors_to_move_up
            if intended_next_floor >= total_number_of_floors:
                break

            adjusted_next_floor = adjust_floor_level(
                building_a_floors_status, 
                building_b_floors_status,
                intended_next_floor, 
                next_building_index, 
                total_number_of_floors
            )

            if adjusted_next_floor == target_top_floor_index:
                print(current_moves_count + 1)
                return

            if (adjusted_next_floor, next_building_index) not in visited_states_to_minimum_moves:
                visited_states_to_minimum_moves[
                    (adjusted_next_floor, next_building_index)
                ] = current_moves_count + 1
                bfs_queue.append(
                    (current_moves_count + 1, adjusted_next_floor, next_building_index)
                )
    print("NA")

while True:
    total_number_of_floors = int(input())
    if total_number_of_floors == 0:
        break

    building_a_floors_status = list(map(int, input().split()))
    building_b_floors_status = list(map(int, input().split()))

    find_minimum_moves_to_top_floor(
        building_a_floors_status, 
        building_b_floors_status, 
        total_number_of_floors
    )