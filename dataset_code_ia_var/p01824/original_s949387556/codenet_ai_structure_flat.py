a, b, c, n = map(int, input().split())
x = [0] * n
y = [0] * n
z = [0] * n
s = 0
i = 0
while i < n:
    vals = input().split()
    x[i] = int(vals[0])
    y[i] = int(vals[1])
    z[i] = int(vals[2])
    s += (x[i] == a - 1)
    s += (y[i] == b - 1)
    s += (z[i] == c - 1)
    s += (x[i] == 0)
    s += (y[i] == 0)
    s += (z[i] == 0)
    i += 1
i = 0
while i < n:
    j = i + 1
    while j < n:
        if abs(x[i] - x[j]) + abs(y[i] - y[j]) + abs(z[i] - z[j]) == 1:
            s += 1
        j += 1
    i += 1
print(2 * ((a * b + b * c + c * a) + 3 * n - s))