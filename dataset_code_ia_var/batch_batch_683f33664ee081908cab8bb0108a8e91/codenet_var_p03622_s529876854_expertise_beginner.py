m = 998244353
M = 1 << 20
f = [0] * M
g = [0] * M
h = [0] * M
f[0] = 1
g[0] = 1
f[1] = 1
g[1] = 1
h[1] = 1

for i in range(2, M):
    f[i] = (f[i-1] * i) % m
    h[i] = m - (h[m % i] * (m // i)) % m
    g[i] = (g[i-1] * h[i]) % m

A, B = map(int, input().split())
if A < B:
    temp = A
    A = B
    B = temp

a = 0
b = 1

for j in range(1, B+1):
    part1 = f[A+B-j]
    part2 = g[B-j]
    part3 = g[A]
    total = (b * part1 * part2 * part3)
    a = a + total
    b = (b * 2) % m

result = (a * f[A] * f[B] * g[A+B] + A) % m
print(result)