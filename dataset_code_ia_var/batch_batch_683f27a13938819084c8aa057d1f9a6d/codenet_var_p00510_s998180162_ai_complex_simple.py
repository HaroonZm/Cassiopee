from functools import reduce
from itertools import accumulate, chain, repeat
import operator

n = int(input())
s = m = int(input())

lst = list(chain.from_iterable([map(int, input().split())] for _ in range(n)))
deltas = [in_c - out_c for in_c, out_c in zip(lst[::2], lst[1::2])]

states = list(accumulate(chain([m], deltas)))
neg_found = next((i for i, v in enumerate(states[1:], 1) if v < 0), None)
s = 0 if neg_found is not None else max(states)
print(s)