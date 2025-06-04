while True:

    number_of_lines = int(input())

    if number_of_lines == 0:
        break

    line_lengths = [
        len(input()) for current_line_index in range(number_of_lines)
    ]

    required_syllable_pattern = [5, 7, 5, 7, 7]

    minimal_starting_index_for_pattern = number_of_lines + 1

    for start_index in range(number_of_lines):

        syllable_pattern_index = 0
        current_syllable_sum = 0

        for end_index in range(start_index, number_of_lines):

            current_syllable_sum += line_lengths[end_index]

            if current_syllable_sum == required_syllable_pattern[syllable_pattern_index]:
                current_syllable_sum = 0
                syllable_pattern_index += 1

            elif current_syllable_sum > required_syllable_pattern[syllable_pattern_index]:
                break

            if syllable_pattern_index == 5:
                minimal_starting_index_for_pattern = min(
                    minimal_starting_index_for_pattern,
                    start_index + 1
                )
                break

    print(minimal_starting_index_for_pattern)