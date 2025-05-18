import sys
input = sys.stdin.readline
a, b, c, d = map(int, input().split())
t = -float("inf")
if 0 in range(a, b + 1) or (0 in range(c, d + 1)): t = 0
print(max(a * c, b * d, a * d, b * c, t))