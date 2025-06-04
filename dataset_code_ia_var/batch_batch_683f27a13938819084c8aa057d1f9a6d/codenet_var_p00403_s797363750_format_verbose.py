length_of_sequence = int(input())

input_sequence = list(map(int, input().split()))

active_elements_stack = []

for current_index in range(len(input_sequence)):

    current_value = input_sequence[current_index]

    if current_value > 0:

        if active_elements_stack.count(current_value):

            print(current_index + 1)
            exit(0)

        else:

            active_elements_stack.append(current_value)

    else:

        absolute_value = abs(current_value)

        if len(active_elements_stack) == 0 or active_elements_stack[-1] != absolute_value:

            print(current_index + 1)
            exit(0)

        else:

            del active_elements_stack[-1]

print('OK')