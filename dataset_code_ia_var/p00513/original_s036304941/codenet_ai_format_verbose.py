def is_prime(candidate_number):

    if candidate_number % 2 == 0:
        return 0

    upper_limit_for_divisor = int(candidate_number ** 0.5 + 1)

    for potential_divisor in range(3, upper_limit_for_divisor, 2):
        if candidate_number % potential_divisor == 0:
            return 0

    return 1


user_input_count = int(input())
user_values = [int(input()) for _ in range(user_input_count)]

sum_of_primes = 0

for single_value in user_values:

    test_number = single_value * 2 + 1
    sum_of_primes += is_prime(test_number)

print(sum_of_primes)