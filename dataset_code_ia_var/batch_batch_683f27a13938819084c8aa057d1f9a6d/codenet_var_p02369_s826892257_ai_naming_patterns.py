import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

CONST_INF = 2000000000
CONST_MOD = 1000000007
CONST_EPSILON = 0.000000001

node_count, edge_count = map(int, input().split())
reachability_matrix = [[None for _ in range(node_count)] for _ in range(node_count)]

for row_idx in range(node_count):
    for col_idx in range(node_count):
        reachability_matrix[row_idx][col_idx] = (row_idx == col_idx)

for edge_idx in range(edge_count):
    edge_from, edge_to = map(int, input().split())
    reachability_matrix[edge_from][edge_to] = True

for intermediate_node in range(node_count):
    for source_node in range(node_count):
        if not reachability_matrix[source_node][intermediate_node]:
            continue
        for target_node in range(node_count):
            if not reachability_matrix[intermediate_node][target_node]:
                continue
            reachability_matrix[source_node][target_node] = True

for first_node in range(node_count - 1):
    for second_node in range(first_node + 1, node_count):
        if reachability_matrix[first_node][second_node] and reachability_matrix[second_node][first_node]:
            print("1")
            sys.exit()

print("0")