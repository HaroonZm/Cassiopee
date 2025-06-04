import math
input_values = [int(input()) for input_index in range(5)]
division_results = [
    math.ceil(input_values[1] / input_values[3]),
    math.ceil(input_values[2] / input_values[4])
]
sorted_division_results = sorted(division_results)
final_result = input_values[0] - sorted_division_results[-1]
print(final_result)