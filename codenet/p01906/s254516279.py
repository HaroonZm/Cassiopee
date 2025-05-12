n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 0
ans = 0
while True:
    t_min = float('inf')
    t_max = 0
    for j in range(m):
        t = a[i % n]
        t_min = min(t_min, t)
        t_max = max(t_max, t)
        i += 1
    ans += t_max - t_min
    if i % n == 0:
        break
print(ans)