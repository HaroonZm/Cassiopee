def calculate_gcd(number1, number2):

    if number2 == 0:
        return number1
    else:
        return calculate_gcd(number2, number1 % number2)


def calculate_lcm(number1, number2):

    return number1 * number2 // calculate_gcd(number1, number2)


while True:

    try:
        input_values = input().split()
        first_number = int(input_values[0])
        second_number = int(input_values[1])
        gcd_result = calculate_gcd(first_number, second_number)
        print(gcd_result)

    except EOFError:
        break