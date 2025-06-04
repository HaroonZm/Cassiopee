item_count, selection_limit, _unused_param = map(int, input().split())
item_quantities = [0] + list(map(int, input().split()))
item_list = [tuple(map(int, input().split())) for _ in range(item_count)]
item_list.sort(key=lambda item: item[1], reverse=True)
total_value = 0
selected_count = 0
for item_index in range(item_count):
    item_type = item_list[item_index][0]
    item_value = item_list[item_index][1]
    if item_quantities[item_type]:
        item_quantities[item_type] -= 1
        total_value += item_value
        selected_count += 1
        if selected_count == selection_limit:
            break
print(total_value)