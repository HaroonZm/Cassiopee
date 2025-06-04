def main():
    from collections import deque
    from functools import cmp_to_key

    # Lecture et extraction des données d'entrée
    input_values = list(map(int, open(0).read().split()))
    number_of_items, max_weight, *raw_items = input_values

    items = [list(grouped_item) for grouped_item in zip(*[iter(raw_items)] * 3)]

    # Calcul de la valeur maximale par item et somme totale max possible
    max_item_value = max(item_value for item_value, item_weight, item_count in items)
    total_possible_value = 0
    items_to_decompose = []

    for item_index, (item_value, item_weight, item_count) in enumerate(items):
        max_count_for_grouping = min(item_count, max_item_value - 1)
        remaining_count_to_split = item_count - max_count_for_grouping
        items[item_index][2] = max_count_for_grouping

        if remaining_count_to_split:
            items_to_decompose.append((item_value, item_weight, remaining_count_to_split))

        total_possible_value += item_value * max_count_for_grouping

    INFINITE_WEIGHT = 1 << 60
    min_weight_for_value = [INFINITE_WEIGHT] * (total_possible_value + 1)
    min_weight_for_value[0] = 0

    for item_value, item_weight, item_count in items:
        for value_offset in range(item_value):
            monotonic_queue = deque()
            for group_count in range(total_possible_value + 1):
                value_at_index = value_offset + group_count * item_value
                if value_at_index > total_possible_value:
                    break
                current_weight = min_weight_for_value[value_at_index] - group_count * item_weight
                while monotonic_queue and monotonic_queue[-1][1] >= current_weight:
                    monotonic_queue.pop()
                monotonic_queue.append((group_count, current_weight))

                if monotonic_queue:
                    oldest_group_count, oldest_weight = monotonic_queue[0]
                    min_weight_for_value[value_at_index] = oldest_weight + group_count * item_weight
                    if oldest_group_count == group_count - item_count:
                        monotonic_queue.popleft()

    # Tri des items restants selon densité valeur/poids (glouton)
    items_to_decompose.sort(
        key=cmp_to_key(lambda item_a, item_b: -1 if item_a[0] * item_b[1] > item_a[1] * item_b[0] else 1)
    )

    maximal_value_achieved = 0

    for current_value, current_weight in enumerate(min_weight_for_value):
        if current_weight > max_weight:
            continue
        remaining_weight = max_weight - current_weight
        temp_value = current_value

        for leftover_item_value, leftover_item_weight, leftover_item_count in items_to_decompose:
            max_number_of_this_item = min(leftover_item_count, remaining_weight // leftover_item_weight)
            if max_number_of_this_item:
                temp_value += max_number_of_this_item * leftover_item_value
                remaining_weight -= max_number_of_this_item * leftover_item_weight

        if maximal_value_achieved < temp_value:
            maximal_value_achieved = temp_value

    print(maximal_value_achieved)


if __name__ == '__main__':
    main()