n = int(input())
if n % 2:
    print(((n - 1) * (n - 2) + (n - 1)) // 2)
else:
    print(n * (n - 2) // 2)
for i in range(n):
    for j in range(i + 1, n):
        if i + j != n - 2 + (0 if n % 2 else 1):
            print(i + 1, j + 1)