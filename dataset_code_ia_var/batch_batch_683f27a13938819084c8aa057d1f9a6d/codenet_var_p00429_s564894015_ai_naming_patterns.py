def generate_sequence(sequence, iterations):
    for iteration_index in range(iterations):
        next_sequence = ""
        current_char = sequence[0]
        current_count = 1
        for char_index in range(1, len(sequence)):
            if sequence[char_index] == current_char:
                current_count += 1
            else:
                next_sequence += str(current_count) + current_char
                current_char = sequence[char_index]
                current_count = 1
        sequence = next_sequence + str(current_count) + current_char
    return sequence

while True:
    iteration_input = input()
    if iteration_input == "0":
        break
    sequence_input = raw_input()
    print generate_sequence(sequence_input, int(iteration_input))