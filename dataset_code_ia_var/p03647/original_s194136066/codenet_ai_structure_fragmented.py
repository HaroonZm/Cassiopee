import sys
from collections import Counter

def read_int_list():
    return list(map(int, input().split()))

def read_int():
    return int(input())

def read_str_list():
    return input().split()

def read_str():
    return input()

def get_status_possible():
    return 'POSSIBLE'

def get_status_impossible():
    return 'IMPOSSIBLE'

def increment_counter(counter, key):
    counter[key] += 1
    return counter

def check_condition(counter, key):
    return counter[key] == 2

def process_edge(a, b, n, counter):
    changed = False
    if a == 1:
        counter = increment_counter(counter, b)
        if check_condition(counter, b):
            changed = True
    if b == n:
        counter = increment_counter(counter, a)
        if check_condition(counter, a):
            changed = True
    return counter, changed

def handle_all_edges(m, n):
    counter = Counter()
    result_flag = False
    for _ in range(m):
        a, b = read_int_list()
        counter, changed = process_edge(a, b, n, counter)
        if changed:
            result_flag = True
    return result_flag

def solve():
    n, m = read_int_list()
    possible = get_status_possible()
    impossible = get_status_impossible()
    found = handle_all_edges(m, n)
    if found:
        return possible
    else:
        return impossible

def output_result(res):
    print(res)

def main():
    res = solve()
    output_result(res)

if __name__ == '__main__':
    main()