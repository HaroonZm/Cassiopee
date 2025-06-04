import itertools

number_of_elements = int(input())

input_integer_list = list(map(int, input().split()))

modulus_value = 10 ** 9 + 7

accumulated_sum_list = list(itertools.accumulate(input_integer_list))

final_sum = 0

for current_index in range(number_of_elements - 1):
    
    current_element = input_integer_list[current_index]
    
    sum_of_remaining_elements = accumulated_sum_list[number_of_elements - 1] - accumulated_sum_list[current_index]
    
    product_modulo = (current_element * sum_of_remaining_elements) % modulus_value
    
    final_sum += product_modulo

print(final_sum % modulus_value)