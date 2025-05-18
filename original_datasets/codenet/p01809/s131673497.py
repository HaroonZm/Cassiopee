def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n
p, q = map(int, input().split())
q //= gcd(p, q)

x = q; y = 1; k = 2
while k*k <= x:
    if x % k == 0:
        while x % k == 0: x //= k
        y *= k
    k += 1
y *= x

print(y)