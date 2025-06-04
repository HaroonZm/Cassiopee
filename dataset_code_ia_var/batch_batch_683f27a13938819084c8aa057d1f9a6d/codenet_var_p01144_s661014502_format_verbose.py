while True:
    number_of_items, max_capacity = map(int, input().split())
    
    if number_of_items == 0:
        break

    item_list = []
    for _ in range(number_of_items):
        item_quantity, item_cost_per_unit = map(int, input().split())
        item_list.append([item_quantity, item_cost_per_unit])

    # Sort items by cost per unit in descending order to remove from most expensive first
    item_list = sorted(item_list, key=lambda item: -item[1])

    current_capacity = max_capacity

    for item in item_list:
        if current_capacity <= 0:
            break

        if item[0] <= current_capacity:
            current_capacity -= item[0]
            item[0] = 0
        else:
            item[0] -= current_capacity
            current_capacity = 0

    total_cost = 0
    for item in item_list:
        remaining_quantity = item[0]
        cost_per_unit = item[1]
        total_cost += remaining_quantity * cost_per_unit

    print(total_cost)