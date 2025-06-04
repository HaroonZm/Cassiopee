from sys import stdin
from operator import mul
from functools import partial

x, y = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(x)]
B = [int(stdin.readline()) for _ in range(y)]
dot = lambda row: sum(map(mul, row, B))
print(*map(dot, A), sep='\n')