def compute_combination_modulo(total_elements, select_elements, modulo):

    if select_elements < 0 or select_elements > total_elements:
        return 0

    select_elements = min(select_elements, total_elements - select_elements)

    return factorial_modulo_cache[total_elements] * inverse_factorial_modulo_cache[select_elements] * inverse_factorial_modulo_cache[total_elements - select_elements] % modulo

modulo_value = 10 ** 9 + 7

max_n = 5000

factorial_modulo_cache = [1, 1]
inverse_factorial_modulo_cache = [1, 1]
modular_inverse_cache = [0, 1]

for current_number in range(2, max_n + 1):

    factorial_modulo_cache.append((factorial_modulo_cache[-1] * current_number) % modulo_value)

    modular_inverse_cache.append((-modular_inverse_cache[modulo_value % current_number] * (modulo_value // current_number)) % modulo_value)

    inverse_factorial_modulo_cache.append((inverse_factorial_modulo_cache[-1] * modular_inverse_cache[-1]) % modulo_value)

number_of_elements, subset_size = map(int, input().split())

if number_of_elements == 1:

    print(1)

elif subset_size == 1:

    print(pow(2, number_of_elements - 2, modulo_value))

elif subset_size == number_of_elements:

    dynamic_programming_table = [[0 for _ in range(subset_size + 1)] for _ in range(subset_size)]

    prefix_sum_cache = [0] * (subset_size + 1)

    dynamic_programming_table[0][subset_size] = 1

    prefix_sum_cache[subset_size] = 1

    for subproblem_index in range(1, subset_size):

        for partition_index in range(subset_size - subproblem_index, subset_size + 1):

            if partition_index == subset_size - subproblem_index:

                dynamic_programming_table[subproblem_index][partition_index] = (prefix_sum_cache[subset_size] - prefix_sum_cache[partition_index]) % modulo_value

            else:

                dynamic_programming_table[subproblem_index][partition_index] = (dynamic_programming_table[subproblem_index - 1][partition_index] + prefix_sum_cache[subset_size] - prefix_sum_cache[partition_index]) % modulo_value

        prefix_sum_cache = [dynamic_programming_table[subproblem_index][partition_index] for partition_index in range(subset_size + 1)]

        for index in range(1, subset_size + 1):

            prefix_sum_cache[index] += prefix_sum_cache[index - 1]

            prefix_sum_cache[index] %= modulo_value

    print(dynamic_programming_table[number_of_elements - 1][1])

else:

    dynamic_programming_table = [[0 for _ in range(subset_size + 1)] for _ in range(subset_size)]

    prefix_sum_cache = [0] * (subset_size + 1)

    dynamic_programming_table[0][subset_size] = 1

    prefix_sum_cache[subset_size] = 1

    for subproblem_index in range(1, subset_size):

        for partition_index in range(subset_size - subproblem_index, subset_size + 1):

            if partition_index == subset_size - subproblem_index:

                dynamic_programming_table[subproblem_index][partition_index] = (prefix_sum_cache[subset_size] - prefix_sum_cache[partition_index]) % modulo_value

            else:

                dynamic_programming_table[subproblem_index][partition_index] = (dynamic_programming_table[subproblem_index - 1][partition_index] + prefix_sum_cache[subset_size] - prefix_sum_cache[partition_index]) % modulo_value

        prefix_sum_cache = [dynamic_programming_table[subproblem_index][partition_index] for partition_index in range(subset_size + 1)]

        for index in range(1, subset_size + 1):

            prefix_sum_cache[index] += prefix_sum_cache[index - 1]

            prefix_sum_cache[index] %= modulo_value

    total_ways = 0

    for candidate_total in range(number_of_elements - subset_size + 1, number_of_elements + 1):

        dp_table_index = candidate_total - number_of_elements + subset_size

        total_ways += dynamic_programming_table[subset_size - 1][dp_table_index] * compute_combination_modulo(candidate_total - 2, number_of_elements - subset_size - 1, modulo_value)

    total_ways *= pow(2, number_of_elements - subset_size - 1, modulo_value)

    print(total_ways % modulo_value)