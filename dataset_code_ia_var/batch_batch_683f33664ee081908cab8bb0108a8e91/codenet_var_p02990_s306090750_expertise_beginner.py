n, k = input().split()
n = int(n)
k = int(k)
a = n - k + 1
for i in range(1, k + 1):
    if i > n - k + 1:
        print(0)
    else:
        print(a % 1000000007)
        a = a * (k - i) * (n - k + 1 - i)
        a = a // (i * (i + 1))