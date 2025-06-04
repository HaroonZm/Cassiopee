from sys import stdin
from collections import Counter
import numpy as np

def read_input():
    return stdin.readline()

def parse_first_line(line):
    return [int(x) for x in line.split()]

def parse_array_line(line):
    return [int(a) for a in line.split()]

def to_numpy_array(lst):
    return np.array(lst, dtype=np.int64)

def prepend_zero(arr):
    return np.hstack([0, arr])

def mod_array(arr, mod):
    return arr % mod

def cumulative_sum(arr):
    return arr.cumsum()

def compute_cum_remainders(A, M):
    arr_with_zero = prepend_zero(A)
    arr_mod = mod_array(arr_with_zero, M)
    cumsum_arr = cumulative_sum(arr_mod)
    return mod_array(cumsum_arr, M)

def count_remainders(arr):
    return Counter(arr)

def calculate_combinations_from_counts(counts):
    total = 0
    for count in counts.values():
        total += count * (count - 1) // 2
    return total

def main():
    first_line = read_input()
    N, M = parse_first_line(first_line)
    array_line = read_input()
    A_raw = parse_array_line(array_line)
    A = to_numpy_array(A_raw)
    cum_remainders = compute_cum_remainders(A, M)
    remainder_counts = count_remainders(cum_remainders)
    combinations = calculate_combinations_from_counts(remainder_counts)
    print(combinations)

main()