def compute_modular_inverses_list(size_max:int, modulus:int) -> list:
    modular_inverse_list = [0, 1]
    for current_index in range(2, size_max + 1):
        modular_inverse_list.append(
            modulus - (modulus // current_index) * modular_inverse_list[modulus % current_index] % modulus
        )
    return modular_inverse_list

def compute_factorials_list(size_max:int, modulus:int) -> list:
    factorial_list = [1, 1]
    factorial_current = 1
    for current_index in range(2, size_max + 1):
        factorial_current = factorial_current * current_index % modulus
        factorial_list.append(factorial_current)
    return factorial_list

def compute_factorials_inverse_list(size_max:int, modular_inverse_list:list, modulus:int) -> list:
    factorial_inverse_list = [1, 1]
    for current_index in range(2, size_max + 1):
        factorial_inverse_list.append(
            factorial_inverse_list[current_index - 1] * modular_inverse_list[current_index] % modulus
        )
    return factorial_inverse_list

def compute_binomial_coefficient(n_value:int, r_value:int, modulus:int, factorial_list:list, factorial_inverse_list:list) -> int:
    if not (0 <= r_value <= n_value):
        return 0
    return (factorial_list[n_value] * factorial_inverse_list[r_value] % modulus) * factorial_inverse_list[n_value - r_value] % modulus

MODULUS_CONST = 10**9 + 7
MAX_SIZE = 2 * 10**5 + 1

height_size, width_size, blocked_row_count, blocked_column_count = map(int, input().split())

modular_inverse_list = compute_modular_inverses_list(MAX_SIZE, MODULUS_CONST)
factorial_list = compute_factorials_list(MAX_SIZE, MODULUS_CONST)
factorial_inverse_list = compute_factorials_inverse_list(MAX_SIZE, modular_inverse_list, MODULUS_CONST)

result_sum = 0
for current_height in range(height_size - blocked_row_count):
    left_comb = compute_binomial_coefficient(
        current_height + (blocked_column_count - 1), current_height, MODULUS_CONST, factorial_list, factorial_inverse_list
    )
    right_comb = compute_binomial_coefficient(
        (height_size - current_height - 1) + (width_size - blocked_column_count - 1),
        width_size - blocked_column_count - 1,
        MODULUS_CONST,
        factorial_list,
        factorial_inverse_list
    )
    result_sum = (result_sum + left_comb * right_comb) % MODULUS_CONST

print(result_sum)