from statistics import median

n = int(input())
a = [None] * n
b = [None] * n
for i in range(n):
    A, B = map(int, input().split())
    a[i], b[i] = A, B

if n % 2 == 1:
    print(abs(median(b) - median(a)) + 1)
else:
    print(int(abs(median(b) - median(a)) * 2) + 1)