def read_input():
    return map(int, input().split())

def read_steps(m):
    return [int(input()) for _ in range(m)]

def init_dp(n):
    return [0 for _ in range(n+10)]

def set_base_case(dp):
    dp[0] = 1

def set_broken_steps(dp, a):
    for x in a:
        mark_broken_step(dp, x)

def mark_broken_step(dp, x):
    dp[x] = -1

def get_mod():
    return 10**9 + 7

def update_dp(i, dp, mod):
    if dp[i] < 0:
        return
    increment_step(i+1, dp, mod, dp[i])
    increment_step(i+2, dp, mod, dp[i])

def increment_step(idx, dp, mod, value):
    if dp[idx] >= 0:
        dp[idx] += value
        dp[idx] %= mod

def compute_result(n, dp, mod):
    for i in range(n):
        update_dp(i, dp, mod)
    return dp[n]

def print_result(res):
    print(res)

def main():
    n, m = read_input()
    a = read_steps(m)
    dp = init_dp(n)
    set_base_case(dp)
    set_broken_steps(dp, a)
    mod = get_mod()
    result = compute_result(n, dp, mod)
    print_result(result)

main()