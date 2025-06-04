mod = 10**9 + 7

def read_input():
    return int(input()), input()

def compute_length(s):
    return len(s)

def init_fact_list(size):
    return [1]

def append_factorial(fact, i):
    fact.append((fact[-1] * i) % mod)

def compute_factorials(limit):
    fact = init_fact_list(limit)
    for i in range(1, limit):
        append_factorial(fact, i)
    return fact

def append_revfact(revfact, value):
    revfact.append(value)

def compute_revfacts(fact, limit):
    revfact = []
    for i in range(limit):
        val = pow(fact[i], mod - 2, mod)
        append_revfact(revfact, val)
    return revfact

def init_pow_list():
    return [1]

def append_pow(pow_list, multiplier):
    pow_list.append((pow_list[-1] * multiplier) % mod)

def compute_powers(multiplier, limit):
    pow_list = init_pow_list()
    for i in range(1, limit):
        append_pow(pow_list, multiplier)
    return pow_list

def calculate_coef1(pow1, pow2, k, i):
    return (pow1[k - i] * pow2[i]) % mod

def calculate_coef2(fact, revfact, k, l, i):
    if i <= k:
        val = (fact[k + l - 1 - i] * revfact[l - 1] * revfact[k - i]) % mod
        return val
    return 0

def update_answer(ans, coef1, coef2):
    ans += coef1 * coef2
    ans %= mod
    return ans

def solve():
    k, s = read_input()
    l = compute_length(s)
    fac_size = k + l + 1
    fact = compute_factorials(fac_size)
    revfact = compute_revfacts(fact, fac_size)
    pow1 = compute_powers(25, fac_size)
    pow2 = compute_powers(26, fac_size)
    ans = 0
    for i in range(k + l):
        coef1 = calculate_coef1(pow1, pow2, k, i)
        coef2 = calculate_coef2(fact, revfact, k, l, i)
        ans = update_answer(ans, coef1, coef2)
    print(ans)

solve()