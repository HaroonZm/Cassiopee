from itertools import cycle

INITIAL_VALUE = 32

while True:
    input_count = int(input())
    if input_count == 0:
        break

    input_values_list = [int(value) for value in input().split(" ")]

    current_value = INITIAL_VALUE

    for current_input_value in cycle(input_values_list):
        current_value -= (current_value - 1) % 5
        print(current_value)

        if current_input_value < current_value:
            current_value -= current_input_value
            print(current_value)
        else:
            print(0)
            break