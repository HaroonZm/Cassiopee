input_string = raw_input()

count_valid_partitions = 0

for partition_index in range(len(input_string)):
    
    is_current_char_zero = input_string[partition_index] == "0"
    is_last_char = partition_index == len(input_string) - 1
    
    if is_current_char_zero and not is_last_char:
        continue

    left_partition_value = int(input_string[:partition_index]) if partition_index else 0
    right_partition_value = int(input_string[partition_index:])
    
    is_left_value_smaller_or_equal = left_partition_value <= right_partition_value
    is_left_and_right_same_parity = (left_partition_value % 2) == (right_partition_value % 2)
    
    if is_left_value_smaller_or_equal and is_left_and_right_same_parity:
        count_valid_partitions += 1

print count_valid_partitions