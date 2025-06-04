import itertools
import bisect
from fractions import Fraction
from math import factorial

def read_input():
    return map(int, input().split())

def read_and_sort_values():
    return sorted(list(map(int, input().split())), reverse=True)

def get_factorial(n):
    return factorial(n)

def compute_comb(n, r):
    return get_factorial(n) // (get_factorial(r) * get_factorial(n - r))

def get_accumulated_values(V):
    return list(itertools.accumulate(V))

def get_averages(accumulated, count):
    return [Fraction(a, i) for i, a in enumerate(accumulated, 1)]

def get_max_average(averages, A, B):
    return max(averages[A - 1:B])

def get_indices_with_max_average(averages, A, B, max_num):
    result = []
    for i, v in enumerate(averages):
        if A <= i + 1 <= B and v == max_num:
            result.append(i)
    return result

def invert_values(V):
    return [-v for v in V]

def get_left_index(Vm, value):
    return bisect.bisect_left(Vm, value)

def get_right_index(Vm, value):
    return bisect.bisect_right(Vm, value)

def compute_total_combs(max_indices, Vm):
    total = 0
    for ind in max_indices:
        l = get_left_index(Vm, Vm[ind])
        r = get_right_index(Vm, Vm[ind])
        total += compute_comb(r - l, ind - l + 1)
    return total

def print_results(max_num, C):
    print(float(max_num))
    print(C)

def main():
    N, A, B = read_input()
    V = read_and_sort_values()
    acc_vals = get_accumulated_values(V)
    Ave = get_averages(acc_vals, N)
    max_num = get_max_average(Ave, A, B)
    max_indices = get_indices_with_max_average(Ave, A, B, max_num)
    Vm = invert_values(V)
    C = compute_total_combs(max_indices, Vm)
    print_results(max_num, C)

main()