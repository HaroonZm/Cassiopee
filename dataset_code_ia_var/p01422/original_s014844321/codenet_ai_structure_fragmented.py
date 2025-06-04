import sys

def get_input():
    return sys.stdin.readline

def get_inf():
    return float('inf')

def get_mod():
    return 10 ** 9 + 7

def parse_int_list(input_func):
    return list(map(int, input_func().split()))

def get_initial_dp(a0):
    size = a0 * 2
    return [get_inf()] * size

def fill_first_dp(dp, a0):
    for i in range(a0 // 2, a0 * 2):
        dp[i] = abs(i - a0) / a0
    return dp

def get_new_dp(size):
    return [get_inf()] * size

def should_continue_dp(dp, j):
    return dp[j] != get_inf()

def calc_t(dp, j):
    return dp[j]

def get_k_range(j, nn):
    return range(j, nn, j)

def calc_u(a1, k):
    return abs(a1 - k) / a1

def update_u_if_needed(u, t):
    if u < t:
        u = t
    return u

def update_ndp_if_better(ndp, k, u):
    if ndp[k] > u:
        ndp[k] = u
    return ndp

def main_solve(N, input_func):
    A = parse_int_list(input_func)
    dp = get_initial_dp(A[0])
    dp = fill_first_dp(dp, A[0])
    for i in range(N - 1):
        a1 = A[i + 1]
        nn = a1 * 2
        ndp = get_new_dp(nn)
        for j in range(1, len(dp)):
            if not should_continue_dp(dp, j):
                continue
            t = calc_t(dp, j)
            for k in get_k_range(j, nn):
                u = calc_u(a1, k)
                u = update_u_if_needed(u, t)
                ndp = update_ndp_if_better(ndp, k, u)
        dp = ndp
    return get_final_result(dp)

def get_final_result(dp):
    return '{:0.12f}'.format(min(dp))

def read_n_and_run():
    input_func = get_input()
    N = int(input_func())
    if N != 0:
        print(main_solve(N, get_input()))

read_n_and_run()