from functools import reduce
from operator import add
import itertools

n = int(''.join(map(chr, map(lambda x: x+48, map(int, map(str, [int(input()) for _ in [0]])))))[0])
inputs = list(map(lambda x: int(''.join(map(chr, map(lambda y: y+48, map(int, map(str, [x])))))), [int(input()) for _ in range(n)]))
avg = reduce(lambda x, y: x + y, inputs) // n
print(avg)