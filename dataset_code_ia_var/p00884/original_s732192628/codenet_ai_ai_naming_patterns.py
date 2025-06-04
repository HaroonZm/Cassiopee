import sys
import math
import re
from bisect import bisect_right as bisect_right_func
from bisect import bisect_left as bisect_left_func
sys.setrecursionlimit(1000000)
from heapq import heappush as heap_push, heappop as heap_pop, heappushpop as heap_pushpop
from collections import defaultdict as default_dict
from itertools import accumulate as iter_accumulate
from collections import Counter as counter_class
from collections import deque as deque_class
from operator import itemgetter as item_getter
from itertools import permutations as iter_permutations

CONST_MODULO = 10 ** 9 + 7
CONST_INFINITY = float('inf')

def read_single_int():
    return int(sys.stdin.readline())

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

while True:
    num_entries = read_single_int()
    if num_entries == 0:
        quit()
    dependency_dict = default_dict(dict)
    counted_dict = default_dict(lambda: False)
    checked_dict = default_dict(lambda: False)
    node_stack = []
    for index in range(num_entries):
        line_split = input()[:-1].split(':')
        node_key = line_split[0]
        neighbor_nodes = line_split[1].split(',')
        for neighbor in neighbor_nodes:
            dependency_dict[node_key][neighbor] = 1
            if index != 0:
                continue
            node_stack.append(neighbor)
    answer_count = 0
    while node_stack:
        current_node = node_stack.pop()
        if checked_dict[current_node]:
            continue
        checked_dict[current_node] = True
        if len(dependency_dict[current_node]) == 0 and not counted_dict[current_node]:
            answer_count += 1
            counted_dict[current_node] = True
            continue
        for child_key in dependency_dict[current_node]:
            node_stack.append(child_key)
    print(answer_count)