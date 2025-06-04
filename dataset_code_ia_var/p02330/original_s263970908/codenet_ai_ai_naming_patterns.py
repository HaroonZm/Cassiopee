import sys
import bisect

def run_combination_counter():
    input_n, input_k, input_l, input_r = map(int, sys.stdin.readline().split())
    input_values = tuple(map(int, sys.stdin.readline().split()))
    mid_idx = (input_n - 1) // 2
    left_subsets_by_count = [[] for _ in range(mid_idx + 1)]

    for left_mask in range(1 << mid_idx):
        left_count = 0
        left_sum = 0
        for left_bit in range(mid_idx):
            if (left_mask >> left_bit) & 1:
                left_count += 1
                left_sum += input_values[left_bit]
        left_subsets_by_count[left_count].append(left_sum)

    for subsets in left_subsets_by_count:
        subsets.sort()

    total_valid_combinations = 0
    right_length = input_n - mid_idx
    for right_mask in range(1 << right_length):
        right_count = 0
        right_sum = 0
        for right_bit in range(right_length):
            if (right_mask >> right_bit) & 1:
                right_count += 1
                right_sum += input_values[mid_idx + right_bit]
        for total_count in range(input_k - right_count, input_k - right_count + 1):
            if 0 <= total_count <= mid_idx:
                valid_left = bisect.bisect_right(left_subsets_by_count[total_count], input_r - right_sum) - \
                             bisect.bisect_right(left_subsets_by_count[total_count], input_l - right_sum - 1)
                total_valid_combinations += valid_left

    print(total_valid_combinations)

if __name__ == '__main__':
    run_combination_counter()