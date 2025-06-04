input_value_1, input_value_2, input_value_3 = map(int, input().split())
accumulated_sum = 0
iteration_counter = 0
while True:
    iteration_counter += 1
    accumulated_sum += input_value_1
    if (iteration_counter % 7) == 0:
        accumulated_sum += input_value_2
    if accumulated_sum >= input_value_3:
        print(iteration_counter)
        break