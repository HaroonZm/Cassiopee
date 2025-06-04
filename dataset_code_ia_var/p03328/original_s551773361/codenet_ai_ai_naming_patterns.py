input_value_start, input_value_end = map(int, input().split())

value_difference = input_value_end - input_value_start
for iteration_index in range(1000):
    if value_difference == iteration_index + 1:
        result_output = iteration_index * (iteration_index + 1) // 2 - input_value_start
        print(result_output)