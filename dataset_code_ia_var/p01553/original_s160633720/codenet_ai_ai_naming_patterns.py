import sys
import math
from bisect import bisect_right as bisect_right_fn
from bisect import bisect_left as bisect_left_fn
sys.setrecursionlimit(2147483647)
from heapq import heappush as heap_push_fn, heappop as heap_pop_fn, heappushpop as heap_pushpop_fn
from collections import defaultdict as defaultdict_cls
from itertools import accumulate as accumulate_fn
from collections import Counter as counter_cls
from collections import deque as deque_cls
from operator import itemgetter as itemgetter_fn
from itertools import permutations as permutations_fn

MOD_CONST = 10**9 + 7
INF_CONST = float('inf')

def read_single_int():
    return int(sys.stdin.readline())

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def main():
    input_size = read_single_int()
    dp_table = [[0] * (input_size + 2) for _ in range(input_size + 1)]
    dp_table[0][0] = 1
    for position_idx in range(input_size):
        input_char = input()
        if input_char == 'U':
            for connect_count in range(input_size):
                dp_table[position_idx + 1][connect_count] += dp_table[position_idx][connect_count]
                dp_table[position_idx + 1][connect_count + 1] += dp_table[position_idx][connect_count] * (position_idx - connect_count)
                dp_table[position_idx + 1][connect_count + 1] %= MOD_CONST
        elif input_char == '-':
            for connect_count in range(input_size):
                dp_table[position_idx + 1][connect_count + 1] += dp_table[position_idx][connect_count]
                dp_table[position_idx + 1][connect_count + 1] %= MOD_CONST
        else:
            for connect_count in range(input_size):
                dp_table[position_idx + 1][connect_count + 2] += dp_table[position_idx][connect_count] * (position_idx - connect_count) * (position_idx - connect_count)
                dp_table[position_idx + 1][connect_count + 2] %= MOD_CONST
                dp_table[position_idx + 1][connect_count + 1] += dp_table[position_idx][connect_count] * (position_idx - connect_count)
                dp_table[position_idx + 1][connect_count + 1] %= MOD_CONST
    print(dp_table[input_size][input_size])

if __name__ == "__main__":
    main()