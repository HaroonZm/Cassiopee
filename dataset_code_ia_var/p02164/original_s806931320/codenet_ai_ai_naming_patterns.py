import sys
import math
from collections import defaultdict, deque
from heapq import heappush, heappop
import bisect
import random

def read_int_list():
    return [int(token) for token in sys.stdin.readline().split()]

def read_int():
    return int(sys.stdin.readline())

def read_string_lists():
    return [list(token) for token in sys.stdin.readline().split()]

def read_string():
    chars = list(sys.stdin.readline())
    if chars and chars[-1] == "\n":
        return chars[:-1]
    return chars

def read_int_repeated(count):
    return [read_int() for _ in range(count)]

def read_int_list_repeated(count):
    return [read_int_list() for _ in range(count)]

def read_string_repeated(count):
    return [read_string() for _ in range(count)]

def read_string_lists_repeated(count):
    return [read_string_lists() for _ in range(count)]

sys.setrecursionlimit(1000000)
MOD_VALUE = 1000000007

def solve_main():
    from itertools import permutations as iter_permutations

    def calc_dot_product(vector1, vector2):
        return sum(a * b for a, b in zip(vector1, vector2))

    point_count = read_int()
    point_list = read_int_list_repeated(point_count)
    min_angle_sum = float("inf")

    for index_perm in iter_permutations(range(point_count), point_count):
        current_x, current_y = 0, 0
        angle_sum = 0
        current_vector = [1, 0]
        for idx in index_perm:
            target_x, target_y = point_list[idx]
            next_vector = [target_x - current_x, target_y - current_y]
            dot = calc_dot_product(current_vector, next_vector)
            norm_product = (calc_dot_product(current_vector, current_vector) * calc_dot_product(next_vector, next_vector)) ** 0.5
            if norm_product != 0:
                angle_sum += math.acos(dot / norm_product)
            current_x, current_y = target_x, target_y
            current_vector = [next_vector[0], next_vector[1]]
        # Return to origin
        return_x, return_y = 0, 0
        return_vector = [return_x - current_x, return_y - current_y]
        dot = calc_dot_product(current_vector, return_vector)
        norm_product = (calc_dot_product(current_vector, current_vector) * calc_dot_product(return_vector, return_vector)) ** 0.5
        if norm_product != 0:
            angle_sum += math.acos(dot / norm_product)
        min_angle_sum = min(min_angle_sum, angle_sum)
    print(min_angle_sum * 180 / math.pi)

if __name__ == "__main__":
    solve_main()