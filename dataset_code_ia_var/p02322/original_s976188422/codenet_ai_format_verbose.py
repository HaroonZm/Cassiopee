import sys
from collections import deque

read_line_from_stdin = sys.stdin.readline
write_to_stdout = sys.stdout.write

def solve_knapsack_problem_with_multiple_items():
    number_of_item_types, maximum_total_weight = map(int, read_line_from_stdin().split())
    
    item_values = [0] * number_of_item_types
    item_weights = [0] * number_of_item_types
    item_quantities = [0] * number_of_item_types
    
    for item_type_index in range(number_of_item_types):
        value, weight, quantity = map(int, read_line_from_stdin().split())
        item_values[item_type_index] = value
        item_weights[item_type_index] = weight
        item_quantities[item_type_index] = quantity

    maximum_single_value = max(item_values)
    
    theoretical_maximum_total_value = sum(
        value * min(maximum_single_value, quantity) 
        for value, quantity in zip(item_values, item_quantities)
    )

    minimum_weight_for_value = [maximum_total_weight + 1] * (theoretical_maximum_total_value + 1)
    minimum_weight_for_value[0] = 0

    for item_type_index in range(number_of_item_types):
        value_per_item = item_values[item_type_index]
        weight_per_item = item_weights[item_type_index]
        available_quantity = item_quantities[item_type_index]
        use_quantity = min(maximum_single_value, available_quantity)
        item_quantities[item_type_index] -= use_quantity
        
        for start_remainder in range(value_per_item):
            deque_minimums = deque()
            for item_count_multiple in range((theoretical_maximum_total_value - start_remainder) // value_per_item + 1):
                current_value_index = start_remainder + item_count_multiple * value_per_item
                adjusted_weight = minimum_weight_for_value[current_value_index] - item_count_multiple * weight_per_item

                while deque_minimums and adjusted_weight <= deque_minimums[-1][1]:
                    deque_minimums.pop()
                deque_minimums.append((item_count_multiple, adjusted_weight))

                earliest_count, min_adjusted_weight = deque_minimums[0]
                minimum_weight_for_value[current_value_index] = min_adjusted_weight + item_count_multiple * weight_per_item

                if deque_minimums and earliest_count <= item_count_multiple - use_quantity:
                    deque_minimums.popleft()

    item_indices_sorted_by_weight_per_value = list(range(number_of_item_types))
    item_indices_sorted_by_weight_per_value.sort(
        key=lambda index: item_weights[index] / item_values[index]
    )
    
    items_sorted_by_efficiency = [
        (item_values[index], item_weights[index], item_quantities[index]) 
        for index in item_indices_sorted_by_weight_per_value
    ]

    maximum_total_value_obtainable = 0

    def greedy_value_maximization():
        yield 0
        for current_total_value in range(theoretical_maximum_total_value + 1):
            if minimum_weight_for_value[current_total_value] > maximum_total_weight:
                continue
            remaining_weight_capacity = maximum_total_weight - minimum_weight_for_value[current_total_value]
            achievable_value = current_total_value
            for value, weight, quantity in items_sorted_by_efficiency:
                max_number_of_this_item = min(quantity, remaining_weight_capacity // weight) if weight > 0 else 0
                achievable_value += max_number_of_this_item * value
                remaining_weight_capacity -= max_number_of_this_item * weight
            yield achievable_value

    write_to_stdout("%d\n" % max(greedy_value_maximization()))

solve_knapsack_problem_with_multiple_items()