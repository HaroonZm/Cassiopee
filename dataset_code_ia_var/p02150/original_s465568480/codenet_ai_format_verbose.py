first_value, decrement_value, maximum_value = [int(number_string) for number_string in input().split()]

difference_per_iteration = first_value - decrement_value

number_of_iterations = max(0, (maximum_value - decrement_value)) // difference_per_iteration

final_sum = maximum_value + number_of_iterations * decrement_value

MODULO_CONSTANT = 1000000007

print(final_sum % MODULO_CONSTANT)