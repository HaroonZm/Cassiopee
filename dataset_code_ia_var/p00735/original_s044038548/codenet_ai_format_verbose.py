import sys

def sieve_of_modular_primes(maximum_number):

    sieve_flags = [0, 0, 0, 0, 0, 0] + [1 for _ in range(maximum_number - 5)]

    modular_prime_list = []

    current_number = 6
    while current_number <= maximum_number:

        if sieve_flags[current_number] == 0:
            current_number += 1
            continue

        if current_number % 7 != 1 and current_number % 7 != 6:
            sieve_flags[current_number] = 0
            current_number += 1
            continue

        modular_prime_list.append(current_number)

        multiple_factor = 2
        while current_number * multiple_factor <= maximum_number:
            sieve_flags[current_number * multiple_factor] = 0
            multiple_factor += 1

        current_number += 1

    return modular_prime_list

modular_prime_candidates = sieve_of_modular_primes(300000)

while True:

    input_number = int(raw_input())

    if input_number == 1:
        break

    sys.stdout.write("%d:" % input_number)

    for candidate_prime in modular_prime_candidates:

        if candidate_prime > input_number:
            break

        quotient, remainder = divmod(input_number, candidate_prime)

        if remainder != 0:
            continue

        quotient_mod_seven = quotient % 7

        if quotient_mod_seven == 1 or quotient_mod_seven == 6:
            sys.stdout.write(" %d" % candidate_prime)

    print ""