while True:

    try:

        user_input_number = input()
        valid_combination_count = 0

        if user_input_number < 50:

            for first_digit in range(10):

                for second_digit in range(10):

                    for third_digit in range(10):

                        for fourth_digit in range(10):

                            if (first_digit + second_digit + third_digit + fourth_digit) == user_input_number:

                                valid_combination_count += 1

        print valid_combination_count

    except EOFError:
        break