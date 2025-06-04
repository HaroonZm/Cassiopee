case_index = 1
while True:
    input_size = input()
    if input_size == 0:
        break
    grid_size = input_size
    current_value = 1
    matrix = [[0 for col_index in range(grid_size)] for row_index in range(grid_size)]
    current_row = current_col = 0
    if grid_size == 1:
        matrix[current_row][current_col] = 1
    while current_value < grid_size * grid_size:
        matrix[current_row][current_col] = current_value
        if current_col < grid_size - 1:
            current_col += 1
            current_value += 1
            matrix[current_row][current_col] = current_value
        else:
            current_row += 1
            current_value += 1
            matrix[current_row][current_col] = current_value
        while current_col > 0 and current_row < grid_size - 1:
            current_row += 1
            current_col -= 1
            current_value += 1
            matrix[current_row][current_col] = current_value
        if current_row < grid_size - 1:
            current_row += 1
            current_value += 1
            matrix[current_row][current_col] = current_value
        else:
            current_col += 1
            current_value += 1
            matrix[current_row][current_col] = current_value
        while current_row > 0 and current_col < grid_size - 1:
            current_row -= 1
            current_col += 1
            current_value += 1
            matrix[current_row][current_col] = current_value
    print "Case %d:" % case_index
    for row_index in range(grid_size):
        print "%3d" * grid_size % tuple(matrix[row_index])
    case_index += 1