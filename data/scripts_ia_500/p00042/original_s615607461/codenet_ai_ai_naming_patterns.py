case_number = 0
for weight_limit_str in iter(input, '0'):
    case_number += 1
    max_weight = int(weight_limit_str)
    dp_array = [0] * (max_weight + 1)
    num_items = int(input())
    for _ in range(num_items):
        value_str, weight_str = input().split(',')
        item_value = int(value_str)
        item_weight = int(weight_str)
        for current_weight in range(max_weight, item_weight - 1, -1):
            if dp_array[current_weight] < dp_array[current_weight - item_weight] + item_value:
                dp_array[current_weight] = dp_array[current_weight - item_weight] + item_value
    for possible_weight in range(max_weight + 1):
        if dp_array[max_weight] == dp_array[possible_weight]:
            print(f'Case {case_number}:\n{dp_array[max_weight]}\n{possible_weight}')
            break