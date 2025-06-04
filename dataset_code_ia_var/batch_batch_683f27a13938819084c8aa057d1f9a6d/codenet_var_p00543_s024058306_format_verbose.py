number_of_elements, number_of_passes = map(int, input().split())

element_values_by_index = {}

for current_element_index in range(number_of_elements):
    element_values_by_index[current_element_index + 1] = int(input())

for current_pass_index in range(number_of_passes):
    current_divisor = current_pass_index + 1
    for current_element_position in range(number_of_elements):
        left_index = current_element_position + 1
        if left_index == number_of_elements:
            break
        right_index = left_index + 1
        left_modulo = element_values_by_index[left_index] % current_divisor
        right_modulo = element_values_by_index[right_index] % current_divisor
        if left_modulo > right_modulo:
            temporary_swap_variable = element_values_by_index[left_index]
            element_values_by_index[left_index] = element_values_by_index[right_index]
            element_values_by_index[right_index] = temporary_swap_variable

for index_output in range(number_of_elements):
    print(element_values_by_index[index_output + 1])