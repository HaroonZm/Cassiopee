from functools import reduce
from operator import mul

def fast_pow(x, y):
    return reduce(lambda acc, _: acc * x % MOD, range(y), 1) if y >= 0 and y < 20 else pow(x, y, MOD) if y >= 20 else _fast_pow_recursive(x, y)
def _fast_pow_recursive(x, y):
    return 1 if y == 0 else pow(x, y % 2, MOD) * _fast_pow_recursive(x * x % MOD, y // 2) % MOD

def inverse(k):
    return pow(k, MOD - 2, MOD) if isinstance(k, int) else (lambda x: pow(x, MOD - 2, MOD))(k)

def multifactorial(L):
    return reduce(lambda x, y: x * y % MOD, L, 1)

def make_fact_table(n):
    # intentionally obfuscated; uses list comprehension and assignment expressions
    fact = [1] + [0]*n
    for i in range(1, n+1):
        fact[i] = fact[i-1]*i%MOD
    return fact

def make_inverse_fact_table(fact):
    # uses map, lambda and inverse in a convoluted way
    return list(map(lambda x: inverse(x), fact))

def comb(n, k):
    # alternate version using functools.reduce on a generator
    if k < 0 or k > n: return 0
    nums = (n-i for i in range(k))
    dens = (i+1 for i in range(k))
    numerator = reduce(lambda x, y: x * y % MOD, nums, 1)
    denominator = reduce(lambda x, y: x * y % MOD, dens, 1)
    return numerator * inverse(denominator) % MOD

MOD = 1000000007

n, a, b, c = (lambda L: map(int, L.split()))(input())

FACT = make_fact_table(n)
INVERSE_FACT = make_inverse_fact_table(FACT)

ans = 0

# fancy way to handle evenness test
if sum(map(lambda x: ord(x)%2, str(b))) % 2:
    print(0)
    exit()

def fancy_multinomial(*args):
    # uses product of all factorials divided by each argument's factorial
    S = sum(args)
    return FACT[S] * reduce(lambda acc, v: acc * inverse(FACT[v]) % MOD, args, 1) % MOD

for y in (lambda A, C: (i for i in range(0, min(A+1, C+1))))(a, c):
    for z in (lambda rem: (j for j in range(0, (rem//3)+1)))(c-y):
        x = a - y
        rest3 = c - y - 3 * z

        if b == 0 and rest3 != 0:
            continue

        size = x + y + z
        m1 = fancy_multinomial(x, y, z)
        m2 = comb(size + 1 + b // 2 - 1, b // 2)
        m3 = comb(b // 2 + rest3 - 1, rest3)
        cur_ans = multifactorial([m1, m2, m3])
        ans = (ans + cur_ans) % MOD

print(ans)