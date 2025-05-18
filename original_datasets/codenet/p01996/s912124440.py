n,m = map(int, input().split())
a = list(map(int, input().split()))
num = m
for i in range(m):
    if a[i] <= m:
        num -= 1
print(num)