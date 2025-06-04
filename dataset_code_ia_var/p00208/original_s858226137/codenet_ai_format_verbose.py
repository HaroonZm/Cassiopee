list_of_allowed_digits = [0, 1, 2, 3, 5, 7, 8, 9]

user_input_number = input()

while user_input_number != 0:

    base8_digits_in_reversed_order = []
    current_power_of_eight = 1

    while current_power_of_eight * 8 <= user_input_number:
        current_power_of_eight *= 8

    while current_power_of_eight > 0:
        current_digit = user_input_number // current_power_of_eight
        base8_digits_in_reversed_order.append(current_digit)
        user_input_number %= current_power_of_eight
        current_power_of_eight //= 8

    converted_number_string = ''

    for digit_index in range(len(base8_digits_in_reversed_order)):
        mapped_digit = list_of_allowed_digits[base8_digits_in_reversed_order[digit_index]]
        converted_number_string += str(mapped_digit)

    print(converted_number_string)

    user_input_number = input()