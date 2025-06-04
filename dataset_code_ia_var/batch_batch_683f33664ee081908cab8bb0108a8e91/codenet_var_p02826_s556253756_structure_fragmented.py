import numpy as np

def read_input():
    return map(int, input().split())

def generate_coef(n):
    return np.minimum(np.arange(n,1,-1), np.arange(1,n))

def initialize_dp(n):
    dp = np.zeros(n, dtype=np.int64)
    set_dp_base(dp)
    return dp

def set_dp_base(dp):
    dp[0] = 1

def copy_dp(dp):
    return dp.copy()

def compute_ndp(ndp, dp, c, n):
    for i in generate_range(c, n):
        add_to_ndp(ndp, dp, i, n)
    return ndp

def generate_range(c, n):
    return range(c, n, c)

def add_to_ndp(ndp, dp, i, n):
    ndp[i:] += dp[:n-i]

def mod_dp(ndp, m):
    return ndp % m

def final_result(dp, n, m):
    arr = compute_arr(n)
    res = (dp * arr) % m
    return np.sum(res) % m

def compute_arr(n):
    return np.arange(n, 0, -1)

def main():
    n, m = read_input()
    coef = generate_coef(n)
    dp = initialize_dp(n)
    for c in coef:
        ndp = copy_dp(dp)
        ndp = compute_ndp(ndp, dp, c, n)
        dp = mod_dp(ndp, m)
    print(final_result(dp, n, m))

main()