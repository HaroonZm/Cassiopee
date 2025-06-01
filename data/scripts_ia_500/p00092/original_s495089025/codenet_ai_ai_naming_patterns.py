table_cells = [''] * 1002
dp_matrix = [[0] * 1002 for _ in range(1002)]

while True:
    matrix_size = int(input())
    if matrix_size == 0:
        break
    for row_index in range(matrix_size):
        table_cells[row_index] = input()
    max_square_size = 0

    for row_index in range(matrix_size):
        for col_index in range(matrix_size):
            if table_cells[row_index][col_index] == '*':
                dp_matrix[row_index][col_index] = 0
            else:
                min_adjacent = dp_matrix[row_index - 1][col_index - 1]
                if dp_matrix[row_index][col_index - 1] < min_adjacent:
                    min_adjacent = dp_matrix[row_index][col_index - 1]
                if dp_matrix[row_index - 1][col_index] < min_adjacent:
                    min_adjacent = dp_matrix[row_index - 1][col_index]
                dp_matrix[row_index][col_index] = min_adjacent + 1
                if dp_matrix[row_index][col_index] > max_square_size:
                    max_square_size = dp_matrix[row_index][col_index]
    print(max_square_size)