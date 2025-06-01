def load_icicles():
    icicle_heights = []
    first_line = input().strip().split(" ")
    count_icicles, length_limit = int(first_line[0]), int(first_line[1])
    while len(icicle_heights) < count_icicles:
        icicle_heights.append(int(input().strip()))
    return icicle_heights, count_icicles, length_limit

def calculate_differences(icicle_heights, count_icicles):
    difference_indicators = [0] * count_icicles
    for index in range(count_icicles):
        diff_right = icicle_heights[index + 1] - icicle_heights[index] if index != count_icicles - 1 else -icicle_heights[index]
        diff_left = icicle_heights[index] - icicle_heights[index - 1] if index != 0 else icicle_heights[index]
        diff_right = 1 if diff_right > 0 else -1
        diff_left = 1 if diff_left > 0 else -1
        if diff_right - diff_left < 0:
            difference_indicators[index] = -1
        elif diff_right - diff_left > 0:
            difference_indicators[index] = 1
        else:
            difference_indicators[index] = 0
    return difference_indicators

icicle_heights, count_icicles, length_limit = load_icicles()
difference_indicators = calculate_differences(icicle_heights, count_icicles)

times_until_fall = [-1] * count_icicles
local_min_indices = [idx for idx in range(count_icicles) if difference_indicators[idx] == -1]

for local_min_index in local_min_indices:
    times_until_fall[local_min_index] = length_limit - icicle_heights[local_min_index]
    left_boundary_reached, right_boundary_reached = False, False
    left_position, right_position = local_min_index, local_min_index

    while not (left_boundary_reached and right_boundary_reached):
        left_position -= 1
        if left_position < 0:
            left_boundary_reached = True
        if not left_boundary_reached:
            if times_until_fall[left_position] == -1:
                times_until_fall[left_position] = (length_limit - icicle_heights[left_position]) + times_until_fall[left_position + 1]
            else:
                times_until_fall[left_position] = (length_limit - icicle_heights[left_position]) + max(times_until_fall[left_position - 1], times_until_fall[left_position + 1])
            if difference_indicators[left_position] == 1:
                left_boundary_reached = True

        right_position += 1
        if right_position >= count_icicles:
            right_boundary_reached = True
        if not right_boundary_reached:
            if times_until_fall[right_position] == -1:
                times_until_fall[right_position] = (length_limit - icicle_heights[right_position]) + times_until_fall[right_position - 1]
            else:
                times_until_fall[right_position] = (length_limit - icicle_heights[right_position]) + max(times_until_fall[right_position - 1], times_until_fall[right_position + 1])
            if difference_indicators[right_position] == 1:
                right_boundary_reached = True

print(max(times_until_fall))