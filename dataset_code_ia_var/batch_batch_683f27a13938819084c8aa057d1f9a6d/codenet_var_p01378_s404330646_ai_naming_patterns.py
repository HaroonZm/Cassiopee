input_string = input()
delimiter_index = input_string.index("i")
left_segment = "." + input_string[:delimiter_index][::-1]
right_segment = "." + input_string[delimiter_index + 3:]
trans_table = str.maketrans("(){}[]", ")(}{][")
reversed_left_segment = left_segment.translate(trans_table)
matrix_rows = len(right_segment)
matrix_cols = len(reversed_left_segment)
dp_matrix = [[0 for dp_col in range(matrix_cols)] for dp_row in range(matrix_rows)]
for row_idx in range(1, matrix_rows):
    for col_idx in range(1, matrix_cols):
        if right_segment[row_idx] == reversed_left_segment[col_idx]:
            dp_matrix[row_idx][col_idx] = dp_matrix[row_idx - 1][col_idx - 1] + 1
        else:
            dp_matrix[row_idx][col_idx] = max(dp_matrix[row_idx - 1][col_idx], dp_matrix[row_idx][col_idx - 1])
print(3 + 2 * dp_matrix[-1][-1])