input_digits = list(input())
unknown_index = input_digits.index('?')
weight_pattern = [6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

weighted_sum = 0
for idx in range(11):
    if input_digits[idx] != '?':
        weighted_sum += int(input_digits[idx]) * weight_pattern[idx]

if unknown_index < 11:
    possible_values = []
    for digit_candidate in range(10):
        current_sum = weighted_sum + digit_candidate * weight_pattern[unknown_index]
        mod_value = current_sum % 11
        if mod_value <= 1:
            expected_control_digit = 0
        else:
            expected_control_digit = 11 - mod_value
        if expected_control_digit == int(input_digits[11]):
            possible_values.append(digit_candidate)
    if len(possible_values) == 1:
        print(possible_values[0])
    else:
        print('MULTIPLE')
elif unknown_index == 11:
    mod_value = weighted_sum % 11
    if mod_value <= 1:
        control_digit = 0
    else:
        control_digit = 11 - mod_value
    print(control_digit)