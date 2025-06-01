a = [int(input()) for _ in range(5)]
x, y = a[0] * a[4], a[1] + max(a[4] - a[2], 0) * a[3]
print(min(x, y))