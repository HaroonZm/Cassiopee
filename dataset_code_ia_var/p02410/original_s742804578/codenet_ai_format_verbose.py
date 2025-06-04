number_of_rows_matrix_A, number_of_columns_matrix_A = map(int, input().split())

matrix_A = []
for row_index in range(number_of_rows_matrix_A):
    row_of_matrix_A = list(map(int, input().split()))
    matrix_A.append(row_of_matrix_A)

matrix_B = []
for row_index in range(number_of_columns_matrix_A):
    element_of_matrix_B = int(input())
    matrix_B.append(element_of_matrix_B)

result_vector = []

for row_index in range(number_of_rows_matrix_A):
    dot_product_result = 0
    for column_index in range(number_of_columns_matrix_A):
        dot_product_result += matrix_A[row_index][column_index] * matrix_B[column_index]
    result_vector.append(dot_product_result)

for result in result_vector:
    print(result)