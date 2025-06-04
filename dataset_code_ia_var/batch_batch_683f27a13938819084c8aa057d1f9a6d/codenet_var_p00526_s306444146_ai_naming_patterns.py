segment_count = int(input())
segment_values = list(map(int, input().split()))
block_lengths = []
block_start_index = 0

for position_index in range(segment_count - 1):
    if segment_values[position_index + 1] == segment_values[position_index]:
        block_end_index = position_index + 1
        block_lengths.append(block_end_index - block_start_index)
        block_start_index = block_end_index
block_lengths.append(segment_count - block_start_index)

max_sum_blocks = 0

for block_index in range(len(block_lengths) - 2):
    current_sum = block_lengths[block_index] + block_lengths[block_index + 1] + block_lengths[block_index + 2]
    if current_sum > max_sum_blocks:
        max_sum_blocks = current_sum

if len(block_lengths) == 2:
    pair_sum_1 = block_lengths[0] + block_lengths[1]
    pair_sum_2 = block_lengths[-2] + block_lengths[-1]
    max_sum_blocks = max(max_sum_blocks, pair_sum_1, pair_sum_2)

if len(block_lengths) == 1:
    max_sum_blocks = block_lengths[0]

print(max_sum_blocks)