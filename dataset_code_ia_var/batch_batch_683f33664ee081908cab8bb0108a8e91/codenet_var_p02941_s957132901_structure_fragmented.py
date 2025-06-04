import sys
import math
import bisect
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
inf = float('inf')

def read_int():
    return int(sys.stdin.readline())

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def push_heap(h, v, i):
    heappush(h, (-v, i))

def pop_heap(h):
    v, i = heappop(h)
    return -v, i

def get_prev_idx(i, n):
    return (i - 1) % n

def get_next_idx(i, n):
    return (i + 1) % n

def compute_tmp(V, i, n):
    return V[get_next_idx(i, n)] + V[get_prev_idx(i, n)]

def compute_s(v, ai, tmp):
    return (v - ai) // tmp

def update_v(v, s, tmp):
    return v - s * tmp

def update_V(V, i, v):
    V[i] = v

def check_valid(s):
    return s > 0

def push_if_needed(h, v, i, ai):
    if v != ai:
        push_heap(h, v, i)

def handle_invalid():
    print(-1)
    quit()

def try_continue(v, ai):
    return v == ai

def add_to_ans(ans, s):
    return ans + s

def main():
    n = read_int()
    a = read_int_list()
    b = read_int_list()
    h = []
    V = [0] * n
    for i, v in enumerate(b):
        push_heap(h, v, i)
        V[i] = v
    ans = 0
    while h:
        v, i = pop_heap(h)
        tmp = compute_tmp(V, i, n)
        if try_continue(v, a[i]):
            continue
        s = compute_s(v, a[i], tmp)
        if not check_valid(s):
            handle_invalid()
        ans = add_to_ans(ans, s)
        v = update_v(v, s, tmp)
        update_V(V, i, v)
        push_if_needed(h, v, i, a[i])
    print(ans)

if __name__ == "__main__":
    main()