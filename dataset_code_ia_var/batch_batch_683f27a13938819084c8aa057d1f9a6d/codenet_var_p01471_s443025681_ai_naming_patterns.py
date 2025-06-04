input_line = (raw_input()).split(" ")
item_count = int(input_line[0])
capacity_limit = int(input_line[1])
items_list = [0] * item_count
positive_items = []
negative_items = []
current_capacity = 0.0
total_value = 0.0

for item_index in range(item_count):
    item_line = (raw_input()).split(" ")
    items_list[item_index] = [0] * 3
    items_list[item_index][1] = int(item_line[0]) * 1.0  # weight
    items_list[item_index][2] = int(item_line[1]) * 1.0  # value
    if items_list[item_index][1] <= 0 and items_list[item_index][2] >= 0:
        current_capacity += items_list[item_index][1]
        total_value += items_list[item_index][2]
    elif items_list[item_index][1] > 0 and items_list[item_index][2] > 0:
        positive_items.append([1.0 * items_list[item_index][1] / items_list[item_index][2], items_list[item_index][1], items_list[item_index][2], 0.0])
    elif items_list[item_index][1] < 0 and items_list[item_index][2] < 0:
        negative_items.append([-1.0 * items_list[item_index][1] / items_list[item_index][2], items_list[item_index][1], items_list[item_index][2], 0.0])

positive_items = sorted(positive_items)
negative_items = sorted(negative_items)
negative_index = 0

for positive_index in range(len(positive_items)):
    if positive_items[positive_index][1] + current_capacity <= capacity_limit:
        current_capacity += positive_items[positive_index][1]
        total_value += positive_items[positive_index][2]
        positive_items[positive_index][3] = 1.0
    else:
        positive_items[positive_index][3] = 1.0 * (capacity_limit - current_capacity) / positive_items[positive_index][1]
        current_capacity = capacity_limit
        total_value += positive_items[positive_index][2] * positive_items[positive_index][3]
        continue_swapping = True if (len(negative_items) > 0 and (positive_items[positive_index][0] < (-negative_items[negative_index][0]))) else False
        while continue_swapping:
            if (1 - positive_items[positive_index][3]) * positive_items[positive_index][1] / (-negative_items[negative_index][1]) < 1 - negative_items[negative_index][3]:
                negative_items[negative_index][3] += (1 - positive_items[positive_index][3]) * positive_items[positive_index][1] / (-negative_items[negative_index][1])
                total_value += (1 - positive_items[positive_index][3]) * (positive_items[positive_index][2] - negative_items[negative_index][2] * positive_items[positive_index][1] / negative_items[negative_index][1])
                positive_items[positive_index][3] = 1.0
                continue_swapping = False
            else:
                positive_items[positive_index][3] += (1 - negative_items[negative_index][3]) * (-negative_items[negative_index][1]) / positive_items[positive_index][1]
                total_value += (1 - negative_items[negative_index][3]) * (negative_items[negative_index][2] + positive_items[positive_index][2] * (-negative_items[negative_index][1]) / positive_items[positive_index][1])
                negative_items[negative_index][3] = 1.0
                negative_index += 1
                if negative_index >= len(negative_items):
                    continue_swapping = False
                elif positive_items[positive_index][0] >= (-negative_items[negative_index][0]):
                    continue_swapping = False

print(total_value)