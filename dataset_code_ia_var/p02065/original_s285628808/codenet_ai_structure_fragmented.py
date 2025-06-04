from collections import Counter

def read_input():
    return map(int, input().split())

def initialize_dp(size):
    return [Counter() for _ in range(size)]

def add_state(dp, i, key, value, mod):
    dp[i][key] = (dp[i][key] + value) % mod

def can_skip_state(top, K):
    return len(top) > K+1

def process_none_left(i, top, v, dp, mod, K):
    if top and i+1 - top[0] <= K:
        key = (i+1, top)
        add_state(dp, i+1, key, v, mod)

def process_non_none_left(i, left, top, v, dp, mod, K):
    if (i+1 - left <= K) and len(top) > 1 and (i+1 - top[1] <= K):
        key = (i+1, top[1:])
        add_state(dp, i+1, key, v, mod)

def process_top_extension(i, left, top, v, dp, mod, K):
    if top and (i+1 - top[-1] <= K):
        new_top = list(top) + [i+1]
        new_top_tuple = tuple(new_top)
        key = (left, new_top_tuple)
        add_state(dp, i+1, key, v, mod)

def process_dp_iteration(i, dp, mod, K):
    for (left, top), v in dp[i].items():
        if can_skip_state(top, K):
            continue
        if left is None:
            process_none_left(i, top, v, dp, mod, K)
        else:
            process_non_none_left(i, left, top, v, dp, mod, K)
        process_top_extension(i, left, top, v, dp, mod, K)

def dp_main_loop(N, K, mod, dp):
    for i in range(2*N-1):
        process_dp_iteration(i, dp, mod, K)

def is_final_state_valid(left, top, N):
    return len(top) == 1 and left == 2*N - 1

def accumulate_result(dp, N, mod):
    res = 0
    for (left, top), v in dp[2*N-1].items():
        if is_final_state_valid(left, top, N):
            res = (res + v) % mod
    return res

def print_result(res):
    print(res)

def main():
    N, K, mod = read_input()
    dp = initialize_dp(2*N)
    dp[0][(None, (0,))] = 1
    dp_main_loop(N, K, mod, dp)
    res = accumulate_result(dp, N, mod)
    print_result(res)

main()