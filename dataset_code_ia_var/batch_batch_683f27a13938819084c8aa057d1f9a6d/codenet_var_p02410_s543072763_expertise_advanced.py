from operator import mul
from sys import stdin

def readints():
    return map(int, stdin.readline().split())

n, m = map(int, stdin.readline().split())
matrix = [list(readints()) for _ in range(n)]
vector = [int(stdin.readline()) for _ in range(m)]

for row in matrix:
    print(sum(map(mul, row, vector)))