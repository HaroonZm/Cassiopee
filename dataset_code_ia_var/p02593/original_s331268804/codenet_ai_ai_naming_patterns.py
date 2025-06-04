import os
import sys

import numpy as np

def process_rooks(input_data):
    rook_count = input_data[0]
    x_coords = input_data[1::2]
    y_coords = input_data[2::2]
    x_sort_idx = np.argsort(x_coords)
    y_sort_idx = np.argsort(y_coords)
    x_order = np.argsort(x_sort_idx)
    y_order = np.argsort(y_sort_idx)

    def get_coords_by_xpos(xpos):
        rook_idx = x_sort_idx[xpos]
        return x_coords[rook_idx], y_coords[rook_idx]

    def update_state(lx, ly, rx, ry, llt, lrt, rlt, rrt, left_grp_x, right_grp_x, rook_group_size):
        left_x, left_y = get_coords_by_xpos(left_grp_x)
        right_x, right_y = get_coords_by_xpos(right_grp_x)
        diag_time = abs(right_x - left_x) + abs(right_y - left_y) - rook_group_size

        lllt_time = llt + abs(right_x - lx) + abs(right_y - ly) + diag_time
        llrt_time = llt + abs(lx - left_x) + abs(ly - left_y) + diag_time
        lrlt_time = lrt + abs(right_x - rx) + abs(right_y - ry) + diag_time
        lrrt_time = lrt + abs(rx - left_x) + abs(ry - left_y) + diag_time
        rllt_time = rlt + abs(right_x - lx) + abs(right_y - ly) + diag_time
        rlrt_time = rlt + abs(lx - left_x) + abs(ly - left_y) + diag_time
        rrlt_time = rrt + abs(right_x - rx) + abs(right_y - ry) + diag_time
        rrrt_time = rrt + abs(rx - left_x) + abs(ry - left_y) + diag_time

        llt_new = min(lllt_time, lrlt_time)
        lrt_new = min(llrt_time, lrrt_time)
        rlt_new = min(rllt_time, rrlt_time)
        rrt_new = min(rlrt_time, rrrt_time)

        return left_x, left_y, right_x, right_y, llt_new, lrt_new, rlt_new, rrt_new

    rook_free = np.zeros(rook_count, dtype=np.int8)
    for idx in range(rook_count):
        x_pos = x_order[idx]
        y_pos = y_order[idx]
        prev_x_idx = -1 if x_pos == 0 else x_sort_idx[x_pos - 1]
        next_x_idx = -2 if x_pos == rook_count - 1 else x_sort_idx[x_pos + 1]
        prev_y_idx = -3 if y_pos == 0 else y_sort_idx[y_pos - 1]
        next_y_idx = -4 if y_pos == rook_count - 1 else y_sort_idx[y_pos + 1]
        if prev_x_idx == prev_y_idx or prev_x_idx == next_y_idx:
            rook_free[x_pos - 1] = 1
        if next_x_idx == prev_y_idx or next_x_idx == next_y_idx:
            rook_free[x_pos] = 1

    free_range_left = np.zeros(rook_count, dtype=np.int64)
    free_range_right = np.zeros(rook_count, dtype=np.int64)
    range_left_idx = 0
    for cur_x in range(rook_count - 1):
        if rook_free[cur_x] == 0:
            range_left_idx = cur_x + 1
        free_range_left[cur_x + 1] = range_left_idx
    range_right_idx = rook_count - 1
    free_range_right[range_right_idx] = range_right_idx
    for cur_x in range(rook_count - 2, -1, -1):
        if rook_free[cur_x] == 0:
            range_right_idx = cur_x
        free_range_right[cur_x] = range_right_idx

    extra_moves_left = np.zeros(rook_count, dtype=np.int64)
    extra_moves_right = np.zeros(rook_count, dtype=np.int64)
    INF_CONST = 10 ** 18
    left_x_idx = 0
    while left_x_idx < rook_count:
        right_x_idx = free_range_right[left_x_idx]
        if left_x_idx == right_x_idx:
            left_x_idx = right_x_idx + 1
            continue

        left_rook_idx = x_sort_idx[left_x_idx]
        right_rook_idx = x_sort_idx[right_x_idx]
        left_y_order = y_order[left_rook_idx]
        right_y_order = y_order[right_rook_idx]
        left_y_order, right_y_order = min(left_y_order, right_y_order), max(left_y_order, right_y_order)

        group_left_origin = left_x_idx
        cur_lx = x_coords[left_rook_idx]
        cur_ly = y_coords[left_rook_idx]
        cur_rx = x_coords[right_rook_idx]
        cur_ry = y_coords[right_rook_idx]
        cur_llt, cur_lrt, cur_rlt, cur_rrt = 0, INF_CONST, INF_CONST, 0

        while True:
            prev_x_idx = -1 if left_x_idx == 0 else x_sort_idx[left_x_idx - 1]
            prev_y_idx = -2 if left_y_order == 0 else y_sort_idx[left_y_order - 1]
            next_x_idx = -3 if right_x_idx == rook_count - 1 else x_sort_idx[right_x_idx + 1]
            next_y_idx = -4 if right_y_order == rook_count - 1 else y_sort_idx[right_y_order + 1]

            if prev_x_idx == prev_y_idx:
                left_group_x = free_range_left[left_x_idx - 1]
                rook_group_size = left_x_idx - left_group_x
                if next_x_idx == next_y_idx:
                    right_group_x = free_range_right[right_x_idx + 1]
                    rook_group_size += right_group_x - right_x_idx
                    cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt = \
                        update_state(cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt, left_group_x, right_group_x, rook_group_size)
                    left_x_idx = left_group_x
                    right_x_idx = right_group_x
                    u_y_order = y_order[x_sort_idx[left_x_idx]]
                    v_y_order = y_order[x_sort_idx[right_x_idx]]
                    left_y_order, right_y_order = min(left_y_order, right_y_order, u_y_order, v_y_order), max(left_y_order, right_y_order, u_y_order, v_y_order)
                else:
                    cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt = \
                        update_state(cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt, left_group_x, left_group_x, rook_group_size)
                    left_x_idx = left_group_x
                    u_y_order = y_order[x_sort_idx[left_x_idx]]
                    left_y_order, right_y_order = min(left_y_order, right_y_order, u_y_order), max(left_y_order, right_y_order, u_y_order)
            elif prev_x_idx == next_y_idx:
                left_group_x = free_range_left[left_x_idx - 1]
                rook_group_size = left_x_idx - left_group_x
                if next_x_idx == prev_y_idx:
                    right_group_x = free_range_right[right_x_idx + 1]
                    rook_group_size += right_group_x - right_x_idx
                    cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt = \
                        update_state(cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt, left_group_x, right_group_x, rook_group_size)
                    left_x_idx = left_group_x
                    right_x_idx = right_group_x
                    u_y_order = y_order[x_sort_idx[left_x_idx]]
                    v_y_order = y_order[x_sort_idx[right_x_idx]]
                    left_y_order, right_y_order = min(left_y_order, right_y_order, u_y_order, v_y_order), max(left_y_order, right_y_order, u_y_order, v_y_order)
                else:
                    cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt = \
                        update_state(cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt, left_group_x, left_group_x, rook_group_size)
                    left_x_idx = left_group_x
                    u_y_order = y_order[x_sort_idx[left_x_idx]]
                    left_y_order, right_y_order = min(left_y_order, right_y_order, u_y_order), max(left_y_order, right_y_order, u_y_order)
            elif next_x_idx == next_y_idx or next_x_idx == prev_y_idx:
                right_group_x = free_range_right[right_x_idx + 1]
                rook_group_size = right_group_x - right_x_idx
                cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt = \
                    update_state(cur_lx, cur_ly, cur_rx, cur_ry, cur_llt, cur_lrt, cur_rlt, cur_rrt, right_group_x, right_group_x, rook_group_size)
                right_x_idx = right_group_x
                v_y_order = y_order[x_sort_idx[right_x_idx]]
                left_y_order, right_y_order = min(left_y_order, right_y_order, v_y_order), max(left_y_order, right_y_order, v_y_order)
            else:
                extra_moves_left[group_left_origin] = min(cur_llt, cur_lrt)
                extra_moves_right[group_left_origin] = min(cur_rlt, cur_rrt)
                break
        left_x_idx = right_x_idx + 1

    min_time_array = np.zeros(rook_count, dtype=np.int64)
    for idx in range(rook_count):
        x_pos = x_order[idx]
        rook_x = x_coords[idx]
        rook_y = y_coords[idx]
        group_lx = free_range_left[x_pos]
        group_lx_coord = x_coords[x_sort_idx[group_lx]]
        group_ly_coord = y_coords[x_sort_idx[group_lx]]
        group_rx = free_range_right[x_pos]
        group_rx_coord = x_coords[x_sort_idx[group_rx]]
        group_ry_coord = y_coords[x_sort_idx[group_rx]]
        left_time = extra_moves_left[group_lx]
        right_time = extra_moves_right[group_lx]
        diag_time = abs(group_rx_coord - group_lx_coord) + abs(group_ry_coord - group_ly_coord) - (group_rx - group_lx)
        right_left_time = abs(group_rx_coord - rook_x) + abs(group_ry_coord - rook_y) + diag_time
        left_right_time = abs(rook_x - group_lx_coord) + abs(rook_y - group_ly_coord) + diag_time
        min_time_array[idx] = min(left_time + right_left_time, right_time + left_right_time)
    return min_time_array

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('optimized_rook_module')
    cc.export('process_rooks', '(i8[:],)')(process_rooks)
    cc.compile()
    exit()

if os.name == 'posix':
    from optimized_rook_module import process_rooks
else:
    from numba import njit
    process_rooks = njit('(i8[:],)', cache=True)(process_rooks)
    print('compiled', file=sys.stderr)

input_block = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
result_times = process_rooks(input_block)
print('\n'.join(map(str, result_times)))