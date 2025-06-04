def verify_matrix_sum_properties():
    
    matrix_with_zero_column = []
    matrix_with_zero_column.append([])  # Padding for 1-based index compatibility
    
    row_one = list(map(int, ('0 ' + input()).split()))
    matrix_with_zero_column.append(row_one)
    
    row_two = list(map(int, ('0 ' + input()).split()))
    matrix_with_zero_column.append(row_two)

    row_three = list(map(int, ('0 ' + input()).split()))
    matrix_with_zero_column.append(row_three)
    
    row_constants = [0] * 4
    column_constants = [0] * 4
    
    row_constants[1] = 0  # By definition
    
    # Calculate column constants based on first row
    for column_index in range(1, 4):
        column_constants[column_index] = matrix_with_zero_column[1][column_index] - row_constants[1]
    
    # Calculate row constants for rows 2 and 3 based on first column
    for row_index in range(2, 4):
        row_constants[row_index] = matrix_with_zero_column[row_index][1] - column_constants[1]
    
    # Validate condition across all elements
    for row_index in range(1, 4):
        for column_index in range(1, 4):
            expected_value = row_constants[row_index] + column_constants[column_index]
            if matrix_with_zero_column[row_index][column_index] != expected_value:
                print('No')
                return
    
    print('Yes')

verify_matrix_sum_properties()