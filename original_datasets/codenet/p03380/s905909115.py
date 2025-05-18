n = int(input())
a = sorted([int(_) for _ in input().split()])[::-1]
m = a[0]
half = m/2
r = a[1]
for i in range(1, n):
    if abs(half-a[i]) < abs(half-r):
        r = a[i]

print(m, r)