number_of_iterations = int(input())

for current_iteration_index in range(number_of_iterations):

    differing_bit_positions = []

    binary_current_iteration = '0' * (11 - len(bin(current_iteration_index))) + bin(current_iteration_index)[2:]

    for comparison_index in range(current_iteration_index + 1, number_of_iterations):

        binary_comparison = '0' * (11 - len(bin(comparison_index))) + bin(comparison_index)[2:]

        for bit_position in range(9):

            if binary_current_iteration[bit_position] != binary_comparison[bit_position]:

                differing_bit_positions.append(9 - bit_position)
                break

    stringified_positions = list(map(str, differing_bit_positions))
    print(' '.join(stringified_positions))