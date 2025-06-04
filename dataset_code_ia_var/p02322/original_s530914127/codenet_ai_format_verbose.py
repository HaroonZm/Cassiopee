from typing import Tuple, List
from heapq import heappush, heappop

def calculate_maximum_knapsack_value(maximum_knapsack_weight: int, item_value_weight_list: List[Tuple[int, int]]) -> float:
    def branch_and_bound_estimate(current_weight: int, current_value: int, current_index: int) -> Tuple[int, float]:
        for next_item_index in range(current_index, total_number_of_items):
            item_value, item_weight = item_value_weight_list[next_item_index]
            if current_weight + item_weight > maximum_knapsack_weight:
                remaining_weight_capacity = maximum_knapsack_weight - current_weight
                estimated_fractional_value = (item_value / item_weight) * remaining_weight_capacity
                return (-current_value, -current_value - estimated_fractional_value)
            current_weight += item_weight
            current_value += item_value
        return (-current_value, float(-current_value))

    total_number_of_items = len(item_value_weight_list)

    item_value_weight_list.sort(key=lambda value_weight: value_weight[1], reverse=True)
    item_value_weight_list.sort(key=lambda value_weight: value_weight[0] / value_weight[1], reverse=True)

    initial_cost, initial_upper_bound = branch_and_bound_estimate(0, 0, 0)

    priority_queue = [(initial_upper_bound, initial_cost, 0, 0, 0)]
    best_negative_value_so_far = initial_cost

    while priority_queue:
        current_priority, current_best_estimate, accumulated_weight, accumulated_value, next_item_index = heappop(priority_queue)

        if current_priority > best_negative_value_so_far:
            break

        if next_item_index < total_number_of_items:
            next_item_value, next_item_weight = item_value_weight_list[next_item_index]

            if accumulated_weight + next_item_weight <= maximum_knapsack_weight:
                heappush(priority_queue, (
                    current_priority,
                    current_best_estimate,
                    accumulated_weight + next_item_weight,
                    accumulated_value + next_item_value,
                    next_item_index + 1
                ))

            skipping_cost, skipping_upper_bound = branch_and_bound_estimate(accumulated_weight, accumulated_value, next_item_index + 1)
            if skipping_upper_bound < best_negative_value_so_far:
                if skipping_cost < best_negative_value_so_far:
                    best_negative_value_so_far = skipping_cost
                heappush(priority_queue, (
                    skipping_upper_bound,
                    skipping_cost,
                    accumulated_weight,
                    accumulated_value,
                    next_item_index + 1
                ))

    return -best_negative_value_so_far

if __name__ == '__main__':
    number_of_items, knapsack_capacity = map(int, input().split())
    expanded_item_value_weight_list: List[Tuple[int, int]] = []

    for _ in range(number_of_items):
        item_value, item_weight, item_count = map(int, input().split())
        power_of_two = 1
        remaining_count = item_count
        while (power_of_two <= remaining_count):
            expanded_item_value_weight_list.append((item_value * power_of_two, item_weight * power_of_two))
            remaining_count -= power_of_two
            power_of_two <<= 1
        if remaining_count > 0:
            expanded_item_value_weight_list.append((item_value * remaining_count, item_weight * remaining_count))

    print(calculate_maximum_knapsack_value(knapsack_capacity, expanded_item_value_weight_list))