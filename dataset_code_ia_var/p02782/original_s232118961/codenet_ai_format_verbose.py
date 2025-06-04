MODULUS = 10 ** 9 + 7

def precompute_factorials_and_inverses(maximum_n):
    """
    Pré-calcule les factorielles modulo MODULUS et leurs inverses modulaires jusqu'à maximum_n, inclus.
    """
    factorial_modulo_list = [0] * (maximum_n + 1)
    factorial_modulo_list[0] = 1

    for integer_value in range(maximum_n):
        factorial_modulo_list[integer_value + 1] = (factorial_modulo_list[integer_value] * (integer_value + 1)) % MODULUS

    inverse_modulo_list = [1] * (maximum_n + 1)
    inverse_modulo_list[maximum_n] = pow(factorial_modulo_list[maximum_n], MODULUS - 2, MODULUS)

    for integer_value in range(maximum_n, 1, -1):
        inverse_modulo_list[integer_value - 1] = (inverse_modulo_list[integer_value] * integer_value) % MODULUS

    return factorial_modulo_list, inverse_modulo_list

def compute_binomial_modulo(sum_index, first_index):
    """
    Calcule C(sum_index, first_index) modulo MODULUS à l'aide des listes pré-calculées.
    """
    factorial_sum = precomputed_factorials[sum_index]
    factorial_first_inverse = precomputed_inverses[first_index]
    factorial_second_inverse = precomputed_inverses[sum_index - first_index]
    binomial_modulo = (factorial_sum * factorial_first_inverse * factorial_second_inverse) % MODULUS
    return binomial_modulo

def compute_sum_for_range(start_row, end_row, column_value):
    """
    Additionne les valeurs du binôme (x + 1, column_value) pour x dans l'intervalle [start_row, end_row].
    """
    cumulative_sum_modulo = 0

    for row_index in range(start_row, end_row + 1):
        binomial_result = compute_binomial_modulo(row_index + column_value + 1, row_index + 1)
        cumulative_sum_modulo = (cumulative_sum_modulo + binomial_result) % MODULUS

    return cumulative_sum_modulo

input_row1, input_column1, input_row2, input_column2 = map(int, input().split())

maximum_index = max(input_row1, input_row2, input_column1, input_column2) * 2 + 2

precomputed_factorials, precomputed_inverses = precompute_factorials_and_inverses(maximum_index)

sum_over_right_rectangle = compute_sum_for_range(input_row1, input_row2, input_column2)
sum_over_left_rectangle = compute_sum_for_range(input_row1, input_row2, input_column1 - 1)

final_result = (sum_over_right_rectangle - sum_over_left_rectangle) % MODULUS

print(final_result)