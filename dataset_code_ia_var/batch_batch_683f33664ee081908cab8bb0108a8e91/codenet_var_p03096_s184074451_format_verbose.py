MODULO_CONSTANT = 10**9 + 7

number_of_inputs = int(input())

color_input_sequence = []

for input_index in range(number_of_inputs):
    current_color = int(input())
    color_input_sequence.append(current_color)

compressed_color_sequence = color_input_sequence[:1]

for sequence_index in range(1, number_of_inputs):
    if color_input_sequence[sequence_index] != compressed_color_sequence[-1]:
        compressed_color_sequence.append(color_input_sequence[sequence_index])

length_of_compressed_sequence = len(compressed_color_sequence)

color_to_indices_map = {}

for compressed_index in range(length_of_compressed_sequence):
    color_value = compressed_color_sequence[compressed_index]
    if color_value not in color_to_indices_map:
        color_to_indices_map[color_value] = [compressed_index]
    else:
        color_to_indices_map[color_value].append(compressed_index)

dynamic_programming_ways = [1] + [0] * (length_of_compressed_sequence - 1)

for dp_index in range(1, length_of_compressed_sequence):
    current_color = compressed_color_sequence[dp_index]
    dynamic_programming_ways[dp_index] = dynamic_programming_ways[dp_index - 1]

    indices_list_for_current_color = color_to_indices_map[current_color]

    if len(indices_list_for_current_color) < 5:
        for reversed_index in reversed(indices_list_for_current_color):
            if reversed_index < dp_index:
                dynamic_programming_ways[dp_index] += dynamic_programming_ways[reversed_index]
                break
    else:
        left_pointer = 0
        right_pointer = len(indices_list_for_current_color)
        while left_pointer <= right_pointer:
            middle_index = (left_pointer + right_pointer) // 2
            if indices_list_for_current_color[middle_index] < dp_index and indices_list_for_current_color[middle_index + 1] >= dp_index:
                dynamic_programming_ways[dp_index] += dynamic_programming_ways[indices_list_for_current_color[middle_index]]
                break
            elif indices_list_for_current_color[middle_index] >= dp_index:
                right_pointer = middle_index - 1
            elif indices_list_for_current_color[middle_index + 1] < dp_index:
                left_pointer = middle_index + 1
            else:
                print("error")

print(dynamic_programming_ways[-1] % MODULO_CONSTANT)