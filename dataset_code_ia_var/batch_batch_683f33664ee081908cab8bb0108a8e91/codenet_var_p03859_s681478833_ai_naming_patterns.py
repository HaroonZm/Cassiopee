MODULO = 10**9 + 7

input_length, num_operations = map(int, input().split())
left_bound, right_bound = -1, -1
input_string = input()
operation_ranges = []
for operation_index in range(num_operations):
    operation_left, operation_right = map(int, input().split())
    operation_left -= 1
    operation_right -= 1
    if left_bound <= operation_left and operation_right <= right_bound:
        continue
    else:
        left_bound, right_bound = operation_left, operation_right
        operation_ranges.append((operation_left, operation_right))

effective_operations = len(operation_ranges)
operation_owner_index = [-1] * input_length
for op_idx in range(effective_operations):
    segment_left, segment_right = operation_ranges[op_idx]
    for current_pos in range(segment_left, segment_right + 1):
        operation_owner_index[current_pos] = op_idx

dp_table = [[0 for dp_col in range(input_length + 1)] for dp_row in range(input_length + 1)]

for dp_col in range(input_length + 1):
    dp_table[-1][dp_col] = 1

for string_pos in range(input_length - 1, -1, -1):
    operation_id = operation_owner_index[string_pos]
    if operation_id != -1:
        seg_left, seg_right = operation_ranges[operation_id]
        ones_count_in_range = sum(int(input_string[check_pos]) for check_pos in range(seg_right + 1))
        zeros_count_in_range = seg_right + 1 - ones_count_in_range
        for ones_placed in range(ones_count_in_range + 1):
            remaining_ones = ones_count_in_range - ones_placed
            remaining_zeros = zeros_count_in_range - (string_pos - ones_placed)
            if remaining_ones == 0:
                if remaining_zeros > 0:
                    dp_table[string_pos][ones_placed] = dp_table[string_pos + 1][ones_placed]
            else:
                if remaining_zeros > 0:
                    dp_table[string_pos][ones_placed] = (dp_table[string_pos + 1][ones_placed + 1] + dp_table[string_pos + 1][ones_placed]) % MODULO
                elif remaining_zeros == 0:
                    dp_table[string_pos][ones_placed] = dp_table[string_pos + 1][ones_placed + 1]
    else:
        if input_string[string_pos] == "1":
            for dp_col in range(input_length):
                dp_table[string_pos][dp_col] = dp_table[string_pos + 1][dp_col + 1]
        else:
            for dp_col in range(input_length + 1):
                dp_table[string_pos][dp_col] = dp_table[string_pos + 1][dp_col]

print(dp_table[0][0])