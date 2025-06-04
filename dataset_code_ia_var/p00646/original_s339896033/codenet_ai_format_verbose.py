while True:

    user_input = input()

    if user_input == 0:
        break

    remaining_number = user_input
    current_divisor = 2
    count_of_divisors = 1

    while current_divisor * current_divisor <= remaining_number:

        if remaining_number % current_divisor == 0:

            exponent_of_current_prime = 0

            while remaining_number % current_divisor == 0:
                remaining_number /= current_divisor
                exponent_of_current_prime += 1

            count_of_divisors *= (exponent_of_current_prime * 2 + 1)

        current_divisor += 1

    if remaining_number != 1:
        count_of_divisors *= 3

    result = count_of_divisors / 2 + 1

    print(result)