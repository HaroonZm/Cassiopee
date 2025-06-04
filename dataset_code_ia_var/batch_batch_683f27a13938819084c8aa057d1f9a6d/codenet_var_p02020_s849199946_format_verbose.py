number_of_elements = int(input())

elements_list = [int(element_string) for element_string in input().split()]

total_sum_of_elements = sum(elements_list)

if total_sum_of_elements % 2 == 0:
    print(total_sum_of_elements // 2)

else:
    smallest_odd_element = 0
    elements_list.sort()
    for element in elements_list:
        if element % 2 == 1:
            smallest_odd_element = element
            break
    print((total_sum_of_elements - smallest_odd_element) // 2)