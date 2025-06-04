number_of_elements, number_of_passes = map(int, input().split())

element_list = [int(input()) for element_index in range(number_of_elements)]

for pass_index in range(number_of_passes):
    
    modulus_value = pass_index + 1

    for current_index in range(number_of_elements - 1):

        current_modulus = element_list[current_index] % modulus_value
        next_modulus = element_list[current_index + 1] % modulus_value

        if current_modulus > next_modulus:
            element_list[current_index], element_list[current_index + 1] = (
                element_list[current_index + 1],
                element_list[current_index]
            )

for output_index in range(number_of_elements):
    print(element_list[output_index])