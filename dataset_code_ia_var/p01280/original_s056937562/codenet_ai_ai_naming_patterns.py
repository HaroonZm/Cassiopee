from itertools import cycle as cyc

def main_loop():
    while True:
        group_count = int(input())
        if group_count == 0:
            break
        group_data = {}
        for group_index in range(group_count):
            input_tokens = [int(token) for token in input().split()]
            key_id, rotation, *quantity_list = input_tokens
            rotated_quantities = quantity_list[rotation:] + quantity_list[:rotation]
            if key_id not in group_data:
                group_data[key_id] = rotated_quantities
            else:
                group_data[key_id] = [prev + curr for prev, curr in zip(group_data[key_id], rotated_quantities)]
        circle_length = 16 * 9 * 5 * 7 * 11
        special_keys = [13, 17, 19, 23, 1]
        special_sum = sum(max(group_data.pop(special_key, [0])) for special_key in special_keys)
        cycle_max = max(
            sum(values) for _, values in zip(
                range(circle_length - 1),
                zip(*[cyc(vals) for vals in group_data.values()])
            )
        )
        print(special_sum + cycle_max)

main_loop()