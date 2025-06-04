import sys
input_stream = sys.stdin.readline
output_stream = sys.stdout.write

def process_selection():
    num_items = int(input_stream())
    label_list = [0] * num_items
    value_list = [0] * num_items
    for idx in range(num_items):
        label_str, value_str = input_stream().split()
        label_list[idx] = 1 if label_str == 'y' else 0
        value_list[idx] = int(value_str)
    result_count = 0
    index_sequence = list(range(num_items))
    index_sequence.sort(key=lambda idx: value_list[idx])
    used_flags = [0] * num_items
    for current_idx in index_sequence:
        if label_list[current_idx] == 0 or used_flags[current_idx]:
            continue
        current_value = value_list[current_idx]
        used_flags[current_idx] = 1
        result_count += 1
        left_idx = current_idx - 1
        while left_idx >= 0 and (label_list[left_idx] or value_list[left_idx] < current_value):
            if label_list[left_idx]:
                used_flags[left_idx] = 1
            left_idx -= 1
        right_idx = current_idx + 1
        while right_idx < num_items and (label_list[right_idx] or value_list[right_idx] < current_value):
            if label_list[right_idx]:
                used_flags[right_idx] = 1
            right_idx += 1
    output_stream(f"{result_count}\n")

process_selection()