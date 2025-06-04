number_of_elements = int(input())

input_numbers_list = list(map(int, input().split()))

even_indexed_elements = []
odd_indexed_elements = []

for current_index in range(number_of_elements):
    if current_index % 2 == 0:
        even_indexed_elements.append(input_numbers_list[current_index])
    else:
        odd_indexed_elements.append(input_numbers_list[current_index])

if number_of_elements % 2 == 0:
    for element in reversed(odd_indexed_elements):
        print(element, end=' ')
    for element in even_indexed_elements:
        print(element, end=' ')
else:
    for element in reversed(even_indexed_elements):
        print(element, end=' ')
    for element in odd_indexed_elements:
        print(element, end=' ')