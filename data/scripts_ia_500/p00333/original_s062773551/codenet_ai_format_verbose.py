def calculate_gcd(number1, number2):

    if number1 < number2:
        number1, number2 = number2, number1

    if number1 % number2 == 0:
        return number2
    else:
        return calculate_gcd(number2, number1 % number2)


width, height, count_copies = map(int, input().split())

greatest_common_divisor = calculate_gcd(width, height)

number_of_squares = (width // greatest_common_divisor) * (height // greatest_common_divisor) * count_copies

print(number_of_squares)