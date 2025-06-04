input_size = int(input())
input_list = list(map(int, input().split()))
for index in range(input_size):
    input_list[index] ^= index & 1
block_lengths = []
current_value = input_list[0]
current_count = 0
for index in range(input_size):
    if current_value != input_list[index]:
        block_lengths.append(current_count)
        current_count = 1
    else:
        current_count += 1
    current_value = input_list[index]
block_lengths.append(current_count)
if len(block_lengths) == 1:
    print(block_lengths[0])
elif len(block_lengths) == 2:
    print(block_lengths[0] + block_lengths[1])
else:
    max_sum = 0
    for block_index in range(len(block_lengths) - 2):
        sum_blocks = block_lengths[block_index] + block_lengths[block_index + 1] + block_lengths[block_index + 2]
        if sum_blocks > max_sum:
            max_sum = sum_blocks
    print(max_sum)