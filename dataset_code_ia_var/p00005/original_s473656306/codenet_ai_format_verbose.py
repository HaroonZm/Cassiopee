def calculate_greatest_common_divisor(smaller_number, larger_number):

    remainder = larger_number % smaller_number

    if smaller_number % remainder == 0:
        return remainder

    else:
        return calculate_greatest_common_divisor(remainder, smaller_number)


while True:

    try:
        first_input, second_input = list(map(float, input().split()))
    except EOFError:
        break

    if first_input >= second_input:
        smaller_value, larger_value = second_input, first_input
    else:
        smaller_value, larger_value = first_input, second_input

    if larger_value % smaller_value != 0:
        greatest_common_divisor = calculate_greatest_common_divisor(smaller_value, larger_value)
    else:
        greatest_common_divisor = smaller_value

    least_common_multiple = (smaller_value * larger_value) / greatest_common_divisor

    print("{0} {1}".format(int(greatest_common_divisor), int(least_common_multiple)))