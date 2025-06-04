n, m = map(int, input().split())
if n >= m:
    print(0)
    exit()
a = list(map(int, input().split()))
a = sorted(a)
b = [0] * (m - 1)
for i in range(m - 1):
    b[i] = a[i + 1] - a[i]
b = sorted(b)
b = b[:m - n]
print(sum(b))