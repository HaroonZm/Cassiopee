input_start_value, input_end_value = map(int, input().split())

range_difference = input_end_value - input_start_value
accumulated_total = 0

for sequence_index in range(range_difference - 1):
    accumulated_total += sequence_index + 1

final_result = accumulated_total - input_start_value
print(final_result)