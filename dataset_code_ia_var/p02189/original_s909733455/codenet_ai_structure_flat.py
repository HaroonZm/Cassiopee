n = int(input())
a = list(map(int, input().split()))
m = a[0]
idx = 0
for i in range(1, n):
    if a[i] < m:
        m = a[i]
        idx = i
print(idx + 1)