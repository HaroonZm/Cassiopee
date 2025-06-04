while True:

    quantity_of_items, items_in_each_bag = input().split()

    quantity_of_items = int(quantity_of_items)
    items_in_each_bag = int(items_in_each_bag)

    if quantity_of_items == 0:
        break

    item_prices = list(map(int, input().split()))

    item_prices.sort(reverse=True)

    for current_item_index in range(quantity_of_items):
        if (current_item_index + 1) % items_in_each_bag == 0:
            item_prices[current_item_index] = -1

    number_of_discarded_items = quantity_of_items // items_in_each_bag

    for _ in range(number_of_discarded_items):
        item_prices.remove(-1)

    total_payment = sum(item_prices)

    print(total_payment)