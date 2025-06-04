from sys import stdin
from operator import mul
from functools import partial

n, m = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
b = list(map(int, (stdin.readline() for _ in range(m))))
dot = lambda row: sum(map(mul, row, b))
print('\n'.join(map(str, map(dot, a))))