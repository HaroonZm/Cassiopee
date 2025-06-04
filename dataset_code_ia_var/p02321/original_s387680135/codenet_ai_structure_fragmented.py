from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def IR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

def set_large_recursion():
    sys.setrecursionlimit(1000000)

def get_mod():
    return 1000000007

def read_n_W():
    return LI()

def init_value_lists(n):
    return ([None for _ in range(n)], [None for _ in range(n)])

def fill_v_w_lists(n, v, w):
    for i in range(n):
        vi, wi = LI()
        v[i] = vi
        w[i] = wi
    return v, w

def init_a_b():
    return [[0,0]], [[0,0]]

def compute_m(n):
    return n // 2

def fill_subsets_a(m, v, w, a):
    for i in range(m):
        a = add_a_subsets(i, v, w, a)
    return a

def add_a_subsets(i, v, w, a):
    cur_len = 1 << i
    for j in range(cur_len):
        a.append([a[j][0] + v[i], a[j][1] + w[i]])
    return a

def fill_subsets_b(n, m, v, w, b):
    for i in range(n - m):
        b = add_b_subsets(i, v, w, m, b)
    return b

def add_b_subsets(i, v, w, m, b):
    cur_len = 1 << i
    for j in range(cur_len):
        b.append([b[j][0] + v[i + m], b[j][1] + w[i + m]])
    return b

def sort_by_weight(lst):
    return sorted(lst, key=lambda x: x[1])

def make_monotone_max_b(b):
    ma = b[0][0]
    for i in range(1, len(b)):
        if ma > b[i][0]:
            b[i][0] = ma
        else:
            ma = b[i][0]
    return b

def search_max(a, b, W):
    ans = 0
    i = len(b) - 1
    for va, wa in a:
        rem = W - wa
        while i > 0 and b[i][1] > rem:
            i -= 1
        if b[i][1] <= rem:
            ans = max(ans, va + b[i][0])
    return ans

def main():
    set_large_recursion()
    mod = get_mod()
    n, W = read_n_W()
    v, w = init_value_lists(n)
    v, w = fill_v_w_lists(n, v, w)
    a, b = init_a_b()
    m = compute_m(n)
    a = fill_subsets_a(m, v, w, a)
    b = fill_subsets_b(n, m, v, w, b)
    a = sort_by_weight(a)
    b = sort_by_weight(b)
    b = make_monotone_max_b(b)
    ans = search_max(a, b, W)
    print(ans)

main()