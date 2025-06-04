input_str, max_segments = input().split()
max_segments = int(max_segments)
max_segments = min(max_segments, 300)
MODULO = 998244353

segment_lengths = []
current_length = 0
for index in range(len(input_str)):
    if input_str[index] == "0":
        segment_lengths.append(current_length)
        current_length = 0
    else:
        current_length += 1

if current_length != 0:
    segment_lengths.append(current_length)

num_segments = len(segment_lengths)
max_segments = min(sum(segment_lengths), max_segments)

dp_table = [[[0 for _ in range(max_segments + 1)] for _ in range(max_segments + 1)] for _ in range(num_segments + 1)]
for j_idx in range(max_segments + 1):
    dp_table[num_segments][j_idx][j_idx] = 1

prefix_sum = [segment_lengths[i] for i in range(num_segments)]
suffix_sum = [segment_lengths[i] for i in range(num_segments)]
for idx in range(1, num_segments):
    prefix_sum[idx] += prefix_sum[idx - 1]
prefix_sum = [0] + prefix_sum
for idx in range(num_segments - 2, -1, -1):
    suffix_sum[idx] += suffix_sum[idx + 1]

for seg_idx in range(num_segments - 1, -1, -1):
    for start_seg in range(max_segments + 1):
        for end_seg in range(min(prefix_sum[seg_idx], max_segments) + 1):
            min_shift = max(end_seg - start_seg, -segment_lengths[seg_idx])
            temp_sum = 0
            for l_var in range(max(0, min_shift), max_segments - start_seg + 1):
                temp_sum += dp_table[seg_idx + 1][start_seg + l_var][end_seg]
            for l_var in range(1, min(max_segments - end_seg, -min_shift) + 1):
                temp_sum += dp_table[seg_idx + 1][start_seg][end_seg + l_var]
            dp_table[seg_idx][start_seg][end_seg] = temp_sum % MODULO

print(dp_table[0][0][0])