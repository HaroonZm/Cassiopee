def create_factorial_list_size(n):
    return [1] * (n + 1)

def initialize_first_two_factorials(F):
    F[0] = 1
    F[1] = 1

def compute_factorials(F, n, p):
    for i in range(2, n + 1):
        F[i] = F[i - 1] * i % p

def fib(n, p):
    F = create_factorial_list_size(n)
    initialize_first_two_factorials(F)
    compute_factorials(F, n, p)
    return F

def get_N_from_F(F):
    return len(F) - 1

def duplicate_factorial_list(F):
    return list(F)

def set_last_inverse(Finv, F, p):
    Finv[-1] = pow(F[-1], p - 2, p)

def compute_inverse_factorials(Finv, N, p):
    for i in range(N - 1, -1, -1):
        Finv[i] = Finv[i + 1] * (i + 1) % p

def finv(F, p):
    N = get_N_from_F(F)
    Finv = duplicate_factorial_list(F)
    set_last_inverse(Finv, F, p)
    compute_inverse_factorials(Finv, N, p)
    return Finv

def multiply_and_mod(a, b, p):
    return a * b % p

def comb(F, Finv, n, a, p):
    temp = multiply_and_mod(F[n], Finv[a], p)
    temp = multiply_and_mod(temp, Finv[n - a], p)
    return temp

def read_input():
    return map(int, input().split())

def get_factorials(N, p):
    return fib(N, p)

def get_inverse_factorials(F, p):
    return finv(F, p)

def should_continue_due_to_A(_A, K):
    return _A > K

def calc_A_times_a(A, a):
    return A * a

def B_divides_difference(K, _A, B):
    return (K - _A) % B == 0

def calc_b(K, _A, B):
    return (K - _A) // B

def is_b_within_range(b, N):
    return b <= N

def update_cnt(cnt, F, Finv, N, a, b, p):
    value1 = comb(F, Finv, N, a, p)
    value2 = comb(F, Finv, N, b, p)
    new_cnt = cnt + value1 * value2
    return new_cnt % p

def main_process():
    N, A, B, K = read_input()
    p = 998244353
    F = get_factorials(N, p)
    Finv = get_inverse_factorials(F, p)
    cnt = 0
    upper_a = min(N + 1, K // A + 1)
    for a in range(upper_a):
        _A = calc_A_times_a(A, a)
        if should_continue_due_to_A(_A, K):
            continue
        if not B_divides_difference(K, _A, B):
            continue
        b = calc_b(K, _A, B)
        if not is_b_within_range(b, N):
            continue
        cnt = update_cnt(cnt, F, Finv, N, a, b, p)
    print(cnt)

main_process()