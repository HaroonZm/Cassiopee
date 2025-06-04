total_elements = int(input())

input_numbers = [int(number_str) for number_str in input().split()]

current_positive_stack = []

has_error_occurred = False

for current_index in range(total_elements):

    current_number = input_numbers[current_index]

    if current_number > 0:

        if current_number in current_positive_stack:
            print(current_index + 1)
            has_error_occurred = True
            break

        else:
            current_positive_stack.append(current_number)

    else:

        if (len(current_positive_stack) > 0 and
                current_positive_stack[-1] == abs(current_number)):
            current_positive_stack.pop()

        else:
            print(current_index + 1)
            has_error_occurred = True
            break

if not has_error_occurred:
    print("OK")