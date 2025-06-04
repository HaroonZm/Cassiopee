total_number_of_elements, selection_limit = map(int, input().split())

modulo = 10 ** 9 + 7

factorial_combination_from_n = [1] * (total_number_of_elements)

for current_index in range(total_number_of_elements - 1):
    numerator = factorial_combination_from_n[current_index] * (total_number_of_elements - current_index)
    denominator_inverse = pow(current_index + 1, modulo - 2, modulo)
    factorial_combination_from_n[current_index + 1] = numerator * denominator_inverse % modulo

factorial_combination_from_n_minus_one = [1] * (total_number_of_elements)

for current_index in range(total_number_of_elements - 1):
    numerator = factorial_combination_from_n_minus_one[current_index] * (total_number_of_elements - 1 - current_index)
    denominator_inverse = pow(current_index + 1, modulo - 2, modulo)
    factorial_combination_from_n_minus_one[current_index + 1] = numerator * denominator_inverse % modulo

final_summation_result = 0

maximum_possible_selection = min(total_number_of_elements - 1, selection_limit)

for combination_size in range(maximum_possible_selection + 1):
    product_of_combinations = (
        factorial_combination_from_n[combination_size] *
        factorial_combination_from_n_minus_one[combination_size]
    )
    final_summation_result += product_of_combinations
    final_summation_result %= modulo

print(final_summation_result)