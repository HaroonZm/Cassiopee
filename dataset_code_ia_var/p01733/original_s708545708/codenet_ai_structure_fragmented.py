import sys
from collections import deque
import itertools as it

def set_recursion_limit():
    sys.setrecursionlimit(1000000)

def get_input_value():
    return input_value_wrapper()

def input_value_wrapper():
    return custom_input_cast(input())

def custom_input_cast(s):
    return int(s)

def initialize_lst():
    return []

def initialize_m():
    return {}

def get_range(N):
    return range(N)

def get_input_line():
    return custom_split(raw_input())

def custom_split(s):
    return s.split()

def convert_to_ints(strs):
    return map(int, strs)

def unpack_vars(vals):
    return vals

def update_m(m, key, w):
    m[key] = w

def append_neighbors(lst, x, y):
    lst.append((x - 1, y - 1))
    lst.append((x - 1, y))
    lst.append((x, y - 1))
    lst.append((x, y))

def process_inputs(N, lst, m):
    for i in get_range(N):
        x, y, w = unpack_vars(convert_to_ints(get_input_line()))
        update_m(m, (x, y), w)
        append_neighbors(lst, x, y)

def initialize_ans():
    return 0

def iterate_lst(lst):
    for p in lst:
        yield p

def extract_x(p):
    return p[0]

def extract_y(p):
    return p[1]

def get_sum_for_point(x, y, m):
    S = 0
    if (x, y) in m:
        S += m[(x, y)]
    if (x + 1, y) in m:
        S += m[(x + 1, y)]
    if (x, y + 1) in m:
        S += m[(x, y + 1)]
    if (x + 1, y + 1) in m:
        S += m[(x + 1, y + 1)]
    return S

def update_ans(ans, S):
    return max(ans, S)

def output_result(ans):
    print(str(ans) + " / 1")

def main():
    set_recursion_limit()
    N = get_input_value()
    lst = initialize_lst()
    m = initialize_m()
    process_inputs(N, lst, m)
    ans = initialize_ans()
    for p in iterate_lst(lst):
        x = extract_x(p)
        y = extract_y(p)
        S = get_sum_for_point(x, y, m)
        ans = update_ans(ans, S)
    output_result(ans)

if __name__ == "__main__":
    main()