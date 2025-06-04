prime_candidate_flags = [1] * 500000

for odd_number in range(3, 999, 2):

    index_in_flags = odd_number // 2

    if prime_candidate_flags[index_in_flags]:

        start_index = (odd_number * odd_number) // 2

        prime_candidate_flags[start_index::odd_number] = [0] * len(prime_candidate_flags[start_index::odd_number])


def is_prime(number):

    if number < 500000:

        return prime_candidate_flags[number]

    actual_number_to_check = 2 * number + 1

    for possible_divisor in range(3, int(actual_number_to_check ** 0.5 + 1), 2):

        if actual_number_to_check % possible_divisor == 0:

            return 0

    return 1


number_of_inputs = int(input())

total_primes_found = 0

for _ in range(number_of_inputs):

    number_to_check = int(input())

    total_primes_found += is_prime(number_to_check)

print(total_primes_found)