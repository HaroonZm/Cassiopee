from math import gcd as calculate_gcd

def compute_least_common_multiple_of_two_numbers(first_number, second_number):
    return (first_number * second_number) // calculate_gcd(first_number, second_number)


def compute_least_common_multiple_of_list(numbers_list):
    least_common_multiple = 1
    for current_number in numbers_list:
        least_common_multiple = compute_least_common_multiple_of_two_numbers(
            least_common_multiple, current_number
        )
    return least_common_multiple


number_of_elements = int(input())

integer_list = [int(element_as_string) for element_as_string in input().split()]

modulo_value = 10 ** 9 + 7

final_answer = 0

least_common_multiple_of_all_elements = compute_least_common_multiple_of_list(integer_list)
least_common_multiple_of_all_elements %= modulo_value

for current_index in range(number_of_elements):
    modular_inverse_of_element = pow(
        integer_list[current_index], modulo_value - 2, modulo_value
    )
    current_contribution = (least_common_multiple_of_all_elements * modular_inverse_of_element) % modulo_value
    final_answer = (final_answer + current_contribution) % modulo_value

print(final_answer)