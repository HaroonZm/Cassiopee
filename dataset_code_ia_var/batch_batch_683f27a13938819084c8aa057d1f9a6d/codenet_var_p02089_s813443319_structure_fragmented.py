from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def get_initial_input_B():
    n, Q, L, R = LI()
    return n, Q, L, R

def get_a_list_B(n):
    return LI()

def sort_a_list_B(a):
    a.sort()
    return a

def get_queries_B(Q):
    return LIR(Q)

def apply_query_type_1(am, x, s, t):
    if am < x:
        return am
    am += s
    am *= t
    return am

def apply_query_type_2(am, x, s, t):
    if am > x:
        return am
    am -= s
    if am < 0:
        am = -((-am) // t)
    else:
        am //= t
    return am

def process_query_B(am, query):
    for q, x, s, t in query:
        if q == 1:
            am = apply_query_type_1(am, x, s, t)
        else:
            am = apply_query_type_2(am, x, s, t)
    return am

def lower_bound_search_B(a, n, L, query):
    l = -1
    r = n
    while r - l > 1:
        m = (l + r) >> 1
        am = a[m]
        am = process_query_B(am, query)
        if am < L:
            l = m
        else:
            r = m
    return r

def upper_bound_search_B(a, n, R, query):
    l = 0
    r = n
    while r - l > 1:
        m = (l + r) >> 1
        am = a[m]
        am = process_query_B(am, query)
        if am <= R:
            l = m
        else:
            r = m
    return r

def calculate_result_B(left, right):
    return right - left

def print_result_B(res):
    print(res)

def B():
    n, Q, L, R = get_initial_input_B()
    a = get_a_list_B(n)
    a = sort_a_list_B(a)
    query = get_queries_B(Q)
    left = lower_bound_search_B(a, n, L, query)
    right = upper_bound_search_B(a, n, R, query)
    res = calculate_result_B(left, right)
    print_result_B(res)
    return

def main():
    B()

if __name__ == "__main__":
    main()