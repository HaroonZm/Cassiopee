number_of_items, max_weight_capacity = map(int, raw_input().split())

item_weights = sorted([int(raw_input()) for _ in xrange(number_of_items)])

total_weight_of_all_items = sum(item_weights)

number_of_ways_to_achieve_weight = [1] + [0] * max_weight_capacity

total_valid_combinations = 0 if total_weight_of_all_items > max_weight_capacity else 1

for current_index, current_item_weight in zip(xrange(number_of_items, -1, -1), item_weights[::-1]):
    
    total_weight_of_all_items -= current_item_weight
    
    remaining_capacity = max_weight_capacity - total_weight_of_all_items
    
    if remaining_capacity >= 0:
        sum_combinations_for_current = sum(
            number_of_ways_to_achieve_weight[
                max(0, remaining_capacity - current_item_weight + 1)
                : remaining_capacity + 1
            ]
        )
        total_valid_combinations = (
            total_valid_combinations + sum_combinations_for_current
        ) % (10 ** 9 + 7)
    
    for possible_weight in xrange(max_weight_capacity, current_item_weight - 1, -1):
        number_of_ways_to_achieve_weight[possible_weight] += number_of_ways_to_achieve_weight[possible_weight - current_item_weight]
        
print total_valid_combinations