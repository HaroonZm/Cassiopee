import sys

input_stream = sys.stdin.readline
output_stream = sys.stdout.write

def count_possible_strings():
    MODULO_BASE = 10**9 + 7

    number_of_strings = int(input_stream())
    max_string_length = 20
    number_of_letters_in_alphabet = 26

    ascii_code_for_lower_a = ord('a')
    ascii_code_for_question_mark = ord('?')

    # Initialize matrix to store character codes for each string, padding with 'a'-1
    character_code_matrix = [
        [ascii_code_for_lower_a - 1] * max_string_length 
        for _ in range(number_of_strings)
    ]

    # Populate character code matrix by converting input strings to character codes
    for string_index in range(number_of_strings):
        input_string = input_stream().strip()
        for character_position, character in enumerate(input_string):
            character_code_matrix[string_index][character_position] = ord(character)

    # Memoization table for dynamic programming:
    # Dimensions: [start_idx][end_idx][current_position][current_char_or_state]
    memoized_results = [
        [
            [
                [-1] * (number_of_letters_in_alphabet + 2) 
                for _ in range(max_string_length + 1)
            ] 
            for _ in range(number_of_strings + 1)
        ] 
        for _ in range(number_of_strings + 1)
    ]

    # Initialize base cases where interval length is zero
    for start_idx in range(number_of_strings + 1):
        for current_position in range(max_string_length + 1):
            for char_state in range(number_of_letters_in_alphabet + 2):
                memoized_results[start_idx][start_idx][current_position][char_state] = 1

    # Initialize additional base cases
    for start_idx in range(number_of_strings + 1):
        for end_idx in range(start_idx + 1, number_of_strings + 1):
            for current_position in range(max_string_length + 1):
                memoized_results[start_idx][end_idx][current_position][number_of_letters_in_alphabet + 1] = 0
            for char_state in range(number_of_letters_in_alphabet + 2):
                memoized_results[start_idx][end_idx][max_string_length][char_state] = (start_idx + 1 == end_idx)

    def compute_dp_result(start_idx, end_idx, current_position, char_state):
        if memoized_results[start_idx][end_idx][current_position][char_state] != -1:
            return memoized_results[start_idx][end_idx][current_position][char_state]

        total_count = compute_dp_result(start_idx, end_idx, current_position, char_state + 1)

        for split_point in range(start_idx + 1, end_idx + 1):
            current_char_code = character_code_matrix[split_point - 1][current_position]
            expected_char_code = ascii_code_for_lower_a + char_state - 1

            if current_char_code != ascii_code_for_question_mark:
                if current_char_code != expected_char_code:
                    break
            else:
                if char_state == 0:
                    break

            left_count = compute_dp_result(start_idx, split_point, current_position + 1, 0)
            right_count = compute_dp_result(split_point, end_idx, current_position, char_state + 1)

            total_count += (left_count * right_count) % MODULO_BASE
            total_count %= MODULO_BASE

        memoized_results[start_idx][end_idx][current_position][char_state] = total_count % MODULO_BASE
        return memoized_results[start_idx][end_idx][current_position][char_state]

    answer = compute_dp_result(0, number_of_strings, 0, 0)

    output_stream("%d\n" % answer)

count_possible_strings()