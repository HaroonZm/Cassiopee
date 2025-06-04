def compute_combinatorial_count(number_of_elements, target_sum):
    MODULO = 10 ** 9 + 7

    if target_sum % 2:
        print(0)
        exit()
    
    half_sum = target_sum // 2

    dp_table = [[[0 for _ in range(number_of_elements ** 2)] for _ in range(number_of_elements + 2)] for _ in range(number_of_elements + 1)]
    dp_table[0][0][0] = 1

    for current_element in range(1, number_of_elements + 1):
        previous_dp = dp_table[current_element - 1]
        for current_subset_size in range(current_element + 1):
            for current_sum in range(current_subset_size, half_sum + 1):
                total_ways = 0

                if current_sum >= current_subset_size:
                    # Case 1: Left-side, Horizontal, Both on top
                    total_ways += previous_dp[current_subset_size][current_sum - current_subset_size] * current_subset_size * 2
                    total_ways += previous_dp[current_subset_size][current_sum - current_subset_size]
                    total_ways += previous_dp[current_subset_size + 1][current_sum - current_subset_size] * (current_subset_size + 1) ** 2

                if current_subset_size > 0 and current_sum >= current_subset_size:
                    # Case 2: Both retained
                    total_ways += dp_table[current_element - 1][current_subset_size - 1][current_sum - current_subset_size]

                dp_table[current_element][current_subset_size][current_sum] = total_ways % MODULO

    print(dp_table[number_of_elements][0][half_sum])


if __name__ == "__main__":
    number_of_elements, target_sum = map(int, input().split())
    compute_combinatorial_count(number_of_elements, target_sum)