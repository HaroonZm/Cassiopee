import collections as collections_module
while True:
    num_items = int(input())
    if num_items == 0:
        break
    item_list = raw_input().split()
    for current_length in range(1, num_items + 1):
        counter = collections_module.Counter(item_list[:current_length])
        most_common_list = counter.most_common() + [('', 0)]
        if most_common_list[0][1] > most_common_list[1][1] + num_items - current_length:
            print most_common_list[0][0], current_length
            break
    else:
        print("TIE")