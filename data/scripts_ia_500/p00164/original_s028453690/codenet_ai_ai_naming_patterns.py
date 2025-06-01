from itertools import cycle

INITIAL_VALUE = 32
MODULO_BASE = 5

while True:
    count_of_numbers = int(input())
    if count_of_numbers == 0:
        break

    input_numbers = [int(value) for value in input().split(" ")]

    current_value = INITIAL_VALUE
    result_values = []

    for number in cycle(input_numbers):

        current_value -= (current_value - 1) % MODULO_BASE
        result_values.append(current_value)

        if number < current_value:
            current_value -= number
            result_values.append(current_value)
        else:
            result_values.append(0)
            break

    print("\n".join(str(value) for value in result_values))