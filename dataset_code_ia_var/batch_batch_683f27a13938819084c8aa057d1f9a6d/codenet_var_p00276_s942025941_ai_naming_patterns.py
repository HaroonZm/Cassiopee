num_queries = int(input())

for query_index in range(num_queries):
    coins_collected, apples_collected, num_operations = map(int, input().split())

    if num_operations <= coins_collected and num_operations <= apples_collected:
        total_sets_formed = num_operations
        coins_collected -= total_sets_formed
        apples_collected -= total_sets_formed

        if apples_collected <= coins_collected:
            if 2 * apples_collected >= coins_collected:
                total_sets_formed += coins_collected >> 1
            else:
                total_sets_formed += apples_collected
                coins_collected -= 2 * apples_collected
                total_sets_formed += coins_collected // 3
        else:
            total_sets_formed += coins_collected >> 1
    elif apples_collected <= coins_collected and apples_collected <= num_operations:
        total_sets_formed = apples_collected + (coins_collected - apples_collected) // 3
    else:
        total_sets_formed = coins_collected

    print(total_sets_formed)