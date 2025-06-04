n = int(input())
l = [0, 1]
a = 0
b = 1
c = 1
p = 998244353
i = 2
while i < n:
    l.append(l[p % i] * (p - int(p // i)) % p)
    i += 1
i = n
while i > n // 2:
    a = (a + b * c % p) % p
    b = (b + b % p) % p
    c = c * i * l[n + 1 - i] % p
    i -= 1
print((pow(3, n, p) - 2 * a) % p)