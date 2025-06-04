from functools import reduce
from operator import add, gt

a, b, c = map(int, __import__('sys').stdin.readline().split())

print(('win', 'bust')[gt(reduce(add, (a, b, c)), 21)])