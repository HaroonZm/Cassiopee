def is_between(val_start, val_end, val_check):
    range_max = max(val_start, val_end)
    range_min = min(val_start, val_end)
    return range_min <= val_check <= range_max

while True:
    current_position = [10, 10]
    collection_result = 'No'
    total_jewel_count = int(input())
    if total_jewel_count == 0:
        break
    jewel_coordinate_list = []
    for jewel_index in range(total_jewel_count):
        jewel_coordinates = list(map(int, input().split()))
        jewel_coordinate_list.append(jewel_coordinates)

    instruction_count = int(input())
    for instruction_index in range(instruction_count):
        instruction_input = input().split()
        if collection_result == 'Yes':
            continue
        instruction_direction = instruction_input[0]
        instruction_distance = int(instruction_input[1])

        if instruction_direction == 'E':
            move_axis, move_delta = 'x', instruction_distance
        elif instruction_direction == 'W':
            move_axis, move_delta = 'x', -instruction_distance
        elif instruction_direction == 'N':
            move_axis, move_delta = 'y', instruction_distance
        elif instruction_direction == 'S':
            move_axis, move_delta = 'y', -instruction_distance
        else:
            raise NotImplementedError

        jewels_to_collect = []
        for jewel_position in jewel_coordinate_list:
            if (
                move_axis == 'x' and
                current_position[1] == jewel_position[1] and
                is_between(0, move_delta, jewel_position[0] - current_position[0])
            ) or (
                move_axis == 'y' and
                current_position[0] == jewel_position[0] and
                is_between(0, move_delta, jewel_position[1] - current_position[1])
            ):
                jewels_to_collect.append(jewel_position)

        for collected_jewel in jewels_to_collect:
            jewel_coordinate_list.remove(collected_jewel)

        if move_axis == 'x':
            current_position[0] += move_delta
        elif move_axis == 'y':
            current_position[1] += move_delta

        if not jewel_coordinate_list:
            collection_result = 'Yes'
    print(collection_result)