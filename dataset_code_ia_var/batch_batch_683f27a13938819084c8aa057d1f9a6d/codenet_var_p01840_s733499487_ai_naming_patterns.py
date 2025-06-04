input_n, input_m, input_t = map(int, input().split())
occupied_distance = 0
positions_list = [int(position_value) for position_value in input().split()]
current_block_start = positions_list[0] - input_m
current_block_end = positions_list[0] + input_m
for position_index in range(1, input_n):
    if positions_list[position_index] > current_block_end + input_m:
        occupied_distance += current_block_end - current_block_start
        current_block_start = positions_list[position_index] - input_m
    current_block_end = positions_list[position_index] + input_m
if current_block_end < input_t:
    occupied_distance += current_block_end - current_block_start
else:
    occupied_distance += input_t - current_block_start
print(input_t - occupied_distance)