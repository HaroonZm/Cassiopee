o = 998244353
r = 2500100
f = [1]
for i in range(1, r):
    f.append(f[-1] * i % o)

def v(x):
    return pow(x, o - 2, o)

def c(n, k):
    return f[n] * v(f[n - k]) * v(f[k]) % o

n, m = map(int, input().split())
a = (c(n + 3 * m - 1, n - 1) - n * c(n + m - 2, n - 1)) % o
if n > m + 1:
    for i in range(m + 1, min(3 * m, n) + 1):
        if (3 * m - i) % 2:
            continue
        x = (3 * m - i) // 2
        a = (a - c(n, i) * c(x + n - 1, n - 1)) % o
print(a)