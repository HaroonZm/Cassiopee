input_str, max_blocks = input().split()
max_blocks = int(max_blocks)
max_blocks = min(max_blocks, 300)
modulo = 998244353

segments = []
current_segment = 0
for idx in range(len(input_str)):
    if input_str[idx] == "0":
        segments.append(current_segment)
        current_segment = 0
    else:
        current_segment += 1
if current_segment != 0:
    segments.append(current_segment)

num_segments = len(segments)
max_blocks = min(sum(segments), max_blocks)

dp_table = [[[0 for _ in range(max_blocks + 1)] for _ in range(max_blocks + 1)] for _ in range(num_segments + 1)]

for count1 in range(max_blocks + 1):
    dp_table[num_segments][count1][count1] = 1

prefix_sum = [segments[i] for i in range(num_segments)]
suffix_sum = [segments[i] for i in range(num_segments)]
for idx in range(1, num_segments):
    prefix_sum[idx] += prefix_sum[idx - 1]
prefix_sum = [0] + prefix_sum
for idx in range(num_segments - 2, -1, -1):
    suffix_sum[idx] += suffix_sum[idx + 1]

for seg_idx in range(num_segments - 1, -1, -1):
    for filled_blocks in range(min(prefix_sum[seg_idx], max_blocks) + 1):
        for used_blocks in range(min(max_blocks, filled_blocks + suffix_sum[seg_idx]) + 1):
            min_delta = max(filled_blocks - used_blocks, -segments[seg_idx])
            total_ways = 0
            for add_blocks in range(max(0, min_delta), max_blocks - used_blocks + 1):
                total_ways += dp_table[seg_idx + 1][used_blocks + add_blocks][filled_blocks]
            for split_blocks in range(1, min(max_blocks - filled_blocks, -min_delta) + 1):
                total_ways += dp_table[seg_idx + 1][used_blocks][filled_blocks + split_blocks]
            dp_table[seg_idx][used_blocks][filled_blocks] = total_ways % modulo

print(dp_table[0][0][0])