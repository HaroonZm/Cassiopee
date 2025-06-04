from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_list_of_integers():
    return list(map(int, sys.stdin.readline().split()))

def read_single_integer():
    return int(sys.stdin.readline())

def read_list_of_lists_of_strings():
    return list(map(list, sys.stdin.readline().split()))

def read_list_of_characters():
    return list(sys.stdin.readline())[:-1]

def read_multiple_integers(number_of_lines):
    integer_list = [None for _ in range(number_of_lines)]
    for line_index in range(number_of_lines):
        integer_list[line_index] = read_single_integer()
    return integer_list

def read_multiple_lists_of_integers(number_of_lines):
    list_of_integer_lists = [None for _ in range(number_of_lines)]
    for line_index in range(number_of_lines):
        list_of_integer_lists[line_index] = read_list_of_integers()
    return list_of_integer_lists

def read_multiple_lists_of_characters(number_of_lines):
    list_of_character_lists = [None for _ in range(number_of_lines)]
    for line_index in range(number_of_lines):
        list_of_character_lists[line_index] = read_list_of_characters()
    return list_of_character_lists

def read_multiple_lists_of_lists_of_strings(number_of_lines):
    list_of_lists_of_strings = [None for _ in range(number_of_lines)]
    for line_index in range(number_of_lines):
        list_of_lists_of_strings[line_index] = read_list_of_lists_of_strings()
    return list_of_lists_of_strings

sys.setrecursionlimit(1_000_000)
MODULO = 1_000_000_007

def combination(n, k):
    return factorial_list[n] * modular_inverse_list[k] * modular_inverse_list[n - k] % MODULO

n, k = read_list_of_integers()

if n < k:
    print(0)
    quit()

factorial_list = [1 for _ in range(k + 1)]
for i in range(k):
    factorial_list[i + 1] = factorial_list[i] * (i + 1) % MODULO

modular_inverse_list = [None for _ in range(n + 1)]
modular_inverse_list[k] = pow(factorial_list[k], MODULO - 2, MODULO)
for i in range(k - 1, -1, -1):
    modular_inverse_list[i] = modular_inverse_list[i + 1] * (i + 1) % MODULO

result = 0
for subset_size in range(k + 1):
    if subset_size % 2:
        result -= combination(k, subset_size) * pow(k - subset_size, n, MODULO) % MODULO
    else:
        result += combination(k, subset_size) * pow(k - subset_size, n, MODULO) % MODULO
    result %= MODULO

print(result)