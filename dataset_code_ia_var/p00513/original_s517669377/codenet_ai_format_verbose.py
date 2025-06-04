def is_odd_prime(number_to_check):

    if number_to_check % 2 == 0:
        return 0

    for divisor in range(3, int(number_to_check ** 0.5 + 1), 2):
        if number_to_check % divisor == 0:
            return 0

    return 1


number_of_iterations = int(input())

total_sum_of_primes = 0

for iteration_index in range(number_of_iterations):

    input_number = int(input())
    odd_candidate = input_number * 2 + 1

    total_sum_of_primes += is_odd_prime(odd_candidate)

print(total_sum_of_primes)