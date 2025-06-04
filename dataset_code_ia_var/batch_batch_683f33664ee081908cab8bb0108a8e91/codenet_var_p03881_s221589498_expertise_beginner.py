a = raw_input().split()
b = raw_input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    b[i] = int(b[i])

c = []
for i in range(len(a)):
    total = a[i] + b[i]
    if total > 0:
        part1 = a[i] / 100.0
        part2 = b[i] / 100.0
        part3 = total / 100.0
        part4 = float(a[i]) / total
        c.append((part1, part2, part3, part4))

n = len(c)
c.sort(key=lambda x: x[3], reverse=True)

u = []
for i in range(n):
    u.append(0)

res = 1
for i in range(n):
    if c[i][2] != 0:
        if res / c[i][2] < 1:
            du = res / c[i][2]
        else:
            du = 1
        u[i] = du
        res -= du * c[i][2]
        if res <= 0:
            break

ans = 0
for i in range(n):
    ans += c[i][0] * u[i]

print ans