import sys

n, a, b = map(int, sys.stdin.readline().split())
x = min(a, b)
y = max(a + b - n, 0)
print(x, y)