from math import log2 as math_log2, ceil as math_ceil

input_value_total, input_value_threshold = map(int, input().split())

if input_value_total <= input_value_threshold:
    probability_list = [0] * input_value_total
    iteration_count = input_value_total + 1
    cumulative_score = 0
else:
    probability_list = [0] * (input_value_threshold - 1)
    iteration_count = input_value_threshold
    cumulative_score = (input_value_total - input_value_threshold + 1) / input_value_total

for loop_index in range(1, iteration_count):
    current_probability = (1 / input_value_total) * pow(
        0.5, math_ceil(math_log2(input_value_threshold / loop_index))
    )
    probability_list[loop_index - 1] = current_probability

final_result = sum(probability_list) + cumulative_score
print(final_result)