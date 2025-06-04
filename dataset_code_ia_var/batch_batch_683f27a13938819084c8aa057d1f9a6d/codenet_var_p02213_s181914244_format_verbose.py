import sys

sys.setrecursionlimit(10**7)

dice_pattern_matrix = [
    [6, 3, 1, 4],
    [2, 0, 2, 0],
    [1, 3, 6, 4],
    [5, 0, 5, 0]
]

grid_height, grid_width = map(int, input().split())

input_grid = [input() for _ in range(grid_height)]

visited_cells = [
    [0] * grid_width for _ in range(grid_height)
]

def perform_depth_first_search(current_row, current_col):

    visited_cells[current_row][current_col] = 1

    for row_offset, col_offset in [
        (0, -1), (0, 1), (1, 0), (-1, 0)
    ]:
        next_row = current_row + row_offset
        next_col = current_col + col_offset

        if not (0 <= next_row < grid_height and 0 <= next_col < grid_width):
            continue

        if visited_cells[next_row][next_col] == 1:
            continue

        expected_value = str(dice_pattern_matrix[next_row % 4][next_col % 4])

        if input_grid[next_row][next_col] == expected_value:
            perform_depth_first_search(next_row, next_col)

perform_depth_first_search(0, 0)

result = "YES" if visited_cells[grid_height - 1][grid_width - 1] else "NO"
print(result)