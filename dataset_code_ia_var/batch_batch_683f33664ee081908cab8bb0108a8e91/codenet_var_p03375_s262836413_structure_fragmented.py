from collections import defaultdict

def generate_fact_dict(N):
    return {i: None for i in range(N+1)}

def generate_inverse_dict(N):
    return {i: None for i in range(1, N+1)}

def generate_fact_inverse_dict(N):
    return {i: None for i in range(N+1)}

def initialize_fact_dict(fact):
    fact[0] = 1
    fact[1] = 1

def initialize_fact_inverse_dict(fact_inverse):
    fact_inverse[0] = 1
    fact_inverse[1] = 1

def initialize_inverse_dict(inverse):
    inverse[1] = 1

def preprocess_factorials(N, mod, fact, inverse, fact_inverse):
    for i in range(2, N+1):
        update_fact(i, mod, fact)
        update_inverse(i, mod, inverse)
        update_fact_inverse(i, inverse, fact_inverse, mod)

def update_fact(i, mod, fact):
    fact[i] = i * fact[i-1] % mod

def update_inverse(i, mod, inverse):
    q, r = divmod(mod, i)
    inverse[i] = (- (q % mod) * inverse[r]) % mod

def update_fact_inverse(i, inverse, fact_inverse, mod):
    fact_inverse[i] = inverse[i] * fact_inverse[i-1] % mod

def binom_checker(n, r):
    return not (n < r or n < 0 or r < 0)

def get_binom(n, r, fact, fact_inverse, mod):
    return fact[n] * (fact_inverse[r] * fact_inverse[n-r] % mod) % mod

class Combinatorics:
    def __init__(self, N, mod):
        self.mod = mod
        self.fact = generate_fact_dict(N)
        self.inverse = generate_inverse_dict(N)
        self.fact_inverse = generate_fact_inverse_dict(N)
        initialize_fact_dict(self.fact)
        initialize_fact_inverse_dict(self.fact_inverse)
        initialize_inverse_dict(self.inverse)
        preprocess_factorials(N, self.mod, self.fact, self.inverse, self.fact_inverse)

    def binom(self, n, r):
        if not binom_checker(n, r):
            return 0
        else:
            return get_binom(n, r, self.fact, self.fact_inverse, self.mod)

def process_input():
    return map(int, input().split())

def initialize_combo_and_ans(N, M):
    com = Combinatorics(N, M)
    ans = 0
    return com, ans

def initialize_pow2(N, M):
    arr_len = N*N // 4 + 1
    arr = [0] * arr_len
    arr[0] = 1
    for i in range(1, arr_len):
        arr[i] = (arr[i-1] * 2) % M
    return arr

def initialize_pow_pow2(N, M):
    arr = [0] * (N+1)
    arr[0] = 2
    for i in range(1, N+1):
        arr[i] = pow(arr[i-1], 2, M)
    return arr

def ways2_factory(N):
    return {n: defaultdict(int) for n in range(N+1)}

def update_ways2_for_n_ge_1(ways2, n, i, M):
    ways2[n][i] = (ways2[n][i] + ways2[n-1][i]) % M
    if i >= 1:
        ways2[n][i] = (ways2[n][i] + ways2[n-1][i-1]) % M
    ways2[n][i] = (ways2[n][i] + (i*ways2[n-1][i]) % M) % M

def increment_temp(temp, ways2, n, i, pow2, N, M):
    return (temp + (ways2[n][i] * pow2[(N-n)*i]) % M) % M

def ways2_case_n_eq_0(ways2, n):
    ways2[n][0] = 1
    return ways2[n][0]

def compute_ways(n, temp, pow_pow2, N, M):
    return (temp * pow_pow2[N-n]) % M

def update_ans_for_even_n(ans, com, N, n, ways, M):
    return (ans + (com.binom(N, n) * ways) % M) % M

def update_ans_for_odd_n(ans, com, N, n, ways, M):
    return (ans - (com.binom(N, n) * ways) % M) % M

def main():
    N, M = process_input()
    com, ans = initialize_combo_and_ans(N, M)
    pow2 = initialize_pow2(N, M)
    pow_pow2 = initialize_pow_pow2(N, M)
    ways2 = ways2_factory(N)
    for n in range(N+1):
        temp = 0
        if n >= 1:
            for i in range(n+1):
                update_ways2_for_n_ge_1(ways2, n, i, M)
                temp = increment_temp(temp, ways2, n, i, pow2, N, M)
        else:
            temp += ways2_case_n_eq_0(ways2, n)
        ways = compute_ways(n, temp, pow_pow2, N, M)
        if n % 2 == 0:
            ans = update_ans_for_even_n(ans, com, N, n, ways, M)
        else:
            ans = update_ans_for_odd_n(ans, com, N, n, ways, M)
    print(ans)

main()