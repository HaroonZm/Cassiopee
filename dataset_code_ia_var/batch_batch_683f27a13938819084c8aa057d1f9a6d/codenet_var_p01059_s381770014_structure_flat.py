n, m = map(int, input().split())
a = list(map(int, input().split()))
c = []
c.append(a[0] - 1)
c.append(n - a[m - 1])
i = 0
while i < m - 1:
    c.append((a[i + 1] - a[i]) // 2)
    i += 1
res = c[0]
j = 1
while j < len(c):
    if c[j] > res:
        res = c[j]
    j += 1
print(res)