import sys
import numpy as np

read_line = sys.stdin.readline

MOD_CONST = 10 ** 9 + 7

total_length, query_count = map(int, read_line().split())
char_array = np.array(list(read_line().rstrip()), dtype='U1')
query_ranges = [[int(x) for x in read_line().split()] for _ in range(query_count)]

cumsum_zeros = (char_array == '0').cumsum()
cumsum_ones = (char_array == '1').cumsum()
max_zeros_prefix = cumsum_zeros.copy()
max_ones_prefix = cumsum_ones.copy()

for left_idx, right_idx in query_ranges:
    max_zeros_prefix[left_idx - 1] = max(max_zeros_prefix[left_idx - 1], cumsum_zeros[right_idx - 1])
    max_ones_prefix[left_idx - 1] = max(max_ones_prefix[left_idx - 1], cumsum_ones[right_idx - 1])

np.maximum.accumulate(max_zeros_prefix, out=max_zeros_prefix)
np.maximum.accumulate(max_ones_prefix, out=max_ones_prefix)

dp_array = np.zeros(total_length + 1, dtype=np.int64)
dp_array[0] = 1

for pos in range(total_length):
    prev_dp_array = dp_array
    dp_array = np.zeros(total_length + 1, dtype=np.int64)
    zero_left = max(0, (pos + 1) - max_zeros_prefix[pos])
    zero_right = max_ones_prefix[pos]
    dp_array[zero_left:zero_right + 1] += prev_dp_array[zero_left:zero_right + 1]
    one_left = max(1, zero_left)
    dp_array[one_left:zero_right + 1] += prev_dp_array[one_left - 1:zero_right]
    dp_array %= MOD_CONST

final_answer = dp_array.sum()
print(final_answer)