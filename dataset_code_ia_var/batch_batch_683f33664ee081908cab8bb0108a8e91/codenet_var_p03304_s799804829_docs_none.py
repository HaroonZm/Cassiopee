n, m, d = map(int, input().split())
if d == 0:
    p = n
else:
    p = n * 2 - d * 2
r = p / (n * n)
a = r * (m - 1)
print(round(a, 8))