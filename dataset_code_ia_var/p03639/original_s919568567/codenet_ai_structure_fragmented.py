from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *
from heapq import *

def read():
    return int(input())

def reads():
    return [int(x) for x in input().split()]

def count_modulo_elements(A, mod, value):
    return sum(is_modulo_value(a, mod, value) for a in A)

def is_modulo_value(a, mod, value):
    return a % mod == value

def compute_counts(A):
    c1 = count_c1(A)
    c2 = count_c2(A)
    c4 = count_c4(A)
    return c1, c2, c4

def count_c1(A):
    return count_modulo_elements(A, 2, 1)

def count_c2(A):
    return count_modulo_elements(A, 4, 2)

def count_c4(A):
    return count_modulo_elements(A, 4, 0)

def check_condition(c1, c2, c4):
    if is_first_case_impossible(c1, c4):
        return False
    if is_second_case_impossible(c1, c4, c2):
        return False
    return True

def is_first_case_impossible(c1, c4):
    return c1 > c4 + 1

def is_second_case_impossible(c1, c4, c2):
    return c1 == c4 + 1 and c2 > 0

def print_result(flag):
    if flag:
        output_yes()
    else:
        output_no()

def output_yes():
    print("Yes")

def output_no():
    print("No")

def main():
    N = read()
    A = reads()
    c1, c2, c4 = compute_counts(A)
    flag = check_condition(c1, c2, c4)
    print_result(flag)

main()