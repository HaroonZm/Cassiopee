user_input_string = raw_input()

valid_pairs_count = 0

for current_index in range(len(user_input_string)):

    is_current_char_zero = (user_input_string[current_index] == "0")
    is_not_last_char = (current_index != len(user_input_string) - 1)

    if is_current_char_zero and is_not_last_char:
        continue

    if current_index == 0:
        left_substring_as_int = 0
    else:
        left_substring_as_int = int(user_input_string[:current_index])

    right_substring_as_int = int(user_input_string[current_index:])

    is_left_less_or_equal_right = (left_substring_as_int <= right_substring_as_int)
    is_left_and_right_same_parity = (left_substring_as_int % 2 == right_substring_as_int % 2)

    if is_left_less_or_equal_right and is_left_and_right_same_parity:
        valid_pairs_count += 1

print valid_pairs_count