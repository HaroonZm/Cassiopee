import sys

input_count_total = int(sys.stdin.readline().rstrip())
input_swap_count = int(sys.stdin.readline().rstrip())
swap_operations_list = []
for swap_index in range(input_swap_count):
    swap_operations_list.append(list(map(int, sys.stdin.readline().rstrip().split(','))))
for position_index in range(input_count_total):
    current_position = position_index + 1
    for swap_pair in reversed(swap_operations_list):
        if current_position in swap_pair:
            current_position = swap_pair[0] if current_position == swap_pair[1] else swap_pair[1]
    print(current_position)