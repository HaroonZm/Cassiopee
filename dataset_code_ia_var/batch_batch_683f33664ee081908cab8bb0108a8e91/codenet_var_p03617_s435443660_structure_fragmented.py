import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal

def set_recursion():
    sys.setrecursionlimit(10 ** 9)

def get_mod():
    return 10 ** 9 + 7

def s():
    return input()

def i():
    return int(input())

def S():
    return input().split()

def I():
    return map(int, input().split())

def L():
    return list(input().split())

def l():
    return list(map(int, input().split()))

def lcm(a, b):
    return a * b // math.gcd(a, b)

def read_prices():
    return list(I())

def read_requirement():
    return i()

def calculate_combinations(Q, H, S, D):
    c1 = price_for_quarter(Q)
    c2 = price_for_half(H)
    c3 = price_for_whole(S)
    c4 = price_for_double(D)
    combo_list = [c1, c2, c3, c4]
    return combo_list

def price_for_quarter(Q):
    return [Q * 8, 0.25, Q]

def price_for_half(H):
    return [H * 4, 0.5, H]

def price_for_whole(S):
    return [S * 2, 1, S]

def price_for_double(D):
    return [D, 2, D]

def sort_combinations(combos):
    return sorted(combos)

def process_combinations(ans, N, combos):
    for idx in range(len(combos)):
        ans, N, done = process_one_combination(ans, N, combos, idx)
        if done:
            output_result(ans)
            break

def process_one_combination(ans, N, combos, idx):
    a, b, c = combos[idx]
    if can_use_this(b, N):
        count = how_many_times(N, b)
        ans = increment_ans(ans, count, c)
        N = decrement_N(N, count, b)
    if is_done(N):
        return ans, N, True
    return ans, N, False

def can_use_this(b, N):
    return b <= N

def how_many_times(N, b):
    return int(N // b)

def increment_ans(ans, count, c):
    return ans + count * c

def decrement_N(N, count, b):
    return N - count * b

def is_done(N):
    return N == 0

def output_result(ans):
    print(ans)

def main():
    set_recursion()
    mod = get_mod()
    Q, H, S, D = read_prices()
    N = read_requirement()
    combinations = calculate_combinations(Q, H, S, D)
    ordered_combos = sort_combinations(combinations)
    process_combinations(0, N, ordered_combos)

main()