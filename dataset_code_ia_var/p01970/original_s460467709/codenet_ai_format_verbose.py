from collections import defaultdict

MAXIMUM_NUMBER_FOR_SIEVE = 1000000
SIEVE_ROOT_LIMIT = 1000
MODULO_CONSTANT = 1000000007

prime_flags = [True] * (MAXIMUM_NUMBER_FOR_SIEVE + 1)
prime_flags[0] = False
prime_flags[1] = False

for current_number in range(2, SIEVE_ROOT_LIMIT + 1):

    if prime_flags[current_number]:

        for composite_candidate in range(current_number * current_number, MAXIMUM_NUMBER_FOR_SIEVE + 1, current_number):
            prime_flags[composite_candidate] = False

input_sequence_size = int(input())
input_sequence = list(map(int, input().split()))

initial_sum_for_even_subsequence = 0
initial_count_for_prime_subsequence = 1

last_prime_used_in_subsequence = 0

state_to_count_mapping = {}
state_to_count_mapping[(last_prime_used_in_subsequence, 0)] = initial_sum_for_even_subsequence
state_to_count_mapping[(last_prime_used_in_subsequence, 1)] = initial_count_for_prime_subsequence

for number_in_sequence in input_sequence:

    updated_state_to_count = defaultdict(int)

    for state_key, subsequence_count in state_to_count_mapping.items():
        last_prime_in_state, sequence_type = state_key

        if prime_flags[number_in_sequence]:

            if sequence_type == 0:
                if last_prime_in_state < number_in_sequence:
                    updated_state_to_count[(number_in_sequence, 0)] = (
                        updated_state_to_count[(number_in_sequence, 0)] + subsequence_count
                    ) % MODULO_CONSTANT

                    updated_state_to_count[(last_prime_in_state, 1)] = (
                        updated_state_to_count[(last_prime_in_state, 1)] + subsequence_count
                    ) % MODULO_CONSTANT
                else:
                    updated_state_to_count[(last_prime_in_state, 1)] = (
                        updated_state_to_count[(last_prime_in_state, 1)] + subsequence_count
                    ) % MODULO_CONSTANT

            else:
                if last_prime_in_state < number_in_sequence:
                    updated_state_to_count[(number_in_sequence, 0)] = (
                        updated_state_to_count[(number_in_sequence, 0)] + subsequence_count
                    ) % MODULO_CONSTANT

        if not prime_flags[number_in_sequence]:

            if sequence_type == 0:
                updated_state_to_count[(last_prime_in_state, 1)] = (
                    updated_state_to_count[(last_prime_in_state, 1)] + subsequence_count
                ) % MODULO_CONSTANT

    state_to_count_mapping = updated_state_to_count

result_total_subsequences = sum(state_to_count_mapping.values()) % MODULO_CONSTANT

print(result_total_subsequences)