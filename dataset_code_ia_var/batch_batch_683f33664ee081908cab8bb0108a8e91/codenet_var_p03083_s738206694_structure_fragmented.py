def get_U():
    return 2*10**5

def get_MOD():
    return 10**9+7

def init_array(size, value):
    return [value] * (size+1)

def compute_fact(U, MOD, fact):
    for i in range(1, U+1):
        fact[i] = (fact[i-1]*i) % MOD

def compute_two(U, MOD, two):
    for i in range(1, U+1):
        two[i] = (two[i-1]*2) % MOD

def compute_fact_inv_U(U, MOD, fact, fact_inv):
    fact_inv[U] = pow(fact[U], MOD-2, MOD)

def compute_two_inv_U(U, MOD, two, two_inv):
    two_inv[U] = pow(two[U], MOD-2, MOD)

def compute_fact_inv(U, fact_inv, MOD):
    for i in range(U, 0, -1):
        fact_inv[i-1] = (fact_inv[i]*i) % MOD

def compute_two_inv(U, two_inv, MOD):
    for i in range(U, 0, -1):
        two_inv[i-1] = (two_inv[i]*2) % MOD

def prepare_precomputation():
    U = get_U()
    MOD = get_MOD()
    fact = init_array(U, 1)
    fact_inv = init_array(U, 1)
    two = init_array(U, 1)
    two_inv = init_array(U, 1)
    compute_fact(U, MOD, fact)
    compute_two(U, MOD, two)
    compute_fact_inv_U(U, MOD, fact, fact_inv)
    compute_two_inv_U(U, MOD, two, two_inv)
    compute_fact_inv(U, fact_inv, MOD)
    compute_two_inv(U, two_inv, MOD)
    return fact, fact_inv, two, two_inv

def comb(n, k, fact, fact_inv, MOD):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[k]
    z %= MOD
    z *= fact_inv[n-k]
    z %= MOD
    return z

def get_input():
    return map(int, input().split())

def update_p(i, B, comb, fact, fact_inv, MOD, two_inv):
    return comb(i-1, B-1, fact, fact_inv, MOD) * two_inv[i] % MOD

def update_q(i, W, comb, fact, fact_inv, MOD, two_inv):
    return comb(i-1, W-1, fact, fact_inv, MOD) * two_inv[i] % MOD

def compute_ans(i, p, q, MOD, two_inv):
    ans = 1 - p + q
    ans %= MOD
    ans *= two_inv[1]
    ans %= MOD
    return ans

def problem_main():
    fact, fact_inv, two, two_inv = prepare_precomputation()
    MOD = get_MOD()
    B, W = get_input()
    p = 0
    q = 0
    for i in range(1, B+W+1):
        ans = compute_ans(i, p, q, MOD, two_inv)
        print(ans)
        p = (p + update_p(i, B, comb, fact, fact_inv, MOD, two_inv)) % MOD
        q = (q + update_q(i, W, comb, fact, fact_inv, MOD, two_inv)) % MOD

problem_main()