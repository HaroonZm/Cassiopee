number_of_elements, number_of_modulos = map(int, input().split())

list_of_numbers = [0] * number_of_elements

for index_input in range(number_of_elements):

    list_of_numbers[index_input] = int(input())

for current_modulo in range(1, number_of_modulos + 1):

    if current_modulo == 1:

        continue

    else:

        for index_compare in range(number_of_elements - 1):

            if (list_of_numbers[index_compare] % current_modulo) > (list_of_numbers[index_compare + 1] % current_modulo):

                temporary_value = list_of_numbers[index_compare]
                list_of_numbers[index_compare] = list_of_numbers[index_compare + 1]
                list_of_numbers[index_compare + 1] = temporary_value

for index_output in range(number_of_elements):

    print(list_of_numbers[index_output])