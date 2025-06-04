def is_type_a_pattern(middle_string):

    length_of_middle = len(middle_string)

    if length_of_middle % 2 == 0:
        return False

    index_of_central_char = (length_of_middle - 1) // 2

    for symmetric_index in range(index_of_central_char):
        if middle_string[symmetric_index] != "=" or middle_string[length_of_middle - 1 - symmetric_index] != "=":
            return False

    if middle_string[index_of_central_char] != "#":
        return False

    return True


def is_type_b_pattern(middle_string):

    length_of_middle = len(middle_string)

    if length_of_middle % 2 == 1:
        return False

    number_of_pairs = length_of_middle // 2

    for pair_index in range(number_of_pairs):
        if middle_string[2 * pair_index] != "Q" or middle_string[2 * pair_index + 1] != "=":
            return False

    return True


def determine_pattern_type(full_string):

    minimum_required_length = 6

    if len(full_string) < minimum_required_length:
        return "NA"

    if full_string.startswith(">'") and full_string.endswith("~"):
        middle_substring = full_string[2:-1]
        if is_type_a_pattern(middle_substring):
            return "A"
        else:
            return "NA"

    if full_string.startswith(">^") and full_string.endswith("~~"):
        middle_substring = full_string[2:-2]
        if is_type_b_pattern(middle_substring):
            return "B"
        else:
            return "NA"

    return "NA"


number_of_test_cases = int(input())

for test_case_index in range(number_of_test_cases):

    input_string = input()

    result = determine_pattern_type(input_string)

    print(result)