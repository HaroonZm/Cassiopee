import numpy as np
import sys

def parse_input():
    N, K = read_N_and_K()
    XYC = read_XYC(N)
    return N, K, XYC

def read_N_and_K():
    return map(int, input().split())

def read_XYC(N):
    return [parse_XYC_line() for _ in range(N)]

def parse_XYC_line():
    return input().split()

def initialize_A(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def compute_indices(x, y, c, K):
    i = idx_i(x, c, K)
    j = idx_j(y, K)
    i0 = i % K
    j0 = j % K
    return i, j, i0, j0

def idx_i(x, c, K):
    x = int(x)
    if c == "W":
        return x % (K*2)
    else:
        return (x + K) % (K*2)

def idx_j(y, K):
    return int(y) % (K*2)

def process_one_entry(x, y, c, K, add_sum2d):
    i, j, i0, j0 = compute_indices(x, y, c, K)
    if cond_main(i, j, K):
        process_case_A(i0, j0, K, add_sum2d)
    else:
        process_case_B(i0, j0, K, add_sum2d)

def cond_main(i, j, K):
    return (i < K and j < K) or (i >= K and j >= K)

def process_case_A(i0, j0, K, add_sum2d):
    # case: (i<K and j<K) or (i>=K and j>=K)
    add_sum2d(0, 0, i0, j0)
    add_sum2d(i0+K, 0, K*2, j0)
    add_sum2d(i0, j0, i0+K, j0+K)
    add_sum2d(0, j0+K, i0, K*2)
    add_sum2d(i0+K, j0+K, K*2, K*2)

def process_case_B(i0, j0, K, add_sum2d):
    # case: else
    add_sum2d(i0, 0, i0+K, j0)
    add_sum2d(0, j0, i0, j0+K)
    add_sum2d(i0+K, j0, K*2, j0+K)
    add_sum2d(i0, j0+K, i0+K, K*2)

def main():
    N, K, XYC = parse_input()
    size = K * 2 + 1
    A = initialize_A(size)

    def add_sum2d(i1, j1, i2, j2):
        A[i1][j1] += 1
        A[i1][j2] -= 1
        A[i2][j1] -= 1
        A[i2][j2] += 1

    for x, y, c in XYC:
        process_one_entry(x, y, c, K, add_sum2d)

    AA = convert_to_numpy(A)
    AA = cumulative_sum_2d(AA, K)
    print(max_array_value(AA))

def convert_to_numpy(A):
    return np.array(A)

def cumulative_sum_2d(AA, K):
    return row_col_additions(AA, K)

def row_col_additions(AA, K):
    for i in range(K*2):
        add_row(AA, i)
    for j in range(K*2):
        add_col(AA, j)
    return AA

def add_row(AA, i):
    AA[i+1, :] += AA[i, :]

def add_col(AA, j):
    AA[:, j+1] += AA[:, j]

def max_array_value(AA):
    return AA.max()

if __name__ == "__main__":
    main()