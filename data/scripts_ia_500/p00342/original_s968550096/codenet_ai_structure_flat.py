n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0.0
i = 0
while i < n - 2:
    val = (a[n - 1] + a[n - 2]) / (a[i + 1] - a[i])
    if val > ans:
        ans = val
    i += 1
val = (a[n - 1] + a[n - 4]) / (a[n - 2] - a[n - 3])
if val > ans:
    ans = val
val = (a[n - 3] + a[n - 4]) / (a[n - 1] - a[n - 2])
if val > ans:
    ans = val
print('%.8f' % ans)