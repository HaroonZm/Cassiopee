while True:

    user_input_numbers = map(int, raw_input().split())

    sorted_numbers = sorted(user_input_numbers)

    sum_of_numbers = sum(sorted_numbers)

    if sum_of_numbers == 0:
        break
    else:
        smallest_number = sorted_numbers[0]
        middle_number = sorted_numbers[1]
        print smallest_number, middle_number