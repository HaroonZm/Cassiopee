from collections import defaultdict
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
        l[i] = SR()
    return l

mod = 1000000007

def read_input():
    n, m = read_n_and_m()
    a = read_a(m)
    f = build_f(n, m, a)
    k = build_k(n, a, f)
    q, p = read_queries()
    process_queries(q, p, n, k)
    
def read_n_and_m():
    l = LI()
    return l[0], l[1]

def read_a(m):
    return LI()

def build_f(n, m, a):
    f = init_f(n)
    update_f_with_a(f, m, a)
    update_f_with_last_gap(f, n, a)
    return f

def init_f(n):
    return [0 for _ in range(n + 1)]

def update_f_with_a(f, m, a):
    for i in range(1, m):
        update_f_element(f, a, i)

def update_f_element(f, a, i):
    idx = a[i] - a[i-1] - 1
    f[idx] += 1

def update_f_with_last_gap(f, n, a):
    last_gap = n - a[-1]
    f[last_gap] += 1

def build_k(n, a, f):
    k = init_k(n)
    s = [0]
    update_k_with_f(n, f, k, s)
    adjust_k_with_first_a(n, k, a)
    return k

def init_k(n):
    return [0 for _ in range(n + 1)]

def update_k_with_f(n, f, k, s):
    s_acc = 0
    for i in range(n)[::-1]:
        s_acc = accumulate_s(s_acc, f, i)
        k[i] = add_to_k(k, i, s_acc)
    s[0] = s_acc

def accumulate_s(s_acc, f, i):
    return s_acc + f[i]

def add_to_k(k, i, s_acc):
    return k[i] + s_acc + k[i+1]

def adjust_k_with_first_a(n, k, a):
    val = a[0] - 1
    for i in range(n+1):
        k[i] += val

def read_queries():
    q = I()
    p = LI()
    return q, p

def process_queries(q, p, n, k):
    for i in p:
        r = find_r(i, n, k)
        output_result(r, i, k)

def find_r(i, n, k):
    l = 0
    r = n
    while r - l > 1:
        m = midway(l, r)
        if test_k(k, m, i):
            l = m
        else:
            r = m
    return r

def midway(l, r):
    return (l + r) // 2

def test_k(k, m, i):
    return k[m] > i

def output_result(r, i, k):
    if k[r] > i:
        print(-1)
    else:
        print(r)

if __name__ == "__main__":
    read_input()