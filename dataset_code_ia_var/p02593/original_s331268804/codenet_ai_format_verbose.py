import os
import sys
import numpy as np

def solve(input_array):
    number_of_rooks = input_array[0]
    rook_x_coordinates = input_array[1::2]
    rook_y_coordinates = input_array[2::2]

    sorted_x_indices = np.argsort(rook_x_coordinates)
    sorted_y_indices = np.argsort(rook_y_coordinates)

    rook_index_in_sorted_x = np.argsort(sorted_x_indices)
    rook_index_in_sorted_y = np.argsort(sorted_y_indices)

    def get_coordinates_by_sorted_x_index(sorted_x_index):
        rook_original_index = sorted_x_indices[sorted_x_index]
        return rook_x_coordinates[rook_original_index], rook_y_coordinates[rook_original_index]

    def calculate_capture_times(
        leftmost_x, leftmost_y, rightmost_x, rightmost_y,
        leftmost_time, leftmost_right_time, rightmost_left_time, rightmost_time,
        leftmost_previous_sorted_x_index, rightmost_next_sorted_x_index, group_rook_count
    ):
        left_prev_x, left_prev_y = get_coordinates_by_sorted_x_index(leftmost_previous_sorted_x_index)
        right_next_x, right_next_y = get_coordinates_by_sorted_x_index(rightmost_next_sorted_x_index)

        diagonal_moves_required = (
            abs(right_next_x - left_prev_x) +
            abs(right_next_y - left_prev_y) -
            group_rook_count
        )

        leftmost_time_through_ll = (
            leftmost_time +
            abs(right_next_x - leftmost_x) +
            abs(right_next_y - leftmost_y) +
            diagonal_moves_required
        )
        leftmost_time_through_lr = (
            leftmost_time +
            abs(leftmost_x - left_prev_x) +
            abs(leftmost_y - left_prev_y) +
            diagonal_moves_required
        )
        leftmost_right_time_through_lr = (
            leftmost_right_time +
            abs(right_next_x - rightmost_x) +
            abs(right_next_y - rightmost_y) +
            diagonal_moves_required
        )
        leftmost_right_time_through_rr = (
            leftmost_right_time +
            abs(rightmost_x - left_prev_x) +
            abs(rightmost_y - left_prev_y) +
            diagonal_moves_required
        )
        rightmost_left_time_through_ll = (
            rightmost_left_time +
            abs(right_next_x - leftmost_x) +
            abs(right_next_y - leftmost_y) +
            diagonal_moves_required
        )
        rightmost_left_time_through_lr = (
            rightmost_left_time +
            abs(leftmost_x - left_prev_x) +
            abs(leftmost_y - left_prev_y) +
            diagonal_moves_required
        )
        rightmost_time_through_rl = (
            rightmost_time +
            abs(right_next_x - rightmost_x) +
            abs(right_next_y - rightmost_y) +
            diagonal_moves_required
        )
        rightmost_time_through_rr = (
            rightmost_time +
            abs(rightmost_x - left_prev_x) +
            abs(rightmost_y - left_prev_y) +
            diagonal_moves_required
        )

        updated_leftmost_time = min(leftmost_time_through_ll, rightmost_left_time_through_ll)
        updated_leftmost_right_time = min(leftmost_time_through_lr, leftmost_right_time_through_rr)
        updated_rightmost_left_time = min(rightmost_left_time_through_lr, rightmost_time_through_rl)
        updated_rightmost_time = min(leftmost_right_time_through_rr, rightmost_time_through_rr)

        return (
            left_prev_x, left_prev_y, right_next_x, right_next_y,
            updated_leftmost_time, updated_leftmost_right_time,
            updated_rightmost_left_time, updated_rightmost_time
        )

    can_reach_next_in_group = np.zeros(number_of_rooks, dtype=np.int8)
    for rook_index in range(number_of_rooks):
        sorted_x_index = rook_index_in_sorted_x[rook_index]
        sorted_y_index = rook_index_in_sorted_y[rook_index]

        previous_x_original_index = -1 if sorted_x_index == 0 else sorted_x_indices[sorted_x_index - 1]
        next_x_original_index = -2 if sorted_x_index == number_of_rooks - 1 else sorted_x_indices[sorted_x_index + 1]
        previous_y_original_index = -3 if sorted_y_index == 0 else sorted_y_indices[sorted_y_index - 1]
        next_y_original_index = -4 if sorted_y_index == number_of_rooks - 1 else sorted_y_indices[sorted_y_index + 1]

        if (
            previous_x_original_index == previous_y_original_index or
            previous_x_original_index == next_y_original_index
        ):
            can_reach_next_in_group[sorted_x_index - 1] = 1
        if (
            next_x_original_index == previous_y_original_index or
            next_x_original_index == next_y_original_index
        ):
            can_reach_next_in_group[sorted_x_index] = 1

    group_leftmost_sorted_x = np.zeros(number_of_rooks, dtype=np.int64)
    group_rightmost_sorted_x = np.zeros(number_of_rooks, dtype=np.int64)

    current_leftmost_index = 0
    for sorted_x_index in range(number_of_rooks - 1):
        if can_reach_next_in_group[sorted_x_index] == 0:
            current_leftmost_index = sorted_x_index + 1
        group_leftmost_sorted_x[sorted_x_index + 1] = current_leftmost_index

    current_rightmost_index = number_of_rooks - 1
    group_rightmost_sorted_x[current_rightmost_index] = current_rightmost_index
    for sorted_x_index in range(number_of_rooks - 2, -1, -1):
        if can_reach_next_in_group[sorted_x_index] == 0:
            current_rightmost_index = sorted_x_index
        group_rightmost_sorted_x[sorted_x_index] = current_rightmost_index

    group_extra_time_from_left = np.zeros(number_of_rooks, dtype=np.int64)
    group_extra_time_from_right = np.zeros(number_of_rooks, dtype=np.int64)
    LARGE_INF = 10 ** 18

    group_start_sorted_x = 0
    while group_start_sorted_x < number_of_rooks:
        group_end_sorted_x = group_rightmost_sorted_x[group_start_sorted_x]

        if group_start_sorted_x == group_end_sorted_x:
            group_start_sorted_x = group_end_sorted_x + 1
            continue

        leftmost_original_index = sorted_x_indices[group_start_sorted_x]
        rightmost_original_index = sorted_x_indices[group_end_sorted_x]

        leftmost_sorted_y = rook_index_in_sorted_y[leftmost_original_index]
        rightmost_sorted_y = rook_index_in_sorted_y[rightmost_original_index]
        min_sorted_y, max_sorted_y = min(leftmost_sorted_y, rightmost_sorted_y), max(leftmost_sorted_y, rightmost_sorted_y)

        group_leftmost_backup = group_start_sorted_x
        leftmost_x, leftmost_y = rook_x_coordinates[leftmost_original_index], rook_y_coordinates[leftmost_original_index]
        rightmost_x, rightmost_y = rook_x_coordinates[rightmost_original_index], rook_y_coordinates[rightmost_original_index]

        leftmost_time = 0
        leftmost_right_time = LARGE_INF
        rightmost_left_time = LARGE_INF
        rightmost_time = 0

        while True:
            prev_x_original_index = -1 if group_start_sorted_x == 0 else sorted_x_indices[group_start_sorted_x - 1]
            prev_y_original_index = -2 if min_sorted_y == 0 else sorted_y_indices[min_sorted_y - 1]
            next_x_original_index = -3 if group_end_sorted_x == number_of_rooks - 1 else sorted_x_indices[group_end_sorted_x + 1]
            next_y_original_index = -4 if max_sorted_y == number_of_rooks - 1 else sorted_y_indices[max_sorted_y + 1]

            if prev_x_original_index == prev_y_original_index:
                leftmost_previous_sorted_x = group_leftmost_sorted_x[group_start_sorted_x - 1]
                rook_count_in_left_segment = group_start_sorted_x - leftmost_previous_sorted_x

                if next_x_original_index == next_y_original_index:
                    rightmost_next_sorted_x = group_rightmost_sorted_x[group_end_sorted_x + 1]
                    rook_count_in_left_segment += rightmost_next_sorted_x - group_end_sorted_x

                    (
                        leftmost_x, leftmost_y,
                        rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time
                    ) = calculate_capture_times(
                        leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time,
                        leftmost_previous_sorted_x, rightmost_next_sorted_x, rook_count_in_left_segment
                    )

                    group_start_sorted_x = leftmost_previous_sorted_x
                    group_end_sorted_x = rightmost_next_sorted_x
                    sorted_y_leftmost = rook_index_in_sorted_y[sorted_x_indices[group_start_sorted_x]]
                    sorted_y_rightmost = rook_index_in_sorted_y[sorted_x_indices[group_end_sorted_x]]
                    min_sorted_y, max_sorted_y = min(min_sorted_y, max_sorted_y, sorted_y_leftmost, sorted_y_rightmost), max(min_sorted_y, max_sorted_y, sorted_y_leftmost, sorted_y_rightmost)
                else:
                    (
                        leftmost_x, leftmost_y,
                        rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time
                    ) = calculate_capture_times(
                        leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time,
                        leftmost_previous_sorted_x, leftmost_previous_sorted_x, rook_count_in_left_segment
                    )

                    group_start_sorted_x = leftmost_previous_sorted_x
                    sorted_y_leftmost = rook_index_in_sorted_y[sorted_x_indices[group_start_sorted_x]]
                    min_sorted_y, max_sorted_y = min(min_sorted_y, max_sorted_y, sorted_y_leftmost), max(min_sorted_y, max_sorted_y, sorted_y_leftmost)

            elif prev_x_original_index == next_y_original_index:
                leftmost_previous_sorted_x = group_leftmost_sorted_x[group_start_sorted_x - 1]
                rook_count_in_left_segment = group_start_sorted_x - leftmost_previous_sorted_x

                if next_x_original_index == prev_y_original_index:
                    rightmost_next_sorted_x = group_rightmost_sorted_x[group_end_sorted_x + 1]
                    rook_count_in_left_segment += rightmost_next_sorted_x - group_end_sorted_x

                    (
                        leftmost_x, leftmost_y,
                        rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time
                    ) = calculate_capture_times(
                        leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time,
                        leftmost_previous_sorted_x, rightmost_next_sorted_x, rook_count_in_left_segment
                    )

                    group_start_sorted_x = leftmost_previous_sorted_x
                    group_end_sorted_x = rightmost_next_sorted_x
                    sorted_y_leftmost = rook_index_in_sorted_y[sorted_x_indices[group_start_sorted_x]]
                    sorted_y_rightmost = rook_index_in_sorted_y[sorted_x_indices[group_end_sorted_x]]
                    min_sorted_y, max_sorted_y = min(min_sorted_y, max_sorted_y, sorted_y_leftmost, sorted_y_rightmost), max(min_sorted_y, max_sorted_y, sorted_y_leftmost, sorted_y_rightmost)
                else:
                    (
                        leftmost_x, leftmost_y,
                        rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time
                    ) = calculate_capture_times(
                        leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                        leftmost_time, leftmost_right_time,
                        rightmost_left_time, rightmost_time,
                        leftmost_previous_sorted_x, leftmost_previous_sorted_x, rook_count_in_left_segment
                    )

                    group_start_sorted_x = leftmost_previous_sorted_x
                    sorted_y_leftmost = rook_index_in_sorted_y[sorted_x_indices[group_start_sorted_x]]
                    min_sorted_y, max_sorted_y = min(min_sorted_y, max_sorted_y, sorted_y_leftmost), max(min_sorted_y, max_sorted_y, sorted_y_leftmost)

            elif next_x_original_index == next_y_original_index or next_x_original_index == prev_y_original_index:
                rightmost_next_sorted_x = group_rightmost_sorted_x[group_end_sorted_x + 1]
                rook_count_in_right_segment = rightmost_next_sorted_x - group_end_sorted_x

                (
                    leftmost_x, leftmost_y,
                    rightmost_x, rightmost_y,
                    leftmost_time, leftmost_right_time,
                    rightmost_left_time, rightmost_time
                ) = calculate_capture_times(
                    leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                    leftmost_time, leftmost_right_time,
                    rightmost_left_time, rightmost_time,
                    rightmost_next_sorted_x, rightmost_next_sorted_x, rook_count_in_right_segment
                )

                group_end_sorted_x = rightmost_next_sorted_x
                sorted_y_rightmost = rook_index_in_sorted_y[sorted_x_indices[group_end_sorted_x]]
                min_sorted_y, max_sorted_y = min(min_sorted_y, max_sorted_y, sorted_y_rightmost), max(min_sorted_y, max_sorted_y, sorted_y_rightmost)

            else:
                group_extra_time_from_left[group_leftmost_backup] = min(leftmost_time, leftmost_right_time)
                group_extra_time_from_right[group_leftmost_backup] = min(rightmost_left_time, rightmost_time)
                break

        group_start_sorted_x = group_end_sorted_x + 1

    answer_array = np.zeros(number_of_rooks, dtype=np.int64)
    for rook_index in range(number_of_rooks):
        sorted_x_index = rook_index_in_sorted_x[rook_index]
        rook_x = rook_x_coordinates[rook_index]
        rook_y = rook_y_coordinates[rook_index]
        group_leftmost_index = group_leftmost_sorted_x[sorted_x_index]
        leftmost_x = rook_x_coordinates[sorted_x_indices[group_leftmost_index]]
        leftmost_y = rook_y_coordinates[sorted_x_indices[group_leftmost_index]]
        group_rightmost_index = group_rightmost_sorted_x[sorted_x_index]
        rightmost_x = rook_x_coordinates[sorted_x_indices[group_rightmost_index]]
        rightmost_y = rook_y_coordinates[sorted_x_indices[group_rightmost_index]]
        group_left_time = group_extra_time_from_left[group_leftmost_index]
        group_right_time = group_extra_time_from_right[group_leftmost_index]
        diagonal_distance = abs(rightmost_x - leftmost_x) + abs(rightmost_y - leftmost_y) - (group_rightmost_index - group_leftmost_index)
        rightmost_left_time = abs(rightmost_x - rook_x) + abs(rightmost_y - rook_y) + diagonal_distance
        leftmost_right_time = abs(rook_x - leftmost_x) + abs(rook_y - leftmost_y) + diagonal_distance
        answer_array[rook_index] = min(group_left_time + rightmost_left_time, group_right_time + leftmost_right_time)

    return answer_array

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
    exit()

if os.name == 'posix':
    from my_module import solve
else:
    from numba import njit
    solve = njit('(i8[:],)', cache=True)(solve)
    print('compiled', file=sys.stderr)

input_array = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
result_array = solve(input_array)
print('\n'.join(map(str, result_array)))