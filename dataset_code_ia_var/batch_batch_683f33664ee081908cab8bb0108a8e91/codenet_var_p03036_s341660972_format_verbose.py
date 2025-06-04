ratio, decrement, initial_value = map(int, input().split())

current_value = initial_value

for iteration_index in range(10):

    current_value = ratio * current_value - decrement

    print(current_value)