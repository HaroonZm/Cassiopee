while True:
    item_count, group_size = input().split()
    item_count = int(item_count)
    group_size = int(group_size)
    if item_count == 0:
        break
    item_price_list = list(map(int, input().split()))
    item_price_list.sort(reverse=True)
    for item_index in range(item_count):
        if (item_index + 1) % group_size == 0:
            item_price_list[item_index] = -1
    for remove_index in range(item_count // group_size):
        item_price_list.remove(-1)
    total_payment = sum(item_price_list)
    print(total_payment)