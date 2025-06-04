interest_rate, subtraction_value, current_value = map(int, input().split())

for iteration_index in range(10):

    next_value = (interest_rate * current_value) - subtraction_value

    print(next_value)

    current_value = next_value