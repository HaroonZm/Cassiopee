n, x, *a = map(int, open(0).read().split())
m = 1e18
i = 0
while i < n:
    s = 0
    j = 0
    while j < n:
        s += a[j]
        j += 1
    if m > s + x * i:
        m = s + x * i
    b = []
    j = 0
    while j < n:
        if j == 0:
            b.append(a[j])
        else:
            b.append(min(a[j], b[j-1]))
        j += 1
    a = b
    i += 1
print(m)