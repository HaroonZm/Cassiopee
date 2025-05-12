n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
N = 10 ** 6

#逆元テーブル
inv_t = [0]+[1]
for i in range(2,N):
  inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

def comb(n, r):
    ret = 1
    for i in range(1, r + 1):
        ret = (ret * (n - i + 1) * inv_t[i]) % mod
    return ret

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % mod
        x = x * x % mod
        n //= 2

    return K * x % mod

print((pow_k(2, n) - 1 - comb(n, a) - comb(n,b))%mod)