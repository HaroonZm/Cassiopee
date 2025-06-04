def encode_sequence(input_sequence):
    output_sequence = ""
    current_char = input_sequence[0]
    current_count = 1
    for sequence_index in range(1, len(input_sequence)):
        if input_sequence[sequence_index] == current_char:
            current_count += 1
        else:
            output_sequence += str(current_count) + current_char
            current_char = input_sequence[sequence_index]
            current_count = 1
    output_sequence += str(current_count) + current_char
    return output_sequence

while True:
    iteration_count = input()
    if iteration_count == 0:
        break
    sequence_data = raw_input()
    for iteration_index in range(iteration_count):
        sequence_data = encode_sequence(sequence_data)
    print sequence_data