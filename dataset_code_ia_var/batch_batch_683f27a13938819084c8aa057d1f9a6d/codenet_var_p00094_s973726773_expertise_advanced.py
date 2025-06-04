from sys import stdin
from functools import reduce

print(
    reduce(lambda x, y: x * y, map(int, stdin.readline().split())) / 3.305785
)