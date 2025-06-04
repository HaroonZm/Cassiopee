import itertools
import sys

MAX_NUMBER = 999999

list_of_known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

is_prime_flags = [0 for _ in range(MAX_NUMBER + 1)]

for initial_prime in list_of_known_primes:
    is_prime_flags[initial_prime] = 1

def is_divisible_by_known_prime(candidate_number):
    for prime in list_of_known_primes:
        if candidate_number % prime == 0:
            return True
        if candidate_number < prime * prime:
            return False

largest_known_prime = list_of_known_primes[-1]

for candidate_number in range(largest_known_prime, MAX_NUMBER):
    if is_divisible_by_known_prime(candidate_number):
        continue
    else:
        list_of_known_primes.append(candidate_number)
        is_prime_flags[candidate_number] = 1

for input_line in sys.stdin:
    upper_limit = int(input_line)
    print(sum(is_prime_flags[:upper_limit + 1]))