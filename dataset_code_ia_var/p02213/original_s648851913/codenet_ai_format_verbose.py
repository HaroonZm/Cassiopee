import sys

sys.setrecursionlimit(10 ** 6)

height_grid, width_grid = map(int, input().split())

input_grid = [[character for character in input()] for _ in range(height_grid)]

visited_cells = [[False] * width_grid for _ in range(height_grid)]

reference_row_pattern = [['6', '3', '1', '4'], ['1', '3', '6', '4']]
reference_column_pattern = [['6', '2', '1', '5'], ['1', '2', '6', '5']]
pattern_checker_grid = [
    ['6', '3', '1', '4'],
    ['2', '-1', '2', '-1'],
    ['1', '3', '6', '4'],
    ['5', '-1', '5', '-1']
]

delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]

def depth_first_search(current_row, current_col):
    if current_row < 0 or current_row >= height_grid or current_col < 0 or current_col >= width_grid:
        return
    if input_grid[current_row][current_col] == '#':
        return
    if visited_cells[current_row][current_col] is True:
        return

    modulo_four_row = current_row % 4
    modulo_four_col = current_col % 4

    if input_grid[current_row][current_col] != pattern_checker_grid[modulo_four_row][modulo_four_col]:
        return

    visited_cells[current_row][current_col] = True

    for direction_index in range(4):
        next_row = current_row + delta_y[direction_index]
        next_col = current_col + delta_x[direction_index]
        depth_first_search(next_row, next_col)

depth_first_search(0, 0)

print('YES' if visited_cells[height_grid - 1][width_grid - 1] else 'NO')