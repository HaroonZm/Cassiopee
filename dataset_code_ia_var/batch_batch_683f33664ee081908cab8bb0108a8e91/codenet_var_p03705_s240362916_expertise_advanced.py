from sys import stdin

n, a, b = map(int, stdin.readline().split())
if (n == 1 and a != b) or (a > b):
    print(0)
else:
    print((n - 1) * (b - a) + 1)