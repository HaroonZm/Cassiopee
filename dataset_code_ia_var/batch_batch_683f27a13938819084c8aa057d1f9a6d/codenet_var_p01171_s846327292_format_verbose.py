import math

def compute_prime_factors(number_to_factorize, starting_divisor):
    global list_of_prime_factors

    while True:
        if number_to_factorize % starting_divisor == 0:
            list_of_prime_factors.append(starting_divisor)
            if number_to_factorize // starting_divisor == 1:
                break
            else:
                compute_prime_factors(number_to_factorize // starting_divisor, starting_divisor)
                break
        else:
            starting_divisor += 1
            if math.sqrt(number_to_factorize) < starting_divisor:
                list_of_prime_factors.append(int(number_to_factorize))
                break
    return list_of_prime_factors

def calculate_difference_between_largest_and_sum_of_others(list_of_numbers):
    unique_numbers_list = list(set(list_of_numbers))
    unique_numbers_list.sort(reverse=True)
    if len(unique_numbers_list) == 1:
        return unique_numbers_list[0]
    else:
        return unique_numbers_list[0] - sum(unique_numbers_list[1:])

while True:
    input_first_number, input_second_number = map(int, input().split())

    if input_first_number == 0 and input_second_number == 0:
        break

    list_of_prime_factors = []
    result_for_first_input = calculate_difference_between_largest_and_sum_of_others(compute_prime_factors(input_first_number, 2))

    list_of_prime_factors = []
    result_for_second_input = calculate_difference_between_largest_and_sum_of_others(compute_prime_factors(input_second_number, 2))

    if result_for_first_input > result_for_second_input:
        print("a")
    else:
        print("b")