n, t, e = map(int, input().split())
a = list(map(int, input().split()))
tmp = 0
found = False
i = 0
while i < n:
    x = (t - e - 1) // a[i]
    if (x + 1) * a[i] <= t + e:
        print(i + 1)
        found = True
        break
    i += 1
if not found:
    print(-1)