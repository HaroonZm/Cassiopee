MOD = 10**9 + 7

def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def init_arrays(n):
    sum_arr = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    fac = [1 for _ in range(n+1)]
    finv = [1 for _ in range(n+1)]
    inv = [1 for _ in range(n+1)]
    return sum_arr, dp, fac, finv, inv

def compute_fac_inv(n, fac, inv, finv):
    compute_factorials(n, fac)
    compute_inv_array(n, inv)
    compute_factorial_inverses(n, inv, finv)

def compute_factorials(n, fac):
    for i in range(2, n+1):
        fac[i] = fac[i-1]*i % MOD

def compute_inv_array(n, inv):
    for i in range(2, n+1):
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD

def compute_factorial_inverses(n, inv, finv):
    for i in range(2, n+1):
        finv[i] = finv[i-1] * inv[i] % MOD

def fill_sum_array(n, sum_arr, inv):
    for i in range(1, n+1):
        sum_arr[i] = (sum_arr[i-1] + inv[i]) % MOD
    sum_arr[0] = 1

def fill_dp_array(n, dp, sum_arr):
    for i in range(1, n+1):
        dp[i] = (sum_arr[i] + sum_arr[n+1-i] - 1) % MOD

def compute_final_answer(n, dp, a, fac):
    ans = 0
    for i in range(1, n+1):
        ans = (ans + dp[i]*a[i-1]) % MOD
    return (ans * fac[n]) % MOD

def main():
    n, a = read_input()
    sum_arr, dp, fac, finv, inv = init_arrays(n)
    compute_fac_inv(n, fac, inv, finv)
    fill_sum_array(n, sum_arr, inv)
    fill_dp_array(n, dp, sum_arr)
    answer = compute_final_answer(n, dp, a, fac)
    print(answer)

main()