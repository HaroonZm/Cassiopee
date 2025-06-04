n, k = map(int, input().split())
l = 0
r = k + 1
while r - l > 1:
    m = (l + r) // 2
    res = m
    t = m
    i = 0
    while i < n - 1:
        t //= 2
        res += t
        if t == 0:
            break
        i += 1
    if res > k:
        r = m
    else:
        l = m
print(l)