import os
import sys

import numpy as np

def solve(input_array):
    number_of_rooks = input_array[0]
    rook_x_coordinates = input_array[1::2]
    rook_y_coordinates = input_array[2::2]

    x_coordinate_sorted_indices = np.argsort(rook_x_coordinates)
    y_coordinate_sorted_indices = np.argsort(rook_y_coordinates)

    x_coordinate_sort_order = np.argsort(x_coordinate_sorted_indices)
    y_coordinate_sort_order = np.argsort(y_coordinate_sorted_indices)

    def get_coordinates_by_sorted_x_index(sorted_x_index):
        original_index = x_coordinate_sorted_indices[sorted_x_index]
        return rook_x_coordinates[original_index], rook_y_coordinates[original_index]

    def calculate_time(
        left_x, left_y, right_x, right_y,
        left_left_time, left_right_time, right_left_time, right_right_time,
        left_previous_x_index, right_next_x_index, rook_count_between
    ):
        left_prev_x, left_prev_y = get_coordinates_by_sorted_x_index(left_previous_x_index)
        right_next_x, right_next_y = get_coordinates_by_sorted_x_index(right_next_x_index)

        diagonal_movement_time = (
            abs(right_next_x - left_prev_x) + abs(right_next_y - left_prev_y) - rook_count_between
        )

        # Transition costs for all possible start/ends after absorbing another group
        left_left_left_time  = left_left_time  + abs(right_next_x - left_x)   + abs(right_next_y - left_y)  + diagonal_movement_time
        left_left_right_time = left_left_time  + abs(left_x - left_prev_x)    + abs(left_y - left_prev_y)   + diagonal_movement_time
        left_right_left_time = left_right_time + abs(right_next_x - right_x)  + abs(right_next_y - right_y) + diagonal_movement_time
        left_right_right_time= left_right_time + abs(right_x - left_prev_x)   + abs(right_y - left_prev_y)  + diagonal_movement_time

        right_left_left_time = right_left_time + abs(right_next_x - left_x)   + abs(right_next_y - left_y)  + diagonal_movement_time
        right_left_right_time= right_left_time + abs(left_x - left_prev_x)    + abs(left_y - left_prev_y)   + diagonal_movement_time
        right_right_left_time= right_right_time+ abs(right_next_x - right_x)  + abs(right_next_y - right_y) + diagonal_movement_time
        right_right_right_time=right_right_time+ abs(right_x - left_prev_x)   + abs( right_y - left_prev_y) + diagonal_movement_time

        new_left_left_time    = min(left_left_left_time, left_right_left_time)
        new_left_right_time   = min(left_left_right_time, left_right_right_time)
        new_right_left_time   = min(right_left_left_time, right_right_left_time)
        new_right_right_time  = min(right_left_right_time, right_right_right_time)

        return (left_prev_x, left_prev_y, right_next_x, right_next_y,
                new_left_left_time, new_left_right_time, new_right_left_time, new_right_right_time)

    is_rook_freely_reachable = np.zeros(number_of_rooks, dtype=np.int8)

    for rook_input_order in range(number_of_rooks):
        sorted_x_order = x_coordinate_sort_order[rook_input_order]
        sorted_y_order = y_coordinate_sort_order[rook_input_order]

        previous_x_input_order = -1  if sorted_x_order == 0              else x_coordinate_sorted_indices[sorted_x_order - 1]
        next_x_input_order     = -2  if sorted_x_order == number_of_rooks-1 else x_coordinate_sorted_indices[sorted_x_order + 1]
        previous_y_input_order = -3  if sorted_y_order == 0              else y_coordinate_sorted_indices[sorted_y_order - 1]
        next_y_input_order     = -4  if sorted_y_order == number_of_rooks-1 else y_coordinate_sorted_indices[sorted_y_order + 1]

        if previous_x_input_order == previous_y_input_order or previous_x_input_order == next_y_input_order:
            is_rook_freely_reachable[sorted_x_order - 1] = 1
        if next_x_input_order == previous_y_input_order or next_x_input_order == next_y_input_order:
            is_rook_freely_reachable[sorted_x_order] = 1

    leftmost_free_x_index = np.zeros(number_of_rooks, dtype=np.int64)
    rightmost_free_x_index = np.zeros(number_of_rooks, dtype=np.int64)

    contiguous_group_left_border = 0
    for sorted_x_index in range(number_of_rooks - 1):
        if is_rook_freely_reachable[sorted_x_index] == 0:
            contiguous_group_left_border = sorted_x_index + 1
        leftmost_free_x_index[sorted_x_index + 1] = contiguous_group_left_border

    contiguous_group_right_border = number_of_rooks - 1
    rightmost_free_x_index[contiguous_group_right_border] = contiguous_group_right_border
    for sorted_x_index in range(number_of_rooks - 2, -1, -1):
        if is_rook_freely_reachable[sorted_x_index] == 0:
            contiguous_group_right_border = sorted_x_index
        rightmost_free_x_index[sorted_x_index] = contiguous_group_right_border

    time_to_collect_all_but_one_start_left = np.zeros(number_of_rooks, dtype=np.int64)
    time_to_collect_all_but_one_start_right = np.zeros(number_of_rooks, dtype=np.int64)

    LARGE_INF = 10 ** 18
    current_group_left_index = 0

    while current_group_left_index < number_of_rooks:
        current_group_right_index = rightmost_free_x_index[current_group_left_index]

        # Group of a single rook, skip
        if current_group_left_index == current_group_right_index:
            current_group_left_index = current_group_right_index + 1
            continue

        leftmost_input_order = x_coordinate_sorted_indices[current_group_left_index]
        rightmost_input_order = x_coordinate_sorted_indices[current_group_right_index]

        leftmost_y_order = y_coordinate_sort_order[leftmost_input_order]
        rightmost_y_order = y_coordinate_sort_order[rightmost_input_order]

        minimal_group_y_order = min(leftmost_y_order, rightmost_y_order)
        maximal_group_y_order = max(leftmost_y_order, rightmost_y_order)

        original_group_left_x_index = current_group_left_index

        leftmost_x = rook_x_coordinates[leftmost_input_order]
        leftmost_y = rook_y_coordinates[leftmost_input_order]
        rightmost_x = rook_x_coordinates[rightmost_input_order]
        rightmost_y = rook_y_coordinates[rightmost_input_order]

        left_left_time  = 0
        left_right_time = LARGE_INF
        right_left_time = LARGE_INF
        right_right_time = 0

        while True:
            previous_x_input_order = -1 if current_group_left_index == 0 else x_coordinate_sorted_indices[current_group_left_index - 1]
            previous_y_input_order = -2 if minimal_group_y_order == 0 else y_coordinate_sorted_indices[minimal_group_y_order - 1]
            next_x_input_order = -3 if current_group_right_index == number_of_rooks - 1 else x_coordinate_sorted_indices[current_group_right_index + 1]
            next_y_input_order = -4 if maximal_group_y_order == number_of_rooks - 1 else y_coordinate_sorted_indices[maximal_group_y_order + 1]

            if previous_x_input_order == previous_y_input_order:
                left_previous_x_index = leftmost_free_x_index[current_group_left_index - 1]
                rook_count = current_group_left_index - left_previous_x_index

                if next_x_input_order == next_y_input_order:
                    right_next_x_index = rightmost_free_x_index[current_group_right_index + 1]
                    rook_count += right_next_x_index - current_group_right_index

                    (leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                     left_left_time, left_right_time, right_left_time, right_right_time) = \
                        calculate_time(
                            leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                            left_left_time, left_right_time, right_left_time, right_right_time,
                            left_previous_x_index, right_next_x_index, rook_count
                        )
                    current_group_left_index = left_previous_x_index
                    current_group_right_index = right_next_x_index
                    uy_order = y_coordinate_sort_order[x_coordinate_sorted_indices[current_group_left_index]]
                    vy_order = y_coordinate_sort_order[x_coordinate_sorted_indices[current_group_right_index]]
                    minimal_group_y_order = min(minimal_group_y_order, maximal_group_y_order, uy_order, vy_order)
                    maximal_group_y_order = max(minimal_group_y_order, maximal_group_y_order, uy_order, vy_order)
                else:
                    (leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                     left_left_time, left_right_time, right_left_time, right_right_time) = \
                        calculate_time(
                            leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                            left_left_time, left_right_time, right_left_time, right_right_time,
                            left_previous_x_index, left_previous_x_index, rook_count
                        )
                    current_group_left_index = left_previous_x_index
                    uy_order = y_coordinate_sort_order[x_coordinate_sorted_indices[current_group_left_index]]
                    minimal_group_y_order = min(minimal_group_y_order, maximal_group_y_order, uy_order)
                    maximal_group_y_order = max(minimal_group_y_order, maximal_group_y_order, uy_order)

            elif previous_x_input_order == next_y_input_order:
                left_previous_x_index = leftmost_free_x_index[current_group_left_index - 1]
                rook_count = current_group_left_index - left_previous_x_index

                if next_x_input_order == previous_y_input_order:
                    right_next_x_index = rightmost_free_x_index[current_group_right_index + 1]
                    rook_count += right_next_x_index - current_group_right_index
                    (leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                     left_left_time, left_right_time, right_left_time, right_right_time) = \
                        calculate_time(
                            leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                            left_left_time, left_right_time, right_left_time, right_right_time,
                            left_previous_x_index, right_next_x_index, rook_count
                        )
                    current_group_left_index = left_previous_x_index
                    current_group_right_index = right_next_x_index
                    uy_order = y_coordinate_sort_order[x_coordinate_sorted_indices[current_group_left_index]]
                    vy_order = y_coordinate_sort_order[x_coordinate_sorted_indices[current_group_right_index]]
                    minimal_group_y_order = min(minimal_group_y_order, maximal_group_y_order, uy_order, vy_order)
                    maximal_group_y_order = max(minimal_group_y_order, maximal_group_y_order, uy_order, vy_order)
                else:
                    (leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                     left_left_time, left_right_time, right_left_time, right_right_time) = \
                        calculate_time(
                            leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                            left_left_time, left_right_time, right_left_time, right_right_time,
                            left_previous_x_index, left_previous_x_index, rook_count
                        )
                    current_group_left_index = left_previous_x_index
                    uy_order = y_coordinate_sort_order[x_coordinate_sorted_indices[current_group_left_index]]
                    minimal_group_y_order = min(minimal_group_y_order, maximal_group_y_order, uy_order)
                    maximal_group_y_order = max(minimal_group_y_order, maximal_group_y_order, uy_order)

            elif next_x_input_order == next_y_input_order or next_x_input_order == previous_y_input_order:
                right_next_x_index = rightmost_free_x_index[current_group_right_index + 1]
                rook_count = right_next_x_index - current_group_right_index
                (leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                 left_left_time, left_right_time, right_left_time, right_right_time) = \
                    calculate_time(
                        leftmost_x, leftmost_y, rightmost_x, rightmost_y,
                        left_left_time, left_right_time, right_left_time, right_right_time,
                        right_next_x_index, right_next_x_index, rook_count
                    )
                current_group_right_index = right_next_x_index
                vy_order = y_coordinate_sort_order[x_coordinate_sorted_indices[current_group_right_index]]
                minimal_group_y_order = min(minimal_group_y_order, maximal_group_y_order, vy_order)
                maximal_group_y_order = max(minimal_group_y_order, maximal_group_y_order, vy_order)

            else:
                time_to_collect_all_but_one_start_left[original_group_left_x_index] = min(left_left_time, left_right_time)
                time_to_collect_all_but_one_start_right[original_group_left_x_index] = min(right_left_time, right_right_time)
                break

        current_group_left_index = current_group_right_index + 1

    minimum_time_to_collect_all_rooks = np.zeros(number_of_rooks, dtype=np.int64)
    for rook_input_order in range(number_of_rooks):
        sorted_x_order = x_coordinate_sort_order[rook_input_order]
        x = rook_x_coordinates[rook_input_order]
        y = rook_y_coordinates[rook_input_order]

        group_left_x_index = leftmost_free_x_index[sorted_x_order]
        group_left_x = rook_x_coordinates[x_coordinate_sorted_indices[group_left_x_index]]
        group_left_y = rook_y_coordinates[x_coordinate_sorted_indices[group_left_x_index]]

        group_right_x_index = rightmost_free_x_index[sorted_x_order]
        group_right_x = rook_x_coordinates[x_coordinate_sorted_indices[group_right_x_index]]
        group_right_y = rook_y_coordinates[x_coordinate_sorted_indices[group_right_x_index]]

        left_in_group_time = time_to_collect_all_but_one_start_left[group_left_x_index]
        right_in_group_time = time_to_collect_all_but_one_start_right[group_left_x_index]
        diagonal_time_in_group = (
            abs(group_right_x - group_left_x) + abs(group_right_y - group_left_y) - (group_right_x_index - group_left_x_index)
        )
        right_to_input_time = abs(group_right_x - x) + abs(group_right_y - y) + diagonal_time_in_group
        left_to_input_time = abs(x - group_left_x) + abs(y - group_left_y) + diagonal_time_in_group
        minimum_time_to_collect_all_rooks[rook_input_order] = min(
            left_in_group_time + right_to_input_time, right_in_group_time + left_to_input_time
        )

    return minimum_time_to_collect_all_rooks

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    compiling_numba_cc = CC('my_module')
    compiling_numba_cc.export('solve', '(i8[:],)')(solve)
    compiling_numba_cc.compile()
    exit()

if os.name == 'posix':
    from my_module import solve
else:
    from numba import njit
    solve = njit('(i8[:],)', cache=True)(solve)
    print('compiled', file=sys.stderr)

input_array = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
minimum_time_array = solve(input_array)
print('\n'.join(map(str, minimum_time_array)))