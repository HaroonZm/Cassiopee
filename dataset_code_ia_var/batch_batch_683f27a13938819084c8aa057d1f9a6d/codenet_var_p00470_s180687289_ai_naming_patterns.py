for input_line in iter(input, '0 0'):
    width, height = map(int, input_line.split())
    matrix = [[[1, 0, 1, 0] for _ in range(height)] for _ in range(width)]
    for col_idx in range(1, width):
        for row_idx in range(1, height):
            left_val1, left_val2 = matrix[col_idx - 1][row_idx][0:2]
            up_val3, up_val4 = matrix[col_idx][row_idx - 1][2:4]
            matrix[col_idx][row_idx] = [up_val4, left_val1 + left_val2, left_val2, up_val3 + up_val4]
    res_sum = (
        matrix[width - 2][height - 1][0]
        + matrix[width - 2][height - 1][1]
        + matrix[width - 1][height - 2][2]
        + matrix[width - 1][height - 2][3]
    )
    print(res_sum % 10 ** 5)