from numba import njit
import numpy as np

@njit('i8(i8, i8, i8)', cache=True)
def modular_exponentiation(base_value, exponent_value, modulus_value):
    """
    Calculate (base_value ** exponent_value) % modulus_value efficiently using binary exponentiation.
    """
    result = 1
    current_base = base_value

    while exponent_value:
        if exponent_value & 1:
            result = result * current_base % modulus_value
        current_base = current_base * current_base % modulus_value
        exponent_value >>= 1

    return result

@njit('UniTuple(i8[:], 2)(i8, i8)', cache=True)
def compute_factorials_and_inverse_factorials(maximum_value, modulus_value):
    """
    Prepare arrays of factorials and inverse factorials modulo modulus_value up to maximum_value.
    """
    factorial_values = np.ones(maximum_value + 1, dtype=np.int64)

    for index in range(2, maximum_value + 1):
        factorial_values[index] = factorial_values[index - 1] * index % modulus_value

    inverse_factorial_values = np.ones(maximum_value + 1, dtype=np.int64)
    inverse_factorial_values[maximum_value] = modular_exponentiation(factorial_values[maximum_value], modulus_value - 2, modulus_value)

    for index in range(maximum_value, 1, -1):
        inverse_factorial_values[index - 1] = inverse_factorial_values[index] * index % modulus_value

    return factorial_values, inverse_factorial_values

@njit('i8(i8, i8)', cache=True)
def compute_result(total_elements, subset_size):
    modulus_constant = 10 ** 9 + 7

    factorial_array, inverse_factorial_array = compute_factorials_and_inverse_factorials(total_elements, modulus_constant)

    modular_inverse_array = [factorial_array[index - 1] * inverse_factorial_array[index] % modulus_constant for index in range(total_elements + 1)]
    remaining_elements = total_elements - subset_size

    total_answer = 0

    # Case 1: All 'subset_size' elements do not have self-loops
    for excluded_elements_count in range(subset_size):
        ways_choose_l = factorial_array[subset_size] * inverse_factorial_array[excluded_elements_count] % modulus_constant * inverse_factorial_array[subset_size - excluded_elements_count] % modulus_constant
        ways_for_permutation = factorial_array[total_elements - excluded_elements_count - 1] * (subset_size - excluded_elements_count) % modulus_constant
        sign = (-1) ** (excluded_elements_count & 1)
        total_answer = (total_answer + sign * ways_choose_l * ways_for_permutation) % modulus_constant

    # Case 2: The (k+1)th out of 'subset_size' elements gets a self-loop for the first time, after k elements have all completed
    for prefix_length in range(1, subset_size):
        for excluded_elements_count in range(prefix_length):
            ways_choose_l = factorial_array[prefix_length] * inverse_factorial_array[excluded_elements_count] % modulus_constant * inverse_factorial_array[prefix_length - excluded_elements_count] % modulus_constant
            additional_term = factorial_array[total_elements - excluded_elements_count - 1] * (prefix_length - excluded_elements_count) % modulus_constant
            additional_term = additional_term * modular_inverse_array[remaining_elements + prefix_length - excluded_elements_count] % modulus_constant
            sign = (-1) ** (excluded_elements_count & 1)
            total_answer = (total_answer + sign * ways_choose_l * additional_term) % modulus_constant

    return total_answer

if __name__ == "__main__":

    input_total_elements, input_subset_size = map(int, input().split())

    print(compute_result(input_total_elements, input_subset_size))