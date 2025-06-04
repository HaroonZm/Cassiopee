def memoize_func(target_func):
    cache_dict = {}
    def memoized_func(*func_args):
        if func_args not in cache_dict:
            cache_dict[func_args] = target_func(*func_args)
        return cache_dict[func_args]
    return memoized_func

@memoize_func
def tsp_solver(current_index, visited_flag):
    if visited_flag == (1 << num_points) - 1:
        return dist_matrix[current_index][0]
    min_cost = float('inf')
    for next_index in range(num_points):
        if not (visited_flag & (1 << next_index)):
            candidate_cost = dist_matrix[current_index][next_index] + tsp_solver(next_index, visited_flag | (1 << next_index))
            if candidate_cost < min_cost:
                min_cost = candidate_cost
    return min_cost

from sys import stdin as sys_stdin
from collections import defaultdict as collections_defaultdict
from math import isinf as math_isinf

input_line = sys_stdin.readline

num_points, num_edges = map(int, input_line().split())
dist_matrix = [[float('inf')] * num_points for _ in range(num_points)]
for _ in range(num_edges):
    source_idx, target_idx, edge_cost = map(int, input_line().split())
    dist_matrix[source_idx][target_idx] = edge_cost
result_cost = tsp_solver(0, 1)
print(-1 if math_isinf(result_cost) else result_cost)