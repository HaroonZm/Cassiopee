from sys import stdin

x = int(stdin.readline())
print(min(sum(map(int, str(a))) + sum(map(int, str(x - a))) for a in range(1, x)))