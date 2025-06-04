number_of_elements = int(input())

input_elements = [int(element) for element in input().split()]

elements_at_even_indices = []
elements_at_odd_indices = []

for current_index in range(number_of_elements):

    if current_index % 2 == 0:
        elements_at_even_indices.append(input_elements[current_index])
    else:
        elements_at_odd_indices.append(input_elements[current_index])

if number_of_elements % 2 == 0:
    elements_at_odd_indices.reverse()
    ordered_elements = elements_at_odd_indices + elements_at_even_indices
    print(*ordered_elements)
else:
    elements_at_even_indices.reverse()
    ordered_elements = elements_at_even_indices + elements_at_odd_indices
    print(*ordered_elements)