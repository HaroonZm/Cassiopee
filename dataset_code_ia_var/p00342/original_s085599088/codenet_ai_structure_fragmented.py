from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def LS():
    return list(map(list, sys.stdin.readline().split()))

def S():
    return list(sys.stdin.readline())[:-1]

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

sys.setrecursionlimit(1000000)
mod = 1000000007

def read_and_count_elements():
    elements = LI()
    counts = defaultdict(int)
    for i in elements:
        counts[i] += 1
    return counts

def check_all_counts_are_two(counts):
    for v in counts.values():
        if v != 2:
            return False
    return True

def print_result_A(is_two):
    if is_two:
        print("yes")
    else:
        print("no")

def A():
    counts = read_and_count_elements()
    result = check_all_counts_are_two(counts)
    print_result_A(result)
    return

def read_n():
    return I()

def read_a():
    return LI()

def sort_list(l):
    l.sort()
    return l

def initialize_ans():
    return -float("inf")

def range_n(n):
    return range(n)

def reversed_range(n):
    return range(n-1, -1, -1)

def get_m(a, c, d):
    return a[c] - a[d]

def find_e(a, n, c, d):
    for i in reversed_range(n):
        if i != c and i != d:
            return i
    return None

def find_b(a, e, c, d):
    for i in reversed_range(e):
        if i != c and i != d:
            return i
    return None

def compute_candidate(a, e, b, m):
    return (a[e] + a[b]) / m

def update_ans(ans, candidate):
    return max(ans, candidate)

def print_ans(ans):
    print(ans)

def B():
    n = read_n()
    a = read_a()
    a = sort_list(a)
    ans = initialize_ans()
    for c in range_n(n):
        for d in range(c):
            m = get_m(a, c, d)
            e = find_e(a, n, c, d)
            if e is None:
                continue
            b = find_b(a, e, c, d)
            if b is None:
                continue
            candidate = compute_candidate(a, e, b, m)
            ans = update_ans(ans, candidate)
    print_ans(ans)
    return

def C():
    return

def D():
    return

def E():
    return

def F():
    return

def G():
    return

def H():
    return

def I_():
    return

def J():
    return

if __name__ == "__main__":
    B()