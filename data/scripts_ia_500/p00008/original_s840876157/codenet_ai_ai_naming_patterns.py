while True:
    try:
        input_number = int(input())
        count_valid_combinations = 0
        if input_number < 50:
            for digit_a in range(10):
                for digit_b in range(10):
                    for digit_c in range(10):
                        for digit_d in range(10):
                            if digit_a + digit_b + digit_c + digit_d == input_number:
                                count_valid_combinations += 1
        print(count_valid_combinations)
    except EOFError:
        break