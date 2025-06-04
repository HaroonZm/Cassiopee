n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 0
ans = 0
while True:
    t_min = float('inf')
    t_max = 0
    j = 0
    while j < m:
        t = a[i % n]
        if t < t_min:
            t_min = t
        if t > t_max:
            t_max = t
        i += 1
        j += 1
    ans += t_max - t_min
    if i % n == 0:
        break
print(ans)