import sys

def get_input():
    return sys.stdin.readline

def set_recursion():
    sys.setrecursionlimit(10 ** 6)

def import_collections():
    import collections
    return collections

def import_counter():
    from collections import Counter
    return Counter

def import_fractions():
    import fractions
    return fractions

def import_math():
    import math
    return math

def import_deque():
    from collections import deque
    return deque

def import_bisect_left():
    from bisect import bisect_left
    return bisect_left

def import_insort_left():
    from bisect import insort_left
    return insort_left

def import_itertools():
    import itertools
    return itertools

def import_heapify():
    from heapq import heapify
    return heapify

def import_heappop():
    from heapq import heappop
    return heappop

def import_heappush():
    from heapq import heappush
    return heappush

def import_heapq():
    import heapq
    return heapq

def import_numpy():
    import numpy as np
    return np

def get_inf():
    return float("inf")

def get_k():
    return int(input())

def k_leq_50_and_geq_2(k):
    return k <= 50 and k >= 2

def handle_k_between_2_and_50(k):
    a = [k]*k
    output_k_and_list(k, a)

def handle_k_zero():
    print(2)
    print(1, 1)

def handle_k_one():
    print(2)
    print(0, 3)

def compute_x(k):
    return k // 50

def compute_y(k):
    return k % 50

def fill_list_for_y(y, x):
    arr = []
    for i in range(y):
        arr.append(49 + x + 1)
    return arr

def fill_list_for_50_minus_y(amt, x, y):
    arr = []
    for j in range(amt):
        arr.append(49 + x - y)
    return arr

def combine_lists(list1, list2):
    return list1 + list2

def output_50_and_list(a):
    print(50)
    print(*a)

def handle_k_other(k):
    x = compute_x(k)
    y = compute_y(k)
    part1 = fill_list_for_y(y, x)
    part2 = fill_list_for_50_minus_y(50 - y, x, y)
    a = combine_lists(part1, part2)
    output_50_and_list(a)

def output_k_and_list(k, a):
    print(k)
    print(*a)

def process_k(k):
    if k_leq_50_and_geq_2(k):
        handle_k_between_2_and_50(k)
    elif k == 0:
        handle_k_zero()
    elif k == 1:
        handle_k_one()
    else:
        handle_k_other(k)

def main():
    get_input()  # Initializes input
    set_recursion()
    import_collections()
    import_counter()
    import_fractions()
    import_math()
    import_deque()
    import_bisect_left()
    import_insort_left()
    import_itertools()
    import_heapify()
    import_heappop()
    import_heappush()
    import_heapq()
    import_numpy()
    get_inf()
    k = get_k()
    process_k(k)

main()