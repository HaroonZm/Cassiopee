import sys

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 6)

def get_input():
    return sys.stdin.readline

def parse_first_line(input_func):
    n_k = input_func().split()
    return int(n_k[0]), int(n_k[1])

def parse_next_line_as_int_list(input_func):
    return list(map(int, input_func().split()))

def sort_descending(lst):
    return sorted(lst, reverse=True)

def sort_ascending(lst):
    return sorted(lst)

def initialize_binary_search_bounds(aa, ff):
    l = -1
    r = aa[0] * ff[-1]
    return l, r

def calculate_excess(a, f, m):
    b = m // f
    return max(a - b, 0)

def check_mid(aa, ff, m, k):
    s = 0
    for a, f in zip(aa, ff):
        excess = calculate_excess(a, f, m)
        s += excess
        if s > k:
            return False
    return True

def binary_search(aa, ff, k):
    l, r = initialize_binary_search_bounds(aa, ff)
    while l + 1 < r:
        m = (l + r) // 2
        if check_mid(aa, ff, m, k):
            r = m
        else:
            l = m
    return r

def main():
    set_recursion_limit()
    input_func = get_input()
    n, k = parse_first_line(input_func)
    aa = parse_next_line_as_int_list(input_func)
    ff = parse_next_line_as_int_list(input_func)
    aa = sort_descending(aa)
    ff = sort_ascending(ff)
    result = binary_search(aa, ff, k)
    print(result)

main()