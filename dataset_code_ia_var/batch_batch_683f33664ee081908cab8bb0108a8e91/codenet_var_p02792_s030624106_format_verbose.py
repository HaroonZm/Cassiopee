total_range_limit = int(input())


def find_numbers_with_first_and_last_digit_matching(first_digit, last_digit, max_limit):

    matching_numbers = []

    for candidate_number in range(1, max_limit + 1):

        candidate_number_str = str(candidate_number)

        if (candidate_number_str[0] == str(first_digit)) and (candidate_number_str[-1] == str(last_digit)):
            matching_numbers.append(candidate_number)

    return matching_numbers



total_valid_pairs = 0

for starting_digit in range(10):

    for ending_digit in range(10):

        numbers_starting_with_start_and_ending_with_end = find_numbers_with_first_and_last_digit_matching(
            starting_digit, ending_digit, total_range_limit
        )

        numbers_starting_with_end_and_ending_with_start = find_numbers_with_first_and_last_digit_matching(
            ending_digit, starting_digit, total_range_limit
        )

        total_valid_pairs += len(numbers_starting_with_start_and_ending_with_end) * len(numbers_starting_with_end_and_ending_with_start)

print(total_valid_pairs)