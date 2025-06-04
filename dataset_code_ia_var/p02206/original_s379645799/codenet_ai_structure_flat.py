n, k = map(int, input().split())
ok = 0
ng = k + 1
while ng - ok > 1:
    mid = (ng + ok) // 2
    s = 0
    m = mid
    i = 0
    while i < n:
        s += m
        m //= 2
        if m == 0:
            break
        i += 1
    if s <= k:
        ok = mid
    else:
        ng = mid
print(ok)