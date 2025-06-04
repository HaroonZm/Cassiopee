import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations

mod = 10**9 + 7

def read_input():
    return map(int, input().split())

def read_list():
    return list(map(int, input().split()))

def sort_desc(lst):
    return sorted(lst, reverse=True)

def init_factorials(n):
    return build_factorial_list(n)

def build_factorial_list(n):
    f = [1]
    for i in range(1, n+1):
        f.append(multiply_previous(f, i))
    return f

def multiply_previous(f, i):
    return f[i-1] * i

def comb(n, r, fact):
    return fact[n] // fact[r] // fact[n - r]

def get_sum_first_k(lst, k):
    return sum(lst[:k])

def get_average_of_sum(sum_val, k):
    return sum_val / k

def get_max(lst, k):
    return max(lst[:k])

def get_min(lst, k):
    return min(lst[:k])

def get_count(lst, val, rng=None):
    if rng is not None:
        return lst[:rng].count(val)
    return lst.count(val)

def sum_combinations(c, a, b, fact):
    total = 0
    for i in range(a, b+1):
        if c >= i:
            total = add_comb(total, c, i, fact)
    return total

def add_comb(current, c, i, fact):
    return current + comb(c, i, fact)

def print_result(val):
    print(val)

def main():
    n, a, b = read_input()
    v = read_list()
    v = sort_desc(v)
    fact = init_factorials(n)
    result_sum = get_sum_first_k(v, a)
    average = get_average_of_sum(result_sum, a)
    print_result(average)
    max_val = get_max(v, a)
    min_val = get_min(v, a)
    if not are_equal(max_val, min_val):
        count_min_in_first_a = get_count(v, min_val, a)
        count_min_in_all = get_count(v, min_val)
        result = comb(count_min_in_all, count_min_in_first_a, fact)
        print_result(result)
    else:
        count_min_in_all = get_count(v, min_val)
        result = sum_combinations(count_min_in_all, a, b, fact)
        print_result(result)

def are_equal(x, y):
    return x == y

main()