number_of_elements = int(input())

input_numbers_list = [int(element) for element in input().split()]

index_first_valid_number = -1
index_second_valid_number = -1

for first_index in range(number_of_elements):

    for second_index in range(number_of_elements):

        if first_index != second_index and abs(input_numbers_list[first_index] - input_numbers_list[second_index]) % (number_of_elements - 1) == 0:

            index_first_valid_number = first_index
            index_second_valid_number = second_index

print(input_numbers_list[index_first_valid_number], input_numbers_list[index_second_valid_number])