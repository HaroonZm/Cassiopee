number_of_elements_to_read = input()
number_of_elements_to_read = int(number_of_elements_to_read)

input_string_of_numbers = input()

list_of_number_strings = input_string_of_numbers.split(' ')

list_of_number_strings.reverse()

for current_index in range(number_of_elements_to_read):
    
    print(list_of_number_strings[current_index], end='')

    if current_index != number_of_elements_to_read - 1:
        print(' ', end='')

print()