import string
import sys

base64_character_set = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

modulus = 10 ** 9 + 9
base_p = 13
base_q = 19

maximum_matrix_dimension = 1000

power_table_p = [1] * (maximum_matrix_dimension + 1)
power_table_q = [1] * (maximum_matrix_dimension + 1)

for exponent in range(maximum_matrix_dimension):
    power_table_p[exponent + 1] = (power_table_p[exponent] * base_p) % modulus
    power_table_q[exponent + 1] = (power_table_q[exponent] * base_q) % modulus

read_line_from_stdin = sys.stdin.readline
write_to_stdout = sys.stdout.write

def compute_2d_polynomial_hash(matrix, matrix_width, matrix_height):
    hash_matrix = [[0] * (matrix_width + 1) for _ in range(matrix_height + 1)]
    for row_index in range(matrix_height):
        rolling_hash_in_row = 0
        previous_row_hashes = hash_matrix[row_index]
        current_row_hashes = hash_matrix[row_index + 1]
        current_row = matrix[row_index]
        for column_index in range(matrix_width):
            rolling_hash_in_row = (rolling_hash_in_row * base_p + current_row[column_index]) % modulus
            current_row_hashes[column_index + 1] = (rolling_hash_in_row + previous_row_hashes[column_index + 1] * base_q) % modulus
    return hash_matrix

def extract_submatrix_hash(polynomial_hash_matrix, x_start, y_start, x_end, y_end):
    hash_power_p = power_table_p[x_end - x_start]
    hash_power_q = power_table_q[y_end - y_start]
    total_hash = (polynomial_hash_matrix[y_end][x_end] -
                  polynomial_hash_matrix[y_end][x_start] * hash_power_p -
                  polynomial_hash_matrix[y_start][x_end] * hash_power_q +
                  (polynomial_hash_matrix[y_start][x_start] * (hash_power_p * hash_power_q) % modulus)) % modulus
    return total_hash

def rotate_matrix_90_degrees_clockwise(original_matrix, matrix_width, matrix_height):
    rotated_matrix = [[0] * matrix_height for _ in range(matrix_width)]
    for row_index in range(matrix_height):
        for column_index in range(matrix_width):
            rotated_matrix[column_index][matrix_height - 1 - row_index] = original_matrix[row_index][column_index]
    return rotated_matrix

def mirror_matrix_horizontally(original_matrix, matrix_width, matrix_height):
    mirrored_matrix = [[0] * matrix_width for _ in range(matrix_height)]
    for row_index in range(matrix_height):
        for column_index in range(matrix_width):
            mirrored_matrix[row_index][matrix_width - 1 - column_index] = original_matrix[row_index][column_index]
    return mirrored_matrix

def solve_test_case():
    input_matrix_width, input_matrix_height, pattern_size = map(int, read_line_from_stdin().split())
    if input_matrix_width == 0 and input_matrix_height == 0 and pattern_size == 0:
        return False

    base64_character_index = base64_character_set.index

    main_matrix_boolean_rows = []
    for row in range(input_matrix_height):
        raw_row_string = read_line_from_stdin().strip()
        boolean_row = []
        for character in raw_row_string:
            character_value = base64_character_index(character)
            for bit_position in range(5, -1, -1):
                boolean_row.append(int((character_value & (1 << bit_position)) > 0))
        main_matrix_boolean_rows.append(boolean_row)

    pattern_matrix_boolean_rows = []
    for row in range(pattern_size):
        raw_pattern_row_string = read_line_from_stdin().strip()
        pattern_row = []
        for character in raw_pattern_row_string:
            character_value = base64_character_index(character)
            for bit_position in range(5, -1, -1):
                pattern_row.append(int((character_value & (1 << bit_position)) > 0))
        pattern_matrix_boolean_rows.append(pattern_row)

    original_pattern_matrix = pattern_matrix_boolean_rows

    all_pattern_hash_variants = set()
    pattern_matrix = original_pattern_matrix
    for rotation in range(4):
        pattern_hash_matrix = compute_2d_polynomial_hash(pattern_matrix, pattern_size, pattern_size)
        all_pattern_hash_variants.add(pattern_hash_matrix[-1][-1])
        pattern_matrix = rotate_matrix_90_degrees_clockwise(pattern_matrix, pattern_size, pattern_size)

    pattern_matrix = mirror_matrix_horizontally(original_pattern_matrix, pattern_size, pattern_size)
    for rotation in range(4):
        pattern_hash_matrix = compute_2d_polynomial_hash(pattern_matrix, pattern_size, pattern_size)
        all_pattern_hash_variants.add(pattern_hash_matrix[-1][-1])
        pattern_matrix = rotate_matrix_90_degrees_clockwise(pattern_matrix, pattern_size, pattern_size)

    main_matrix_hash = compute_2d_polynomial_hash(main_matrix_boolean_rows, input_matrix_width, input_matrix_height)

    total_pattern_occurrences = 0
    for top_left_row in range(input_matrix_height - pattern_size + 1):
        for top_left_column in range(input_matrix_width - pattern_size + 1):
            submatrix_hash = extract_submatrix_hash(
                main_matrix_hash,
                top_left_column,
                top_left_row,
                top_left_column + pattern_size,
                top_left_row + pattern_size
            )
            if submatrix_hash in all_pattern_hash_variants:
                total_pattern_occurrences += 1

    write_to_stdout(f"{total_pattern_occurrences}\n")
    return True

while solve_test_case():
    pass