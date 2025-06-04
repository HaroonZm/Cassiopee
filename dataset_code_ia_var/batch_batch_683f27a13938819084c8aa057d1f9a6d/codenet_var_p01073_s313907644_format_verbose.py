number_of_items, max_total_selections, max_item_types = map(int, input().split())

item_values = list(map(int, input().split()))
item_selectable_counts = list(map(int, input().split()))

items = list(zip(item_values, item_selectable_counts))

items_sorted_by_value_desc = sorted(items, key=lambda item: -item[0])

# dp_matrix[selected_types][total_selections] 
# = max possible value with selected_types types and total_selections selections
dp_matrix = [
    [0 for _ in range(max_total_selections + 1)]
    for _ in range(max_item_types + 1)
]

for item_value, item_max_count in items_sorted_by_value_desc:
    for selected_types in range(max_item_types - 1, -1, -1):
        for selections_so_far in range(max_total_selections - 1, -1, -1):
            possible_this_item = min(item_max_count, max_total_selections - selections_so_far)
            updated_total_selections = selections_so_far + possible_this_item
            updated_types = selected_types + 1
            new_value = dp_matrix[selected_types][selections_so_far] + possible_this_item * item_value
            dp_matrix[updated_types][updated_total_selections] = max(
                dp_matrix[updated_types][updated_total_selections],
                new_value
            )

maximum_obtainable_value = 0

for selected_types in range(max_item_types + 1):
    for total_selections in range(max_total_selections + 1):
        remaining_selections = max_total_selections - total_selections
        candidate_value = dp_matrix[selected_types][total_selections] + remaining_selections
        maximum_obtainable_value = max(maximum_obtainable_value, candidate_value)

print(maximum_obtainable_value)