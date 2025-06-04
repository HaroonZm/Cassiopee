number_of_rows, number_of_columns = map(int, input().split())

input_matrix = []

for current_row_index in range(number_of_rows):
    current_row_values = list(map(int, input().split()))
    input_matrix.append(current_row_values)

input_vector = []

for current_column_index in range(number_of_columns):
    vector_element = int(input())
    input_vector.append(vector_element)

for row_index in range(number_of_rows):
    matrix_vector_product_result = 0
    for column_index in range(number_of_columns):
        matrix_vector_product_result += input_matrix[row_index][column_index] * input_vector[column_index]

    print(matrix_vector_product_result)