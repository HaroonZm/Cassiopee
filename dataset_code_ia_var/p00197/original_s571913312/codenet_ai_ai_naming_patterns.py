while True:
    input_first, input_second = map(int, input().split())
    if input_first == 0 and input_second == 0:
        break
    iteration_count = 0
    if input_first >= input_second:
        primary_value = input_first
        secondary_value = input_second
    else:
        primary_value = input_second
        secondary_value = input_first
    while True:
        temp_value = primary_value % secondary_value
        primary_value, secondary_value = secondary_value, temp_value
        iteration_count += 1
        if secondary_value == 0:
            greatest_common_divisor = primary_value
            break
    print(greatest_common_divisor, iteration_count)