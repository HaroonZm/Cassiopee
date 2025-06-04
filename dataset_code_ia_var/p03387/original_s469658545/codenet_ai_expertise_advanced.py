from sys import stdin

*a, = map(int, stdin.readline().split())
target = max(a)
adjust = target * 3 - sum(a)
print((adjust + 1) // 2)