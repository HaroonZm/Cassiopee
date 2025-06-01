#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    def readline():
        return sys.stdin.readline()
    def split_line(line):
        return line.split()
    def map_ints(list_of_str):
        return map(int, list_of_str)
    line = readline()
    split = split_line(line)
    mapped = map_ints(split)
    return list(mapped)

def I():
    def readline():
        return sys.stdin.readline()
    def to_int(s):
        return int(s)
    line = readline()
    return to_int(line)

def LS():
    def readline():
        return sys.stdin.readline()
    def split_line(line):
        return line.split()
    def map_list_chars(list_of_str):
        return map(list, list_of_str)
    line = readline()
    split = split_line(line)
    mapped = map_list_chars(split)
    return list(mapped)

def S():
    def readline():
        return sys.stdin.readline()
    def to_list_without_last_char(line):
        return list(line)[:-1]
    line = readline()
    return to_list_without_last_char(line)

def IR(n):
    def create_none_list(size):
        return [None for i in range(size)]
    def assign_values_to_list(lst, size):
        for i in range(size):
            lst[i] = I()
        return lst
    l = create_none_list(n)
    l = assign_values_to_list(l, n)
    return l

def LIR(n):
    def create_none_list(size):
        return [None for i in range(size)]
    def assign_values_to_list(lst, size):
        for i in range(size):
            lst[i] = LI()
        return lst
    l = create_none_list(n)
    l = assign_values_to_list(l, n)
    return l

def SR(n):
    def create_none_list(size):
        return [None for i in range(size)]
    def assign_values_to_list(lst, size):
        for i in range(size):
            lst[i] = S()
        return lst
    l = create_none_list(n)
    l = assign_values_to_list(l, n)
    return l

def LSR(n):
    def create_none_list(size):
        return [None for i in range(size)]
    def assign_values_to_list(lst, size):
        for i in range(size):
            lst[i] = LS()
        return lst
    l = create_none_list(n)
    l = assign_values_to_list(l, n)
    return l

sys.setrecursionlimit(1000000)
mod = 1000000007

#A

def count_elements(lst):
    d = defaultdict(int)
    for i in lst:
        d[i] += 1
    return d

def check_all_values_two(d):
    for i in d.values():
        if i != 2:
            return False
    return True

def print_yes_no(condition):
    if condition:
        print("yes")
    else:
        print("no")

def A():
    e = LI()
    d = count_elements(e)
    condition = check_all_values_two(d)
    print_yes_no(condition)
    return

#B

def read_n():
    return I()

def read_list_int():
    return LI()

def sort_list_inplace(lst):
    lst.sort()

def calculate_max_expression(n, a):
    ans = -float("inf")
    for c in range(n):
        for d in range(c):
            m = a[c]-a[d]
            e = find_last_index_not_in([c,d], n)
            b = find_last_index_not_in([c,d,e], e)
            val = (a[e]+a[b])/m
            if val > ans:
                ans = val
    return ans

def find_last_index_not_in(excluded, start):
    for i in range(start -1, -1, -1):
        if i not in excluded:
            return i
    return None

def B():
    n = read_n()
    a = read_list_int()
    sort_list_inplace(a)
    ans = calculate_max_expression(n, a)
    print(ans)
    return

#C

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def parse_input_string():
    return input()

def count_char_in_string(ch, s):
    return s.count(ch)

def convert_to_float(s):
    return float(s)

def power_10(n):
    return 10**n

def round_value(val):
    return round(val)

def find_index_char_in_string(s, ch):
    return s.find(ch)

def find_decimal_position(s):
    return s.find(".")

def get_fraction_without_parentheses(s):
    n = len(s)
    s_float = convert_to_float(s)
    b = power_10(n-2)
    a = round_value(s_float * b)
    g = gcd(a, b)
    a //= g
    b //= g
    return a, b

def extract_fraction_components(s):
    n_open = find_index_char_in_string(s, "(")
    part_before = s[:n_open]
    t = convert_to_float(part_before)
    b = power_10(n_open-2)
    a = round_value(t*b)
    g = gcd(a,b)
    a //= g
    b //= g
    l = n_open - find_decimal_position(s) - 1
    return a, b, l, n_open

def extract_repeating_decimal_part(s, n_open):
    s_repeating = s[n_open+1:-1]
    m = len(s_repeating)
    c = round_value(float(s_repeating))
    d = (10**m -1) * 10**(s.find("(")-s.find(".")-1)
    return c, d

def reduce_fraction(a, b):
    g = gcd(a, b)
    a //= g
    b //= g
    return a, b

def add_fractions(a1, b1, a2, b2):
    numerator = a1*b2 + a2*b1
    denominator = b1 * b2
    return numerator, denominator

def process_fraction_with_parentheses(s):
    a, b, l, n_open = extract_fraction_components(s)
    c, d = extract_repeating_decimal_part(s, n_open)
    c, d = reduce_fraction(c, d)
    a, b = add_fractions(a, b, c, d)
    a, b = reduce_fraction(a, b)
    return a, b

def print_fraction(a, b):
    print(str(a)+"/"+str(b))

def C():
    s = parse_input_string()
    if count_char_in_string('(', s) == 0:
        a,b = get_fraction_without_parentheses(s)
    else:
        a,b = process_fraction_with_parentheses(s)
    print_fraction(a,b)
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    C()