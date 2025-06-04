target_value = int(input())
state_array = [0] * (target_value + 120)
state_array[0] = 1

for current_index in range(target_value):
    if state_array[current_index] == 1:
        for increment in range(100, 106):
            state_array[current_index + increment] = 1

print(state_array[target_value])