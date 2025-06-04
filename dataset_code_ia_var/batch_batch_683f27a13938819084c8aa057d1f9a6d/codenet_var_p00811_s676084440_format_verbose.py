import math

def generate_prime_numbers_up_to_limit(maximum_number):
    """
    Sieve of Eratosthenes: Generate all prime numbers up to maximum_number (inclusive).
    """
    candidate_numbers = [number for number in range(maximum_number + 1)]
    candidate_numbers[1] = 0  # 1 is not a prime number

    for possible_prime in candidate_numbers:
        if possible_prime > math.sqrt(maximum_number):
            break
        if possible_prime == 0:
            continue
        for composite_number in range(possible_prime * 2, maximum_number, possible_prime):
            candidate_numbers[composite_number] = 0  # Mark composites as 0

    list_of_primes = []
    for prime_candidate in candidate_numbers:
        if prime_candidate != 0:
            list_of_primes.append(prime_candidate)
    return list_of_primes


prime_numbers_up_to_100000 = generate_prime_numbers_up_to_limit(100000)

while True:
    max_product_limit, fraction_numerator, fraction_denominator = map(int, input().split())
    if max_product_limit <= 4 or fraction_numerator == 0 or fraction_denominator == 0:
        break

    selected_prime_1 = 0
    selected_prime_2 = 0
    maximum_product_found = 0

    for index_prime_1 in range(len(prime_numbers_up_to_100000)):
        for index_prime_2 in range(index_prime_1, len(prime_numbers_up_to_100000)):
            prime_1 = prime_numbers_up_to_100000[index_prime_1]
            prime_2 = prime_numbers_up_to_100000[index_prime_2]

            current_product = prime_1 * prime_2
            if (
                current_product <= max_product_limit and
                (fraction_numerator / fraction_denominator <= prime_1 / prime_2 <= 1)
            ):
                if current_product >= maximum_product_found:
                    maximum_product_found = current_product
                    selected_prime_1 = prime_1
                    selected_prime_2 = prime_2
            else:
                break

    print("{0} {1}".format(selected_prime_1, selected_prime_2))