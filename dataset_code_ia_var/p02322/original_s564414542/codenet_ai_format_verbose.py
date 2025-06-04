from heapq import heappush, heappop

def read_ints_from_input():
    return map(int, input().rstrip().split())

def decompose_quantity_by_powers_of_two(value, weight, max_quantity):
    current_quantity = 1
    remaining = max_quantity
    while current_quantity <= remaining:
        yield current_quantity
        remaining -= current_quantity
        current_quantity <<= 1
    if remaining:
        yield remaining

def resolve():
    number_of_items, max_total_weight = read_ints_from_input()
    items = [list(read_ints_from_input()) for _ in range(number_of_items)]

    all_items_by_power_of_two = []
    for value, weight, max_quantity in items:
        for quantity in decompose_quantity_by_powers_of_two(value, weight, max_quantity):
            total_value = value * quantity
            total_weight = weight * quantity
            all_items_by_power_of_two.append((total_value, total_weight))

    all_items_by_power_of_two.sort(key=lambda item: (item[0] / item[1], item[1]), reverse=True)
    total_unique_items = len(all_items_by_power_of_two)

    def upper_bound(best_value, current_weight, index):
        for idx in range(index, total_unique_items):
            item_value, item_weight = all_items_by_power_of_two[idx]
            if current_weight + item_weight > max_total_weight:
                leftover_capacity = max_total_weight - current_weight
                return (-best_value, -best_value - leftover_capacity * item_value / item_weight)
            current_weight += item_weight
            best_value += item_value
        return (-best_value, -best_value)

    initial_upper_bound, initial_secondary_upper_bound = upper_bound(0, 0, 0)
    best_known = initial_upper_bound
    answer = 0

    priority_queue = []
    heappush(priority_queue, (initial_secondary_upper_bound, initial_upper_bound, 0, 0, 0)) 

    while priority_queue:
        queue_secondary_ub, queue_primary_ub, current_value, current_weight, index = heappop(priority_queue)

        if queue_primary_ub > best_known:
            break

        if index >= total_unique_items:
            continue

        item_value, item_weight = all_items_by_power_of_two[index]

        if current_weight + item_weight < max_total_weight:
            heappush(priority_queue, (
                queue_primary_ub,
                queue_secondary_ub,
                current_value + item_value,
                current_weight + item_weight,
                index + 1
            ))

        next_upper_bound, next_secondary_upper_bound = upper_bound(current_value, current_weight, index + 1)
        if next_secondary_upper_bound <= best_known:
            if next_upper_bound < best_known:
                best_known = next_upper_bound
            heappush(priority_queue, (
                next_secondary_upper_bound,
                next_upper_bound,
                current_value,
                current_weight,
                index + 1
            ))

    print(-best_known)

if __name__ == "__main__":
    resolve()