def encode_run_length(sequence):

    encoded_sequence = ""
    current_character = sequence[0]
    current_count = 1

    for index in range(1, len(sequence)):

        if sequence[index] == current_character:
            current_count += 1

        else:
            encoded_sequence += str(current_count) + current_character
            current_character = sequence[index]
            current_count = 1

    encoded_sequence += str(current_count) + current_character

    return encoded_sequence


while True:

    input_iterations = input()
    if input_iterations == 0:
        break

    input_sequence = raw_input()

    for iteration_index in range(input_iterations):
        input_sequence = encode_run_length(input_sequence)

    print input_sequence