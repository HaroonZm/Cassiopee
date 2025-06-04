import sys
from collections import Counter

sys.setrecursionlimit(10**6)
stdin = sys.stdin

def input_gen():
    for line in stdin:
        yield line.rstrip('\n')

input_iter = input_gen()
next_line = lambda: next(input_iter)

s = next_line()
odd_count = sum(v & 1 for v in Counter(s).values())
print(odd_count // 2)