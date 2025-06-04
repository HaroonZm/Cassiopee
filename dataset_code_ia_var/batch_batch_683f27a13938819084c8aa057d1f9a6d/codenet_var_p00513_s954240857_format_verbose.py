number_of_tests = int(input())

count_of_prime_results = 0

def is_prime(number_to_check):
    if number_to_check == 1:
        return 1

    potential_divisor = 3

    while potential_divisor <= number_to_check / potential_divisor:
        if number_to_check % potential_divisor == 0:
            return 0
        potential_divisor += 2

    return 1

for current_test_index in range(number_of_tests):
    input_value = int(input())
    candidate_number = 2 * input_value + 1

    count_of_prime_results += is_prime(candidate_number)

print(count_of_prime_results)