import sys

standard_input_readline = sys.stdin.readline
standard_output_write = sys.stdout.write

def compute_polynomial_sum_with_constraints():
    MODULUS = 10 ** 9 + 7

    number_of_constraints = int(standard_input_readline())

    constraints_lengths = [
        int(standard_input_readline()) 
        for _ in range(number_of_constraints)
    ]

    target_sum = int(standard_input_readline())

    dynamic_programming_array = [0] * (target_sum + 1)
    dynamic_programming_array[target_sum] = 1

    for constraint_index in range(number_of_constraints):
        current_constraint_length = constraints_lengths[constraint_index]
        for partial_sum in range(current_constraint_length, target_sum + 1):
            dynamic_programming_array[partial_sum - current_constraint_length] -= dynamic_programming_array[partial_sum]

    total_result = 0

    for possible_sum in range(target_sum + 1):
        result_contribution = pow(
            possible_sum, 
            number_of_constraints, 
            MODULUS
        ) * dynamic_programming_array[possible_sum]
        total_result += result_contribution

    total_result %= MODULUS

    standard_output_write(f"{total_result}\n")

compute_polynomial_sum_with_constraints()