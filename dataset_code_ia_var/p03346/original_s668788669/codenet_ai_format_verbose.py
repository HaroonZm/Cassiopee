import sys

read_input_line = sys.stdin.readline

def read_integers_as_tuple():
    return map(int, read_input_line().split())

def read_integers_as_list():
    return list(read_integers_as_tuple())

def compute_factorials_up_to_n_with_modulo(max_value, modulo):
    factorial_sequence = [1]
    for integer in range(1, max_value + 1):
        factorial_sequence.append(factorial_sequence[-1] * integer % modulo)
    return factorial_sequence

precomputed_inverses = {}

def modular_inverse(value, modulo):
    if value in precomputed_inverses:
        return precomputed_inverses[value]
    inverse_result = pow(value, modulo - 2, modulo)
    precomputed_inverses[value] = inverse_result
    return inverse_result

def binomial_coefficient_with_modulo(factorial_sequence, total, choose, modulo):
    return (
        factorial_sequence[total] *
        modular_inverse(factorial_sequence[choose], modulo) *
        modular_inverse(factorial_sequence[total - choose], modulo)
    ) % modulo

def process_permutation_and_compute_result():
    number_of_elements = int(read_input_line())
    element_position_order = [0] * number_of_elements

    for input_index in range(number_of_elements):
        element_value = int(read_input_line()) - 1
        element_position_order[element_value] = input_index

    minimum_moves_required = 0
    current_increasing_sequence_length = 0
    previous_position = -1

    for current_position in element_position_order:
        if previous_position < current_position:
            current_increasing_sequence_length += 1
        else:
            minimum_moves_required = max(minimum_moves_required, current_increasing_sequence_length)
            current_increasing_sequence_length = 1
        previous_position = current_position

    minimum_moves_required = max(minimum_moves_required, current_increasing_sequence_length)
    print(number_of_elements - minimum_moves_required)

if __name__ == "__main__":
    process_permutation_and_compute_result()