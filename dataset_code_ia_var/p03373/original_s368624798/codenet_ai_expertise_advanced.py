from sys import stdin

a, b, c, x, y = map(int, stdin.readline().split())

min_total = float('inf')
for i in range(0, max(x, y) + 1):
    total = a * max(x - i, 0) + b * max(y - i, 0) + c * 2 * i
    if total < min_total:
        min_total = total
print(min_total)