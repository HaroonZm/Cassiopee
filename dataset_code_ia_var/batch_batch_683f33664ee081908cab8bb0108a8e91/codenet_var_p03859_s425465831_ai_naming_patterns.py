MODULO_CONST = 10 ** 9 + 7

def segment_counting_solver(seq_len, seg_count, bin_str, seg_bounds):

    prefix_one_counts = [0] * seq_len
    cumulative_ones = 0
    for idx in range(seq_len):
        if bin_str[idx] == '1':
            cumulative_ones += 1
        prefix_one_counts[idx] = cumulative_ones

    dp_table = [[0] * (seq_len + 1) for _ in range(seq_len + 1)]
    dp_table[0][0] = 1
    rightmost_seg_end = 0
    seg_ptr = 0
    for curr_idx in range(seq_len):
        while seg_ptr < seg_count:
            seg_start, seg_end = seg_bounds[seg_ptr]
            if seg_start <= curr_idx:
                rightmost_seg_end = max(rightmost_seg_end, seg_end)
                seg_ptr += 1
            else:
                break
        if rightmost_seg_end <= curr_idx:
            curr_ones = prefix_one_counts[curr_idx]
            if 0 < curr_ones:
                dp_table[curr_idx + 1][prefix_one_counts[curr_idx]] = (dp_table[curr_idx][curr_ones] + dp_table[curr_idx][curr_ones - 1]) % MODULO_CONST
            else:
                dp_table[curr_idx + 1][0] = dp_table[curr_idx][0]
        else:
            min_k = max(0, prefix_one_counts[rightmost_seg_end] - rightmost_seg_end + curr_idx)
            max_k = min(curr_idx + 1, prefix_one_counts[rightmost_seg_end]) + 1
            for one_cnt in range(min_k, max_k):
                if 0 < one_cnt:
                    dp_table[curr_idx + 1][one_cnt] = (dp_table[curr_idx][one_cnt] + dp_table[curr_idx][one_cnt - 1]) % MODULO_CONST
                else:
                    dp_table[curr_idx + 1][0] = dp_table[curr_idx][0]

    return dp_table[seq_len][prefix_one_counts[seq_len - 1]]

def main_executor():
    seq_len, seg_count = input().split()
    seq_len = int(seq_len)
    seg_count = int(seg_count)
    bin_str = input()
    seg_bounds = []
    for _ in range(seg_count):
        seg_l, seg_r = input().split()
        seg_l = int(seg_l) - 1
        seg_r = int(seg_r) - 1
        seg_bounds.append((seg_l, seg_r))

    print(segment_counting_solver(seq_len, seg_count, bin_str, seg_bounds))

if __name__ == '__main__':
    main_executor()