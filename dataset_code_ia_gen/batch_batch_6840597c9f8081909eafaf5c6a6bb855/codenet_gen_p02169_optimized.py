mod = 998244353

def modinv(a, mod=mod):
    return pow(a, mod - 2, mod)

def main():
    M, N, K = map(int, input().split())
    M_mod = M % mod

    max_r = min(M, K - 1)
    # If max_r < 0, then no subtraction needed (sum over r=0..K-1 empty)
    if max_r < 0:
        print(pow(M_mod, N, mod))
        return

    # Precompute factorials and inverses up to max_r
    max_r = int(max_r)
    fact = [1] * (max_r + 1)
    inv_fact = [1] * (max_r + 1)
    for i in range(1, max_r + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[max_r] = modinv(fact[max_r], mod)
    for i in reversed(range(max_r)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def comb(n, r):
        if r < 0 or r > n:
            return 0
        # Here n can be large, so compute combination modulo mod using Lucas theorem or Fermat's little theorem
        # But n can be up to 1e18, so direct factorial-based comb impossible
        # However, since r <= 1000 (K <= 1000), and n can be large, we use multiplicative formula:
        # C(n,r) = n*(n-1)*...*(n-r+1)/r!
        # compute numerator modulo mod with n mod mod first, but direct product needed
        # Wait: since mod is prime and r small, we can do:
        # numerator = product (n - i) mod mod for i=0 to r-1
        # denominator = fact[r]
        # inverse denominator = inv_fact[r]
        numerator = 1
        n_mod = n % mod
        for i in range(r):
            numerator = numerator * ((n_mod - i) % mod) % mod
        return numerator * inv_fact[r] % mod

    result = pow(M_mod, N, mod)
    total_sub = 0
    for r in range(max_r + 1):
        c = comb(M, r)
        pow_val = pow(r, N, mod)
        term = c * pow_val
        if r % 2 == 0:
            total_sub = (total_sub + term) % mod
        else:
            total_sub = (total_sub - term) % mod

    ans = (result - total_sub) % mod
    print(ans)

if __name__ == "__main__":
    main()