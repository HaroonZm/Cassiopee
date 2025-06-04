import math
import queue
import bisect
from collections import deque, defaultdict
import heapq as heapq_module
from sys import stdin, setrecursionlimit

input_reader = stdin.readline
setrecursionlimit(10**7)

MOD_VALUE = 998244353
DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():
    input_length = int(input_reader())
    input_string = input()
    color_map = {"R": 0, "G": 1, "B": 2}
    total_ways = 1
    color_counts = [0, 0, 0]
    state_counts = [0, 0, 0]
    result_counts = [0, 0, 0]
    for current_char in input_string:
        color_index = color_map[current_char]
        color_counts[color_index] += 1
        if color_counts[color_index] > color_counts[color_index-1] and color_counts[color_index] > color_counts[color_index-2]:
            state_counts[color_index] += 1
        elif color_counts[color_index] <= color_counts[color_index-1] and color_counts[color_index] <= color_counts[color_index-2]:
            total_ways *= result_counts[color_index]
            result_counts[color_index] -= 1
        else:
            if state_counts[color_index-1] == 0:
                result_counts[color_index-1] += 1
                total_ways *= state_counts[color_index-2]
                state_counts[color_index-2] -= 1
            else:
                result_counts[color_index-2] += 1
                total_ways *= state_counts[color_index-1]
                state_counts[color_index-1] -= 1
        total_ways %= MOD_VALUE

    for factorial_index in range(1, input_length + 1):
        total_ways *= factorial_index
        total_ways %= MOD_VALUE
    print(total_ways)
    return None

if __name__ == '__main__':
    main()