num_rows, num_cols = map(int, input().split())
input_list = list(map(int, input().split()))

multiplier = 1
expanded_rows = num_rows * multiplier
while expanded_rows % num_cols != 0:
    multiplier += 1
    expanded_rows = num_rows * multiplier
row_division = expanded_rows // num_cols

input_list = input_list * (expanded_rows // num_rows + 1)

result_matrix = []
current_index = 0
for row_idx in range(row_division):
    row_elements = []
    for col_idx in range(num_cols):
        row_elements.append(input_list[current_index])
        current_index += 1
    result_matrix.append(row_elements)

total_range_sum = 0
for matrix_row in result_matrix:
    total_range_sum += max(matrix_row) - min(matrix_row)
print(total_range_sum)