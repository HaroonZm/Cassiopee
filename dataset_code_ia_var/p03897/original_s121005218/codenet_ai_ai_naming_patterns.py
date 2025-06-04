input_value = int(input())
result_pairs = []
for row_index in range(input_value - 1):
    if row_index % 2 == 1:
        result_pairs.append((row_index, 0))
for row_index in range(input_value - 1):
    if row_index % 6 == 1:
        for col_index in range(2, input_value):
            if col_index % 2 == 0:
                result_pairs.append((row_index, col_index))
    if row_index % 6 == 4:
        for col_index in range(input_value):
            if col_index % 2 == 1:
                result_pairs.append((row_index, col_index))
for col_index in range(input_value):
    if (input_value - 1 + col_index) % 2 == 1:
        result_pairs.append((input_value - 1, col_index))
print(len(result_pairs))
for pair_row, pair_col in result_pairs:
    print(pair_row, pair_col)