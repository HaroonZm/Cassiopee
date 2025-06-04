while True:

    user_input_number = int(input())

    if user_input_number == -1:
        break

    initial_value = 4280
    base_deduction = 1150

    if user_input_number <= 10:
        result = initial_value - base_deduction
        print(result)

    elif 10 < user_input_number <= 20:
        additional_deduction = (user_input_number - 10) * 125
        result = initial_value - (base_deduction + additional_deduction)
        print(result)

    elif 20 < user_input_number <= 30:
        additional_deduction = 1250 + (user_input_number - 20) * 140
        result = initial_value - (base_deduction + additional_deduction)
        print(result)

    else:
        additional_deduction = 1250 + 1400 + (user_input_number - 30) * 160
        result = initial_value - (base_deduction + additional_deduction)
        print(result)