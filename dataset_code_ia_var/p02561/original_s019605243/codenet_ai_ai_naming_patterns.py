import os
import sys

import numpy as np

def solve(num_rows, num_cols, cell_state_grid):
    COORD_BITSHIFT = 9
    COORD_BITMASK = (1 << COORD_BITSHIFT) - 1

    def pack_rowcol(row, col):
        return (row << COORD_BITSHIFT) | col

    def unpack_rowcol(rc_key):
        return rc_key >> COORD_BITSHIFT, rc_key & COORD_BITMASK

    def update_match_links(match_arr, left_trace, right_trace, source_idx, target_idx):
        prev_node = right_trace[target_idx]
        while source_idx != prev_node:
            match_arr[target_idx] = prev_node
            target_idx = left_trace[prev_node]
            prev_node = right_trace[target_idx]
        match_arr[target_idx] = prev_node

    def find_augmenting_path(start_idx, num_left, num_right, adj_matrix, match_arr):
        left_trace = np.full(num_left, -1, dtype=np.int64)
        right_trace = np.full(num_right, -1, dtype=np.int64)
        bfs_queue = np.zeros(num_left + 5, dtype=np.int64)
        queue_head, queue_tail = 0, 1
        bfs_queue[0] = start_idx
        visited = np.zeros(num_left, dtype=np.int8)
        visited[start_idx] = 1
        while queue_head < queue_tail:
            left_idx = bfs_queue[queue_head]
            queue_head += 1
            edge_ptr = 0
            while adj_matrix[left_idx, edge_ptr] != -1:
                right_idx = adj_matrix[left_idx, edge_ptr]
                matched_left = match_arr[right_idx]
                if matched_left == -1:
                    right_trace[right_idx] = left_idx
                    update_match_links(match_arr, left_trace, right_trace, start_idx, right_idx)
                    return right_idx
                if visited[matched_left] == 0:
                    left_trace[matched_left] = right_idx
                    right_trace[right_idx] = left_idx
                    bfs_queue[queue_tail] = matched_left
                    queue_tail += 1
                    visited[matched_left] = 1
                edge_ptr += 1
        return -1

    left_nodes = []
    right_nodes = []
    right_index_map = {}

    for row in range(1, num_rows + 1):
        for col in range(1, num_cols + 1):
            if cell_state_grid[row, col]:
                continue
            coord_key = pack_rowcol(row, col)
            if (row ^ col) & 1:
                left_nodes.append(coord_key)
            else:
                right_index_map[coord_key] = len(right_nodes)
                right_nodes.append(coord_key)
    num_left_nodes = len(left_nodes)
    num_right_nodes = len(right_nodes)

    RC_NEIGHBOR_DIFFS = (-(1 << COORD_BITSHIFT), -1, 1, 1 << COORD_BITSHIFT)

    adjacency_matrix = np.full((num_left_nodes, 5), -1, dtype=np.int64)
    for left_idx in range(num_left_nodes):
        left_rc = left_nodes[left_idx]
        ptr = 0
        for delta in RC_NEIGHBOR_DIFFS:
            neighbor_rc = left_rc + delta
            if neighbor_rc in right_index_map:
                adjacency_matrix[left_idx, ptr] = right_index_map[neighbor_rc]
                ptr += 1

    right_match_arr = np.full(num_right_nodes, -1, dtype=np.int64)
    for left_idx in range(num_left_nodes):
        find_augmenting_path(left_idx, num_left_nodes, num_right_nodes, adjacency_matrix, right_match_arr)

    VERTICAL = 2
    UP = 3
    RIGHT = 4
    LEFT = 5

    total_pairs = 0
    for right_idx in range(num_right_nodes):
        left_idx = right_match_arr[right_idx]
        if left_idx == -1:
            continue
        left_row, left_col = unpack_rowcol(left_nodes[left_idx])
        right_row, right_col = unpack_rowcol(right_nodes[right_idx])
        if left_row == right_row:
            min_col, max_col = sorted((left_col, right_col))
            cell_state_grid[left_row, min_col] = RIGHT
            cell_state_grid[right_row, max_col] = LEFT
        else:
            min_row, max_row = sorted((left_row, right_row))
            cell_state_grid[min_row, left_col] = VERTICAL
            cell_state_grid[max_row, right_col] = UP
        total_pairs += 1

    return total_pairs

SOLVE_SIGNATURE = '(i8,i8,i1[:,:],)'
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    code_compiler = CC('my_module')
    code_compiler.export('solve', SOLVE_SIGNATURE)(solve)
    code_compiler.compile()
    exit()

if os.name == 'posix':
    from my_module import solve
else:
    from numba import njit

    solve = njit(SOLVE_SIGNATURE, cache=True)(solve)
    print('compiled', file=sys.stderr)

n_rows, n_cols = map(int, input().split())
parsed_grid = np.ones((n_rows + 2, n_cols + 2), dtype=np.int8)
for line_idx in range(n_rows):
    parsed_grid[line_idx + 1, 1:n_cols + 1] = list(map('.#'.index, input()))

answer = solve(n_rows, n_cols, parsed_grid)
print(answer)
SYMBOLS = '.#v^><'.__getitem__
for row_idx in range(1, n_rows + 1):
    print(''.join(map(SYMBOLS, parsed_grid[row_idx, 1:n_cols + 1])))