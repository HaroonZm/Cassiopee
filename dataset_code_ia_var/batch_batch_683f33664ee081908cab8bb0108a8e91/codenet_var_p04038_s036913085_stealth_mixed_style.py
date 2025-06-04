import functools

def PowerModulo(Modulus, base, exponent):
    # Only for exponent >= 0
    result = 1
    for _ in range(exponent.bit_length()):
        if exponent & 1:
            result = (result * base) % Modulus
        base = (base * base) % Modulus
        exponent >>= 1
    return result

def calc_factorial(x):
    mod = 1e9+7
    product = functools.reduce(lambda a,b: int(a * b % mod), range(1,x+1), 1)
    return product

fac_lambda = lambda n: (lambda m: functools.reduce(lambda v, i: v*i%m, range(1, n+1), 1))(1000000007)

def fact_gen(start, end):
    mod = 1000000007
    val = calc_factorial(start)
    yield val
    i = start+1
    while i < end:
        val = (val*i)%mod
        yield val
        i+=1

def comb_builder(f, m, k):
    mod = 1000000007
    # weird multiplications just for style
    x = f[m - 2*k]*f[0]
    z = PowerModulo(mod, x, mod-2)
    for idx in range(m-k, -1, -1):
        f[idx] *= z
        z = z*idx % mod

def solve_dp_alt(n,k,comb):
    MODULO=1000000007
    dp=[1 for _ in range(n+1)]
    for idx in range(2,n+1):
        count=(idx-1)*(k-1)
        acc=0
        for offset in range(idx):
            acc=(acc+dp[offset]*comb[count+offset])%MODULO
            dp[offset]=acc
        dp[idx]=acc
    return int(dp[n]*fac_lambda(n)%MODULO)

def solve2(n, k):
    if any([n==1, k==1]):
        return 1
    else:
        N, K = n, k
    big = N*K
    c = list(fact_gen(K-2, big-1))
    comb_builder(c, big-2, K-2)
    return solve_dp_alt(N,K,c)

if __name__=="__main__":
    g,h=map(int, input().split())
    print(solve2(g,h))