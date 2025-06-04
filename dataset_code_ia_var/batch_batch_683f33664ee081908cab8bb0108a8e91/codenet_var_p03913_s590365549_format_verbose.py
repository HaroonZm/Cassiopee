total_target_number, additional_cost_per_increment = map(int, input().split())

minimum_total_cost = total_target_number

for increment_count in range(1, 50):

    binary_search_upper_bound = 10 ** 20
    binary_search_lower_bound = 0

    while binary_search_upper_bound - binary_search_lower_bound > 1:

        current_mid_value = (binary_search_upper_bound + binary_search_lower_bound) // 2

        combination_product = 1

        for combination_index in range(increment_count):
            combination_product *= (current_mid_value + combination_index) // increment_count

        if combination_product >= total_target_number:
            binary_search_upper_bound = current_mid_value
        else:
            binary_search_lower_bound = current_mid_value

    current_total_cost = additional_cost_per_increment * (increment_count - 1) + binary_search_upper_bound
    minimum_total_cost = min(minimum_total_cost, current_total_cost)

print(minimum_total_cost)