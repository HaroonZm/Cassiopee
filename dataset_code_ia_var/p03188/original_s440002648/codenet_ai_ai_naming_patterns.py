def solve_k_regular(k_input_value):
    if k_input_value == 1:
        print(1)
        print(1)
        return

    matrix_size = ((k_input_value - 1) // 4 + 1) * 2
    matrix_result = [[0] * matrix_size for _ in range(matrix_size)]
    double_count = 2 * (k_input_value - matrix_size)

    for loop_index in range(matrix_size * 2):
        label_value = loop_index + 1 if loop_index < double_count else double_count + (loop_index - double_count) // 2 + 1
        row_index = loop_index % 2
        col_index = (loop_index // 2 + loop_index % 2) % matrix_size

        for iterator in range(matrix_size // 2):
            matrix_result[row_index][col_index] = label_value
            row_index = (row_index + 2) % matrix_size
            col_index = (col_index + 2) % matrix_size

    print(matrix_size)
    print('\n'.join(' '.join(map(str, result_row)) for result_row in matrix_result))

input_k_value = int(input())
solve_k_regular(input_k_value)