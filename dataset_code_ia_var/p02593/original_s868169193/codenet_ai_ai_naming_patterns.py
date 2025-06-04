import os
import sys
import numpy as np

def process_problem(input_array):
    rook_count = input_array[0]
    coordinate_x = input_array[1::2]
    coordinate_y = input_array[2::2]
    coordinate_x_sort_indices = np.argsort(coordinate_x)
    coordinate_y_sort_indices = np.argsort(coordinate_y)
    coordinate_x_rank = np.argsort(coordinate_x_sort_indices)
    coordinate_y_rank = np.argsort(coordinate_y_sort_indices)

    def get_position_by_x_order(x_order):
        rook_idx = coordinate_x_sort_indices[x_order]
        return coordinate_x[rook_idx], coordinate_y[rook_idx]

    def compute_transition(lx, ly, rx, ry, llt, lrt, rlt, rrt, left_x_order, right_x_order, remove_count):
        left_x, left_y = get_position_by_x_order(left_x_order)
        right_x, right_y = get_position_by_x_order(right_x_order)
        diag_time = abs(right_x - left_x) + abs(right_y - left_y) - remove_count

        lllt = llt + abs(right_x - lx) + abs(right_y - ly) + diag_time
        llrt = llt + abs(lx - left_x) + abs(ly - left_y) + diag_time
        lrlt = lrt + abs(right_x - rx) + abs(right_y - ry) + diag_time
        lrrt = lrt + abs(rx - left_x) + abs(ry - left_y) + diag_time
        rllt = rlt + abs(right_x - lx) + abs(right_y - ly) + diag_time
        rlrt = rlt + abs(lx - left_x) + abs(ly - left_y) + diag_time
        rrlt = rrt + abs(right_x - rx) + abs(right_y - ry) + diag_time
        rrrt = rrt + abs(rx - left_x) + abs(ry - left_y) + diag_time

        llt = min(lllt, lrlt)
        lrt = min(llrt, lrrt)
        rlt = min(rllt, rrlt)
        rrt = min(rlrt, rrrt)
        return left_x, left_y, right_x, right_y, llt, lrt, rlt, rrt

    is_rook_group_freely_removable = np.zeros(rook_count, dtype=np.int8)
    for idx in range(rook_count):
        x_order = coordinate_x_rank[idx]
        y_order = coordinate_y_rank[idx]
        prev_x_idx = -1 if x_order == 0 else coordinate_x_sort_indices[x_order - 1]
        next_x_idx = -2 if x_order == rook_count - 1 else coordinate_x_sort_indices[x_order + 1]
        prev_y_idx = -3 if y_order == 0 else coordinate_y_sort_indices[y_order - 1]
        next_y_idx = -4 if y_order == rook_count - 1 else coordinate_y_sort_indices[y_order + 1]
        if prev_x_idx == prev_y_idx or prev_x_idx == next_y_idx:
            is_rook_group_freely_removable[x_order - 1] = 1
        if next_x_idx == prev_y_idx or next_x_idx == next_y_idx:
            is_rook_group_freely_removable[x_order] = 1

    group_left_boundary = np.zeros(rook_count, dtype=np.int64)
    group_right_boundary = np.zeros(rook_count, dtype=np.int64)
    left_start = 0
    for x_order in range(rook_count - 1):
        if is_rook_group_freely_removable[x_order] == 0:
            left_start = x_order + 1
        group_left_boundary[x_order + 1] = left_start
    right_end = rook_count - 1
    group_right_boundary[right_end] = right_end
    for x_order in range(rook_count - 2, -1, -1):
        if is_rook_group_freely_removable[x_order] == 0:
            right_end = x_order
        group_right_boundary[x_order] = right_end

    group_left_extra_time = np.zeros(rook_count, dtype=np.int64)
    group_right_extra_time = np.zeros(rook_count, dtype=np.int64)
    MAX_INT = 10 ** 18
    l_x_order = 0
    while l_x_order < rook_count:
        r_x_order = group_right_boundary[l_x_order]
        if l_x_order == r_x_order:
            l_x_order = r_x_order + 1
            continue
        left_rook_idx = coordinate_x_sort_indices[l_x_order]
        right_rook_idx = coordinate_x_sort_indices[r_x_order]
        left_y_order = coordinate_y_rank[left_rook_idx]
        right_y_order = coordinate_y_rank[right_rook_idx]
        group_y_min = min(left_y_order, right_y_order)
        group_y_max = max(left_y_order, right_y_order)
        original_l_x = l_x_order
        cur_lx = coordinate_x[left_rook_idx]
        cur_ly = coordinate_y[left_rook_idx]
        cur_rx = coordinate_x[right_rook_idx]
        cur_ry = coordinate_y[right_rook_idx]
        llt, lrt, rlt, rrt = 0, MAX_INT, MAX_INT, 0

        while True:
            prev_x_idx = -1 if l_x_order == 0 else coordinate_x_sort_indices[l_x_order - 1]
            prev_y_idx = -2 if group_y_min == 0 else coordinate_y_sort_indices[group_y_min - 1]
            next_x_idx = -3 if r_x_order == rook_count - 1 else coordinate_x_sort_indices[r_x_order + 1]
            next_y_idx = -4 if group_y_max == rook_count - 1 else coordinate_y_sort_indices[group_y_max + 1]

            if prev_x_idx == prev_y_idx:
                left_x_group = group_left_boundary[l_x_order - 1]
                rook_incr = l_x_order - left_x_group
                if next_x_idx == next_y_idx:
                    right_x_group = group_right_boundary[r_x_order + 1]
                    rook_incr += right_x_group - r_x_order
                    cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt = \
                        compute_transition(cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt, left_x_group, right_x_group, rook_incr)
                    l_x_order = left_x_group
                    r_x_order = right_x_group
                    uy = coordinate_y_rank[coordinate_x_sort_indices[l_x_order]]
                    vy = coordinate_y_rank[coordinate_x_sort_indices[r_x_order]]
                    group_y_min, group_y_max = min(group_y_min, group_y_max, uy, vy), max(group_y_min, group_y_max, uy, vy)
                else:
                    cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt = \
                        compute_transition(cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt, left_x_group, left_x_group, rook_incr)
                    l_x_order = left_x_group
                    uy = coordinate_y_rank[coordinate_x_sort_indices[l_x_order]]
                    group_y_min, group_y_max = min(group_y_min, group_y_max, uy), max(group_y_min, group_y_max, uy)
            elif prev_x_idx == next_y_idx:
                left_x_group = group_left_boundary[l_x_order - 1]
                rook_incr = l_x_order - left_x_group
                if next_x_idx == prev_y_idx:
                    right_x_group = group_right_boundary[r_x_order + 1]
                    rook_incr += right_x_group - r_x_order
                    cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt = \
                        compute_transition(cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt, left_x_group, right_x_group, rook_incr)
                    l_x_order = left_x_group
                    r_x_order = right_x_group
                    uy = coordinate_y_rank[coordinate_x_sort_indices[l_x_order]]
                    vy = coordinate_y_rank[coordinate_x_sort_indices[r_x_order]]
                    group_y_min, group_y_max = min(group_y_min, group_y_max, uy, vy), max(group_y_min, group_y_max, uy, vy)
                else:
                    cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt = \
                        compute_transition(cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt, left_x_group, left_x_group, rook_incr)
                    l_x_order = left_x_group
                    uy = coordinate_y_rank[coordinate_x_sort_indices[l_x_order]]
                    group_y_min, group_y_max = min(group_y_min, group_y_max, uy), max(group_y_min, group_y_max, uy)
            elif next_x_idx == next_y_idx or next_x_idx == prev_y_idx:
                right_x_group = group_right_boundary[r_x_order + 1]
                rook_incr = right_x_group - r_x_order
                cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt = \
                    compute_transition(cur_lx, cur_ly, cur_rx, cur_ry, llt, lrt, rlt, rrt, right_x_group, right_x_group, rook_incr)
                r_x_order = right_x_group
                vy = coordinate_y_rank[coordinate_x_sort_indices[r_x_order]]
                group_y_min, group_y_max = min(group_y_min, group_y_max, vy), max(group_y_min, group_y_max, vy)
            else:
                group_left_extra_time[original_l_x] = min(llt, lrt)
                group_right_extra_time[original_l_x] = min(rlt, rrt)
                break
        l_x_order = r_x_order + 1

    result_time = np.zeros(rook_count, dtype=np.int64)
    for idx in range(rook_count):
        x_order = coordinate_x_rank[idx]
        x_val = coordinate_x[idx]
        y_val = coordinate_y[idx]
        l_x_order = group_left_boundary[x_order]
        leftmost_x = coordinate_x[coordinate_x_sort_indices[l_x_order]]
        leftmost_y = coordinate_y[coordinate_x_sort_indices[l_x_order]]
        r_x_order = group_right_boundary[x_order]
        rightmost_x = coordinate_x[coordinate_x_sort_indices[r_x_order]]
        rightmost_y = coordinate_y[coordinate_x_sort_indices[r_x_order]]
        left_time = group_left_extra_time[l_x_order]
        right_time = group_right_extra_time[l_x_order]
        group_diag = abs(rightmost_x - leftmost_x) + abs(rightmost_y - leftmost_y) - (r_x_order - l_x_order)
        step_rlt = abs(rightmost_x - x_val) + abs(rightmost_y - y_val) + group_diag
        step_lrt = abs(x_val - leftmost_x) + abs(y_val - leftmost_y) + group_diag
        result_time[idx] = min(left_time + step_rlt, right_time + step_lrt)

    return result_time

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    numba_compiler = CC('module_compiled')
    numba_compiler.export('process_problem', '(i8[:],)')(process_problem)
    numba_compiler.compile()
    exit()

if os.name == 'posix':
    from module_compiled import process_problem
else:
    from numba import njit
    process_problem = njit('(i8[:],)', cache=True)(process_problem)
    print('compiled', file=sys.stderr)

input_array = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
output_result = process_problem(input_array)
print('\n'.join(map(str, output_result)))