total_items, group_size, reserved_size = map(int, input().split(' '))

items_per_round = group_size + reserved_size

remaining_items_after_full_groups = total_items % items_per_round

if remaining_items_after_full_groups >= reserved_size:
    max_full_groups = int(total_items / items_per_round)
    print(max_full_groups)
else:
    max_full_groups = int(total_items / items_per_round) - 1
    print(max_full_groups)