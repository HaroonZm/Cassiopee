import sys
import numpy as np

# Systematic input function names
input_buffer = sys.stdin.buffer.read
input_line = sys.stdin.buffer.readline
input_lines = sys.stdin.buffer.readlines

# Systematic constants
MOD_CONST = 998244353

# Parse inputs with systematic variable names
input_values = input_buffer().split()
param_n = int(input_values[0])
param_x = int(input_values[1])

# Systematic function for cumulative product with modulus
def cumulative_product_mod(arr, mod_const):
    arr_length = len(arr)
    block_size = int(arr_length ** 0.5 + 1)
    arr_reshaped = np.resize(arr, block_size ** 2).reshape(block_size, block_size)
    for col in range(1, block_size):
        arr_reshaped[:, col] *= arr_reshaped[:, col - 1]
        arr_reshaped[:, col] %= mod_const
    for row in range(1, block_size):
        arr_reshaped[row] *= arr_reshaped[row - 1, -1]
        arr_reshaped[row] %= mod_const
    return arr_reshaped.ravel()[:arr_length]

# Systematic function for factorial arrays and inverses
def factorial_and_inverse_array(upper_bound, mod_const):
    arr_factorial = np.arange(upper_bound, dtype=np.int64)
    arr_factorial[0] = 1
    factorial_array = cumulative_product_mod(arr_factorial, mod_const)
    arr_inverse = np.arange(upper_bound, 0, -1, dtype=np.int64)
    arr_inverse[0] = pow(int(factorial_array[-1]), mod_const - 2, mod_const)
    factorial_inverse_array = cumulative_product_mod(arr_inverse, mod_const)[::-1]
    return factorial_array, factorial_inverse_array

# Systematic precomputation for factorials and combinations
upper_for_precompute = param_n + param_n + 100
factorial_arr, factorial_inv_arr = factorial_and_inverse_array(upper_for_precompute, MOD_CONST)
combinations_n = factorial_arr[param_n] * factorial_inv_arr[:param_n + 1] % MOD_CONST * factorial_inv_arr[param_n::-1] % MOD_CONST

# Systematic polynomial power function with modulus restriction
def polynomial_sum_below_x(length_n, limit_x):
    def poly_mult(poly_a, poly_b):
        deg_a = len(poly_a) - 1
        deg_b = len(poly_b) - 1
        if deg_a < deg_b:
            deg_a, deg_b = deg_b, deg_a
            poly_a, poly_b = poly_b, poly_a
        result = np.zeros(deg_a + deg_b + 1, np.int64)
        for idx in range(deg_b + 1):
            result[idx:idx + deg_a + 1] += poly_b[idx] * poly_a % MOD_CONST
        result %= MOD_CONST
        return result[:limit_x]
    def poly_power(poly, exponent):
        if exponent == 0:
            return np.array([1], dtype=np.int64)
        half = poly_power(poly, exponent // 2)
        squared = poly_mult(half, half)
        return poly_mult(poly, squared) if exponent & 1 else squared
    base_poly = np.array([1, 1, 1], np.int64)
    raised_poly = poly_power(base_poly, length_n)
    return raised_poly.sum() % MOD_CONST

# Systematic function for type 2 sum
def polynomial_type2_sum(length_n, limit_x):
    acc_array = np.zeros(length_n + 1, np.int64)
    for loop_n in range(limit_x):
        m_val = (limit_x - 1) - (2 + 2 * loop_n)
        if m_val < 0:
            break
        two_arr = np.arange(m_val // 2 + 1, dtype=np.int64)
        one_arr = m_val - 2 * two_arr
        coefficient = factorial_arr[one_arr + two_arr] * factorial_inv_arr[one_arr] % MOD_CONST * factorial_inv_arr[two_arr] % MOD_CONST
        rest_term = length_n - one_arr - two_arr - (2 * loop_n + 2)
        valid_index = rest_term >= 0
        rest_term = rest_term[valid_index]
        coef_valid = coefficient[valid_index]
        acc_array[rest_term] += coef_valid
    acc_array %= MOD_CONST
    return (acc_array * combinations_n % MOD_CONST).sum() % MOD_CONST

# Systematic function for type 3 sum
def polynomial_type3_sum(length_n, limit_x):
    if limit_x % 2 == 0:
        return 0
    if limit_x > length_n:
        return 0
    valid_count = length_n - limit_x + 1
    return combinations_n[:valid_count].sum() % MOD_CONST

# Systematic main calculation and output
result_total = (
    polynomial_sum_below_x(param_n, param_x) +
    polynomial_type2_sum(param_n, param_x) +
    polynomial_type3_sum(param_n, param_x)
) % MOD_CONST
print(result_total)