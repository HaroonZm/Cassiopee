while True:
    input_iterations = input()
    if input_iterations == 0:
        break
    current_sequence = raw_input() + ' '
    for iteration_index in range(input_iterations):
        consecutive_count = 1
        compressed_sequence = ''
        for char_index in range(len(current_sequence) - 1):
            if current_sequence[char_index] == current_sequence[char_index + 1]:
                consecutive_count += 1
            else:
                compressed_sequence += "%d%s" % (consecutive_count, current_sequence[char_index])
                consecutive_count = 1
        current_sequence = compressed_sequence + ' '
    print current_sequence.rstrip()