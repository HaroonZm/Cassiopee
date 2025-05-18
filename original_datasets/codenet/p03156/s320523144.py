n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
x = 0
y = 0
z = 0
for i in range(n):
    if p[i] <= a:
        x += 1
    elif p[i] <= b:
        y += 1
    else:
        z += 1
print(min(x, y, z))