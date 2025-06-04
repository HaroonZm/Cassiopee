user_input_integer = int(input())

balanced_ternary_representation = ''

current_value = user_input_integer

while current_value > 0:

    remainder_modulo_three = current_value % 3

    if remainder_modulo_three == 0:

        balanced_ternary_representation += '0'

    elif remainder_modulo_three == 1:

        balanced_ternary_representation += '+'

    else:

        balanced_ternary_representation += '-'

        current_value += 1

    current_value //= 3

print(balanced_ternary_representation[::-1])