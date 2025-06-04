def factorize_into_prime_divisors(number):
    prime_divisors_list = []
    for current_divisor in range(2, number + 1):
        if number % current_divisor == 0:
            prime_divisors_list.append(current_divisor)
            while number % current_divisor == 0:
                number /= current_divisor
    return prime_divisors_list

def calculate_key_number(prime_divisors_list):
    sum_of_all_but_last = 0
    for index in range(len(prime_divisors_list) - 1):
        sum_of_all_but_last += prime_divisors_list[index]
    key_number_value = prime_divisors_list[-1] - sum_of_all_but_last
    return key_number_value

while True:
    user_input_text = raw_input()
    operand_strings = user_input_text.split()
    first_integer = int(operand_strings[0])
    second_integer = int(operand_strings[1])

    if first_integer == 0 and second_integer == 0:
        break

    prime_divisors_first_integer = factorize_into_prime_divisors(first_integer)
    prime_divisors_second_integer = factorize_into_prime_divisors(second_integer)

    key_number_first_integer = calculate_key_number(prime_divisors_first_integer)
    key_number_second_integer = calculate_key_number(prime_divisors_second_integer)

    if key_number_first_integer > key_number_second_integer:
        print('a')
    else:
        print('b')