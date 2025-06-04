from numpy import array, ones, zeros

MODULUS = 10 ** 9 + 7

matrix_size = int(input())

input_matrix = array([input().split() for _ in range(matrix_size)], dtype="int8")

def compute_matrix_rank(binary_matrix):
    if (binary_matrix == 0).all():
        return 0

    non_zero_row_indices = binary_matrix[:, 0].nonzero()[0]
    if len(non_zero_row_indices) == 0:
        return compute_matrix_rank(binary_matrix[:, 1:])

    pivot_row = binary_matrix[non_zero_row_indices[0]].copy()
    binary_matrix[non_zero_row_indices[0]] = binary_matrix[0]
    binary_matrix[0] = pivot_row

    binary_matrix[1:] ^= binary_matrix[1:, 0][:, None] * binary_matrix[0][None, :]

    return 1 + compute_matrix_rank(binary_matrix[1:, 1:])

matrix_rank = compute_matrix_rank(input_matrix)

powers_of_two_mod = ones(matrix_size + 1, dtype="int64")

for exponent in range(1, matrix_size + 1):
    powers_of_two_mod[exponent] = powers_of_two_mod[exponent - 1] * 2 % MODULUS

dynamic_table = zeros((matrix_size + 1, matrix_size + 1, matrix_size + 1), dtype="int64")
dynamic_table[:, 0, 0] = 1

for submatrix_size in range(1, matrix_size + 1):
    dynamic_table[:, submatrix_size, :submatrix_size] += dynamic_table[:, submatrix_size - 1, :submatrix_size] * powers_of_two_mod[:submatrix_size] % MODULUS
    dynamic_table[:, submatrix_size, 1:submatrix_size + 1] += dynamic_table[:, submatrix_size - 1, 0:submatrix_size] * (powers_of_two_mod[:, None] - powers_of_two_mod[None, 0:submatrix_size]) % MODULUS
    dynamic_table[:, submatrix_size, :] %= MODULUS

inverse_dynamic_entry = pow(int(dynamic_table[matrix_size, matrix_size, matrix_rank]), MODULUS - 2, MODULUS)

total_sum = 0

for free_variables in range(matrix_rank, matrix_size + 1):
    term = (
        dynamic_table[matrix_size, matrix_size, free_variables]
        * dynamic_table[matrix_size, free_variables, matrix_rank]
        % MODULUS
        * pow(2, matrix_size * (matrix_size - free_variables), MODULUS)
        % MODULUS
    )
    total_sum = (total_sum + term) % MODULUS

final_result = total_sum * inverse_dynamic_entry % MODULUS

print(final_result)