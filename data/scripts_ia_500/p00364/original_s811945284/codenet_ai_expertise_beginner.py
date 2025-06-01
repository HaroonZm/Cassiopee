n, x = input().split()
n = int(n)
x = int(x)

max_slope = 0.0

for i in range(n):
    line = input().split()
    xi = float(line[0])
    hi = float(line[1])
    slope = hi / xi
    if slope > max_slope:
        max_slope = slope

result = x * max_slope
print(result)