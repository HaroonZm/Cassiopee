n = int(input())
v = input().split()
for i in range(n):
    v[i] = int(v[i])

v.sort()

for i in range(1, n):
    x = v[0]
    y = v[1]
    del v[0]
    del v[0]
    xy = (x + y) / 2
    v.append(xy)
    v.sort()

print(v[0])