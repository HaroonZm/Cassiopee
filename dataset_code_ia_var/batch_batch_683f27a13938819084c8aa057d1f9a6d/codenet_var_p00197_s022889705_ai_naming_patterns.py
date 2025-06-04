while True:
    input_first, input_second = map(int, input().split())
    if input_first == 0 and input_second == 0:
        break

    result_counter = 0
    first_value = input_first
    second_value = input_second

    while True:
        if second_value == 0:
            break
        if first_value < second_value:
            first_value, second_value = second_value, first_value
        first_value = first_value % second_value
        first_value, second_value = second_value, first_value
        result_counter += 1

    print(first_value, result_counter)