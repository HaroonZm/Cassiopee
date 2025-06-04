def initialize_globals():
    global MOD, fact, factinv, inv
    MOD = 10 ** 9 + 7
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

def get_input():
    K = int(input())
    S = input()
    return K, S

def compute_N(S):
    return len(S)

def extend_lists(limit):
    for i in range(2, limit + 1):
        append_fact(i)
        append_inv(i)
        append_factinv()

def append_fact(i):
    fact.append((fact[-1] * i) % MOD)

def append_inv(i):
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)

def append_factinv():
    factinv.append((factinv[-1] * inv[-1]) % MOD)

def combination_prepare(K, N):
    extend_lists(K + N)

def choose(n, r):
    if (r < 0) or (n < r):
        return 0
    r = adjust_r(n, r)
    return compute_nCr(n, r)

def adjust_r(n, r):
    return min(r, n - r)

def compute_nCr(n, r):
    return fact[n] * factinv[r] * factinv[n - r] % MOD

def pow25(i):
    return pow(25, i, MOD)

def pow26(j):
    return pow(26, j, MOD)

def compute_term(i, N, K):
    comb = choose(i + N - 1, N - 1)
    power_25 = pow25(i)
    power_26 = pow26(K - i)
    return (comb * power_25 % MOD) * power_26 % MOD

def main_loop(K, N):
    ans = 0
    for i in range(K + 1):
        term = compute_term(i, N, K)
        ans = (ans + term) % MOD
    return ans

def print_result(ans):
    print(ans)

def main():
    initialize_globals()
    K, S = get_input()
    N = compute_N(S)
    combination_prepare(K, N)
    ans = main_loop(K, N)
    print_result(ans)

main()