def read_matrix_row_count(row_count):
    return [list(map(int, raw_input().split())) for _ in range(row_count)]

while True:
    matrix1_row_count = int(raw_input())
    if matrix1_row_count == 0:
        break
    matrix1 = read_matrix_row_count(matrix1_row_count)
    matrix2_row_count = int(raw_input())
    matrix2 = read_matrix_row_count(matrix2_row_count)
    matrix1_index = 0
    relation_matrix1 = [-1 for _ in range(matrix1_row_count)]
    relation_matrix2 = [-1 for _ in range(matrix2_row_count)]
    for matrix1_index in range(matrix1_row_count):
        matrix1_height, matrix1_range = matrix1[matrix1_index]
        for matrix2_index in range(matrix2_row_count):
            matrix2_height, matrix2_range = matrix2[matrix2_index]
            if matrix1_height < matrix2_height and matrix1_range < matrix2_range:
                relation_matrix2[matrix2_index] = matrix1_index
            if matrix1_height > matrix2_height and matrix1_range > matrix2_range:
                relation_matrix1[matrix1_index] = matrix2_index
    counter_matrix1 = [-1 for _ in range(matrix1_row_count + 1)]
    counter_matrix2 = [-1 for _ in range(matrix2_row_count + 1)]
    pointer_matrix1 = pointer_matrix2 = 0
    while pointer_matrix1 < matrix1_row_count or pointer_matrix2 < matrix2_row_count:
        if pointer_matrix1 < matrix1_row_count:
            if relation_matrix1[pointer_matrix1] < 0:
                if pointer_matrix1 == 0:
                    counter_matrix1[0] = 1
                else:
                    counter_matrix1[pointer_matrix1] = counter_matrix1[pointer_matrix1 - 1] + 1
                pointer_matrix1 += 1
            elif counter_matrix2[relation_matrix1[pointer_matrix1]] >= 0:
                counter_matrix1[pointer_matrix1] = max(counter_matrix1[pointer_matrix1 - 1], counter_matrix2[relation_matrix1[pointer_matrix1]]) + 1
                pointer_matrix1 += 1
        if pointer_matrix2 < matrix2_row_count:
            if relation_matrix2[pointer_matrix2] < 0:
                if pointer_matrix2 == 0:
                    counter_matrix2[0] = 1
                else:
                    counter_matrix2[pointer_matrix2] = counter_matrix2[pointer_matrix2 - 1] + 1
                pointer_matrix2 += 1
            elif counter_matrix1[relation_matrix2[pointer_matrix2]] >= 0:
                counter_matrix2[pointer_matrix2] = max(counter_matrix2[pointer_matrix2 - 1], counter_matrix1[relation_matrix2[pointer_matrix2]]) + 1
                pointer_matrix2 += 1
    print max(counter_matrix1 + counter_matrix2)