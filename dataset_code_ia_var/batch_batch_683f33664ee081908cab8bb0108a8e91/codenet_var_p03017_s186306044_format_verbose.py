import re

number_of_cells, starting_position_A, starting_position_B, target_position_C, target_position_D = map(int, input().split())

track_state_string = input()

# Indices correction: converting to 0-based index as Python strings use 0-based indexing
# starting_position_A, starting_position_B, target_position_C, target_position_D = map(lambda x: x - 1, [a, b, c, d])

# Check if a blocked cell ('##') exists between the current position and the farthest target
maximum_target_position = max(target_position_B, target_position_D)
blocked_path_pattern = r'##'
substring_to_check_blockages = track_state_string[starting_position_A - 1 : maximum_target_position]

if re.search(blocked_path_pattern, substring_to_check_blockages):
    print('No')
else:
    if target_position_C > target_position_D:
        # In case overtaking is needed, check for at least 3 consecutive free cells ('...')
        overtaking_position_start = starting_position_B - 2
        overtaking_position_end = target_position_D + 1
        overtaking_pattern = r'\.{3,}'
        substring_to_check_overtaking = track_state_string[overtaking_position_start : overtaking_position_end]
        if re.search(overtaking_pattern, substring_to_check_overtaking):
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')