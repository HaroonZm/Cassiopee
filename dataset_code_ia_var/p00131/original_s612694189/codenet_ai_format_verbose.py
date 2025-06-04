import itertools

def toggle_light_and_neighbors(grid, col_index, row_index):
    grid[row_index][col_index] ^= 1

    if row_index > 0:
        grid[row_index - 1][col_index] ^= 1

    if col_index > 0:
        grid[row_index][col_index - 1] ^= 1

    if col_index < 9:
        grid[row_index][col_index + 1] ^= 1

    if row_index < 9:
        grid[row_index + 1][col_index] ^= 1

solution_matrix = [[0] * 10 for _ in xrange(10)]

number_of_test_cases = input()

for test_case_index in xrange(number_of_test_cases):

    initial_grid = [map(int, raw_input().split()) for _ in xrange(10)]

    for first_row_toggle_pattern in itertools.product((0, 1), repeat=10):

        working_grid = [initial_grid[row][:] for row in xrange(10)]

        for column_index in xrange(10):
            if first_row_toggle_pattern[column_index]:
                toggle_light_and_neighbors(working_grid, column_index, 0)
            solution_matrix[0][column_index] = first_row_toggle_pattern[column_index]

        for row_index in xrange(9):
            for col_index in xrange(10):
                if working_grid[row_index][col_index]:
                    toggle_light_and_neighbors(working_grid, col_index, row_index + 1)
                    solution_matrix[row_index + 1][col_index] = 1
                else:
                    solution_matrix[row_index + 1][col_index] = 0

        if not any(working_grid[9]):
            for solution_row_index in xrange(10):
                print " ".join(map(str, solution_matrix[solution_row_index]))
            break