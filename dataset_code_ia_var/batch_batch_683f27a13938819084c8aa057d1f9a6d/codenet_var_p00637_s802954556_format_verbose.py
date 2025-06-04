while True:

    number_of_elements = input()

    if number_of_elements == 0:
        break

    input_sequence = map(int, raw_input().split())

    start_of_sequence = input_sequence[0]
    condensed_ranges = []

    for current_index in range(number_of_elements - 1):

        current_value = input_sequence[current_index]
        next_value = input_sequence[current_index + 1]

        if current_value + 1 != next_value:

            if start_of_sequence != current_value:
                condensed_ranges.append(str(start_of_sequence) + "-" + str(current_value))
            else:
                condensed_ranges.append(str(start_of_sequence))

            start_of_sequence = next_value

    else:
        last_value = input_sequence[-1]
        if start_of_sequence != last_value:
            condensed_ranges.append(str(start_of_sequence) + "-" + str(last_value))
        else:
            condensed_ranges.append(str(start_of_sequence))

    print " ".join(condensed_ranges)