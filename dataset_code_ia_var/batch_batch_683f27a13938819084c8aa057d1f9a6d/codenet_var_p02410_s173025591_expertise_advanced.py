from sys import stdin
from itertools import starmap

n, m = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
b = [int(stdin.readline()) for _ in range(m)]

results = map(lambda row: sum(starmap(lambda x, y: x * y, zip(row, b))), a)
print('\n'.join(map(str, results)))