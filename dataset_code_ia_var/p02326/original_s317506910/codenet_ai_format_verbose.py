number_of_rows, number_of_columns = map(int, input().split())

grid_values = [list(map(int, input().split())) for _ in range(number_of_rows)]

maximal_square_at_cell = [[0] * number_of_columns for _ in range(number_of_rows)]

largest_square_edge = 0

for row_index in range(number_of_rows):
    if grid_values[row_index][0] == 0:
        maximal_square_at_cell[row_index][0] = 1
        largest_square_edge = 1

for column_index in range(number_of_columns):
    if grid_values[0][column_index] == 0:
        maximal_square_at_cell[0][column_index] = 1
        largest_square_edge = 1

for row_index in range(1, number_of_rows):
    for column_index in range(1, number_of_columns):
        if grid_values[row_index][column_index] == 1:
            maximal_square_at_cell[row_index][column_index] = 0
        else:
            smallest_neighbor_square = min(
                maximal_square_at_cell[row_index][column_index - 1],
                maximal_square_at_cell[row_index - 1][column_index],
                maximal_square_at_cell[row_index - 1][column_index - 1]
            )
            maximal_square_at_cell[row_index][column_index] = smallest_neighbor_square + 1
            largest_square_edge = max(largest_square_edge, maximal_square_at_cell[row_index][column_index])

print(largest_square_edge ** 2)