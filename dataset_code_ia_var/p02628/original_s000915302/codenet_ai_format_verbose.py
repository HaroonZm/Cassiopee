number_of_items, number_of_items_to_select = map(int, input().split())

item_values_list = list(map(int, input().split()))

sorted_item_values = sorted(item_values_list)

sum_of_selected_items = 0

for value in sorted_item_values[:number_of_items_to_select]:
    sum_of_selected_items += value

print(sum_of_selected_items)