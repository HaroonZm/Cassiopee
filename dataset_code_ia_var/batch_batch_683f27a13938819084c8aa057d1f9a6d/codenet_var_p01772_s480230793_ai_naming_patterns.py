input_chars_list = list(input())
is_in_sequence = 1
sequence_count = 0
for current_char in input_chars_list:
    if current_char == 'A' and is_in_sequence:
        is_in_sequence = 0
    elif current_char == 'Z' and not is_in_sequence:
        is_in_sequence = 1
        sequence_count += 1
output_result = 'AZ' * sequence_count if sequence_count else -1
print(output_result)