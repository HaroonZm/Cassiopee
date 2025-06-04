def swap_elements_at_indices(first_index, second_index):
    temp_value = numbers_list[first_index]
    numbers_list[first_index] = numbers_list[second_index]
    numbers_list[second_index] = temp_value


number_of_elements, number_of_passes = map(int, input().split())

numbers_list = []

for element_index in range(number_of_elements):
    input_value = int(input())
    numbers_list.append(input_value)

for current_pass in range(number_of_passes):
    for current_index in range(number_of_elements - 1):
        current_modulo = (current_pass + 1)
        if numbers_list[current_index] % current_modulo > numbers_list[current_index + 1] % current_modulo:
            swap_elements_at_indices(current_index, current_index + 1)

for output_index in range(number_of_elements):
    print(numbers_list[output_index])