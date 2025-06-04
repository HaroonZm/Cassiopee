number_of_elements = int(input())

input_numbers_list = list(map(int, input().split()))

for current_index in range(number_of_elements):

    reversed_index = number_of_elements - current_index - 1

    if current_index == number_of_elements - 1:
        print(input_numbers_list[reversed_index])
    else:
        print(input_numbers_list[reversed_index], end=" ")