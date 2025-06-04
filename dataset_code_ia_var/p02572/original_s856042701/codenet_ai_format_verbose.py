def main():

    MODULO_DIVISOR = int(1e9 + 7)

    number_of_elements = int(input())

    input_numbers_list = list(map(int, input().split()))

    total_sum_of_numbers = 0

    suffix_sums_excluding_current = []

    final_pairwise_sum_modulo = 0

    # Step 1: Calculate the total sum modulo MODULO_DIVISOR
    for current_index in range(len(input_numbers_list)):
        total_sum_of_numbers += input_numbers_list[current_index] % MODULO_DIVISOR
        total_sum_of_numbers %= MODULO_DIVISOR

    # Step 2: Build the list of suffix sums (total sum minus cumulative sum so far)
    cumulative_sum_so_far = 0
    for current_index in range(len(input_numbers_list)):
        cumulative_sum_so_far += input_numbers_list[current_index] % MODULO_DIVISOR
        cumulative_sum_so_far %= MODULO_DIVISOR
        elements_remaining_sum = (total_sum_of_numbers - cumulative_sum_so_far) % MODULO_DIVISOR
        suffix_sums_excluding_current.append(elements_remaining_sum)

    # Step 3: Calculate the final answer using pairwise products modulo MODULO_DIVISOR
    for current_index in range(len(suffix_sums_excluding_current)):
        product = (input_numbers_list[current_index] * suffix_sums_excluding_current[current_index]) % MODULO_DIVISOR
        final_pairwise_sum_modulo += product

    final_pairwise_sum_modulo %= MODULO_DIVISOR

    print(final_pairwise_sum_modulo)

if __name__ == '__main__':
    main()