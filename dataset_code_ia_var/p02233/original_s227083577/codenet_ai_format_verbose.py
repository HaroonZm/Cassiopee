user_input_number = int(input())

if user_input_number == 0 or user_input_number == 1:
    print(1)

else:
    fibonacci_sequence = [0] * (user_input_number + 1)

    fibonacci_sequence[0] = 1
    fibonacci_sequence[1] = 1

    for current_index in range(2, user_input_number + 1):
        fibonacci_sequence[current_index] = fibonacci_sequence[current_index - 1] + fibonacci_sequence[current_index - 2]

    print(fibonacci_sequence[user_input_number])