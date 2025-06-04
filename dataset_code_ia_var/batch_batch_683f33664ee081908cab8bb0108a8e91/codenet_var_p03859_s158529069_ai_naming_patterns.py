from collections import deque
import heapq

def atcoder_arc065_d():
    num_length, num_range = map(int, input().split())
    binary_string = input()

    range_info_list = []
    for idx_range in range(num_range):
        left, right = map(int, input().split())
        range_info_list.append([left-1, right-1, idx_range])
    range_info_list.append([num_length, float("inf"), float("inf")])

    next_index_to_process = 0
    ones_count = 0
    one_range_list = []
    one_range_list_index = 0
    current_right = 0

    for loop_index in range(num_range):
        current_left, next_right, _ = range_info_list[loop_index]
        current_right = max(next_right, current_right)
        next_left = range_info_list[loop_index + 1][0]

        for pos in range(max(current_left, next_index_to_process), current_right + 1):
            if binary_string[pos] == "1":
                one_range_list.append([current_left, None])
                ones_count += 1
                next_index_to_process = max(next_index_to_process, pos + 1)
        if current_right - next_left + 1 < ones_count:
            for repeat_index in range(min(ones_count, ones_count - (current_right - next_left + 1))):
                one_range_list[one_range_list_index][1] = current_right - ones_count + 1
                ones_count -= 1
                one_range_list_index += 1

    MODULO_BASE = 10 ** 9 + 7
    arrangement_count_dp = [0] * (num_length + 1)

    for idx_one in range(len(one_range_list)):
        left_index, right_index = one_range_list[idx_one]

        updated_dp = [0] * (num_length + 1)

        if idx_one == 0:
            updated_dp[left_index] += 1
            updated_dp[right_index + 1] -= 1
        else:
            for value_index in range(right_index):
                updated_dp[max(left_index, value_index + 1)] += arrangement_count_dp[value_index]
                updated_dp[right_index + 1] -= arrangement_count_dp[value_index]
        for idx_sum in range(num_length):
            updated_dp[idx_sum + 1] += updated_dp[idx_sum]
            updated_dp[idx_sum] %= MODULO_BASE
            updated_dp[idx_sum + 1] %= MODULO_BASE

        arrangement_count_dp = updated_dp

    print(sum(arrangement_count_dp[0:num_length]) % MODULO_BASE)

atcoder_arc065_d()