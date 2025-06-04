def compute_factorials_and_inverse_factorials(maximum_value, modulo):
    factorial_list = [1] * (maximum_value + 1)
    for integer_value in range(2, maximum_value + 1):
        factorial_list[integer_value] = factorial_list[integer_value - 1] * integer_value % modulo

    inverse_factorial_list = [1] * (maximum_value + 1)
    inverse_factorial_list[maximum_value] = pow(factorial_list[maximum_value], modulo - 2, modulo)
    for integer_value in range(maximum_value, 1, -1):
        inverse_factorial_list[integer_value - 1] = inverse_factorial_list[integer_value] * integer_value % modulo

    return factorial_list, inverse_factorial_list

def compute_result(number_of_elements, number_of_special_items):
    modulo_value = 10 ** 9 + 7

    factorials, inverse_factorials = compute_factorials_and_inverse_factorials(number_of_elements, modulo_value)

    inverse_list = [ factorials[current_index - 1] * inverse_factorials[current_index] % modulo_value for current_index in range(number_of_elements + 1) ]
    remaining_elements = number_of_elements - number_of_special_items

    total_combinations = 0

    # Configuration where none of the special items has a self-loop
    for number_of_fixed_points in range(number_of_special_items):
        combinations_of_special_items = factorials[number_of_special_items] * inverse_factorials[number_of_fixed_points] % modulo_value * inverse_factorials[number_of_special_items - number_of_fixed_points] % modulo_value
        arrangements_of_non_fixed_points = factorials[number_of_elements - number_of_fixed_points - 1] * (number_of_special_items - number_of_fixed_points) % modulo_value

        contribution = ((-1) ** (number_of_fixed_points & 1)) * combinations_of_special_items * arrangements_of_non_fixed_points
        total_combinations = (total_combinations + contribution) % modulo_value

    # Configuration where first k items among the special items have no self-loop, and the (k+1)-th gets the first self-loop
    for number_of_items_with_no_self_loop in range(1, number_of_special_items):
        for number_of_fixed_points in range(number_of_items_with_no_self_loop):
            combinations_of_items = factorials[number_of_items_with_no_self_loop] * inverse_factorials[number_of_fixed_points] % modulo_value * inverse_factorials[number_of_items_with_no_self_loop - number_of_fixed_points] % modulo_value
            arrangements = factorials[number_of_elements - number_of_fixed_points - 1] * (number_of_items_with_no_self_loop - number_of_fixed_points) % modulo_value
            arrangements = arrangements * inverse_list[remaining_elements + number_of_items_with_no_self_loop - number_of_fixed_points] % modulo_value

            contribution = ((-1) ** (number_of_fixed_points & 1)) * combinations_of_items * arrangements
            total_combinations = (total_combinations + contribution) % modulo_value

    return total_combinations

input_number_of_elements, input_number_of_special_items = map(int, input().split())
print(compute_result(input_number_of_elements, input_number_of_special_items))