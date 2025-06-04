def check_for_consecutive_rocks(segment_start_index, segment_end_index):
    for current_position in range(segment_start_index, segment_end_index):
        if path_with_boundaries[current_position] == '#' and path_with_boundaries[current_position + 1] == '#':
            return False
    return True

number_of_cells, starting_position_a, starting_position_b, destination_position_c, destination_position_d = map(int, input().split())

original_path = list(input())

# We add boundaries to simplify index checks at the borders
path_with_boundaries = ['#'] + original_path + ['#']

# Check if there are consecutive rocks blocking either path (blocking progress)
if not check_for_consecutive_rocks(starting_position_a, destination_position_c) or not check_for_consecutive_rocks(starting_position_b, destination_position_d):
    print('No')
    exit()

# If overtaking is needed (person B needs to overtake person A)
if destination_position_c > destination_position_d:
    overtaking_possible = False
    for position in range(starting_position_b, destination_position_d + 1):
        if path_with_boundaries[position - 1] == '.' and path_with_boundaries[position] == '.' and path_with_boundaries[position + 1] == '.':
            overtaking_possible = True
            break
    if not overtaking_possible:
        print('No')
        exit()

# If all checks pass, print 'Yes'
print('Yes')