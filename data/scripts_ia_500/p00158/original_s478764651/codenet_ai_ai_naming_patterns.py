while True:
    input_number = int(input())
    if input_number == 0:
        break
    step_count = 0
    current_value = input_number
    while current_value != 1:
        if current_value % 2 == 0:
            current_value = current_value // 2
        else:
            current_value = 3 * current_value + 1
        step_count += 1
    print(step_count)