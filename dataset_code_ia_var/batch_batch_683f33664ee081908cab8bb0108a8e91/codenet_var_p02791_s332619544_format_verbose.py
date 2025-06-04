number_of_elements = int(input())

element_list = list(map(int, input().split()))

current_minimum = element_list[0]

count_of_new_minimums = 1

for index in range(number_of_elements):
    if element_list[index] < current_minimum:
        current_minimum = element_list[index]
        count_of_new_minimums += 1

print(count_of_new_minimums)