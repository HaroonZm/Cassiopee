num_items = input()
num_swaps = input()
item_indices = range(1, num_items + 1)
swap_iterations = range(num_swaps)
for swap_index in swap_iterations:
    swap_from_index, swap_to_index = map(int, raw_input().split(","))
    item_indices[swap_from_index - 1], item_indices[swap_to_index - 1] = item_indices[swap_to_index - 1], item_indices[swap_from_index - 1]
for item_value in item_indices:
    print item_value