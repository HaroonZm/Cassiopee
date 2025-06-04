user_input_string = raw_input()

number_of_valid_partitions = 0

for current_index in range(len(user_input_string)):

    is_zero_and_not_last_digit = user_input_string[current_index] == "0" and current_index != len(user_input_string) - 1

    if is_zero_and_not_last_digit:
        continue

    left_split_integer = int(user_input_string[:current_index]) if current_index else 0

    right_split_integer = int(user_input_string[current_index:])

    is_non_decreasing_split = left_split_integer <= right_split_integer

    is_same_parity = left_split_integer % 2 == right_split_integer % 2

    if is_non_decreasing_split and is_same_parity:
        number_of_valid_partitions += 1

print number_of_valid_partitions