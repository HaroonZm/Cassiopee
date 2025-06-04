import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time

sys.setrecursionlimit(10 ** 7)
CONST_INF = 10 ** 20
CONST_MOD = 10 ** 9 + 7

def read_int_list(): return list(map(int, input().split()))
def read_float_list(): return list(map(float, input().split()))
def read_str_list(): return input().split()
def read_int(): return int(input())
def read_float(): return float(input())
def read_str(): return input()

def main():
    prob_value = read_float()
    node_count = read_int()
    tree_adj = collections.defaultdict(list)
    for _ in range(node_count - 1):
        from_node, to_node, edge_cost = read_int_list()
        tree_adj[from_node - 1].append((to_node - 1, edge_cost))
        tree_adj[to_node - 1].append((from_node - 1, edge_cost))
    node_levels = [None] * node_count
    node_levels[0] = (0, 0)
    traversal_queue = [(0, 0)]
    while traversal_queue:
        current_node, current_depth = traversal_queue[0]
        traversal_queue = traversal_queue[1:]
        for neighbor_node, neighbor_cost in tree_adj[current_node]:
            if node_levels[neighbor_node]:
                continue
            traversal_queue.append((neighbor_node, current_depth + 1))
            node_levels[neighbor_node] = (current_depth + 1, neighbor_cost)
    partial_sum = 0
    for node_depth, node_cost in node_levels:
        partial_sum += prob_value ** node_depth * node_cost
    result = partial_sum
    for node_depth, node_cost in node_levels:
        result += prob_value ** node_depth * partial_sum
    return result

print(main())