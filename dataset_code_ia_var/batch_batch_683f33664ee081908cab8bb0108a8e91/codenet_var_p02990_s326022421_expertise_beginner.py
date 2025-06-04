MOD = 10**9 + 7

def framod(n, mod):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result

def power(n, r, mod):
    result = 1
    while r > 0:
        if r % 2 == 1:
            result = (result * n) % mod
        n = (n * n) % mod
        r //= 2
    return result

def comb(n, k, mod):
    if k < 0 or k > n:
        return 0
    a = framod(n, mod)
    b = framod(k, mod)
    c = framod(n - k, mod)
    return (a * power(b, mod - 2, mod) * power(c, mod - 2, mod)) % mod

def main():
    N, K = map(int, input().split())
    for i in range(1, K + 1):
        if i <= N - K + 1:
            x = comb(N - K + 1, i, MOD)
            y = comb(K - 1, i - 1, MOD)
            print((x * y) % MOD)
        else:
            print(0)

if __name__ == '__main__':
    main()