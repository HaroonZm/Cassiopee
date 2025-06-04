import numpy as np

def read_n():
    return int(input())

def read_array():
    return np.array(list(map(int, input().split())), dtype=np.int64)

def compute_t(i):
    return 1 << i

def get_mod2t(arr, t):
    return arr.copy() % (2 * t)

def sort_arr(arr):
    arr.sort()
    return arr

def get_2t_minus_e(E, t):
    return 2 * t - E

def get_t_minus_e(E, t):
    return t - E

def get_4t_minus_e(E, t):
    return 4 * t - E

def get_3t_minus_e(E, t):
    return 3 * t - E

def search_left(arr_sorted, values):
    return np.searchsorted(arr_sorted, values, side="left")

def update_D(D, val):
    return D + val

def subtract_D(D, val):
    return D - val

def sum_D(D):
    return D.sum()

def mod2(cnt):
    return cnt % 2

def shift_cnt(cnt, i):
    return cnt << i

def bitwise_or(ans, shifted):
    return ans | shifted

def main_loop(A, B, ans):
    for i in range(30):
        t = compute_t(i)
        C = get_mod2t(B, t)
        E = get_mod2t(A, t)
        C = sort_arr(C)
        E = sort_arr(E)
        D = search_left(C, get_2t_minus_e(E, t))
        D = subtract_D(D, search_left(C, get_t_minus_e(E, t)))
        D = update_D(D, search_left(C, get_4t_minus_e(E, t)))
        D = subtract_D(D, search_left(C, get_3t_minus_e(E, t)))
        cnt = mod2(sum_D(D))
        ans = bitwise_or(ans, shift_cnt(cnt, i))
    return ans

def print_result(ans):
    print(ans)

def main():
    n = read_n()
    A = read_array()
    B = read_array()
    ans = 0
    ans = main_loop(A, B, ans)
    print_result(ans)

main()