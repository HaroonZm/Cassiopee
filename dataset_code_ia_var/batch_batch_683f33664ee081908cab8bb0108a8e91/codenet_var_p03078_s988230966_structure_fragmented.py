import numpy as np

def get_input():
    return input()

def parse_integers_from_input(input_line):
    return list(map(int, input_line.split()))

def get_X_Y_Z_K():
    return parse_integers_from_input(get_input())

def get_array():
    return parse_integers_from_input(get_input())

def get_A():
    return get_array()

def get_B():
    return get_array()

def get_C():
    return get_array()

def reverse_sort_array(arr):
    arr.sort(reverse=True)
    return arr

def min_val(a, b):
    return min(a, b)

def compute_bounds_i(K, X):
    return min_val(K, X)

def compute_bounds_j(K, i, Y):
    return min_val(K // (i + 1), Y)

def compute_bounds_k(K, i, j, Z):
    return min_val(((K // (i + 1) + 1) // (j + 1)), Z)

def append_sum_to_D(D, a_val, b_val, c_val):
    D.append(a_val + b_val + c_val)

def build_D(A, B, C, K, X, Y, Z):
    D = []
    bound_i = compute_bounds_i(K, X)
    for i in range(bound_i):
        bound_j = compute_bounds_j(K, i, Y)
        for j in range(bound_j):
            bound_k = compute_bounds_k(K, i, j, Z)
            for k in range(bound_k):
                append_sum_to_D(D, A[i], B[j], C[k])
    return D

def sort_D_descending(D):
    D.sort(reverse=True)
    return D

def print_first_K_elements(D, K):
    for i in range(K):
        print(int(D[i]))

def main():
    X, Y, Z, K = get_X_Y_Z_K()
    A = get_A()
    B = get_B()
    C = get_C()
    A = reverse_sort_array(A)
    B = reverse_sort_array(B)
    C = reverse_sort_array(C)
    D = build_D(A, B, C, K, X, Y, Z)
    D = sort_D_descending(D)
    print_first_K_elements(D, K)

main()