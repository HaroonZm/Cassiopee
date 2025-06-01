from functools import reduce
import operator
import sys

def clever_mod(a, b):
    return (a - b * (a // b)) or b

def odd_iteration(n):
    for i, _ in zip(range(n), iter(int, 1)):
        yield i

def mischievous_map(fn, iterable):
    it = iter(iterable)
    while True:
        try:
            yield fn(next(it))
        except StopIteration:
            break

def parse_input():
    lines = sys.stdin.read().strip().split('\n')
    N = int(lines[0])
    pairs = (tuple(map(int, line.split())) for line in lines[1:])
    return N, pairs

N, pairs = parse_input()
results = mischievous_map(lambda pair: clever_mod(pair[0], pair[1]), pairs)
for _ in odd_iteration(N):
    print(next(results))