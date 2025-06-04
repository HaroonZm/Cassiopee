import sys

read_input_line = sys.stdin.readline

sys.setrecursionlimit(10**7)

from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil, pi, factorial
from operator import itemgetter

def read_single_integer(): 
    return int(read_input_line())

def read_multiple_integers(): 
    return map(int, read_input_line().split())

def read_integer_list(): 
    return list(map(int, read_input_line().split()))

def read_n_integers(n): 
    return [int(read_input_line()) for _ in range(n)]

def read_n_integer_lists(n): 
    return [[read_integer_list()] for _ in range(n)]

def read_string(): 
    return read_input_line().rstrip()

def print_newline_separated_strings(list_of_strings): 
    print('\n'.join(list_of_strings))

def print_newline_separated_integers(list_of_integers): 
    print('\n'.join(list(map(str, list_of_integers))))

INFINITY = 10**17
MODULO = 10**9 + 7

number_of_nodes, number_of_edges = read_multiple_integers()

node_degree_counter = [0 for _ in range(number_of_nodes)]

for edge_index in range(number_of_edges):
    node_u, node_v = read_multiple_integers()
    node_degree_counter[node_u - 1] += 1
    node_degree_counter[node_v - 1] += 1

for node_index in range(number_of_nodes):
    if node_degree_counter[node_index] % 2 == 1:
        print("NO")
        sys.exit()

print("YES")