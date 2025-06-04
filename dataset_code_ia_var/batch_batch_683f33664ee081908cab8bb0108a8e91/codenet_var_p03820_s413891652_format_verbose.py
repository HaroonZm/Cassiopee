import sys
import numpy as np
import numba
from numba import njit, i8

BYTE_INPUT_READ = sys.stdin.buffer.read

MODULO_CONSTANT = 1_000_000_007

@njit((i8, i8), cache=True)
def compute_combinatorial_result(total_elements, subsequence_length):
    subsequence_length_adjusted = subsequence_length - 1
    
    COMB_MATRIX_SIZE = 2010
    binomial_coefficients = np.zeros((COMB_MATRIX_SIZE, COMB_MATRIX_SIZE), np.int64)
    binomial_coefficients[0, 0] = 1

    # Precompute binomial coefficients
    for row in range(1, COMB_MATRIX_SIZE):
        binomial_coefficients[row] += binomial_coefficients[row - 1]
        binomial_coefficients[row, 1:] += binomial_coefficients[row - 1, :-1]
        binomial_coefficients[row] %= MODULO_CONSTANT

    DP_MAX_INDEX = total_elements + 10
    dynamic_programming_table = np.zeros((DP_MAX_INDEX, DP_MAX_INDEX), np.int64)
    dynamic_programming_table[0, 0] = 1

    # Build DP table
    for n_val in range(1, DP_MAX_INDEX):
        dynamic_programming_table[n_val, n_val] = (
            dynamic_programming_table[n_val - 1, n_val - 1] + dynamic_programming_table[n_val - 1, n_val]
        ) % MODULO_CONSTANT
        for m_val in range(n_val + 1, DP_MAX_INDEX):
            dynamic_programming_table[n_val, m_val] = (
                dynamic_programming_table[n_val - 1, m_val] +
                dynamic_programming_table[n_val, m_val - 1]
            ) % MODULO_CONSTANT

    # Reduce DP values
    for descending_index in range(DP_MAX_INDEX - 1, 0, -1):
        dynamic_programming_table[descending_index] -= dynamic_programming_table[descending_index - 1]
        dynamic_programming_table[descending_index] %= MODULO_CONSTANT

    result = 0

    if subsequence_length_adjusted == total_elements - 1:
        return dynamic_programming_table[:total_elements, total_elements - 1].sum() % MODULO_CONSTANT

    for number_of_selected_elements in range(total_elements - subsequence_length_adjusted, total_elements + 1):
        ways_to_choose_elements = binomial_coefficients[number_of_selected_elements - 2, total_elements - subsequence_length_adjusted - 2]
        count_of_elements_a = total_elements - number_of_selected_elements
        count_of_elements_b = subsequence_length_adjusted - count_of_elements_a
        if count_of_elements_b == 0:
            ways_to_choose_elements = (
                ways_to_choose_elements *
                (dynamic_programming_table[:count_of_elements_a + 1, count_of_elements_a].sum() % MODULO_CONSTANT)
            ) % MODULO_CONSTANT
        else:
            dp_slice = dynamic_programming_table[1:count_of_elements_a + 2, count_of_elements_a + 1]
            comb_slice = binomial_coefficients[count_of_elements_b - 1:count_of_elements_a + count_of_elements_b, count_of_elements_b - 1][::-1]
            multiplied_sum = (dp_slice * comb_slice % MODULO_CONSTANT).sum() % MODULO_CONSTANT
            ways_to_choose_elements = (ways_to_choose_elements * multiplied_sum) % MODULO_CONSTANT
        result += ways_to_choose_elements

    result %= MODULO_CONSTANT

    for power_of_two_multiplier in range(total_elements - subsequence_length_adjusted - 2):
        result = (result * 2) % MODULO_CONSTANT

    return result % MODULO_CONSTANT

input_total_elements, input_subsequence_length = map(int, BYTE_INPUT_READ().split())
print(compute_combinatorial_result(input_total_elements, input_subsequence_length))