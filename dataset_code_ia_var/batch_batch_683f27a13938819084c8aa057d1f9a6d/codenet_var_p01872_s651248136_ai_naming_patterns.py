def validate_identifier(identifier_str):
    total_score = 0
    for position_idx in range(1, 7):
        total_score += int(identifier_str[position_idx]) * (position_idx + 1)
    for position_idx in range(7, 12):
        total_score += int(identifier_str[position_idx]) * (position_idx - 5)
    control_digit = 11 - total_score % 11
    if str(control_digit) == identifier_str[0] or (control_digit >= 10 and identifier_str[0] == "0"):
        return True
    return False

def resolve_missing_digit(identifier_with_missing):
    missing_idx = identifier_with_missing.index("?")
    valid_digits_count = 0
    valid_digit_value = None
    for candidate_digit in range(10):
        test_identifier = (
            identifier_with_missing[:missing_idx]
            + str(candidate_digit)
            + identifier_with_missing[missing_idx + 1 :]
        )
        if validate_identifier(test_identifier):
            valid_digits_count += 1
            valid_digit_value = candidate_digit
    if valid_digits_count == 1:
        return valid_digit_value
    return None

reversed_input_str = input()[::-1]
missing_digit_result = resolve_missing_digit(reversed_input_str)
print(missing_digit_result if missing_digit_result is not None else "MULTIPLE")