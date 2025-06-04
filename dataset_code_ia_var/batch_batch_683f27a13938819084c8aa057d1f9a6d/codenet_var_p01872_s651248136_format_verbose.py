def is_valid_nir(nir_string_reversed):
    calculated_control_sum = 0

    for digit_position in range(1, 7):
        calculated_control_sum += int(nir_string_reversed[digit_position]) * (digit_position + 1)

    for digit_position in range(7, 12):
        calculated_control_sum += int(nir_string_reversed[digit_position]) * (digit_position - 5)

    control_key = 11 - (calculated_control_sum % 11)

    is_control_key_match = (str(control_key) == nir_string_reversed[0])
    is_alternative_zero_case = (control_key >= 10 and nir_string_reversed[0] == "0")

    return is_control_key_match or is_alternative_zero_case

def find_unique_missing_digit(original_nir_with_missing_digit):
    missing_digit_index = original_nir_with_missing_digit.index("?")
    number_of_valid_possibilities = 0
    valid_replacement_digit = None

    for candidate_digit in range(10):
        candidate_digit_str = str(candidate_digit)
        nir_with_candidate = (
            original_nir_with_missing_digit[:missing_digit_index]
            + candidate_digit_str
            + original_nir_with_missing_digit[missing_digit_index + 1:]
        )
        if is_valid_nir(nir_with_candidate):
            number_of_valid_possibilities += 1
            valid_replacement_digit = candidate_digit

    if number_of_valid_possibilities == 1:
        return valid_replacement_digit
    else:
        return None

input_nir_reversed = input()[::-1]
replacement_digit = find_unique_missing_digit(input_nir_reversed)

if replacement_digit is not None:
    print(replacement_digit)
else:
    print("MULTIPLE")