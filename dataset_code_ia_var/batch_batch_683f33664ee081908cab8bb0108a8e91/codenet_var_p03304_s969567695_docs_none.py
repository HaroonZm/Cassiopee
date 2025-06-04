n, m, d = map(int, input().split())
if (n - d) < (1 + d):
    ex = (2 * (n - d)) / (n ** 2)
    ans = ex * (m - 1)
else:
    ex = 2 * (n - d) / (n ** 2)
    if d == 0:
        ans = ex * (m - 1) / 2
    else:
        ans = ex * (m - 1)
print(ans)