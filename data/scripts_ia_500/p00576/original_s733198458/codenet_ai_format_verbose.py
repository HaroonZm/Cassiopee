presence_flags = [0] * 2020

number_of_elements = int(input())
initial_values = [int(value) for value in input().split()]

for value in initial_values:
    presence_flags[value] = 1

number_of_indices = int(input())
indices_to_increment = [int(index) for index in input().split()]

for index in indices_to_increment:
    zero_based_index = index - 1

    current_value = initial_values[zero_based_index]

    if current_value + 1 != 2020:
        if presence_flags[current_value + 1] == 0:
            presence_flags[current_value + 1] = 1
            presence_flags[current_value] = 0
            initial_values[zero_based_index] = current_value + 1

for value in range(2020):
    if presence_flags[value] == 1:
        print(value)