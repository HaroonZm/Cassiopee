import sys
sys_input = sys.stdin.readline
sys.setrecursionlimit(10**7)

from collections import Counter as col_counter
from collections import deque as col_deque
from collections import defaultdict as col_defaultdict
from itertools import combinations as iter_combinations, permutations as iter_permutations, accumulate as iter_accumulate, groupby as iter_groupby, product as iter_product
from bisect import bis_util_left, bis_util_right
from heapq import heap_utilify, heap_utilpop, heap_utilpush
from math import floor as math_floor, ceil as math_ceil, pi as math_pi, factorial as math_factorial
from operator import itemgetter as op_itemgetter

def int_input(): return int(sys_input())
def map_int_input(): return map(int, sys_input().split())
def list_int_input(): return list(map(int, sys_input().split()))
def list_int_input_n(n): return [int(sys_input()) for _ in range(n)]
def matrix_list_int_input_n(n): return [[list_int_input()] for _ in range(n)]
def str_input(): return sys_input().rstrip()
def print_str_lines(seq): print('\n'.join(seq))
def print_int_lines(seq): print('\n'.join(map(str, seq)))

CONST_INF = 10**17
CONST_MOD = 10**9 + 7

num_nodes, num_edges = map_int_input()
node_degree_list = [0 for _ in range(num_nodes)]

for _ in range(num_edges):
    node_a, node_b = map_int_input()
    node_degree_list[node_a - 1] += 1
    node_degree_list[node_b - 1] += 1

for deg in node_degree_list:
    if deg % 2 == 1:
        print("NO")
        sys.exit()

print("YES")