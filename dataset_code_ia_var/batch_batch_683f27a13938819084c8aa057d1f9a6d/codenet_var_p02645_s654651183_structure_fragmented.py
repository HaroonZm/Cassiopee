import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import math
import bisect

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

def set_large_recursion_limit():
    sys.setrecursionlimit(1000000)

def read_input():
    return input()

def get_first_three_characters(s):
    return s[0:3]

def print_string(s):
    print(s)

def process_and_print_first_three():
    s = read_input()
    first_three = get_first_three_characters(s)
    print_string(first_three)

def main():
    set_large_recursion_limit()
    process_and_print_first_three()

main()