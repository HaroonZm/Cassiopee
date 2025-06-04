import sys
import numpy as np

def read_stdin():
    return sys.stdin.buffer.read()

def readline_stdin():
    return sys.stdin.buffer.readline()

def readlines_stdin():
    return sys.stdin.buffer.readlines()

def read_line_and_strip():
    return readline_stdin().rstrip()

def split_bytes_to_ints(byte_string):
    return list(map(int, byte_string.split()))

def to_char_list(S):
    return list(S)

def str_to_ord_arr(S):
    return np.array(list(S)) - ord('a')

def get_l_and_r():
    full_input = read_stdin()
    l, r = split_bytes_to_ints(full_input)
    return l, r

def Z_algorithm_inner(S, N, arr, i, j):
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        arr[i] = j
        if not j:
            i += 1
            continue
        k = 1
        while i+k < N and k+arr[k] < j:
            arr[i+k] = arr[k]
            k += 1
        i += k
        j -= k
    return arr

def Z_algorithm(S):
    N = len(S)
    arr = [0] * N
    arr[0] = N
    if N == 1:
        return arr
    return Z_algorithm_inner(S, N, arr, 1, 0)

def shift_S_naive(S, i):
    return S[:i] * 2

def is_double_naive_candidate(T, S):
    if len(T) > len(S) and T[:len(S)] == S:
        return True
    return False

def double_naive(S):
    L = len(S)
    for i in range(1, L+1):
        T = shift_S_naive(S, i)
        if is_double_naive_candidate(T, S):
            return T

def find_opt_len(Z, N):
    for x in range(N//2+1, N):
        z = Z[x]
        if x + z >= N:
            return x
    return N

def doubled_short_prefix(S, opt_len):
    return S[:opt_len] * 2

def F(S):
    N = len(S)
    Z = Z_algorithm(S)
    opt_len = find_opt_len(Z, N)
    return doubled_short_prefix(S, opt_len)

def F_chain(S):
    S1 = F(S)
    S2 = F(S1)
    T = F(S2)
    return S2, T

def halve_string(S):
    return S[:len(S)//2]

def prepare_sequence_arrays(S, T):
    S_arr = str_to_ord_arr(S)
    T_arr = str_to_ord_arr(T)
    return S_arr, T_arr

def prepare_lengths(S_arr, T_arr, num=100):
    lengths = [len(S_arr), len(T_arr)]
    for _ in range(num):
        lengths.append(lengths[-1] + lengths[-2])
    return lengths

def bin_count_with_len(arr, minlength=26):
    return np.bincount(arr, minlength=minlength)

def prepare_ctr(S_arr, T_arr, num=100):
    ctr = [bin_count_with_len(S_arr), bin_count_with_len(T_arr)]
    for _ in range(num):
        ctr.append(ctr[-1] + ctr[-2])
    return ctr

def get_dist_base_case(N, R, S_arr, T_arr):
    if N == 0:
        return np.bincount(S_arr[:R], minlength=26)
    if N == 1:
        return np.bincount(T_arr[:R], minlength=26)
    return None

def get_dist_recursive(N, R, S_arr, T_arr, lengths, ctr):
    base = get_dist_base_case(N, R, S_arr, T_arr)
    if base is not None:
        return base
    if lengths[N-1] >= R:
        return get_dist_recursive(N-1, R, S_arr, T_arr, lengths, ctr)
    return ctr[N-1] + get_dist_recursive(N-2, R - lengths[N-1], S_arr, T_arr, lengths, ctr)

def get_dist(N, R, S_arr, T_arr, lengths, ctr):
    return get_dist_recursive(N, R, S_arr, T_arr, lengths, ctr)

def print_output(c):
    print(*c)

def main():
    raw_S = read_line_and_strip()
    S_str = raw_S
    l, r = get_l_and_r()
    S2, T = F_chain(S_str)
    S_final = halve_string(S2)
    T_final = halve_string(T)
    S_arr, T_arr = prepare_sequence_arrays(S_final, T_final)
    lengths = prepare_lengths(S_arr, T_arr, num=100)
    ctr = prepare_ctr(S_arr, T_arr, num=100)
    res_r = get_dist(99, r, S_arr, T_arr, lengths, ctr)
    res_l = get_dist(99, l-1, S_arr, T_arr, lengths, ctr)
    c = res_r - res_l
    print_output(c)

if __name__ == "__main__":
    main()