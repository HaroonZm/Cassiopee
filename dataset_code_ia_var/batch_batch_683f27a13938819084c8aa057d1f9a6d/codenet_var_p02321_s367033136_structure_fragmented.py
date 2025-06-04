import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def get_params():
    n, w = MAP()
    return n, w

def split_items(total_items):
    part1 = total_items // 2
    part2 = total_items - part1
    return part1, part2

def build_initial_list():
    return [[0, 0]]

def extend_list_with_items(n, vw):
    for _ in range(n):
        v, w = MAP()
        vw = extend_with_given_item(vw, v, w)
    return vw

def extend_with_given_item(vw, v, w):
    new_items = []
    for i in range(len(vw)):
        p = vw[i].copy()
        p[0] += v
        p[1] += w
        new_items.append(p)
    vw.extend(new_items)
    return vw

def sort_vw(vw):
    return sorted(vw, key=lambda x: (x[1], -x[0]))

def remove_useless(vw, n):
    tmp_v = 0
    for i in range(1<<n):
        v, w = vw[i]
        if tmp_v < v:
            tmp_v = v
        else:
            vw[i][0] = tmp_v
    return vw

def two_pointer_search(n1, n2, vw1, vw2, W):
    idx1 = 0
    idx2 = 2 ** n2 - 1
    ans = 0
    return two_pointer_loop(n1, n2, vw1, vw2, W, idx1, idx2, ans)

def two_pointer_loop(n1, n2, vw1, vw2, W, idx1, idx2, ans):
    while idx1 < 2 ** n1 and idx2 >= 0:
        v1, w1 = get_item(vw1, idx1)
        v2, w2 = get_item(vw2, idx2)
        idx2, v2, w2 = decrease_idx2_until_fit(W, w1, vw2, idx2)
        if w1 + w2 <= W:
            ans = update_answer(ans, v1, v2)
        idx1 = increment_index(idx1)
    return ans

def get_item(vw, idx):
    return vw[idx][0], vw[idx][1]

def decrease_idx2_until_fit(W, w1, vw2, idx2):
    v2, w2 = get_item(vw2, idx2)
    while idx2 > 0 and w1 + w2 > W:
        idx2 -= 1
        v2, w2 = get_item(vw2, idx2)
    return idx2, v2, w2

def update_answer(ans, v1, v2):
    v_sum = v1 + v2
    return ans if ans > v_sum else v_sum

def increment_index(idx):
    return idx + 1

def print_answer(ans):
    print(ans)

def main():
    N, W = get_params()
    n1, n2 = split_items(N)
    vw1 = build_initial_list()
    vw2 = build_initial_list()
    vw1 = extend_list_with_items(n1, vw1)
    vw2 = extend_list_with_items(n2, vw2)
    vw1 = sort_vw(vw1)
    vw2 = sort_vw(vw2)
    vw2 = remove_useless(vw2, n2)
    ans = two_pointer_search(n1, n2, vw1, vw2, W)
    print_answer(ans)

if __name__ == '__main__':
    main()