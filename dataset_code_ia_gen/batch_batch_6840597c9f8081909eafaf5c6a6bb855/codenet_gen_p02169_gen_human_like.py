mod = 998244353

def modpow(base, exp, mod):
    result = 1
    b = base % mod
    e = exp
    while e > 0:
        if e & 1:
            result = (result * b) % mod
        b = (b * b) % mod
        e >>= 1
    return result

def modinv(a, mod):
    # Fermat's little theorem since mod is prime
    return modpow(a, mod - 2, mod)

def comb(n, k, mod):
    # Since k <= 1000, precompute factorials modulo mod up to k
    # and use Lucas theorem for large n and small k
    # but n can be >= mod so we need special handling
    # However, k <= 1000 < mod so we can use Lucas theorem straightforwardly
    # For p = mod prime
    def fact_and_inv(n):
        f = [1] * (n+1)
        for i in range(1, n+1):
            f[i] = f[i-1] * i % mod
        inv = [1] * (n+1)
        inv[n] = modinv(f[n], mod)
        for i in reversed(range(1, n)):
            inv[i] = inv[i+1] * (i+1) % mod
        return f, inv

    def nCr_mod_p(n, r):
        # Lucas theorem decomposition for nCr mod prime
        if r > n:
            return 0
        f, inv = fact_and_inv(k)
        res = 1
        while n > 0 or r > 0:
            n_i = n % mod
            r_i = r % mod
            if r_i > n_i:
                return 0
            # Compute n_iCr_i using precomputed factorial
            res *= f[n_i] * inv[r_i] % mod * inv[n_i - r_i] % mod
            res %= mod
            n //= mod
            r //= mod
        return res

    return nCr_mod_p(n, k)

def main():
    import sys
    M, N, K = map(int, sys.stdin.readline().split())

    if K > min(M, N):
        # Impossible to have K or more distinct characters if K > M or K > N
        print(0)
        return

    # Sum of number of strings that use exactly i distinct characters for i in [K,M]
    # For i > M, 0, for i > N, 0, so i in [K, min(M, N)]
    # Number with exactly i distinct chars:
    # C(M, i) * number_of_strings_using_all_i_chars
    # Number of strings that use all i distinct chars:
    # Using inclusion-exclusion:
    # sum_{j=0}^{i} (-1)^j C(i, j) (i - j)^N
    # Because total strings over i letters: i^N
    # Subtract those missing at least one letter: sum over j of missing exactly j letters: C(i, j)*(i-j)^N alternating
    
    max_i = min(M, N)
    ans = 0
    for i in range(K, max_i+1):
        c = comb(M, i, mod)
        tot = 0
        for j in range(i+1):
            sign = 1 if j % 2 == 0 else -1
            val = comb(i, j, mod) * modpow(i - j, N, mod) % mod
            tot += sign * val
        tot %= mod
        ans += c * tot
        ans %= mod

    print(ans % mod)

if __name__ == "__main__":
    main()