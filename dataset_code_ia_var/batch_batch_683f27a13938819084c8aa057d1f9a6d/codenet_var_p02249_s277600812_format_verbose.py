import sys

input_stream_readline = sys.stdin.readline
output_stream_write = sys.stdout.write

MODULUS = 10**9 + 9
ROW_POLYNOMIAL_BASE = 13
COLUMN_POLYNOMIAL_BASE = 19

row_power_table = None
column_power_table = None

def precompute_polynomial_power_tables(max_length):
    global row_power_table, column_power_table
    
    row_power_table = [1] * (max_length + 1)
    column_power_table = [1] * (max_length + 1)
    
    for index in range(max_length):
        row_power_table[index + 1]    = row_power_table[index]    * ROW_POLYNOMIAL_BASE    % MODULUS
        column_power_table[index + 1] = column_power_table[index] * COLUMN_POLYNOMIAL_BASE % MODULUS

def compute_2d_rolling_hash(character_matrix, width, height):
    hash_matrix = [[0] * (width + 1) for _ in range(height + 1)]
    
    for row_index in range(height):
        row_hash_sum = 0
        previous_row_hashes = hash_matrix[row_index]
        current_row_hashes  = hash_matrix[row_index + 1]
        character_row = character_matrix[row_index]
        
        for column_index in range(width):
            character_codepoint = character_row[column_index]
            row_hash_sum = (row_hash_sum * ROW_POLYNOMIAL_BASE + character_codepoint) % MODULUS
            
            current_row_hashes[column_index + 1] = (
                row_hash_sum + previous_row_hashes[column_index + 1] * COLUMN_POLYNOMIAL_BASE
            ) % MODULUS
            
    return hash_matrix

def query_submatrix_hash(hash_matrix, left, top, right, bottom):
    row_length  = right  - left
    col_length  = bottom - top
    row_power   = row_power_table[row_length]
    col_power   = column_power_table[col_length]
    
    total_hash = (
        hash_matrix[bottom][right]
        - hash_matrix[bottom][left] * row_power
        - hash_matrix[top][right] * col_power
        + hash_matrix[top][left] * (row_power * col_power % MODULUS)
    ) % MODULUS
    return total_hash

def find_pattern_occurrences():
    precompute_polynomial_power_tables(1001)
    
    input_matrix_height, input_matrix_width = map(int, input_stream_readline().split())
    
    input_matrix = [
        list(map(ord, input_stream_readline().strip()))
        for _ in range(input_matrix_height)
    ]
    
    pattern_matrix_height, pattern_matrix_width = map(int, input_stream_readline().split())
    
    pattern_matrix = [
        list(map(ord, input_stream_readline().strip()))
        for _ in range(pattern_matrix_height)
    ]
    
    input_matrix_hashes   = compute_2d_rolling_hash(input_matrix, input_matrix_width, input_matrix_height)
    pattern_matrix_hashes = compute_2d_rolling_hash(pattern_matrix, pattern_matrix_width, pattern_matrix_height)
    pattern_full_hash = pattern_matrix_hashes[-1][-1]
    
    max_row_offset = input_matrix_height - pattern_matrix_height + 1
    max_col_offset = input_matrix_width  - pattern_matrix_width  + 1
    
    for row_offset in range(max_row_offset):
        for col_offset in range(max_col_offset):
            if pattern_full_hash == query_submatrix_hash(
                input_matrix_hashes,
                col_offset,
                row_offset,
                col_offset + pattern_matrix_width,
                row_offset + pattern_matrix_height
            ):
                output_stream_write(f"{row_offset} {col_offset}\n")

find_pattern_occurrences()