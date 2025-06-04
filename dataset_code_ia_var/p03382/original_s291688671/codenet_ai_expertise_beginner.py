n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

x = a[0]
for i in range(1, n):
    if a[i] > x:
        x = a[i]

y = 0
for i in range(n):
    if a[i] != x:
        if y == 0:
            y = a[i]
        elif abs(a[i]*2 - x) < abs(y*2 - x):
            y = a[i]

print(x, end=' ')
print(y)