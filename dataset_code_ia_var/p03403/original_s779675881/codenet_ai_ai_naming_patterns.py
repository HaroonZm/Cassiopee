import sys
import math
import itertools
import collections
import bisect

def read_input():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')

CONST_INF = float('inf')
CONST_MOD = 10**9 + 7

total_min = CONST_INF
total_ans = 0
total_count = 0
total_product = 1

input_n = int(read_input())
input_arr = list(map(int, read_input().split()))
arr_extended = [0] + input_arr + [0]
accumulated_diff_sum = 0

for idx in range(input_n + 1):
    accumulated_diff_sum += abs(arr_extended[idx + 1] - arr_extended[idx])

for idx in range(1, input_n + 1):
    removed_cost = abs(arr_extended[idx + 1] - arr_extended[idx]) + abs(arr_extended[idx] - arr_extended[idx - 1])
    added_cost = abs(arr_extended[idx + 1] - arr_extended[idx - 1])
    updated_sum = accumulated_diff_sum - removed_cost + added_cost
    print(updated_sum)