number_of_elements = int(input())

list_of_integers = list(map(int, input().split()))

list_of_integers.sort()

total_sum_of_elements = sum(list_of_integers)

if total_sum_of_elements % 2 == 0:

    print(total_sum_of_elements // 2)

else:

    for index in range(number_of_elements):

        if list_of_integers[index] % 2 == 1:

            first_odd_element = list_of_integers[index]

            break

    adjusted_sum = total_sum_of_elements - first_odd_element

    print(adjusted_sum // 2)