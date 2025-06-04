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
    return list(sys.stdin.readline())[:-1]

def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

def read_line():
    return input()

def split_line(line):
    return line.split()

def parse_int_list(str_list):
    return [int(i) for i in str_list]

def extract_name_and_numbers(line):
    parts = split_line(line)
    name = parts[0]
    numbers = parse_int_list(parts[1:])
    return name, numbers

def compute_value(params):
    p, a, b, c, d, e, f, s, m = params
    value_numerator = f * s * m - p
    value_denominator = a + b + c + (d + e) * m
    return value_numerator / value_denominator

def build_lis_entry(name, params):
    value = compute_value(params)
    return (value, name)

def process_entries(n):
    lis = []
    for _ in range(n):
        line = read_line()
        name, params = extract_name_and_numbers(line)
        entry = build_lis_entry(name, params)
        lis.append(entry)
    return lis

def sort_lis(lis):
    def sort_key(x):
        return (-x[0], x[1])
    return sorted(lis, key=sort_key)

def print_names_from_lis(lis):
    for value, name in lis:
        print(name)

def print_end_delimiter():
    print("#")

def solve(n):
    lis = process_entries(n)
    lis = sort_lis(lis)
    print_names_from_lis(lis)
    print_end_delimiter()
    return

def main_loop():
    while True:
        n = I()
        if is_zero(n):
            break
        solve(n)

def is_zero(n):
    return n == 0

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    mod = 1000000007
    main_loop()