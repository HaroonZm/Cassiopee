from functools import reduce

def compute_greatest_common_divisor(first_number, second_number):
    while second_number:
        first_number, second_number = second_number, first_number % second_number
    return first_number

def compute_least_common_multiple(first_number, second_number):
    return first_number * second_number // compute_greatest_common_divisor(first_number, second_number)

def compute_least_common_multiple_for_list(*number_list):
    return reduce(compute_least_common_multiple, number_list)

number_of_values = int(input())

input_values_list = [0] * number_of_values

for index in range(number_of_values):
    input_values_list[index] = int(input())

overall_least_common_multiple = compute_least_common_multiple_for_list(*input_values_list)

print(overall_least_common_multiple)