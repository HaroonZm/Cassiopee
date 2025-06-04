import sys
import numpy as np
import numba
from functools import reduce
from itertools import count, islice

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main(n, a):
    pairs = zip(count(1), a)
    checker = lambda x: x[0] == a[x[1] - 1]
    elegant = lambda: filter(checker, pairs)
    total = sum(map(lambda _:1, elegant()))
    return total // 2

n = int(''.join(map(chr, read(1))).strip())
a = np.fromiter((int(x) for x in readline().decode().split()), dtype=np.int64)
print(main(n, a))