import sys
import math
import os
import bisect

ENV_PYDEV = os.environ.get('PYDEV')
if ENV_PYDEV == "True":
    sys.stdin = open("sample-input.txt", "rt")

def compute_max_consecutive_one_length(grid_size, grid_data):
    max_length = 0
    # Horizontal check
    for row_data in grid_data:
        segments = row_data.split('0')
        row_max = max(len(segment) for segment in segments)
        if row_max > max_length:
            max_length = row_max
    # Vertical check
    for col_idx in range(grid_size):
        col_str = ''.join(grid_data[row_idx][col_idx] for row_idx in range(grid_size))
        segments = col_str.split('0')
        col_max = max(len(segment) for segment in segments)
        if col_max > max_length:
            max_length = col_max
    # Diagonal checks
    for diag_offset in range(-grid_size, 2 * grid_size):
        # Diagonal: top-left to bottom-right
        diag_str_pos = ''.join(
            grid_data[row_idx + col_idx][col_idx]
            for col_idx in range(grid_size)
            if 0 <= row_idx + col_idx < grid_size
            for row_idx in [diag_offset - col_idx]
        )
        if diag_str_pos:
            segments = diag_str_pos.split('0')
            diag_max = max(len(segment) for segment in segments)
            if diag_max > max_length:
                max_length = diag_max
        # Diagonal: bottom-left to top-right
        diag_str_neg = ''.join(
            grid_data[row_idx - col_idx][col_idx]
            for col_idx in range(grid_size)
            if 0 <= row_idx - col_idx < grid_size
            for row_idx in [diag_offset + col_idx]
        )
        if diag_str_neg:
            segments = diag_str_neg.split('0')
            diag_max = max(len(segment) for segment in segments)
            if diag_max > max_length:
                max_length = diag_max
    return max_length

while True:
    input_n = int(input())
    if input_n == 0:
        break
    input_grid = [input().strip() for _ in range(input_n)]
    result_length = compute_max_consecutive_one_length(input_n, input_grid)
    print(result_length)