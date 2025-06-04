HASH_BASE_ROW = 1009
HASH_BASE_COL = 1013
BIT_MASK_32 = (1 << 32) - 1

def compute_2d_rolling_hash(matrix, matrix_rows, matrix_cols):
    global pattern_rows, pattern_cols, rolling_hash
    temp_row_hashes = [[0] * matrix_cols for _ in range(matrix_rows)]
    max_row_idx = matrix_rows - pattern_rows
    max_col_idx = matrix_cols - pattern_cols

    base1_power = 1
    for _ in range(pattern_cols):
        base1_power = (base1_power * HASH_BASE_ROW) & BIT_MASK_32

    for current_row in range(matrix_rows):
        rolling_row_hash = 0
        for col_window in range(pattern_cols):
            rolling_row_hash = rolling_row_hash * HASH_BASE_ROW + matrix[current_row][col_window]
        for current_col in range(max_col_idx):
            temp_row_hashes[current_row][current_col] = rolling_row_hash
            rolling_row_hash = (rolling_row_hash * HASH_BASE_ROW - base1_power * matrix[current_row][current_col] + matrix[current_row][current_col + pattern_cols]) & BIT_MASK_32
        temp_row_hashes[current_row][max_col_idx] = rolling_row_hash

    base2_power = 1
    for _ in range(pattern_rows):
        base2_power = (base2_power * HASH_BASE_COL) & BIT_MASK_32

    for current_col in range(max_col_idx + 1):
        rolling_col_hash = 0
        for row_window in range(pattern_rows):
            rolling_col_hash = rolling_col_hash * HASH_BASE_COL + temp_row_hashes[row_window][current_col]
        for current_row in range(max_row_idx):
            rolling_hash[current_row][current_col] = rolling_col_hash
            rolling_col_hash = (rolling_col_hash * HASH_BASE_COL - base2_power * temp_row_hashes[current_row][current_col] + temp_row_hashes[current_row + pattern_rows][current_col]) & BIT_MASK_32
        rolling_hash[max_row_idx][current_col] = rolling_col_hash

text_matrix_row_count, text_matrix_col_count = map(int, input().split())
text_matrix = [[ord(char) for char in input().strip()] for _ in range(text_matrix_row_count)]

pattern_rows, pattern_cols = map(int, input().split())
pattern_matrix = [[ord(char) for char in input().strip()] for _ in range(pattern_rows)]

if text_matrix_row_count >= pattern_rows and text_matrix_col_count >= pattern_cols:
    rolling_hash = [[0] * text_matrix_col_count for _ in range(text_matrix_row_count)]

    compute_2d_rolling_hash(pattern_matrix, pattern_rows, pattern_cols)
    pattern_hash_key = rolling_hash[0][0] & BIT_MASK_32

    compute_2d_rolling_hash(text_matrix, text_matrix_row_count, text_matrix_col_count)

    for row_index in range(text_matrix_row_count - pattern_rows + 1):
        for col_index in range(text_matrix_col_count - pattern_cols + 1):
            if rolling_hash[row_index][col_index] & BIT_MASK_32 == pattern_hash_key:
                print(row_index, col_index)