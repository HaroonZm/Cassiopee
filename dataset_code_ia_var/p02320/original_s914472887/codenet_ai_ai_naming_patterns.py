input_item_count, input_weight_limit, *input_item_data = map(int, open(0).read().split())
item_count_weight_quantity_map = {}
for item_value, item_weight, item_quantity in zip(*[iter(input_item_data)]*3):
    item_key = (item_value, item_weight)
    item_count_weight_quantity_map[item_key] = item_count_weight_quantity_map.get(item_key, 0) + item_quantity
max_value_at_weight = [0] * (input_weight_limit + 1)
for (item_value, item_weight), item_quantity in item_count_weight_quantity_map.items():
    current_weight = item_weight
    current_value = item_value
    item_quantity_bits = item_quantity.bit_length()
    for quantity_power_index in range(item_quantity_bits):
        if quantity_power_index == item_quantity_bits - 1:
            pack_weight = current_weight * (item_quantity - 2 ** (item_quantity_bits - 1) + 1)
            pack_value = current_value * (item_quantity - 2 ** (item_quantity_bits - 1) + 1)
        else:
            pack_weight = current_weight * (2 ** quantity_power_index)
            pack_value = current_value * (2 ** quantity_power_index)
        for possible_weight in range(input_weight_limit, pack_weight - 1, -1):
            possible_value = max_value_at_weight[possible_weight - pack_weight] + pack_value
            if possible_value > max_value_at_weight[possible_weight]:
                max_value_at_weight[possible_weight] = possible_value
print(max_value_at_weight[input_weight_limit])