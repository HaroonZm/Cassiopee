import math
input_value_a, input_value_b = map(int, input().split())
range_divisor = (2 * input_value_b) + 1
division_result = input_value_a / range_divisor
minimum_group_count = math.ceil(division_result)
print(minimum_group_count)