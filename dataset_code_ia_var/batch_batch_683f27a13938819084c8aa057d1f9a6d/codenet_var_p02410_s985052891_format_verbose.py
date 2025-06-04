number_of_rows, number_of_columns = map(int, input().split())

coefficient_matrix = [
    list(map(int, input().split()))
    for row_index in range(number_of_rows)
]

vector_values = [
    int(input())
    for column_index in range(number_of_columns)
]

for row_index in range(number_of_rows):
    weighted_sum = sum([
        coefficient_matrix[row_index][column_index] * vector_values[column_index]
        for column_index in range(number_of_columns)
    ])
    print(weighted_sum)