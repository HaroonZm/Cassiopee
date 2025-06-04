import sys
import numpy as np

def get_stdin_buffer():
    return sys.stdin.buffer

def read_stdin(buffer):
    return buffer.read()

def readline_stdin(buffer):
    return buffer.readline()

def readlines_stdin(buffer):
    return buffer.readlines()

def parse_N_K(line):
    N, K = map(int, line.split())
    return N, K

def parse_array(line):
    return np.array(line.split(), np.int64)

def sort_array(arr, reverse=False):
    arr = np.sort(arr)
    if reverse:
        arr = arr[::-1]
    return arr

def read_input():
    buffer = get_stdin_buffer()
    n_k_line = readline_stdin(buffer)
    a_line = readline_stdin(buffer)
    f_line = readline_stdin(buffer)
    return n_k_line, a_line, f_line

def prepare_data(n_k_line, a_line, f_line):
    N, K = parse_N_K(n_k_line)
    A = parse_array(a_line)
    F = parse_array(f_line)
    A = sort_array(A)
    F = sort_array(F, reverse=True)
    return N, K, A, F

def compute_maximum_for_x(A, F, x):
    return np.maximum(0, A - x // F)

def compute_sum_maximum(A, F, x):
    arr = compute_maximum_for_x(A, F, x)
    return arr.sum()

def can_achieve_x(A, F, K, x):
    sum_max = compute_sum_maximum(A, F, x)
    return sum_max <= K

def binary_search(A, F, K, left, right):
    while left + 1 < right:
        mid = (left + right) // 2
        if can_achieve_x(A, F, K, mid):
            right = mid
        else:
            left = mid
    return right

def main():
    n_k_line, a_line, f_line = read_input()
    N, K, A, F = prepare_data(n_k_line, a_line, f_line)
    left = -1
    right = 10**13
    answer = binary_search(A, F, K, left, right)
    print(answer)

main()