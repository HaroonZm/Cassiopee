initial_row_count, initial_column_count, target_row_count, target_column_count = map(int, input().split())

MODULO = 998244353

dynamic_programming_grid = [
    [0] * (target_column_count + 1)
    for _ in range(target_row_count + 1)
]

dynamic_programming_grid[initial_row_count][initial_column_count] = 1

for current_row in range(initial_row_count + 1, target_row_count + 1):
    dynamic_programming_grid[current_row][initial_column_count] = (
        dynamic_programming_grid[current_row - 1][initial_column_count] * initial_column_count % MODULO
    )

for current_column in range(initial_column_count + 1, target_column_count + 1):
    dynamic_programming_grid[initial_row_count][current_column] = (
        dynamic_programming_grid[initial_row_count][current_column - 1] * initial_row_count % MODULO
    )

for current_row in range(initial_row_count + 1, target_row_count + 1):
    for current_column in range(initial_column_count + 1, target_column_count + 1):

        value_from_above = (
            dynamic_programming_grid[current_row - 1][current_column] * current_column
        )

        value_from_left = (
            (dynamic_programming_grid[current_row][current_column - 1] -
             dynamic_programming_grid[current_row - 1][current_column - 1] * (current_column - 1)
            ) * current_row
        )

        value_from_diagonal = (
            dynamic_programming_grid[current_row - 1][current_column - 1] * (current_column - 1)
        )

        dynamic_programming_grid[current_row][current_column] = (
            value_from_above + value_from_left + value_from_diagonal
        ) % MODULO

print(dynamic_programming_grid[target_row_count][target_column_count])