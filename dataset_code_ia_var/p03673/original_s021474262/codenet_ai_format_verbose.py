from collections import deque

number_of_elements = int(input())
input_numbers_list = list(map(int, input().split()))

is_number_of_elements_even = (number_of_elements % 2 == 0)

result_deque = deque()

for current_index in range(number_of_elements):

    if current_index % 2 == 0:
        result_deque.append(input_numbers_list[current_index])
    else:
        result_deque.appendleft(input_numbers_list[current_index])

reordered_list = list(result_deque)

if is_number_of_elements_even:
    for current_element in reordered_list:
        print(current_element, end=" ")
else:
    for current_element in reversed(reordered_list):
        print(current_element, end=" ")