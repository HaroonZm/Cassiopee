from collections import deque

number_of_elements = int(input())

input_numbers = list(map(int, input().split()))

resulting_deque = deque()

for current_index in range(number_of_elements):

    if current_index % 2 == 0:

        resulting_deque.append(input_numbers[current_index])

    else:

        resulting_deque.appendleft(input_numbers[current_index])

ordered_result_list = list(resulting_deque)

if number_of_elements % 2 == 1:

    ordered_result_list = reversed(list(resulting_deque))

print(*ordered_result_list)