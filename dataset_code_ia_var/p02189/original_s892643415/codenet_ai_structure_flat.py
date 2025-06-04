N = int(input())
a = [int(x) for x in input().split()]
m = a[0]
idx = 0
for i in range(1, N):
    if a[i] < m:
        m = a[i]
        idx = i
print(idx + 1)