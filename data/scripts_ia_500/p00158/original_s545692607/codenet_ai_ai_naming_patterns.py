while True:
    number_input = int(raw_input())
    if number_input == 0:
        break
    transformation_count = 0
    current_number = number_input
    while current_number != 1:
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = current_number * 3 + 1
        transformation_count += 1
    print transformation_count