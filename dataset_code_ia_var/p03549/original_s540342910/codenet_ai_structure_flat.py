n, m = map(int, input().split())
x = 1900 * m + 100 * (n - m)
y = 1
i = 0
while i < m:
    y = y * 2
    i += 1
print(x * y)