import sys

number_of_rows, number_of_columns = map(int, sys.stdin.readline().split())

maximal_square_side_grid = [
    [0] * number_of_columns for _ in range(number_of_rows)
]

input_grid = [
    [int(cell) for cell in sys.stdin.readline().split()] for _ in range(number_of_rows)
]

for current_row in range(number_of_rows):
    maximal_square_side_grid[current_row][0] = 1 if input_grid[current_row][0] == 0 else 0

for current_column in range(number_of_columns):
    maximal_square_side_grid[0][current_column] = 1 if input_grid[0][current_column] == 0 else 0

for row_index in range(1, number_of_rows):
    for column_index in range(1, number_of_columns):
        if input_grid[row_index][column_index] == 0:
            maximal_square_side_grid[row_index][column_index] = (
                min(
                    maximal_square_side_grid[row_index - 1][column_index - 1],
                    maximal_square_side_grid[row_index - 1][column_index],
                    maximal_square_side_grid[row_index][column_index - 1]
                ) + 1
            )

largest_square_side = max(
    [max(row) for row in maximal_square_side_grid]
)

print(largest_square_side ** 2)