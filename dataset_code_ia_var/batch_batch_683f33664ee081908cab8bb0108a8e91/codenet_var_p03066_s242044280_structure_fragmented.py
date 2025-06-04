import sys
import numpy as np

def read_stdin():
    return sys.stdin.buffer.read()

def read_stdin_split():
    return read_stdin().split()

def parse_ints(lst, idx=0, count=2):
    return map(int, lst[idx:idx+count])

def get_mod():
    return 998244353

def power_mod(a, n, mod):
    return pow(int(a), n, mod)

def get_U(N):
    return N + N + 100

def as_np_arange(U, dtype=np.int64):
    return np.arange(U, dtype=dtype)

def resize_arr(arr, Lsq):
    return np.resize(arr, Lsq ** 2).reshape(Lsq, Lsq)

def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L ** 0.5 + 1)
    arr = resize_arr(arr, Lsq)
    arr = cumprod_stage1(arr, MOD, Lsq)
    arr = cumprod_stage2(arr, MOD, Lsq)
    return arr.ravel()[:L]

def cumprod_stage1(arr, MOD, Lsq):
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    return arr

def cumprod_stage2(arr, MOD, Lsq):
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    return arr

def make_fact(U, MOD):
    x = as_np_arange(U)
    x[0] = 1
    fact = cumprod(x, MOD)
    y = as_np_arange(U, dtype=np.int64)[::-1]
    y[0] = power_mod(fact[-1], MOD - 2, MOD)
    fact_inv = cumprod(y, MOD)[::-1]
    return fact, fact_inv

def make_combN(N, fact, fact_inv, MOD):
    a = fact[N]
    b = fact_inv[:N+1]
    c = fact_inv[N::-1]
    d = a * b % MOD
    e = d * c % MOD
    return e

def polynomial_mult(P, Q, X, MOD):
    dP = len(P) - 1
    dQ = len(Q) - 1
    if dP < dQ:
        dP, dQ = dQ, dP
        P, Q = Q, P
    R = np.zeros(dP + dQ + 1, np.int64)
    for n in range(dQ + 1):
        R[n:n + dP + 1] += Q[n] * P % MOD
    R %= MOD
    return R[:X]

def polynomial_power(P, n, X, MOD):
    if n == 0:
        return np.array([1], dtype=np.int64)
    Q = polynomial_power(P, n // 2, X, MOD)
    Q = polynomial_mult(Q, Q, X, MOD)
    if n & 1:
        return polynomial_mult(P, Q, X, MOD)
    else:
        return Q

def F1_prepare_poly():
    return np.array([1, 1, 1], np.int64)

def F1(N, X, MOD):
    P = F1_prepare_poly()
    Q = polynomial_power(P, N, X, MOD)
    return F1_final_sum(Q, MOD)

def F1_final_sum(Q, MOD):
    return Q.sum() % MOD

def F2_loop_range(X):
    return range(X)

def F2_calc_m(X, n):
    return (X - 1) - (2 + 2 * n)

def F2_construct_two_and_one(m):
    two = np.arange(m // 2 + 1, dtype=np.int64)
    one = m - 2 * two
    return two, one

def F2_calc_coef(fact, fact_inv, one, two, MOD):
    return fact[one + two] * fact_inv[one] % MOD * fact_inv[two] % MOD

def F2_filter_rest(rest, coef):
    ind = rest >= 0
    return rest[ind], coef[ind]

def F2_update_x(x, rest, coef):
    x[rest] += coef
    return x

def F2_finish(x, combN, MOD):
    return (x * combN % MOD).sum() % MOD

def F2(N, X, fact, fact_inv, combN, MOD):
    x = np.zeros(N + 1, np.int64)
    for n in F2_loop_range(X):
        m = F2_calc_m(X, n)
        if m < 0:
            break
        two, one = F2_construct_two_and_one(m)
        coef = F2_calc_coef(fact, fact_inv, one, two, MOD)
        rest = N - one - two - (2 * n + 2)
        rest, coef = F2_filter_rest(rest, coef)
        x = F2_update_x(x, rest, coef)
    x %= MOD
    return F2_finish(x, combN, MOD)

def is_X_even(X):
    return X % 2 == 0

def F3_check_X_even(X):
    return is_X_even(X)

def F3_check_X_gt_N(X, N):
    return X > N

def F3_check_n(N, X):
    return N - X + 1

def F3(N, X, combN, MOD):
    if F3_check_X_even(X):
        return 0
    if F3_check_X_gt_N(X, N):
        return 0
    n = F3_check_n(N, X)
    return combN[:n].sum() % MOD

def answer_sum(a, b, c, MOD):
    return (a + b + c) % MOD

def main():
    input_lst = read_stdin_split()
    N, X = parse_ints(input_lst)
    MOD = get_mod()
    U = get_U(N)
    fact, fact_inv = make_fact(U, MOD)
    combN = make_combN(N, fact, fact_inv, MOD)
    ans1 = F1(N, X, MOD)
    ans2 = F2(N, X, fact, fact_inv, combN, MOD)
    ans3 = F3(N, X, combN, MOD)
    answer = answer_sum(ans1, ans2, ans3, MOD)
    print(answer)

main()