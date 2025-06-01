N = 200020
a = [0] * N
n = int(input())
for _ in range(n):
    x, y = input().split()
    s = int(x) + int(y)
    a[s] = a[s] + 1
for i in range(N - 1):
    a[i + 1] = a[i + 1] + a[i] // 2
    a[i] = a[i] % 2
    if a[i] != 0:
        print(i, 0)