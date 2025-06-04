n, d = map(int, input().split())
if d == 1:
    print(n * (n - 1) // 2)
else:
    print((n - 1) + (n - d - 1) * n - ((n - d - 1) * (n + d - 2) // 2))