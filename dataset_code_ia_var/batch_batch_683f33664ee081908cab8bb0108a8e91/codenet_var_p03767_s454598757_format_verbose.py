number_of_elements = int(input())

input_numbers = list(map(int, input().split()))

input_numbers.sort()

sum_of_selected_elements = 0

for selected_index in range(number_of_elements):
    element_index = selected_index * 2 + number_of_elements
    sum_of_selected_elements += input_numbers[element_index]

print(sum_of_selected_elements)