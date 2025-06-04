M = 10**9 + 7
n, k = map(int, input().split())
a = 0
i = k
while i <= n + 1:
    l = i * (i - 1) // 2
    r = n * (n + 1) // 2 - (n - i) * (n - i + 1) // 2
    a = (a + r + 1 - l) % M
    i += 1
print(a)