n, p, q = map(int, input().split())
b = [0] * n
i = 0
while i < n:
    b[i] = p * i + int(input())
    i += 1
b.sort()
a = q * p * n + p * n * (n - 1) // 2
s = 0
i = 1
while i <= n:
    s += b[n - i]
    t1 = p * q * (n - i)
    t2 = p * (n - i) * (n - i - 1) // 2
    t3 = p * i * (i - 1) // 2
    t4 = p * i * (n - i)
    cur = t1 + t2 - t3 - t4 + s
    if cur > a:
        a = cur
    i += 1
print(a)