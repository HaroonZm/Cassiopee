n = int(input())
t = [0] * (n + 1)
x = [0] * (n + 1)
y = [0] * (n + 1)
i = 1
while i <= n:
    a, b, c = input().split()
    t[i] = int(a)
    x[i] = int(b)
    y[i] = int(c)
    i += 1
i = 0
while i < n:
    dt = abs(t[i + 1] - t[i])
    dx = abs(x[i + 1] - x[i])
    dy = abs(y[i + 1] - y[i])
    tmp = dt - (dx + dy)
    if tmp < 0 or tmp % 2 != 0:
        print('No')
        exit()
    i += 1
print('Yes')