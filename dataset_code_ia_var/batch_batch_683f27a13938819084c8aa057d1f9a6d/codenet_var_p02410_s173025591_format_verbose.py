number_of_rows, number_of_columns = map(int, input().split())

matrix_of_coefficients = []

for row_index in range(number_of_rows):
    row_values = list(map(int, input().split()))
    matrix_of_coefficients.append(row_values)

column_vector = []

for column_index in range(number_of_columns):
    vector_value = int(input())
    column_vector.append(vector_value)

for matrix_row_index in range(number_of_rows):
    scalar_product_result = 0

    for matrix_column_index in range(number_of_columns):
        scalar_product_result += (
            matrix_of_coefficients[matrix_row_index][matrix_column_index] * column_vector[matrix_column_index]
        )

    print(scalar_product_result)