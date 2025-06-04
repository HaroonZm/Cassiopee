from collections import defaultdict

def main():
    def compute_prime_numbers(upto_number_inclusive):
        is_number_prime = [True] * (upto_number_inclusive + 1)
        is_number_prime[0] = is_number_prime[1] = False

        for potential_prime in range(2, int(upto_number_inclusive ** 0.5) + 1):
            if is_number_prime[potential_prime]:
                for multiple in range(potential_prime * potential_prime, upto_number_inclusive + 1, potential_prime):
                    is_number_prime[multiple] = False

        return [number for number in range(upto_number_inclusive + 1) if is_number_prime[number]]

    MAX_INPUT_VALUE = 100000
    all_primes_up_to_max = compute_prime_numbers(MAX_INPUT_VALUE)

    divisors_prime_factors = [[] for _ in range(MAX_INPUT_VALUE + 1)]
    for prime in all_primes_up_to_max:
        for number in range(prime, MAX_INPUT_VALUE + 1, prime):
            divisors_prime_factors[number].append(prime)

    total_elements = int(input())
    input_numbers = list(map(int, input().split()))

    disjoint_set_parents = [index for index in range(MAX_INPUT_VALUE + 1)]

    def find_set_representative(element):
        if element == disjoint_set_parents[element]:
            return element
        disjoint_set_parents[element] = find_set_representative(disjoint_set_parents[element])
        return disjoint_set_parents[element]

    for input_index, input_value in enumerate(input_numbers):
        smallest_prime_divisor = min(divisors_prime_factors[input_value])

        representative_leader = find_set_representative(smallest_prime_divisor)

        for prime_divisor in divisors_prime_factors[input_value]:
            disjoint_set_parents[find_set_representative(prime_divisor)] = representative_leader

        disjoint_set_parents[find_set_representative(input_value)] = representative_leader

    set_representative_to_indices = defaultdict(set)
    for input_index, input_value in enumerate(input_numbers):
        set_representative_to_indices[find_set_representative(input_value)].add(input_index)

    sorted_input_numbers = sorted(input_numbers)

    for current_index, current_value in enumerate(sorted_input_numbers):
        if current_index not in set_representative_to_indices[find_set_representative(current_value)]:
            print(0)
            break
    else:
        print(1)

main()