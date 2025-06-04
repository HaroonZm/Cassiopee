number_of_elements = int(input())

input_numbers_list = list(map(int, input().split()))

input_numbers_list.sort(reverse=True)

maximum_total = 0

for current_index in range(1, len(input_numbers_list) - number_of_elements):

    if current_index % 2 == 1:

        maximum_total += input_numbers_list[current_index]

print(maximum_total)