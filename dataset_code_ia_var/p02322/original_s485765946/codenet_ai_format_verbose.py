#!/usr/bin/env python3
# DPL_1_I: Combinatorial - Knapsack Problem with Limitations II

from heapq import heappush, heappop

def get_maximum_knapsack_value(maximum_knapsack_weight, knapsack_items):
    def estimate_optimal_value_from_partial(current_weight, current_value, current_index):
        for next_item_index in range(current_index, number_of_items):
            item_value, item_weight = knapsack_items[next_item_index]
            if current_weight + item_weight > maximum_knapsack_weight:
                estimated_fractional_value = -current_value - (item_value / item_weight) * (maximum_knapsack_weight - current_weight)
                return (-current_value, estimated_fractional_value)
            current_weight += item_weight
            current_value += item_value
        return (-current_value, -float(current_value))

    number_of_items = len(knapsack_items)

    knapsack_items.sort(key=lambda item: item[1], reverse=True)
    knapsack_items.sort(key=lambda item: item[0] / item[1], reverse=True)

    initial_upper_bound, initial_cost = estimate_optimal_value_from_partial(0, 0, 0)
    search_heap = [
        (initial_cost, initial_upper_bound, 0, 0, 0)
    ]
    current_maximum_cost = initial_upper_bound

    while search_heap:
        current_cost_estimate, upper_bound, accumulated_weight, accumulated_value, current_item_index = heappop(search_heap)
        if current_cost_estimate > current_maximum_cost:
            break
        if current_item_index < number_of_items:
            item_value, item_weight = knapsack_items[current_item_index]
            next_weight = accumulated_weight + item_weight
            next_value = accumulated_value + item_value

            if next_weight <= maximum_knapsack_weight:
                heappush(
                    search_heap,
                    (current_cost_estimate, upper_bound, next_weight, next_value, current_item_index + 1)
                )

            next_upper_bound, next_cost_estimate = estimate_optimal_value_from_partial(accumulated_weight, accumulated_value, current_item_index + 1)
            if next_cost_estimate < current_maximum_cost:
                if next_upper_bound < current_maximum_cost:
                    current_maximum_cost = next_upper_bound
                heappush(
                    search_heap,
                    (next_cost_estimate, next_upper_bound, accumulated_weight, accumulated_value, current_item_index + 1)
                )

    return -current_maximum_cost

def main():
    number_of_types_of_items, maximum_knapsack_weight = [int(x) for x in input().split()]
    split_items = []

    for _ in range(number_of_types_of_items):
        item_value, item_weight, item_count = [int(x) for x in input().split()]
        for bit_position in range(item_count.bit_length() - 1):
            power_of_two_count = 2 ** bit_position
            item_count -= power_of_two_count
            split_items.append((item_value * power_of_two_count, item_weight * power_of_two_count))
        if item_count > 0:
            split_items.append((item_value * item_count, item_weight * item_count))

    print(get_maximum_knapsack_value(maximum_knapsack_weight, split_items))

if __name__ == '__main__':
    main()