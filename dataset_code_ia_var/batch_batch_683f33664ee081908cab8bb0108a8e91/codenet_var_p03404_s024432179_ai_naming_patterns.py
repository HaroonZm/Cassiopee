import numpy as np

def get_input_values():
    return [int(value) for value in input().split()]

def initialize_grid(rows, cols):
    return np.zeros([rows, cols], dtype=np.int32)

def set_rightmost_column(grid):
    grid[:, -1] = 1

def mark_upper_diagonal_blocks(grid, block_count, row_start, col_start):
    for idx in range(block_count):
        grid[row_start - idx * 2, col_start:] = 1

def mark_vertical_segments(grid, segment_count, row_init, col_init, row_decrement, col_reset, segment_threshold):
    col = col_init
    row = row_init
    for _ in range(segment_count):
        grid[row, col] = 1
        col -= row_decrement
        if col == segment_threshold:
            col = col_init
            row -= row_decrement

def mark_horizontal_segments(grid, segment_count, row_init, col_init, col_increment, row_increment, col_threshold):
    col = col_init
    row = row_init
    for _ in range(segment_count):
        grid[row, col] = 1
        col += col_increment
        if col == col_threshold:
            col = col_init
            row += row_increment

def print_grid_dimensions(rows, cols):
    print(rows, cols)

def output_grid(grid, filled_char="#", empty_char="."):
    for row in grid:
        print("".join([filled_char if val == 1 else empty_char for val in row]))

def main():
    PARAM_A, PARAM_B = get_input_values()
    GRID_ROWS, GRID_COLS = 100, 100
    grid_matrix = initialize_grid(GRID_ROWS, GRID_COLS)
    set_rightmost_column(grid_matrix)
    mark_upper_diagonal_blocks(grid_matrix, block_count=20, row_start=99, col_start=1)
    mark_vertical_segments(
        grid_matrix,
        segment_count=PARAM_A - 1,
        row_init=98,
        col_init=97,
        row_decrement=2,
        col_reset=97,
        segment_threshold=3
    )
    mark_horizontal_segments(
        grid_matrix,
        segment_count=PARAM_B - 1,
        row_init=1,
        col_init=1,
        col_increment=2,
        row_increment=2,
        col_threshold=95
    )
    print_grid_dimensions(GRID_ROWS, GRID_COLS)
    output_grid(grid_matrix)

main()