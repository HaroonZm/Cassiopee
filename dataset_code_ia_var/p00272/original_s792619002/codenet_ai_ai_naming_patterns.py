for index_input in range(4):
    item_type, item_quantity = map(int, input().split())
    if item_type == 1:
        print(6000 * item_quantity)
    elif item_type == 2:
        print(4000 * item_quantity)
    elif item_type == 3:
        print(3000 * item_quantity)
    elif item_type == 4:
        print(2000 * item_quantity)