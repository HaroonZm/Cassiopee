def initialize_globals():
    mod = 10**9 + 7
    N = 10**5
    g1 = [1] * (N + 1)
    g2 = [1] * (N + 1)
    inverse = [1] * (N + 1)
    return mod, N, g1, g2, inverse

def fill_tables(N, mod, g1, g2, inverse):
    for i in range(2, N + 1):
        fill_table_step(i, mod, g1, g2, inverse)
    finalize_inverse(inverse)

def fill_table_step(i, mod, g1, g2, inverse):
    g1[i] = (g1[i - 1] * i) % mod
    inverse[i] = ((-inverse[mod % i] * (mod // i)) % mod)
    g2[i] = (g2[i - 1] * inverse[i]) % mod

def finalize_inverse(inverse):
    inverse[0] = 0

def get_input():
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    return N, M, A

def initialize_dp(N, M, start_value):
    dp = []
    for i in range(M + 1):
        dp.append([0 for _ in range(2 ** N)])
    dp[0][0] = start_value
    return dp

def comb(n, r, g1, g2, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

def compute_k_term(n, a_i, j, k, g1, g2, mod):
    return (g1[n - a_i - j] * g2[n - a_i + 1 - (j + 2 ** k)]) % mod

def get_g1_value(n, j, k, g1):
    return g1[n - 1 - j - 2 ** k]

def get_pow2k(k):
    return 2 ** k

def add_to_dp(dp, i, j, k, n, a_i, mod, g1, g2):
    value = (((-1) * (compute_k_term(n, a_i, j, k, g1, g2, mod)) *
             ((dp[i - 1][j + 2 ** k] + get_g1_value(n, j, k, g1)) * get_pow2k(k)) % mod) % mod) % mod
    return value

def fill_dp(N, M, A, dp, g1, g2, mod):
    for i in range(1, M + 1):
        for j in range(2 ** N):
            update_dp_cell(N, A, dp, g1, g2, mod, i, j)

def update_dp_cell(N, A, dp, g1, g2, mod, i, j):
    dp[i][j] = dp[i - 1][j]
    for k in range(N):
        if is_k_term_applicable(j, k, N, A[i]):
            dp[i][j] = (dp[i][j] + add_to_dp(dp, i, j, k, 2 ** N, A[i], mod, g1, g2)) % mod

def is_k_term_applicable(j, k, N, a_i):
    return ((j >> k) & 1 == 0) and ((2 ** N - a_i - j) >= (2 ** k - 1))

def calculate_result(dp, M, N, mod):
    return (dp[M][0] * pow(2, N, mod)) % mod

def main():
    mod, upper_N, g1, g2, inverse = initialize_globals()
    fill_tables(upper_N, mod, g1, g2, inverse)
    N, M, A = get_input()
    dp = initialize_dp(N, M, g1[2 ** N - 1])
    fill_dp(N, M, A, dp, g1, g2, mod)
    print(calculate_result(dp, M, N, mod))

main()