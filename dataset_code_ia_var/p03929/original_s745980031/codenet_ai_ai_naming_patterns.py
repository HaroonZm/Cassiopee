num_total, value_target = (int(item) for item in input().split())
matrix_values = [[4, 2, 0, 9, 7]] + [[0 for col_idx in range(5)] for row_idx in range(10)]
for row_idx in range(1, 11):
    for col_idx in range(5):
        matrix_values[row_idx][col_idx] = (matrix_values[row_idx - 1][col_idx] + 8) % 11
count_result, remaining_rows = ((num_total - 2) // 11) * 5, (num_total - 2) % 11
for row_idx in range(remaining_rows):
    count_result += matrix_values[row_idx].count(value_target)
print(count_result)