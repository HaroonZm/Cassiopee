from functools import reduce
from itertools import accumulate, dropwhile
from operator import eq, add
from sys import stdin

n = int(next(stdin).rstrip())
br = list(map(int, next(stdin).rstrip().split()))

def find_cur(seq):
    return reduce(lambda acc, x: x if eq(x, acc+1) else acc, seq, 0)

cur = find_cur(br)

print({True: n - cur, False: -1}[cur != 0])