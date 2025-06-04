import sys
import math
import re
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000)
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')

def I():
    return int(sys.stdin.readline())

def LI():
    return list(map(int, sys.stdin.readline().split()))

def read_n():
    return I()

def is_zero(n):
    return n == 0

def build_defaultdicts():
    f = defaultdict(dict)
    t = defaultdict(lambda: False)
    ch = defaultdict(lambda: False)
    return f, t, ch

def initialize_stack():
    return []

def parse_input_line():
    x = input()[:-1].split(':')
    y = x[1].split(',')
    return x[0], y

def process_first_line(f, stack, x, y):
    for j in y:
        f[x][j] = 1
        stack.append(j)

def process_other_line(f, x, y):
    for j in y:
        f[x][j] = 1

def build_graph(n):
    f, t, ch = build_defaultdicts()
    stack = initialize_stack()
    for i in range(n):
        x, y = parse_input_line()
        if i == 0:
            process_first_line(f, stack, x, y)
        else:
            process_other_line(f, x, y)
    return f, t, ch, stack

def is_empty_dict(d):
    return len(d) == 0

def should_increase_ans(f, x, t):
    return is_empty_dict(f[x]) and not t[x]

def process_stack_node(x, ch, f, t, ans_data, stack):
    if ch[x]:
        return
    ch[x] = True
    if should_increase_ans(f, x, t):
        ans_data[0] += 1
        t[x] = True
        return
    for i, j in f[x].items():
        stack.append(i)

def process_stack(stack, ch, f, t):
    ans_data = [0]
    while stack:
        x = stack.pop()
        process_stack_node(x, ch, f, t, ans_data, stack)
    return ans_data[0]

def print_ans(ans):
    print(ans)

def main_loop():
    while True:
        n = read_n()
        if is_zero(n):
            quit()
        f, t, ch, stack = build_graph(n)
        ans = process_stack(stack, ch, f, t)
        print_ans(ans)

main_loop()