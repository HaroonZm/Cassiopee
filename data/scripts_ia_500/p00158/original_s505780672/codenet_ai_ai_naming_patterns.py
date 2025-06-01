while True:
    input_number = int(input())
    if input_number == 0:
        break
    steps_count = 0
    current_number = input_number
    while current_number != 1:
        steps_count += 1
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = current_number * 3 + 1
    print(steps_count)