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
import copy
import functools

sys.setrecursionlimit(10**7)

CONST_INF = 10**20
CONST_EPSILON = 1.0 / 10**13
CONST_MODULO = 10**9 + 7
DIR_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def input_list_int(): return [int(x) for x in sys.stdin.readline().split()]
def input_list_int0(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def input_list_float(): return [float(x) for x in sys.stdin.readline().split()]
def input_list_str(): return sys.stdin.readline().split()
def input_single_int(): return int(sys.stdin.readline())
def input_single_float(): return float(sys.stdin.readline())
def input_single_str(): return input()
def print_flush(val): return print(val, flush=True)

def is_crossing_segments(a_start, a_end, b_start, b_end):
    ax1, ay1 = a_start
    ax2, ay2 = a_end
    bx1, by1 = b_start
    bx2, by2 = b_end

    t_cross_1 = (ax1 - ax2) * (by1 - ay1) + (ay1 - ay2) * (ax1 - bx1)
    t_cross_2 = (ax1 - ax2) * (by2 - ay1) + (ay1 - ay2) * (ax1 - bx2)
    return t_cross_1 * t_cross_2 < 0

def are_segments_crossing(a_start, a_end, b_start, b_end):
    return is_crossing_segments(a_start, a_end, b_start, b_end) and is_crossing_segments(b_start, b_end, a_start, a_end)

def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calc_distance_points(p1, p2):
    return calc_distance(p1[0], p1[1], p2[0], p2[1])

def main_func():
    result_list = []

    def solve_case(num_a, num_b):
        pos_a = [input_list_int() for _ in range(num_a)]
        pos_b = [input_list_int() for _ in range(num_b)]

        def bfs_search(pos_list, opp_start, opp_end, search_range):
            dist_dict = collections.defaultdict(lambda: CONST_INF)
            start_idx = 0
            end_idx = 1
            dist_dict[start_idx] = 0
            queue = []
            heapq.heappush(queue, (0, start_idx))
            visited_dict = collections.defaultdict(bool)
            while queue:
                curr_dist, curr_node = heapq.heappop(queue)
                if visited_dict[curr_node]:
                    continue
                visited_dict[curr_node] = True
                if curr_node == end_idx:
                    return dist_dict[curr_node]
                for next_node in search_range:
                    if visited_dict[next_node]:
                        continue
                    if are_segments_crossing(pos_list[curr_node], pos_list[next_node], opp_start, opp_end):
                        continue
                    edge_weight = calc_distance_points(pos_list[curr_node], pos_list[next_node])
                    next_dist = curr_dist + edge_weight
                    if dist_dict[next_node] > next_dist:
                        dist_dict[next_node] = next_dist
                        heapq.heappush(queue, (next_dist, next_node))
            return -1

        dist_a = calc_distance_points(pos_a[0], pos_a[1])
        dist_b = calc_distance_points(pos_b[0], pos_b[1])
        search_result_a = bfs_search(pos_a, pos_b[0], pos_b[1], list(range(1, num_a)))
        search_result_b = bfs_search(pos_b, pos_a[0], pos_a[1], list(range(1, num_b)))
        final_result = -1
        if search_result_a < 0:
            if search_result_b < 0:
                return final_result
            return '{:0.9f}'.format(search_result_b + dist_a)
        if search_result_b < 0:
            return '{:0.9f}'.format(search_result_a + dist_b)
        return '{:0.9f}'.format(min(search_result_a + dist_b, search_result_b + dist_a))

    while True:
        count_a, count_b = input_list_int()
        if count_a == 0:
            break
        result_list.append(solve_case(count_a, count_b))
        break

    return '\n'.join(map(str, result_list))

print(main_func())