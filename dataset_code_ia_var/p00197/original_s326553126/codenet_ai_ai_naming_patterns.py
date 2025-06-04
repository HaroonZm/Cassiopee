while True:
    input_first_value, input_second_value = map(int, input().split())
    if input_first_value == 0 and input_second_value == 0:
        break
    if input_first_value >= input_second_value:
        current_max = input_first_value
        current_min = input_second_value
    else:
        current_max = input_second_value
        current_min = input_first_value
    iteration_count = 0
    while True:
        temp = current_max % current_min
        current_max, current_min = current_min, temp
        iteration_count += 1
        if current_min == 0:
            break
    print(current_max, iteration_count)