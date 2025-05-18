n, m = map(int, input().split())
*x, = map(int, input().split())
*y, = map(int, input().split())

MOD = 10**9+7

def calc(v, l):
    r = 0
    for i in range(l):
        r = r + i*v[i] - (l-1-i)*v[i]
        r %= MOD
    return r

print((calc(x, n)*calc(y, m)) % MOD)