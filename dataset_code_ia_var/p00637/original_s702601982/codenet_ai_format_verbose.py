while True:

    number_of_elements = int(input())

    if number_of_elements == 0:
        break

    sequence_of_numbers = list(map(int, input().split()))

    current_index = 0

    while current_index < number_of_elements:

        range_start_index = current_index

        while (
            range_start_index + 1 < number_of_elements
            and sequence_of_numbers[range_start_index + 1] - sequence_of_numbers[range_start_index] == 1
        ):
            range_start_index += 1

        is_last_output = number_of_elements - 1 == range_start_index

        output_separator = "\n" if is_last_output else " "

        if current_index == range_start_index:
            print(
                "{}{}".format(sequence_of_numbers[current_index], output_separator),
                end=''
            )
            current_index += 1
        else:
            print(
                "{}-{}{}".format(
                    sequence_of_numbers[current_index],
                    sequence_of_numbers[range_start_index],
                    output_separator
                ),
                end=''
            )
            current_index = range_start_index + 1