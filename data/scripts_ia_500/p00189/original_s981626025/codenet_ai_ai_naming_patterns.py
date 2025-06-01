import sys
import math
import fractions
import itertools
from collections import deque
import copy
import bisect
import heapq

CONSTANT_MODULO = float('inf')
CONSTANT_INFINITY = 10 ** 18 + 7
read_input_line = lambda: sys.stdin.readline().strip()

def compute_all_pairs_shortest_path(distance_matrix):
    """
    distance_matrix[i][j] represents the cost from node i to node j.
    After processing, distance_matrix[i][j] contains the shortest cost from i to j.
    """
    node_count = len(distance_matrix)
    for intermediate_index in range(node_count):
        for start_index in range(node_count):
            for end_index in range(node_count):
                current_distance = distance_matrix[start_index][end_index]
                new_distance = distance_matrix[start_index][intermediate_index] + distance_matrix[intermediate_index][end_index]
                distance_matrix[start_index][end_index] = min(current_distance, new_distance)
    return distance_matrix

while True:
    node_count = int(read_input_line())
    if node_count == 0:
        break
    edges_input = [list(map(int, read_input_line().split())) for _ in range(node_count)]

    adjacency_matrix = [[CONSTANT_INFINITY for _ in range(10)] for _ in range(10)]
    for index in range(10):
        adjacency_matrix[index][index] = 0

    for edge in edges_input:
        node_a = edge[0]
        node_b = edge[1]
        cost = edge[2]
        adjacency_matrix[node_a][node_b] = cost
        adjacency_matrix[node_b][node_a] = cost

    shortest_path_matrix = compute_all_pairs_shortest_path(adjacency_matrix)

    for row_index in range(10):
        for col_index in range(10):
            if shortest_path_matrix[row_index][col_index] == CONSTANT_INFINITY:
                shortest_path_matrix[row_index][col_index] = 0

    candidates = []
    for node_index in range(10):
        total_distance = sum(shortest_path_matrix[node_index])
        if total_distance != 0:
            candidates.append([total_distance, node_index])

    candidates.sort()
    print(candidates[0][1], candidates[0][0])