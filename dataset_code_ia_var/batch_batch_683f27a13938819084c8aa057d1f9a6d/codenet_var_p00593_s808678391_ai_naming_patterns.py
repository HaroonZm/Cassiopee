current_case_number = 1
while True:
    matrix_size = int(input())
    if matrix_size == 0:
        break
    matrix_pixels = [[0] * matrix_size for _ in range(matrix_size)]
    matrix_max_index = matrix_size - 1
    position_indices = [0, 0]
    current_pixel_value = 1
    while position_indices[0] < matrix_size:
        row_index, column_index = position_indices
        matrix_pixels[row_index][column_index] = current_pixel_value
        is_sum_indices_odd = (row_index + column_index) % 2
        direction_index = not is_sum_indices_odd
        advance_index = is_sum_indices_odd
        if position_indices[direction_index] == matrix_max_index:
            position_indices[advance_index] += 1
        elif position_indices[advance_index] == 0:
            position_indices[direction_index] += 1
        else:
            position_indices[direction_index] += 1
            position_indices[advance_index] -= 1
        current_pixel_value += 1
    print('Case {}:'.format(current_case_number))
    for pixel_row in matrix_pixels:
        print(''.join('{:>3}'.format(pixel_value) for pixel_value in pixel_row))
    current_case_number += 1